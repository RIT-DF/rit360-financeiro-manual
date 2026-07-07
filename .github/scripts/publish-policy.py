#!/usr/bin/env python3
"""Publica versões de documentos legais (privacidade/termos) na EF publish_policy_version.

Lê o frontmatter de cada documento legal vigente, valida que o snapshot
congelado daquela versão existe (para nunca registrar uma URL pendente) e
chama a Edge Function, que é idempotente por (type, version): se a versão já
foi publicada, a EF responde 200 "already_published" e nada muda.

Sem dependências externas — só biblioteca padrão. Pensado para rodar no
GitHub Actions do repositório bussola-docs (onde o manual é publicado).

Variáveis de ambiente:
  POLICY_PUBLISH_TOKEN  (obrigatória) token estático aceito pela EF
  FUNCTIONS_BASE        base das Edge Functions (default: projeto de produção)
  SITE_BASE             base pública do manual (default: https://docs.bf.rit.org.br)
"""

import json
import os
import sys
import urllib.error
import urllib.request

# slug do arquivo no manual -> tipo de documento esperado pela EF
DOCS = [
    ("privacidade", "privacy"),
    ("termos", "terms"),
]

FUNCTIONS_BASE = os.environ.get(
    "FUNCTIONS_BASE",
    "https://jswyzxutdkrbrleotklo.supabase.co/functions/v1",
).rstrip("/")
SITE_BASE = os.environ.get("SITE_BASE", "https://docs.bf.rit.org.br").rstrip("/")
TOKEN = os.environ.get("POLICY_PUBLISH_TOKEN", "")


def parse_frontmatter(path):
    """Extrai o bloco YAML simples entre os dois primeiros '---'."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---"):
        raise ValueError(f"{path}: sem frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError(f"{path}: frontmatter não fechado")
    block = text[3:end]
    data = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
            value = value[1:-1]
        data[key.strip()] = value
    return data


def as_bool(value):
    return str(value).strip().lower() in ("true", "yes", "1")


def publish(doc_type, frontmatter):
    version = (frontmatter.get("version") or "").strip()
    if not version:
        raise ValueError(f"{doc_type}: frontmatter sem 'version'")

    slug = "privacidade" if doc_type == "privacy" else "termos"
    snapshot = os.path.join("legal", f"{slug}-{version}.md")
    if not os.path.isfile(snapshot):
        raise SystemExit(
            f"::error::Snapshot ausente: {snapshot}. Congele a versão {version} "
            f"de {slug} antes de publicar (veja o runbook das políticas legais)."
        )

    document_url = f"{SITE_BASE}/{slug}/{version}/"
    body = {
        "type": doc_type,
        "version": version,
        "document_url": document_url,
        "change_summary": frontmatter.get("change_summary", ""),
        "requires_reconsent": as_bool(frontmatter.get("requires_reconsent", "true")),
    }

    if os.environ.get("DRY_RUN"):
        print(f"[dry-run] POST {FUNCTIONS_BASE}/publish_policy_version")
        print(f"[dry-run] body: {json.dumps(body, ensure_ascii=False)}")
        return "dry_run"

    req = urllib.request.Request(
        f"{FUNCTIONS_BASE}/publish_policy_version",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:500]
        raise SystemExit(f"::error::{doc_type} {version}: HTTP {exc.code} — {detail}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"::error::{doc_type} {version}: falha de rede — {exc.reason}")

    status = payload.get("status", "?")
    print(f"{doc_type} {version} -> {status} ({document_url})")
    return status


def main():
    if not TOKEN:
        raise SystemExit("::error::POLICY_PUBLISH_TOKEN não definido (secret do repositório).")

    published = []
    for slug, doc_type in DOCS:
        path = f"{slug}.md"
        if not os.path.isfile(path):
            print(f"::warning::{path} não encontrado — pulando.")
            continue
        frontmatter = parse_frontmatter(path)
        published.append(publish(doc_type, frontmatter))

    if not published:
        raise SystemExit("::error::Nenhum documento legal processado.")
    print(f"OK: {len(published)} documento(s) processado(s).")


if __name__ == "__main__":
    main()
