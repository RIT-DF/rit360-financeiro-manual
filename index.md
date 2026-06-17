---
title: "Início"
nav_order: 1
permalink: /
---

<style>
.home-intro { max-width: 720px; margin: 2rem 0 2.5rem; font-size: 1.05rem; line-height: 1.7; }
.home-intro p { margin: 0 0 1rem; }
.module-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; margin: 1.5rem 0 2.5rem; }
.module-card { display: block; padding: 1.25rem 1rem; border: 1px solid #dde3ec; border-radius: 8px; text-decoration: none; color: #222; background: #f8fafd; transition: box-shadow 0.15s; }
.module-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-color: #aac; text-decoration: none; }
.module-card-icon { font-size: 1.75rem; margin-bottom: 0.5rem; }
.module-card-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 0.3rem; color: #0F4855; }
.module-card-desc { font-size: 0.82rem; color: #555; line-height: 1.4; }
.section-title { font-size: 1.15rem; font-weight: 700; margin: 2rem 0 0.75rem; color: #333; border-bottom: 2px solid #e0e7ef; padding-bottom: 0.4rem; }
.quick-links { display: flex; flex-wrap: wrap; gap: 0.6rem; margin: 0.75rem 0 2rem; }
.quick-links a { padding: 0.4rem 1rem; border: 1px solid #cdd9d4; border-radius: 20px; font-size: 0.88rem; text-decoration: none; color: #0F4855; background: #eef4f2; }
.quick-links a:hover { background: #dce8f8; }
</style>

<div class="home-intro">
  <p>O <strong>Bússola Financeira</strong> é a plataforma de gestão financeira para Organizações da Sociedade Civil (OSCs) desenvolvida pela <a href="https://rit.org.br" target="_blank" rel="noopener noreferrer">RIT — Rede de Inovação e Transformação</a>. Acesse o sistema em <a href="https://bf.rit.org.br" target="_blank" rel="noopener noreferrer">bf.rit.org.br</a>.</p>
  <p>Esta documentação <strong>não é só um manual de botões</strong>: cada seção explica o porquê das funcionalidades, conceitos financeiros relevantes para OSC (fluxo de caixa, regime de caixa, estorno, quórum de aprovação) e boas práticas que vimos funcionarem na rede. Leia na ordem que quiser; comece pelos <a href="/primeiros-passos/">Primeiros Passos</a> se você acabou de chegar.</p>
</div>

<div class="section-title">Módulos</div>

<div class="module-grid">
  <a class="module-card" href="/modulos/painel/">
    <div class="module-card-icon">📊</div>
    <div class="module-card-title">Painel</div>
    <div class="module-card-desc">Cockpit da sua OSC — saldos, resumo e pendências por papel</div>
  </a>
  <a class="module-card" href="/modulos/movimentacoes/">
    <div class="module-card-icon">💸</div>
    <div class="module-card-title">Movimentações</div>
    <div class="module-card-desc">Receitas, despesas e transferências — o coração do sistema</div>
  </a>
  <a class="module-card" href="/modulos/reembolsos/">
    <div class="module-card-icon">🔄</div>
    <div class="module-card-title">Reembolsos</div>
    <div class="module-card-desc">Solicitar e aprovar reembolsos de despesas pagas do bolso</div>
  </a>
  <a class="module-card" href="/modulos/pedidos-pagamento/">
    <div class="module-card-icon">📋</div>
    <div class="module-card-title">Pedidos de Pagamento</div>
    <div class="module-card-desc">Autorizar pagamentos a fornecedores antes da despesa acontecer</div>
  </a>
  <a class="module-card" href="/modulos/projetos/">
    <div class="module-card-icon">📁</div>
    <div class="module-card-title">Projetos</div>
    <div class="module-card-desc">Planejar, executar, acompanhar a saúde e encerrar iniciativas da OSC</div>
  </a>
  <a class="module-card" href="/modulos/relatorios/">
    <div class="module-card-icon">📈</div>
    <div class="module-card-title">Relatórios</div>
    <div class="module-card-desc">Análises financeiras consolidadas — Visão Geral, Receitas, Despesas, Atenção e Previsão</div>
  </a>
</div>

<div class="section-title">Meu Perfil</div>

<div class="module-grid">
  <a class="module-card" href="/configuracoes/perfil/">
    <div class="module-card-icon">👤</div>
    <div class="module-card-title">Meu Perfil</div>
    <div class="module-card-desc">Dados pessoais, dados para reembolso, preferências de notificação por canal e evento</div>
  </a>
</div>

<div class="section-title">Configurações da Organização <small style="font-weight: 400; color: #666;">(admin e tesoureiro)</small></div>

<div class="module-grid">
  <a class="module-card" href="/configuracoes/organizacao/">
    <div class="module-card-icon">🏢</div>
    <div class="module-card-title">Organização</div>
    <div class="module-card-desc">Dados da OSC e integrações (WooCommerce, Google Drive, WhatsApp, Telegram)</div>
  </a>
  <a class="module-card" href="/configuracoes/usuarios/">
    <div class="module-card-icon">👥</div>
    <div class="module-card-title">Usuários</div>
    <div class="module-card-desc">Membros da organização, papéis e convites</div>
  </a>
  <a class="module-card" href="/configuracoes/contas/">
    <div class="module-card-icon">🏦</div>
    <div class="module-card-title">Contas Bancárias</div>
    <div class="module-card-desc">Contas financeiras e saldos consolidados</div>
  </a>
  <a class="module-card" href="/configuracoes/categorias/">
    <div class="module-card-icon">🏷️</div>
    <div class="module-card-title">Categorias</div>
    <div class="module-card-desc">Categorias de receita, despesa e centros de custo</div>
  </a>
  <a class="module-card" href="/configuracoes/aprovacoes/">
    <div class="module-card-icon">✅</div>
    <div class="module-card-title">Fluxo de Aprovações</div>
    <div class="module-card-desc">Quórum e aprovadores elegíveis para reembolsos e pedidos</div>
  </a>
</div>

<div class="section-title">Primeiros Passos e Referência</div>

<div class="quick-links">
  <a href="/primeiros-passos/">Primeiro acesso e navegação</a>
  <a href="/papeis/">Papéis e permissões</a>
  <a href="/faq/">Perguntas frequentes</a>
  <a href="/roadmap/">Roadmap</a>
  <a href="/changelog/">Changelog</a>
</div>

<div class="section-title">Suporte e contato</div>

<p>Dúvidas, sugestões ou problemas? Use o botão <strong>💬 Feedback</strong> dentro do Bússola — vai direto para a equipe da RIT, com a versão do app e o seu contexto. Para questões de privacidade ou LGPD, escreva para <a href="mailto:dpo@rit.org.br">dpo@rit.org.br</a>.</p>

<hr>
<p style="font-size:0.8rem; color:#888;">Bússola Financeira v0.32.0 · <a href="https://rit.org.br" target="_blank" rel="noopener noreferrer">RIT — Rede de Inovação e Transformação</a> · <a href="https://github.com/RIT-DF/bussola-docs" target="_blank" rel="noopener noreferrer">repositório público desta documentação</a></p>
