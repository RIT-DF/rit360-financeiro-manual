---
layout: section
title: "Configurações — Organização"
permalink: /configuracoes/organizacao/
---

> Disponível para **Presidente (admin)**.

A página **Organização** centraliza os dados da sua OSC e as **integrações** com sistemas externos. Acessada pelo **ícone de engrenagem** no canto superior direito (a engrenagem só aparece para admin e tesoureiro) → Configurações → seção Organização.

[![Configurações — Organização](../assets/screenshots/config-organizacao.png)](../assets/screenshots/config-organizacao.png)
*Configurações — Dados da organização*

> 💡 **Por que isso importa**
> Os dados da OSC aqui aparecem em **todos os documentos gerados pela Bússola** (recibos, declarações, relatórios para financiadores, exportações em PDF). Manter atualizado é o que faz a marca da sua OSC aparecer profissional na prestação de contas. As **integrações** abrem porta para automação: WooCommerce sincroniza vendas, WhatsApp Business envia notificações, Google Drive armazena documentos.

## Identidade da OSC

- **Nome** — como a OSC se identifica oficialmente
- **CNPJ** — formato `XX.XXX.XXX/XXXX-XX`
- **E-mail institucional**
- **Telefone**
- **Site** — endereço completo (`https://...`)
- **Identificador único** — slug não editável usado em URLs e identificações internas (gerado a partir do nome no cadastro)

## Endereço e redes sociais

Endereço completo (CEP, logradouro, número, complemento, bairro, cidade, UF) e perfis em redes sociais (Instagram, Facebook, LinkedIn, YouTube).

> ✓ **Dica · Preencha endereço completo para documentos formais**
> Recibos e declarações geradas pela Bússola usam o endereço daqui. OSC com endereço incompleto no sistema pode acabar com documentos que não passam em conferência de financiador ou contador.

## Logo da organização

Upload da logo da OSC (JPG, PNG ou WebP, até 2 MB). A imagem é redimensionada para 512×512. Aparece em documentos gerados, e em versões futuras vai aparecer na barra superior em vez do nome em texto.

## Configurações operacionais

- **Moeda** — padrão Real (BRL); pode ser alterada se a OSC opera em outra moeda
- **Fuso horário** — todas as datas/horas no sistema seguem esse fuso
- **Início do ano fiscal** — define os recortes de "Ano YTD" e "Ano anterior" nos filtros (default Janeiro)

## Acesso público

- **Aceitar solicitações públicas de vínculo** — quando ativado, qualquer pessoa com o link público da OSC pode pedir vínculo (a OSC ainda precisa aprovar). Desligado por default.

> ⚠️ **Atenção · Acesso público é compartilhamento controlado**
> "Aceitar solicitações públicas de vínculo" não dá acesso automático — ainda passa pelo admin. Mas com o link público, qualquer pessoa pode pedir entrada na sua OSC. Use quando você quiser receber inscrições espontâneas (ex: novos voluntários, novos associados); desligue quando preferir só convidar manualmente.

## Integrações

Integração permite que sistemas externos conversem com a Bússola — economizando trabalho manual de transferir dados de um sistema para outro.

### WooCommerce

[Saiba mais no manual de Movimentações → seção Importar lançamentos](../modulos/movimentacoes/#importar-lançamentos)

Sincroniza pedidos pagos da sua loja online (WooCommerce) como receitas na Bússola. Cron diário automático + botão para importar sob demanda. Refunds no WooCommerce viram estornos automáticos na Bússola. Cada pedido importado tem badge "WooCommerce" clicável na lista de movimentações que abre o pedido original no admin do WC.

Configure URL da loja, Consumer Key e Consumer Secret (com instruções passo a passo de como gerar no admin do WooCommerce), frequência da sincronização, modo de mapeamento de categorias (automático com categoria-mãe ou manual explícito), conta financeira destino, data de corte para backfill.

### Google Drive *(em implantação)*

Armazenamento de documentos da OSC no Google Drive da organização. Anexos de movimentações, reembolsos e pedidos serão sincronizados automaticamente.

### WhatsApp Business *(em implantação)*

Envio de notificações via número oficial WhatsApp Business da OSC. Habilita o canal "WhatsApp" da matriz de notificações dos usuários.

### Telegram *(em implantação)*

Envio de notificações via bot oficial Telegram da OSC para grupos/canais. Complementa o envio individual para usuários que vincularam Telegram no perfil pessoal.

## Por onde seguir

- **Configurações → Usuários** — para gerenciar membros da OSC.
- **Configurações → Contas Bancárias** — para cadastrar as contas que aparecem em Movimentações.
- **Movimentações → Importar Lançamentos** — onde a integração WooCommerce aparece como fonte ao lado do CSV.
