---
layout: page
title: Changelog
permalink: /changelog/
---

# Changelog — Bússola Financeira

Todas as mudanças relevantes do projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [Pré-teste em andamento]

## [0.13.0] — 2026-05-18

### Adicionado
- **Integração com WooCommerce** (BK-149): a Bússola agora sincroniza automaticamente os pedidos pagos da loja online da sua OSC como receitas em Movimentações. Cada pedido `completed` vira um lançamento financeiro com data, valor, cliente, método de pagamento e categoria — sem intervenção manual.
- **Configuração da integração** (BK-149): nova seção "WooCommerce" em **Configurações → Organização**. Admin informa URL da loja, Consumer Key e Consumer Secret (com instruções passo a passo de como gerar no admin do WooCommerce, sem suposições), escolhe a frequência da sincronização (diária / semanal / mensal / desligada), a conta financeira destino, a data de corte para o backfill inicial e o modo de mapeamento de categorias (automático com categoria-mãe ou manual explícito).
- **Sincronização automática diária** (BK-149): todas as OSCs com integração ativa têm seus pedidos sincronizados automaticamente todo dia às 06:00 (horário de Brasília). A frequência efetiva por OSC respeita a configuração escolhida — uma OSC em "Semanal" só roda nas segundas; em "Mensal" só no dia 1; em "Desligada" pula completamente.
- **Importação manual sob demanda** (BK-149): além do cron automático, a página **Movimentações → Importar Lançamentos** (renomeada de "Importar CSV") agora tem duas fontes — CSV (existente) e WooCommerce (nova). Na aba WooCommerce, o admin escolhe o período (Desde a última sincronização / Últimos 7 dias / Últimos 30 dias / Personalizado com 2 datas) e clica "Importar agora".
- **Estorno automático em refunds** (BK-149): se um pedido importado pela Bússola virar `refunded` ou `cancelled` no WooCommerce depois, a próxima sincronização cria automaticamente um lançamento contrário (padrão de estorno do BK-156) e ambos os lançamentos passam a exibir o badge "Estornado". A OSC não precisa fazer nada manualmente — a reconciliação contábil acontece sozinha.
- **Badge "WooCommerce" na lista de movimentações** (BK-149): lançamentos importados da loja online ganham um badge clicável ao lado do título. Clicar abre o pedido original no admin do WooCommerce em nova aba (útil para conferir o pedido completo, falar com o cliente, etc.).
- **Mapeamento inteligente de categorias** (BK-149): no modo automático, a Bússola lê as categorias dos produtos da loja e cria sub-categorias correspondentes sob a categoria-mãe escolhida (ex: "Loja Online" → "Camisetas", "Livros", "Doações"). Renomeação manual prevalece em sincronizações futuras — a Bússola não sobrescreve o nome que a OSC ajustou. No modo manual, o admin mapeia explicitamente cada categoria do WooCommerce para uma categoria contábil da Bússola.
- **Detalhe rico no lançamento** (BK-149): cada movimento importado traz nas observações a lista dos itens comprados, o método de pagamento, o status no WooCommerce, dados do cliente e um link direto para abrir o pedido no admin da loja.
- **Histórico de sincronizações** (BK-149): nova área dentro da configuração da integração mostra as últimas 20 execuções (data, modo, totais de novos/estornados/erros, status). Útil para diagnosticar problemas e acompanhar a saúde da integração.
- **Notificação de falha** (BK-149): se uma sincronização falhar por credenciais inválidas, loja fora do ar ou outro erro grave, os administradores da OSC recebem notificação imediatamente (pelos canais habilitados na matriz de notificações do perfil).

### Notas técnicas
- Sem alteração nos fluxos existentes de Reembolsos, Pedidos de Pagamento, Movimentações manuais ou CSV — a integração WooCommerce é totalmente aditiva.
- LGPD: payload bruto do pedido e e-mail do cliente são preservados na tabela de integração mas **excluídos do audit log** para minimizar duplicação de dados pessoais.
- Pendente para versões futuras: webhook em tempo real (hoje sync é cron + manual), split por método de pagamento, cálculo automático de taxa do gateway, reconciliação com extrato bancário (que vem com BK-067) e múltiplas lojas por OSC.

## [0.12.0] — 2026-05-18

### Adicionado
- **Perfil do usuário em rota própria** (BK-154 + BK-139): a tela de perfil foi separada de Configurações e ganhou rota standalone `/perfil`, acessível a qualquer usuário autenticado pelo item "Meu perfil" no menu do avatar. Quatro boxes consolidados — **Identificação** (foto, nome completo, telefone, data de nascimento, CPF, RG), **Dados para Reembolso**, **Notificações** e **Ações de Conta** — cada um com seu próprio botão de salvar interno (exceto Ações de Conta, com botões por ação).
- **Configurações da organização via ícone de engrenagem na TopNav** (BK-139): o item de texto "Configurações" da TopNav foi substituído por um ícone de engrenagem próximo ao sino de notificações, visível apenas para administradores e tesoureiros (e superadmin). Libera espaço horizontal na barra e torna explícito que Configurações é restrita por papel.
- **Sub-nav de Configurações reorganizada** (BK-154): nova ordem e nomenclatura — Organização → Usuários → **Contas Bancárias** (renomeada de "Contas") → Categorias → **Fluxo de Aprovações** (renomeada de "Pagamentos e Reembolsos"). A URL antiga `/configuracoes/reembolsos` passa a ser `/configuracoes/aprovacoes`. A sub-nav filtra itens pelo papel: tesoureiro vê 3 (Contas Bancárias, Categorias, Fluxo de Aprovações); admin/superadmin veem todos os 5.
- **Matriz granular de preferências de notificação por usuário** (BK-154): novo bloco na seção "Notificações" do perfil com matriz de 10 eventos × 3 canais (e-mail, WhatsApp, Telegram). Eventos cobertos: 5 de reembolso (submetido, aprovação parcial, aprovado, rejeitado, pago) e 5 de pedidos de pagamento (mesmos estados). Default: tudo ligado. Quando o usuário não tem WhatsApp ou Telegram cadastrado, a coluna correspondente aparece desabilitada visualmente com orientação para cadastrar o contato. As notificações disparadas por reembolsos e pedidos de pagamento agora respeitam estritamente essas preferências — silenciam exatamente os pares `(evento, canal)` desligados pelo usuário.
- **Redirects automáticos preservando query params**: bookmarks e links antigos `/configuracoes/perfil?qs` redirecionam para `/perfil?qs`, e `/configuracoes/reembolsos?qs` para `/configuracoes/aprovacoes?qs` — query string e fragmento são preservados.

### Corrigido
- **Race condition no guard de Configurações** (descoberto em QA pós-implementação): acessar qualquer subrota de `/configuracoes/*` por URL direta (refresh, bookmark, link colado no navegador) bloqueava admin e tesoureiro com toast "Acesso restrito" mesmo tendo permissão. O guard agora aguarda o carregamento dos papéis do usuário antes de avaliar — array vazio durante loading não dispara mais redirect indevido.
- **Falha silenciosa ao salvar Notificações com WhatsApp vazio** (descoberto em QA pós-implementação): salvar a seção Notificações sem número de WhatsApp cadastrado falhava silenciosamente no servidor (a matriz salvava, a chamada de contato dava erro 400 invisível ao usuário). A função de preferências passou a tratar valor nulo como remoção da chave; o formulário só envia a chamada de contato quando o valor de fato muda.

## [0.11.0] — 2026-05-18

### Adicionado
- **Pedidos de pagamento recorrentes** (BK-155): agora é possível solicitar pagamentos que se repetem ao longo do tempo (ex: conta de energia, internet, mensalidade). Ao criar uma solicitação, o usuário escolhe entre três tipos — único, recorrente ou parcelado — e configura a frequência (mensal, semanal, quinzenal, bimestral, trimestral, semestral, anual) e a duração (data final, quantidade de ocorrências ou indefinido até cancelar). A aprovação cria a série inteira e o tesoureiro paga ocorrência a ocorrência via Movimentações.
- **Pedidos de pagamento parcelados** (BK-155): solicitação parcelada (ex: compra em 6×) com aprovação única; cada parcela vira um lançamento pendente com data e valor ajustáveis individualmente no momento da criação. Útil para compras de equipamentos ou contratos divididos em prestações.
- **Movimentações recorrentes com duração indefinida** (BK-155): admin e tesoureiro agora podem criar lançamentos recorrentes diretos sem precisar definir data final ou quantidade — opção "Indefinido até cancelar" no fim da série. Gera lote inicial de 12 ocorrências; renovação manual fica como tech debt explícito.
- **Detalhe do pedido recorrente/parcelado com seção "Ocorrências"** (BK-155): lista todas as ocorrências geradas com data prevista, valor estimado, valor real, status individual, conta e data de pagamento. Cada linha tem ações contextuais (Marcar como paga, Ver movimento, Cancelar esta ocorrência) conforme status e papel do usuário.
- **Cancelamento de série com 3 escopos** (BK-155): admin e tesoureiro podem cancelar uma ocorrência específica, todas as ocorrências futuras a partir de uma data, ou a série inteira. Ocorrências já pagas não podem ser canceladas (apenas estornadas via Movimentações).
- **Link cruzado entre lançamentos e pedidos** (BK-155): o detalhe de uma movimentação que veio de um pedido de pagamento aprovado exibe link "Ver pedido de pagamento" para navegação direta ao detalhe da solicitação original.
- **Lista de Pagamentos type-aware** (BK-155): cada linha exibe indicador discreto do tipo (Recorrente · mensal, Parcelado · 6×) e a coluna de valor mostra a representação adequada (R$ X/mês · est. R$ Y para recorrente; R$ X/parcela · total R$ Y para parcelado).
- **Paleta semântica de badges de status** (parte de BK-155): badges de status passaram a usar cores semânticas distintas — teal sólido para pago/aprovado, laranja para pendente/aguardando, vermelho para atrasado/rejeitado, roxo para estornado, cinza para cancelado/rascunho. Facilita leitura rápida das listagens.

### Corrigido
- **Anexos obrigatórios para envio de pedido** (BK-155): submeter um pedido de pagamento para aprovação sem nenhum comprovante anexado passa a ser bloqueado, com mensagem clara. Salvar como rascunho continua sem essa exigência. Validação reforçada tanto no formulário quanto na função de servidor.
- **Solicitante não vê mais Aprovar/Reprovar no próprio pedido** (BK-155): no detalhe e na lista de pedidos, o autor da solicitação não vê mais os botões de aprovação ou reprovação na própria solicitação — comportamento alinhado com o já existente em Reembolsos.

## [0.10.8] — 2026-05-18

### Adicionado
- **Histórico de auditoria na página de detalhe do lançamento** (BK-161): a página de detalhe em `/movimentacoes` foi reorganizada em duas colunas — conteúdo principal à esquerda e um card "Auditoria" à direita com a timeline de eventos do lançamento (quem criou, marcou como pago, estornou, cancelou, etc.), com nome do responsável e data/hora de cada ação. Em mobile as colunas empilham verticalmente. A seção "Criado em / Criado por" anterior foi removida — a informação agora aparece na timeline. Lançamentos sem eventos registrados exibem mensagem de fallback.

## [0.10.7] — 2026-05-18

### Adicionado
- **Contagem de itens nas abas de `/reembolsos`** (BK-097, conclusão): abas de `/reembolsos` passam a exibir contagem entre parênteses, completando a implementação iniciada na v0.10.6. A query passou a carregar todos os reembolsos da OSC de uma vez; filtragem por aba e contagens são derivadas client-side via `useMemo`. O recorte por papel do usuário continua transparente via RLS.

## [0.10.6] — 2026-05-18

### Adicionado
- **Contagem de itens nas abas de listagem** (BK-097, parcial): as abas de status em `/movimentacoes`, `/pagamentos` e `/superadmin/organizacoes` passam a exibir o total de itens entre parênteses ao lado do rótulo — ex: "Pendente (5)", "Pago (30)". As contagens são derivadas dos dados já carregados no cliente, sem queries adicionais. Em `/movimentacoes` a contagem considera os filtros de período e busca ativos.

### Corrigido
- **Tipo de organização exibido como snake_case em `/superadmin/organizacoes`** (BK-097): a coluna Tipo agora exibe labels legíveis (`grupo_escoteiro` → "Grupo Escoteiro", `associacao` → "Associação", etc.) com fallback para titlecase em valores desconhecidos.

## [0.10.5] — 2026-05-18

### Adicionado
- **Flag de auditoria para auto-aprovações** (BK-105): quando o solicitante aprova o próprio pedido por ser o único aprovador elegível — situação permitida pelo sistema — as EFs `approve_reimbursement` e `approve_purchase_order` passam a gravar uma linha adicional no `audit_log` com `metadata.self_approved = true`. Aprovações normais seguem sem essa marca. Facilita a revisão pela comissão fiscal sem necessidade de cruzar manualmente os dados de solicitante e aprovador.

## [0.10.4] — 2026-05-18

### Corrigido
- **Auto-aprovação em pedidos de pagamento** (BK-127): confirmado que a EF `approve_purchase_order` já valida a elegibilidade antes de qualquer gravação no banco — a auto-aprovação é bloqueada quando existem outros aprovadores elegíveis, e permitida quando o solicitante é o único. Comportamento idêntico ao módulo de reembolsos. Nenhuma alteração de código necessária; bump de versão para registrar a validação.
- **Link "Meu perfil" no menu do avatar** (BK-162): o menu dropdown do avatar no menu superior agora exibe "Meu perfil" (navega para Configurações → Perfil) além de "Sair".
- **Título da aba de workflow de aprovação** (BK-147): rótulo corrigido de "Workflow de aprovação de reembolsos" para "Fluxo de aprovação de pagamentos e reembolsos", refletindo que a aba controla o fluxo de ambos os módulos.
- **Fotos de usuários na lista de Configurações → Usuários** (BK-163): avatares na listagem de membros passam a exibir a foto cadastrada; iniciais continuam como fallback quando não há foto. Mesma correção já aplicada ao avatar do menu superior na v0.10.1.

## [0.10.3] — 2026-05-18

### Adicionado
- **Atalhos de período no filtro de Movimentações** (BK-145): além de escolher datas customizadas, o filtro agora oferece atalhos contábeis em um clique — Mês atual, Mês anterior, Trimestre atual, Trimestre anterior, Semestre atual, Ano atual (YTD), Ano anterior, Personalizado e Todos. Cálculo baseado em trimestres e semestres calendário (T1: jan-mar, T2: abr-jun, etc.). Selecionar um atalho preenche as datas automaticamente; editar manualmente as datas troca o filtro para "Personalizado".

### Modificado
- **Filtro de Movimentações abre por padrão em "Mês atual"** em vez de "Todos" — visão operacional do dia a dia é mais comum no fluxo do tesoureiro.

## [0.10.2] — 2026-05-18

### Corrigido
- **Badge "Estornado" volta a aparecer também no lançamento contrário** (BK-160, regressão da v0.10.1): a release anterior introduziu o badge no lançamento original mas a regra de detecção não cobria o lançamento contrário gerado pelo estorno; agora ambos exibem o badge corretamente.

## [0.10.1] — 2026-05-18

Primeira release versionada após a transição de `v0.10 (beta)` para semver puro. Consolida correções de UX no módulo de Movimentações, melhorias no menu superior, publicação dos documentos legais e do manual em domínio próprio, e a primeira preparação do fluxo Google em `/setup` para auto-conclusão (validação E2E pendente). A partir desta versão, marcadores como "(beta)" não fazem mais parte da string da versão.

### Adicionado
- **Avatar do usuário no menu superior** (BK-141): a foto cadastrada em Configurações → Perfil agora aparece no avatar do menu superior em qualquer cenário em que a tela de perfil também exibe a foto; ao trocar a foto, o menu superior atualiza imediatamente sem precisar de F5. Iniciais continuam como fallback quando não há foto.
- **Badge "Recorrente" em lançamentos recorrentes** (BK-158): movimentos pertencentes a uma série recorrente não-parcelada passam a exibir um badge "Recorrente" ao lado do título, em `/movimentacoes` (lista e detalhe). Visibilidade rápida do contexto sem precisar abrir o detalhe.
- **Manual do Usuário publicado** (BK-137): novo manual público em `https://docs.bf.rit.org.br/` cobrindo primeiros passos, movimentações, reembolsos, pagamentos, configurações da OSC, papéis e FAQ. Link no rodapé da aplicação.
- **Política de Privacidade e Termos de Uso publicados** (BK-094): documentos legais publicados em `https://docs.bf.rit.org.br/privacidade/` e `/termos/`. Links discretos no rodapé da aplicação.
- **Documentação em domínio próprio** (BK-153): substituído o domínio padrão do GitHub Pages por `docs.bf.rit.org.br` (Cloudflare DNS + custom domain + HTTPS ativo). Links de Política, Termos e Manual no rodapé já apontam para o novo domínio.

### Corrigido
- **Troca de OSC pelo seletor agora atualiza a tela automaticamente** (BK-151): selecionar outra OSC no menu superior recarrega imediatamente todas as páginas (painel, movimentações, reembolsos, pagamentos, configurações) sem precisar de F5. Antes, a página atual mantinha os dados da OSC anterior até refresh manual.
- **Badge "Parcela X de N" voltou a aparecer** (BK-157): em lançamentos parcelados, o badge "Parcela X de N" deixou de ser exibido em algum refactor recente; foi restaurado. Causa raiz: a fonte de dados parou de expor a informação da série parcelada.
- **Badge "Estornado" agora aparece em ambos os lançamentos** (BK-156): ao estornar um pagamento, tanto o lançamento original quanto o contrário (gerado pelo estorno) passam a exibir o badge "Estornado". Antes só o contrário recebia o badge, dando a falsa impressão de que o original ainda estava "pago" sem indicação. O status no banco do lançamento original permanece "pago" — só a visualização ganha o badge adicional.
- **"Continuar com Google" em `/setup` redireciona corretamente para o painel** (BK-144): no fluxo de configuração inicial via convite, o usuário que escolhia "Continuar com Google" voltava para o formulário de senha em vez de seguir para o painel; agora o cadastro é concluído automaticamente com o nome e a foto do perfil Google e o usuário entra direto no painel. **Validação E2E com convite real pendente em BK-152 antes de declarar verificado.**
- **Link "Manual do Usuário" no rodapé** apontava para `/manual` (404); corrigido para apontar para a raiz do site de docs.

### Modificado
- **Formato da string da versão**: passou de `v0.10 (beta)` para `v0.10.1`. Padronizado em semver puro (MAJOR.MINOR.PATCH); marcadores como "(beta)" não fazem mais parte da string da versão exibida no rodapé e nos feedbacks. A natureza piloto/beta do projeto passa a ser sinalizada (quando necessário) fora da string da versão.

---

### Adicionado (Documentação pública — 2026-05-15)
- **Site de documentação multi-página** em `https://rit-df.github.io/bussola-docs/`: substituído o manual em página única por site Jekyll com navegação por abas (Início, Primeiros Passos, Módulos, Configurações, Papéis, FAQ, Changelog, Legal); cada módulo e aba de configurações tem página dedicada
- **Sub-navegação por seção**: pills de navegação abaixo do título em todas as páginas de Módulos, Configurações e Legal, permitindo navegar entre páginas da seção sem sair da tela
- **Screenshots de configurações** sem dados pessoais: Organização, Contas, Categorias, Fluxo de Aprovação — imagens capturadas com dados fictícios; abas Perfil e Usuários sem screenshot (dados reais visíveis)

### Corrigido (Documentação pública — 2026-05-15)
- **Links absolutos quebrados no GitHub Pages**: 10 links com caminhos absolutos (`/configuracoes/perfil/` etc.) geravam 404; convertidos para caminhos relativos em 8 arquivos
- **Screenshot de perfil com dados pessoais reais**: `manual-09-config-perfil.png` continha telefone, e-mail e CPF reais; arquivo removido e referência eliminada da página de perfil

### Adicionado (Onda 4 — Pedidos de Pagamento)
- **Módulo de Pedidos de Pagamento**: novo módulo completo para solicitação formal de pagamentos a fornecedores e prestadores externos, com fluxo de aprovação configurável e lançamento automático em `financial_movements`; tabelas `purchase_orders`, `purchase_order_approvals`, `purchase_order_attachments`; EFs `submit_purchase_order`, `reject_purchase_order`, `approve_purchase_order`, `pay_purchase_order`; `movement_origin` estendido com valor `purchase_order`
- **Página `/pagamentos` unificada**: abas "Pedidos de pagamento" e "Reembolsos" (aba de reembolsos reutiliza componente existente sem alteração); sub-abas por status (Todos / Rascunho / Aguardando aprovação / Aprovado / Rejeitado / Pago); cards-resumo condicionais ao papel (aprovador, tesoureiro, todos); coluna Ações com botões Aprovar / Reprovar condicionais ao papel e status; ícone "Marcar como pago" não aparece na lista — pagamento é confirmado via `/movimentacoes` (igual a Reembolsos)
- **"Boleto" como forma de pagamento** (pós-lançamento Onda 4): formulário de criação e edição inline do pedido oferecem três opções — PIX, TED, Boleto; selecionar Boleto não exibe campos extras (o arquivo é anexado na seção Documentos); `vendor_payment_info` grava `{ method: 'boleto' }` sem campos adicionais
- **Redirect `/reembolsos`**: rota redireciona automaticamente para `/pagamentos?tab=reembolsos`; links existentes e rotas `/reembolsos/novo` e `/reembolsos/:id` permanecem funcionais
- **Formulário `/pagamentos/novo`**: criação e edição de rascunho com CRUD direto via Supabase client; carregamento de rascunho via `?id=` na URL; campos PIX/TED do fornecedor (sem pré-população do perfil do usuário); uploader com prefixo `purchase-orders/`; botões "Salvar rascunho" e "Enviar para aprovação" com validação por campo
- **Página `/pagamentos/:id`**: detalhe completo com 4 zonas (header, dados, documentos, timeline + ações); preview inline de imagens (thumbnails clicáveis, fallback) e PDF (iframe lazy); ações condicionais — "Editar e reenviar" (solicitante), "Aprovar" / "Reprovar" (aprovador elegível); dados PIX/TED do fornecedor ocultos para voluntários; seção de anexos denominada "Documentos"
- **TopNav**: item "Reembolsos" renomeado para "Pagamentos e Reembolsos"; badge soma pedidos de pagamento aguardando + reembolsos aguardando (ambos os módulos); RPC `count_pending_purchase_orders_for_user` criada
- **Configurações**: aba "Reembolsos" renomeada para "Pagamentos e Reembolsos"; nova subseção "Quem pode solicitar pagamentos" com checkboxes por papel (persiste em `reimbursement_workflow.allowed_requester_roles`; default: Presidente, Tesoureiro, Coordenador de Projeto)
- **Painel**: nova seção "Pedidos de pagamento" com cards condicionais ao papel (aguardando aprovação, aprovados aguardando pagamento, solicitado por mim)

### Adicionado
- **"Continuar com Google" em `/setup`**: usuários convidados podem concluir o primeiro acesso autenticando via Google OAuth em vez de definir senha; botão visível e habilitado somente após aceite da política de privacidade; `setup_token` e versão da política preservados em `sessionStorage` através do redirect OAuth; `complete_setup` valida `claims.sub === uo.user_id` para garantir que a conta Google corresponde ao convite; campo "Nome completo" pré-populado com o nome do perfil Google (editável); campos de senha ocultados no fluxo Google
- **Upsert de `full_name` em `user_profile` ao concluir setup**: `complete_setup` agora grava `user_profile.full_name` em ambos os fluxos (senha e Google) após transição bem-sucedida; fechou lacuna pré-existente onde o nome era salvo apenas em `auth.user_metadata`
- **Canal de feedback de usuários — chip no TopNav**: botão/badge laranja "💬 Feedback" no TopNav, visível para todos os papéis autenticados; abre o `FeedbackModal` ao ser clicado
- **`FeedbackModal`**: modal com grade 2×2 de tiles de categoria (🐛 Bug / 💡 Sugestão / 👍 Elogio / ❓ Outro), textarea de mensagem livre, rodapé com identidade do usuário ("Enviado como [nome] · [e-mail]") e insert direto em `user_feedback` via Supabase client (RLS); toast de confirmação ao enviar; campos limpos ao reabrir
- **Tabela `user_feedback`**: armazena feedbacks com `user_id`, `organization_id`, `category`, `message`, `resolved` (default `false`), `resolved_at`; RLS: INSERT para qualquer autenticado com `user_id = auth.uid()`; SELECT e UPDATE restritos ao superadmin
- **Página `/superadmin/feedbacks`**: tabela com colunas Data, Categoria (badge colorido), Mensagem, Usuário (nome + e-mail), OSC, Resolvido; ordenação automática (não-resolvidos mais novos primeiro, resolvidos ao final); checkbox "Resolvido" executa UPDATE + re-fetch; linha resolvida fica tachada e com opacidade reduzida; contador de itens pendentes no topo
- **Seção "Alterar senha" em `/configuracoes/perfil`**: campos "Nova senha" e "Confirmar nova senha", botão "Alterar senha"; chama `supabase.auth.updateUser({ password })`; erro `weak_password` (HIBP) exibido inline abaixo do campo; sucesso limpa os campos e exibe toast de confirmação
- **Orientação de criação de senha** em `/setup` e em `/configuracoes/perfil`: texto estático "Use ao menos 8 caracteres combinando letras maiúsculas, minúsculas, números e símbolos. Evite senhas comuns." abaixo do campo de senha; substituído por erro inline quando há falha de validação
- **Seção "Dados para reembolso" em `/configuracoes/perfil`**: seletor PIX ou TED, campos condicionais (tipo de chave + valor para PIX; banco/agência/conta para TED), todos opcionais, botão de salvar próprio desabilitado quando não há alteração; lê e grava em `user_profile.default_payment_info` (JSONB) via `useUpdateProfile`; formato compatível com `paymentFromProfile` no formulário de reembolso — prefill automático funciona sem alteração adicional

### Corrigido (pós-lançamento Onda 4 — 2026-05-15)
- **EF `approve_purchase_order` retornava HTTP 500 em toda tentativa de aprovação** (BK-132): a CHECK constraint `fm_account_required_unless_pending_reimbursement` em `financial_movements` só permitia `account_id = NULL` para `origin = 'reimbursement'`; pedidos de pagamento aprovados (origin `purchase_order`) sem conta definida violavam a constraint ao criar o movimento financeiro; corrigido via migration que estendeu a constraint para também aceitar `purchase_order` pendente sem `account_id` — mesmo comportamento já permitido para reembolsos; a EF já passava todos os campos corretamente (prompt #134)
- **Card "AGUARDANDO MINHA APROVAÇÃO" exibia `[object Object][object Object]`** (BK-129): renderização incorreta do retorno da RPC `count_pending_purchase_orders_for_user` no componente de card; corrigido para extrair corretamente o campo numérico (prompt #131)
- **Layout do formulário de pedido de pagamento divergia do formulário de reembolso** (BK-133): DESCRIÇÃO aparecia como textarea grande no topo, antes de DATA DA DESPESA e VALOR; reordenado para DATA DA DESPESA + VALOR no topo, DESTINATÁRIO, DESCRIÇÃO (campo de linha única), CATEGORIA/PROJETO/CENTRO DE CUSTO, DADOS DE PAGAMENTO, OBSERVAÇÕES, DOCUMENTOS — igual ao padrão de `/reembolsos/novo` (prompt #135)

### Modificado (pós-lançamento Onda 4 — 2026-05-15)
- **Rótulo da seção de anexos em pedidos de pagamento**: "COMPROVANTES / NF" substituído por "Documentos" em todos os contextos do módulo (formulário de criação, formulário de edição inline, página de detalhe) — mesma terminologia de Reembolsos (prompt #133)
- **Fluxo de confirmação de pagamento de pedidos**: botão "Confirmar pagamento" removido da coluna AÇÕES da lista `/pagamentos`; o tesoureiro confirma o pagamento diretamente na movimentação financeira gerada em `/movimentacoes` (ícone "Marcar como pago"), igual ao fluxo de Reembolsos; a EF `pay_purchase_order` permanece deployada mas sem ponto de entrada no frontend atual (prompt #133)

### Corrigido
- **Botões "Aprovar"/"Reprovar" não apareciam para aprovadores elegíveis na lista de reembolsos** (BK-123): query do workflow de aprovação (`wfQ`, `organization_settings?key=eq.reimbursement_workflow`) não disparava na `ReembolsosListPage` por problema de timing do React Query — `enabled: !!activeOrganizationId` nunca transitava para `true` a tempo; corrigido para aguardar o `activeOrganizationId` antes de executar o fetch; `isEligibleApprover` agora calcula sobre os dados reais da OSC em vez do `EMPTY_WORKFLOW` padrão; regra de auto-aprovação (não ver botões no próprio reembolso) preservada (prompt #119)
- **Badge de reembolsos pendentes na TopNav não atualizava após aprovação/rejeição** (BK-125): mutations de aprovação e rejeição não invalidavam a query que alimenta o badge; corrigido para invalidar também essa query ao concluir cada mutation com sucesso (prompt #122)
- **Dialog "Reprovar solicitação" — botão habilitado sem motivo** (BK-124): o botão "Confirmar reprovação" estava habilitado mesmo com o campo "Motivo" vazio; corrigido para desabilitar enquanto o campo estiver vazio ou só com espaços (prompt #121)
- **Datas exibidas com 1 dia a menos** (BK-121): `formatDate()` em `shared/lib/format.ts` convertia strings ISO date-only (`"YYYY-MM-DD"`) via `new Date(value)`, que o JavaScript interpreta como UTC midnight; em UTC-3, isso recuava a exibição para o dia anterior. Corrigido detectando o padrão `YYYY-MM-DD` e construindo o `Date` com componentes locais (sem conversão de timezone). Afetava: coluna "Data da despesa" em `/reembolsos`, detalhe do reembolso (`/reembolsos/:id`) e campos Vencimento/Pagamento/Competência em `/movimentacoes/:id`. A lista de movimentações não era afetada (usava `parseISO` do date-fns) (prompt #120)
- **E-mail de convite não chegava ao usuário convidado**: `add_user_to_organization` chamava `send_email` com `Authorization: Bearer SERVICE_ROLE_KEY`; após migração do Supabase para chaves `sb_secret_*` (não-JWT), o gateway rejeitava com 401 antes do código rodar — invitation era criada mas `email_send_log` ficava vazio; corrigido com autenticação Bearer correta + try/catch que grava `failed_all` em `email_send_log` em caso de qualquer falha de chamada
- **`send_email` rejeita chamadas sem JWT**: `verify_jwt = false` declarado explicitamente em `config.toml` para `send_email` e `complete_setup`; autenticação manual aceita Bearer == `SUPABASE_SERVICE_ROLE_KEY` (server-to-server) ou JWT com `app_metadata.is_superadmin = true` (página de teste)
- **Cancelar convite retornava "Não foi possível aplicar a alteração"**: transição `active_pending_setup → removed` estava ausente dos pares válidos na função SQL `_valid_uo_transition`; adicionada via migration; handler do `MemberActionsMenu` agora também marca `invitations.status = revoked` após a transição
- **Botão "Reenviar e-mail de convite" não era clicável**: condição de `disabled` ausente ou incorreta no `MemberActionsMenu` para membros em `active_pending_setup`; corrigido com `disabled={busy}` explícito durante a chamada; `resend_setup_token` usa o mesmo helper `invokeSendEmail` de `add_user_to_organization` com try/catch + `logEmailAttempt('failed_all')` para rastreabilidade em `email_send_log`
- **`complete_setup` retornava "Erro inesperado" para senha rejeitada pelo HIBP**: EF mascarava o `error_code` real do Supabase Auth como 500 genérico; agora propaga o `error_code` original (incluindo `weak_password` com status 422 e mensagem em pt-BR); demais erros do GoTrue também passam adiante o `error_code` real
- **Nome preenchido no setup não era salvo**: `complete_setup` não executava `UPDATE user_profile SET full_name` após a transição; corrigido para gravar o nome enviado no payload
- **Nome não persistia em `/configuracoes/perfil`** (toast de sucesso mas campo voltava vazio ao recarregar): `UPDATE` em `user_profile` retornava 0 linhas — linha ausente ou RLS bloqueando silenciosamente; corrigido com upsert e/ou ajuste de policy
- **Tela em branco em `/configuracoes/reembolsos`** após 1-2 segundos de exibição: violação das Rules of Hooks — `useMemo` e `memberById` estavam declarados após early returns no `ConfiguracoesReembolsosPage`, causando contagem diferente de hooks entre renders e desmonte da árvore pelo React; corrigido movendo todos os hooks para antes de qualquer `return` condicional
- **Tela em branco em `/reembolsos/:id`** ao navegar via SPA (funcionava com F5): efeito cascata do bug anterior — o estado degradado do React contaminava navegações subsequentes na mesma sessão; resolvido com a correção do bug de Rules of Hooks acima

---

### Adicionado (Onda 2 — melhorias pós-lançamento)
- **Botão "Salvar e fazer outro"** no formulário de novo lançamento (`/movimentacoes/novo`): salva e reinicia o formulário mantendo tipo e conta — sem redirecionar para a lista; útil para lançamentos em sequência (prompt 69)
- **Indicação de filtros ativos** abaixo dos cards de totais: quando qualquer filtro está ativo (`isDefault = false`), exibe linha discreta "Filtrado por: [rótulos]" concatenados com " · "; desaparece ao limpar filtros (prompt 70)
- **Ordenação por coluna** na tabela de movimentações: Vencimento, Valor, Status e Conta ordenáveis com ciclo ASC → DESC → sem ordenação; indicador de direção no header ativo; ordenação client-side preservada ao trocar aba ou filtro (prompt 71)
- **EF `delete_movements`**: substitui `bulk_update_movements` com `p_action: 'delete'` para exclusão de lançamentos; coleta `storage_path` de `financial_movement_attachments`, remove arquivos do bucket `movement-attachments` (falha individual não aborta), deleta lançamentos por CASCADE; retorna `{ ok, deleted, storage_cleaned }`; validação de ownership e limite de 500 IDs por chamada (prompt 72)
- **Coluna "Pagamento"** na tabela de movimentações, entre "Vencimento" e "Lançamento": exibe `payment_date` formatada; "—" quando não pago; ordenável com nulos por último no ASC (prompt 73)
- **Ordenação por Categoria** na tabela de movimentações: ordena pelo nome da primeira categoria; splits com múltiplas categorias usam a primeira como critério (prompt 73)
- **Ícones de ação por linha** na tabela de movimentações: coluna "Ações" ao final da tabela (após Valor), sempre visível sem hover; ícone de lápis (editar) em todas as linhas; ícone contextual por status — cancelar (`pendente`/`atrasado`), estorno (`pago`/`efetivado`), lixeira (`cancelado`/`estornado`); clicar abre o mesmo fluxo de confirmação existente (prompt 74)

### Corrigido
- `canDelete()` em `movementActions.ts` expandido para incluir `cancelado` e `estornado` — lançamentos finalizados podem ser excluídos (prompt 75)
- Texto do dialog de confirmação de exclusão em lote corrigido: não menciona mais restrição de status (herdado da RPC antiga) (prompt 75)
- Botão "Excluir" na tela de detalhe (`/movimentacoes/:id`) movido para fora do bloco condicional `!finalized`, tornando-o visível e habilitado para lançamentos `cancelado` e `estornado` (prompt 77)
- Tooltip do botão "Excluir" para lançamentos `pago` atualizado para mensagem coerente com a nova lógica de elegibilidade (prompt 77)

### Modificado
- **Exportação Excel**: pacote `xlsx` (SheetJS, abandonado, vulnerabilidades Prototype Pollution + ReDoS) substituído por `exceljs` (mantido ativamente); comportamento idêntico — mesmo arquivo, colunas e formatação (prompt 76)
- **Ícone de olho (visualizar)** removido das linhas da tabela de movimentações — redundante com o clique na linha; mantido apenas o lápis (editar) (prompt 74)
- **Exclusão de lançamentos** (individual e em lote) migrada da RPC `bulk_update_movements` para a EF `delete_movements`; `bulk_update_movements` continua sendo usada exclusivamente para `mark_paid` (prompt 72)

---

## [v0.9.11] — 2026-05-14 · `onda3-st9.11-configuracoes-reembolsos`

### Adicionado
- **Aba "Reembolsos" em `/configuracoes`** (admin-only): seletor de aprovações necessárias (1 ou 2), checkboxes de papéis elegíveis (Dirigente, Tesoureiro), busca de pessoas específicas como aprovadores independente de papel, lista consolidada "Quem pode aprovar" com origem indicada (papel/pessoa), alerta âmbar quando nenhum aprovador configurado
- Botão Salvar habilitado apenas quando há alteração (`isDirty`) e ao menos um aprovador; mensagem inline "Selecione ao menos um papel ou uma pessoa aprovadora" quando inválido
- Persistência via `set_organization_settings_bulk` com chave `reimbursement_workflow`; leitura via `read_organization_settings` com query própria e filtro client-side

---

## [v0.9.10] — 2026-05-14 · `onda3-st9.10-painel-badge`

### Adicionado
- **Seção "Reembolsos" no `/painel`**: até 3 cards condicionais por papel — "Meus reembolsos pendentes" (rascunhos + rejeitados), "Aguardando minha aprovação" (aprovadores elegíveis) e "Aguardando pagamento" (tesoureiros); cada card clicável navega para `/reembolsos?tab=<status>`
- **Badge real no TopNav**: exibe contagem com prioridade aprovador→tesoureiro→voluntário; oculto quando a contagem relevante = 0
- **RPC `count_pending_reimbursements_for_user(p_org_id)`** (SECURITY DEFINER): retorna `{ volunteer_pending, approver_pending, treasurer_pending }` para o caller autenticado; lê `reimbursement_workflow` para determinar elegibilidade do aprovador
- **Hook `useReimbursementsCounts`** compartilhado entre `/painel` e TopNav (`staleTime: 30s`); elimina chamada dupla à RPC

---

## [v0.9.9] — 2026-05-14 · `onda3-st9.9-edicao-inline-rejeicao`

### Adicionado
- **Edição inline após rejeição** em `/reembolsos/:id`: botão "Editar e reenviar" habilitado para requester quando status = `rejeitado`; expande `EditAndResubmitForm` inline com motivo da rejeição em destaque, campos pré-populados do reembolso e gestão de comprovantes sem ensureDraft
- Sequência de salvamento: `update_reimbursement` → `submit_reimbursement`; em sucesso, página recarrega em `aguardando_aprovacao`
- Botão "Cancelar" recolhe sem salvar; `EditAndResubmitForm` isolado em `Card` próprio abaixo do grid

---

## [v0.9.8] — 2026-05-14 · `onda3-st9.8-preview-comprovantes`

### Adicionado
- **Preview inline de comprovantes** em `/reembolsos/:id`: thumbnails automáticos para imagens (clicáveis para ampliar, fallback textual), botão lazy "Visualizar/Ocultar PDF" com iframe; outros tipos mantêm apenas download
- **Botão "Editar rascunho"** (correção de gap — prompt 85b): em `/reembolsos/:id` com status = `rascunho`, requester navega para `/reembolsos/novo?id=<uuid>`; formulário carrega dados existentes, reutiliza o mesmo ID para uploads e salvamentos

---

## [v0.9.7] — 2026-05-14 · `onda3-st9.7-pay-reimbursement`

### Adicionado
- **EF `pay_reimbursement`**: tesoureiro confirma pagamento; cria `financial_movement` com `origin = 'reimbursement'`; salva `paid_movement_id` no reembolso (link reverso); rollback best-effort do movimento em caso de falha posterior; notifica solicitante via `send_notification`
- **Ação "Confirmar pagamento"** em `/reembolsos/:id`: select de conta financeira + data de pagamento; coordenado com Aprovar/Rejeitar; invalida caches de `financial-movements` e `account-balances`

---

## [v0.9.6] — 2026-05-14 · `onda3-st9.6-approve-reimbursement`

### Adicionado
- **EF `approve_reimbursement`**: voto duplo retorna 409; suporta quorum parcial (notifica aprovadores restantes) e quorum final (notifica solicitante + tesoureiros); voto prévio do mesmo aprovador bloqueia com 409 distinto
- **Ação "Aprovar"** em `/reembolsos/:id`: comentário opcional, detecção de voto prévio desabilita botão, toasts diferenciados para aprovação parcial e final

---

## [v0.9.5] — 2026-05-14 · `onda3-st9.5-detalhe-rejeicao`

### Adicionado
- **Página `/reembolsos/:id`**: 4 zonas — header (status, solicitante, valor), dados (campos + dados de pagamento condicionais por papel), comprovantes e timeline + ações
- **EF `reject_reimbursement`**: registra motivo em `reimbursement_approvals`, transiciona para `rejeitado`, notifica solicitante; motivo obrigatório
- **`lib/eligibility.ts`**: helper reutilizável com `isApprover(roles, userId, workflow)` e `canSeePayment` — única fonte da verdade para elegibilidade na UI (reutilizado em ST-9.6, ST-9.7, ST-9.10 e ST-9.11)
- Dados de pagamento PIX/TED ocultos para voluntários; visíveis apenas para aprovadores elegíveis e tesoureiro

---

## [v0.9.4] — 2026-05-14 · `onda3-st9.4-formulario-submit`

### Adicionado
- **Formulário `/reembolsos/novo`**: data, valor, descrição, categoria, projeto, centro de custo, observações, método de pagamento PIX/TED com campos condicionais; dados pré-populados do perfil com checkbox "Salvar como padrão"; uploader com auto-create de registro rascunho
- **RPCs `create_reimbursement` / `update_reimbursement`** (SECURITY INVOKER): criação e edição de reembolsos com validação de organização
- **EF `submit_reimbursement`**: valida diff vs. snapshot da rejeição anterior, limpa `reimbursement_approvals` da rodada, transiciona para `aguardando_aprovacao`, notifica aprovadores elegíveis
- 3 storage policies para prefixo `reimbursements/{org_id}/{reimbursement_id}/` no bucket `movement-attachments`

### Corrigido
- Rotas `/reembolsos`, `/reembolsos/novo` e `/reembolsos/:id` ausentes do `App.tsx` após ST-9.3 — registradas via prompt de continuação 81c

---

## [v0.9.3] — 2026-05-14 · `onda3-st9.3-rotas-lista`

### Adicionado
- **Listagem `/reembolsos`**: 6 tabs por status (todos, rascunho, aguardando_aprovacao, aprovado, rejeitado, pago) persistidas via `?tab=`; coluna "Solicitante" condicional ao papel; item "Reembolsos" com badge no TopNav (placeholder — badge real na ST-9.10)
- Rotas `/reembolsos`, `/reembolsos/novo` e `/reembolsos/:id` registradas em `App.tsx`

---

## [v0.9.2] — 2026-05-14 · `onda3-st9.2-send-notification`

### Adicionado
- **EF `send_notification`** (infraestrutura global reutilizável por todos os módulos): e-mail ativo via `nodemailer@6.9.14`/STARTTLS reutilizando `_shared/smtp.ts`; push/Telegram/WhatsApp como stubs; despacho paralelo por destinatário e canal; `audit_log` por par (destinatário, canal); HTTP 200 exceto 400 de validação de input
- Interface: `{ organization_id, event_type, recipients: [{ user_id, channels? }], payload: { title, body, link?, data? } }`
- Default quando `notification_preferences` ausente: todos os canais habilitados; skip silencioso quando preferência é false ou dado de contato ausente no perfil

---

## [v0.9.1] — 2026-05-14 · `onda3-st9.1-schema-base`

### Adicionado
- **Schema base de reembolsos**: enum `reimbursement_status` (rascunho → aguardando_aprovacao → aprovado → rejeitado → pago); tabelas `reimbursements`, `reimbursement_approvals`, `reimbursement_attachments` com triggers `updated_at` e auditoria (reuso das funções existentes); RLS role-aware (voluntário vê apenas os próprios; dirigente/tesoureiro/admin/comissão veem todos da OSC)
- **Chave `reimbursement_workflow`** em `organization_settings` (padrão EAV): `{ required_approvals, allowed_approver_roles, allowed_approver_user_ids }`; padrão `{ required_approvals: 1, allowed_approver_roles: ["dirigente"], allowed_approver_user_ids: [] }`
- Campo `default_payment_info` (JSONB) em `user_profile` para dados de pagamento padrão do usuário: `{ payment_method, pix_key_type, pix_key, bank_name, bank_agency, bank_account }`; UI adicionada em `/configuracoes/perfil` na correção pós-Onda 3

---

## [v0.8.18] — 2026-05-13 · `onda2-st8.18-cancelamento`

### Adicionado
- **Cancelamento de lançamentos**: status `cancelado` suportado pelo trigger `_fm_set_defaults_and_status`; colunas `cancelled_at`, `cancelled_by`, `cancelled_reason` em `financial_movements`; índice parcial em `organization_id WHERE cancelled_at IS NOT NULL`
- **EF `cancel_movement`**: suporta três escopos — `this` (lançamento isolado), `this_and_future` (a partir da posição na série), `all` (toda a série recorrente); filtra apenas elegíveis (`pendente` ou `atrasado`) e retorna `{ cancelled_count, skipped_count }` sem erro para os ignorados; motivo obrigatório
- **Modal de cancelamento** em `/movimentacoes/:id`: campo de justificativa obrigatório, seleção de escopo para séries/parcelamentos, exibição de erro inline quando EF recusa
- **Card de auditoria de cancelamento** na tela de detalhe: exibe data, motivo e nome do responsável (resolvido via `get_user_display_names`)
- **Aba "Cancelados"** na lista de movimentações: tab dedicada com filtro de status `cancelado`; lançamentos cancelados excluídos dos totais das demais abas
- **RPC `get_user_display_names(UUID[])`**: SECURITY DEFINER com verificação de co-membership por organização; retorna `{ id, display_name }` preferindo `full_name` do perfil, depois `email`, depois `—`; usada para resolver `cancelled_by` e `reversed_by` na tela de detalhe
- **Hook `useUserDisplayNames`**: chamada única com array de IDs deduplicados, `staleTime` de 5 min, evita N+1

### Adicionado (habilitação contextual de ações — ST-8.18.1)
- **Helper `movementActions.ts`**: única fonte da verdade para elegibilidade de ações por status — `canDelete`, `canCancel`, `canReverse`, `canMarkPaid`; `disabledReason(action, status)` para tooltips individuais; `bulkEligibility(rows, action)` para ações em lote
- **Matriz de elegibilidade aplicada** em `MovimentoDetailPage` e `BulkActionsBar`: botões Excluir, Cancelar, Estornar e Marcar como pago ficam visíveis mas desabilitados quando a ação não é permitida para o status atual; tooltip explicativo ao passar o cursor; lançamentos `cancelado`/`estornado` não exibem nenhuma ação
- **Regra de lote**: cada botão de ação em lote só habilita se TODOS os selecionados forem elegíveis; tooltip contextual quando desabilitado por seleção mista
- **Botão "Estornar" em lote**: adicionado à `BulkActionsBar`; abre modal com motivo obrigatório; chama `reverse_movement` por ID via `Promise.all`

### Corrigido
- `computeTotals` excluía status `estornado` do cálculo mas não `cancelado` — corrigido para ambos
- `filtersToPayload` não tratava a tab `canceladas` — adicionado override de status análogo ao de `estornadas`

---

## [v0.8.17] — 2026-05-13 · `onda2-st8.17-exportacao`

### Adicionado
- **Botão "Exportar"** na barra de ações da lista com dropdown "Exportar PDF" e "Exportar Excel"; aplica os filtros ativos no momento da exportação
- **Exportação PDF**: EF `export_movements_pdf` chama Gotenberg com HTML renderizado no servidor; inclui cabeçalho (nome da OSC + período + filtros), tabela completa e rodapé com totais; download automático no browser
- **Exportação Excel**: geração client-side via `lib/exportExcel.ts`; colunas Vencimento, Pagamento, Título, Tipo, Status, Conta, Categoria(s), Valor (R$, numérico), Fornecedor, Observações; `derivePeriodLabel` para nome do arquivo (inicialmente SheetJS; migrado para `exceljs` em prompt 76)
- **`lib/periodLabel.ts`**: função `derivePeriodLabel` que infere rótulo legível a partir dos filtros de período ativos (ex: "maio-2026")

### Corrigido
- EF `export_movements_pdf` chamava `list_financial_movements` via service_role, que retorna `auth.uid() = NULL` internamente — corrigido para usar padrão `callerClient` das demais EFs que dependem de `auth.uid()`

---

## [v0.8.16] — 2026-05-13 · `onda2-st8.16-parcelamentos`

### Adicionado
- **Modo "Parcelado" no toggle 3-vias** do formulário de novo lançamento: número de parcelas (2–120), frequência, data da 1ª parcela
- **Tabela de parcelas** editável: datas calculadas pela frequência; valor por parcela editável com validação de soma em tempo real; diferença de centavos alocada na última parcela; linha de soma com indicador vermelho/verde; botão Salvar desabilitado enquanto soma divergir
- **Modal de confirmação**: resumo com count e intervalo de datas antes de criar
- **EF `create_installment_series`**: cria `recurring_series` com `is_installment = TRUE`; cria N `financial_movements` com `origin = 'installment'`, `series_position` e `total_amount` individual; valida que `SUM(installment_amounts) === total_amount` quando editado manualmente (tolerância de centavos); rollback total em caso de erro
- **Edição de parcelamentos via `update_recurring_series`**: escopo `all`/`this_and_future` preserva `total_amount` individual por parcela (sem achatar em valor único)

---

## [v0.8.15] — 2026-05-13 · `onda2-st8.15-acoes-em-lote`

### Adicionado
- **Seleção múltipla na lista de movimentações**: checkbox por linha + checkbox de seleção geral no header (com estado indeterminate); seleção limpa ao trocar de tab, filtro ou organização
- **Barra de ações em lote**: aparece quando ≥ 1 lançamento selecionado; exibe contador "N lançamentos selecionados", botão "Limpar seleção", "Marcar como pago" e "Excluir"
- **Ação "Marcar como pago"**: define `payment_date = hoje` nos selecionados com status `pendente` ou `atrasado`; ignora os demais com aviso no toast (ex.: "3 marcados como pagos. 1 ignorado.")
- **Ação "Excluir"**: confirmação destrutiva com count; exclui apenas `pendente` ou `atrasado`; toast com counts de excluídos e ignorados
- **RPC `bulk_update_movements(p_org_id, p_ids, p_action)`**: executa em transação única; valida membership e `organization_id` por linha; ação `mark_paid` ou `delete`; retorna `{ updated, ignored }`; `REVOKE ALL` + `GRANT EXECUTE TO authenticated`

> **Limitação conhecida:** bulk delete remove registros de `financial_movement_attachments` via CASCADE mas não exclui os arquivos do bucket `movement-attachments` (RPCs não têm acesso ao Storage). Arquivos órfãos serão endereçados em manutenção futura.

---

## [v0.8.13b] — 2026-05-13 · `onda2-melhorias-documentos`

### Adicionado
- **Indicador de documentos na lista** (`/movimentacoes`): ícone de clipe (paperclip) discreto na linha do lançamento quando `attachment_count > 0`; lançamentos sem documentos não exibem nada; campo `attachment_count` adicionado à RPC `list_financial_movements` via subquery `COUNT(*) FROM financial_movement_attachments`

### Modificado
- **Formatos de upload ampliados**: zona de upload aceita qualquer formato exceto executáveis e scripts (`.exe`, `.bat`, `.cmd`, `.msi`, `.sh`, `.ps1`, `.vbs`, `.jar` e similares); limite de 10 MB mantido; mensagem de erro inline "Tipo de arquivo não permitido por segurança." para formatos bloqueados
- **Renomeação "Comprovantes" → "Documentos"**: título do card, estado vazio, mensagem de carregamento e toasts em `MovimentoDetailPage`

### Corrigido
- **Lista de movimentações vazia após adição do `attachment_count`**: `list_financial_movements` usava `row_to_jsonb(x)` que falha com tipos anônimos de subquery em PostgreSQL; substituído por `to_jsonb(x)` (compatível com qualquer tipo, incluindo anônimos)

---

## [v0.8.13] — 2026-05-13 · `onda2-st8.13-comprovantes`

### Adicionado
- **Card "Documentos"** funcional em `/movimentacoes/:id`: lista de anexos com nome do arquivo, tamanho formatado e data de envio; botão "Baixar" (URL assinada temporária do Storage) e botão "Remover" (com confirmação inline que exclui do banco e do bucket)
- **Zona de upload** drag-and-drop e clicável: limite de 10 MB; validação de formato e tamanho com mensagem de erro inline; spinner durante envio; upload para bucket `movement-attachments` no caminho `{org_id}/{movement_id}/{filename}` com sufixo numérico em caso de colisão de nome; registro em `financial_movement_attachments` e atualização da lista sem reload
- Substituição do stub "Nenhum documento anexado" pelo componente funcional; comportamento idêntico para lançamentos de qualquer status

---

## [v0.8.12b] — 2026-05-13 · `onda2-st8.12b-bugfixes-recorrencia`

### Corrigido
- **Substituição de categorias em série**: `replaceCategories` fazia DELETE + INSERT em duas transações separadas; o trigger DEFERRED `validate_split_sum` disparava no commit do DELETE (sum=0) antes do INSERT reinserir as linhas — erro `split_sum_mismatch`. Solução: nova RPC `replace_movement_categories_bulk` que executa DELETE + INSERT atomicamente em uma única função PL/pgSQL.
- **Data de vencimento em edição de série**: `scope='all'` e `scope='this_and_future'` aplicavam o valor absoluto de `due_date` a todos os lançamentos, achatando a distribuição temporal. Solução: cálculo de delta em dias entre a data informada e a `due_date` do lançamento de referência, aplicado individualmente por linha; `payment_date` preservada.

---

## [v0.8.12] — 2026-05-13 · `onda2-st8.12-edicao-recorrencia`

### Adicionado
- **Rota `/movimentacoes/:id/editar`** com `EditarMovimentoPage` e `EditarMovimentoFormPage`
- Formulário de edição pré-preenchido via `get_financial_movement`; reutiliza `CategoriesSplitTable` e helpers de opções do formulário de criação; sem toggle de tipo nem bloco de recorrência
- Guard de status: se o movimento carregado não for 'pendente' ou 'atrasado', redireciona imediatamente para `/movimentacoes/:id` com toast "Este lançamento não pode ser editado."
- Banner discreto no topo indicando o escopo da edição ('apenas este lançamento', 'este e os próximos', 'toda a série')
- Modal de escopo em `MovimentoDetailPage`: RadioGroup com 3 opções ('Apenas este lançamento', 'Este e os próximos', 'Toda a série'), padrão `this`; lançamentos sem `recurring_series_id` navegam direto sem modal
- **EF `update_recurring_series`**: operação atômica para os 3 escopos — `this` aplica dados e desvincula da série em uma única transação; `this_and_future` cria nova `recurring_series` com os movimentos afetados reposicionados; `all` atualiza `template_jsonb` e todos os movimentos da série; a mutation do frontend usa sempre a EF para todos os escopos

---

## [v0.8.11] — 2026-05-13 · `onda2-st8.11-recorrencias`

### Adicionado
- Toggle 3-vias (Único / Parcelado stub / Recorrente) no formulário de novo lançamento
- Bloco de configuração de recorrência: frequência (diária, semanal, quinzenal, mensal, bimestral, trimestral, semestral, anual), data de início, modo de término (por nº de ocorrências ou data-fim)
- Preview dinâmico das próximas datas no bloco de recorrência
- Modal de confirmação antes de salvar série recorrente, com resumo do que será criado
- **EF `create_recurring_series`**: cria `recurring_series` + N `financial_movements` com datas calculadas em UTC; rollback em 3 camadas em caso de erro; suporte a `is_installment` e `total_installment_amount`

---

## [v0.8.10] — 2026-05-13 · `onda2-st8.10-estorno`

### Adicionado
- Modal de estorno em `/movimentacoes/:id` com campo de motivo obrigatório, gate no botão "Confirmar" e exibição de erro inline
- Defesa contra estorno de transferências (bloqueio via validação na EF)
- **EF `reverse_movement`**: validações (não estornado, não transferência), insert do movimento inverso com `origin='reversal'` e `status='pago'`, cópia dos splits, atualização do original com `reversed_at` / `reversed_by_movement_id` / `reversed_reason`, rollback manual em caso de erro; erros 403 e 422 mapeados corretamente

---

## [v0.8.9] — 2026-05-13 · `onda2-st8.9-detalhe-lancamento`

### Adicionado
- **`/movimentacoes/:id`** (detalhe do lançamento): header com tipo, status, título e valor; seções condicionais para split com percentuais, info de recorrência, estorno bidirecional e comprovantes placeholder
- Seção de auditoria com datas de criação, atualização e campos de origem
- Botões contextuais por status: "Editar" visível para 'pendente'/'atrasado'; "Estornar" visível para 'pago' não estornado

---

## [v0.8.8] — 2026-05-13 · `onda2-st8.8-split-categorias`

### Adicionado
- Toggle "Distribuir valor entre categorias" no formulário de novo lançamento
- Tabela de split com linhas editáveis de categoria + valor; validação de soma com tolerância de 0,005; gate do botão "Salvar" enquanto soma inválida
- Pré-população automática ao ligar o toggle (distribuição igualitária pelas categorias existentes) e limpeza ao desligar

---

## [v0.8.7] — 2026-05-13 · `onda2-st8.7-novo-lancamento` + hotfixes de RPC

### Corrigido
- **`row_to_jsonb` → `to_jsonb`** em 4 RPCs da Onda 2: `list_financial_movements`, `get_financial_movement`, `get_account_balances`, `create_financial_movement` — PostgreSQL rejeitava `row_to_jsonb(record)` quando usado com alias de subquery; substituído por `to_jsonb` que aceita `record` anônimo (via migration)
- **Payload de categorias em `create_financial_movement`**: formulário enviava `category_id` como campo top-level; corrigido para `categories: [{ category_id, amount }]` conforme a RPC exige
- **Toast de erro genérico**: adicionado log completo do erro Supabase (`code`, `message`, `details`) antes de exibir toast, para facilitar diagnóstico futuro

---

## [v0.8.7] — 2026-05-13 · `onda2-st8.7-novo-lancamento`

### Adicionado
- **`/movimentacoes/novo`** (formulário básico de criação de lançamento)
- Toggle de tipo (Receita/Despesa/Transferência) com cores funcionais; adapta campos dinamicamente: exibe/oculta Categoria e Conta de destino conforme tipo selecionado
- Campos principais: título, data de vencimento, data de pagamento (opcional), valor total com máscara BRL, select de conta com saldo atual (`get_account_balances`), select de categoria com `full_path` (`list_categories`)
- Campos de contexto: Projeto (desabilitado "Em breve" quando vazio), Centro de custo (`list_cost_centers`)
- Seção colapsável "Mais opções": forma de pagamento, beneficiário/pagador, referência bancária, documento fiscal, tags, observações — inputs sempre montados para preservar estado RHF
- Sidebar reativa com resumo dinâmico (badge de tipo, título, valor, conta, categoria, vencimento) e checklist de preenchimento via `useWatch`
- Validações inline: valor > 0, categoria obrigatória para receita/despesa, contas distintas para transferência; botão "Salvar" desabilitado enquanto inválido
- Submissão via `create_financial_movement`; sucesso invalida cache `['movements', orgId]` e navega para `/movimentacoes`
- Schema Zod discriminado por tipo; `buildCreatePayload` converte datas para ISO e campos vazios para `null`

---

## [v0.8.6] — 2026-05-13 · `onda2-st8.6-lista-movimentacoes`

### Adicionado
- **`/movimentacoes`** (lista completa): substituição do stub pela lista funcional
- Filtros-chip persistidos em `sessionStorage` por orgId: Período (padrão: mês corrente), Conta, Categoria (com `full_path`), Status — cada chip com X individual e botão "Limpar filtros"
- 5 tabs por tipo: Todas, Receitas, Despesas, Transferências, Estornadas; tab "Estornadas" desabilita chip de Status e força `status: 'estornado'` no payload
- Tabela com colunas: Vencimento, Lançamento (título + meta), Conta, Categoria (`full_path` ou "N categorias"), Status (badge colorido), Valor (cor por tipo)
- Hover na linha: ícones Eye e Pencil navegam para `/movimentacoes/:id`; linha inteira clicável para o mesmo destino
- Linha de totais calculada client-side: receitas, despesas, saldo do período (ou total único para tabs Transferências/Estornadas); saldo colorido por sinal
- Skeleton de 8 linhas e estado vazio com botão "Limpar filtros"
- Hook `useMovementFilters` + `useMovementsList` (TanStack Query); helpers `filtersToPayload`, `movementLabels`, `computeTotals`

---

## [v0.8.5] — 2026-05-13 · `onda2-st8.5-configuracoes-categorias`

### Adicionado
- **`/configuracoes/categorias`** (acesso admin): 3 tabs — Receitas, Despesas (árvore 2 níveis com indentação), Centros de custo (lista plana)
- Reordenamento via botões ▲/▼ com persistência de `display_order` via `upsert_category` em `Promise.all`
- Slideover criar/editar categoria: kind travado ao da tab ativa na criação; texto fixo na edição; select de pai limitado a raízes do mesmo kind; desabilitado em categorias que já têm filhos
- Slideover criar/editar centro de custo: nome + descrição, via `upsert_cost_center`
- Diálogos de ativar/desativar para categorias e centros de custo, com toast de erro descritivo da RPC
- **Modal "Aplicar template"**: lista templates via `list_category_templates`, preview de categorias por kind, aplicação via `apply_category_template` com toast de contagem; segunda aplicação exibe "Nenhuma categoria nova" (comportamento idempotente)
- Aba "Categorias" na sidebar do `ConfiguracoesLayout` (admin-only, ícone Tag)
- Helpers puros `buildCategoryTree` e `swapDisplayOrder`

---

## [v0.8.4] — 2026-05-13 · `onda2-st8.4-configuracoes-contas`

### Adicionado
- **`/configuracoes/contas`** (acesso admin): lista de contas com saldo atual via VIEW `account_current_balance`, badge de status, opacidade reduzida em contas inativas, estado vazio
- **Slideover de criar/editar conta**: campos obrigatórios (nome, tipo, saldo inicial, data de abertura) + seções colapsáveis "Dados bancários" e "Personalização" (cor, ícone); salva via `upsert_financial_account`
- **Diálogo de ativar/desativar**: confirmação antes de agir; erro da RPC exibido como toast descritivo; usa `toggle_account_status`
- Aba "Contas" adicionada à sidebar do `ConfiguracoesLayout` (visível apenas para admins, ícone Wallet)
- `accountTypeLabels.ts` com mapa enum→label PT para os 7 tipos de conta

---

## [v0.8.3] — 2026-05-13 · `onda2-st8.3-painel-rotas`

### Adicionado
- **`PainelPage`** funcional: bloco de saldos por conta (VIEW `account_current_balance`, apenas contas ativas, saldo total no rodapé, estado vazio com link para `/configuracoes/contas`) + bloco de KPIs do mês corrente via RPC `list_financial_movements` (receitas, despesas, saldo do mês com cor por sinal)
- **`RequireAuth`** em `src/features/auth/components/`: wrapper de rota que verifica sessão via `useAuth()`, exibe spinner durante carregamento e redireciona para `/login` se não autenticado
- **4 rotas stub** registradas em `App.tsx` sob `RequireAuth`: `/movimentacoes`, `/movimentacoes/novo`, `/movimentacoes/importar`, `/movimentacoes/:id`
- Skeleton nos blocos do painel durante carregamento de dados

---

## [v0.8.2] — 2026-05-13 · `onda2-st8.2-schema-movimentacoes`

### Adicionado
- **Enums**: `movement_type` (receita, despesa, transferencia), `movement_origin` (manual, recurring, installment, contribution), `movement_status` (pendente, pago, atrasado, estornado, efetivado)
- **Tabela `recurring_series`**: RLS canônica, suporte a parcelamentos via `is_installment BOOLEAN` + `total_installment_amount`
- **Tabela `financial_movements`**: FK para `financial_accounts`, `recurring_series`, `projects`, `vendors`; coluna `status` controlada por trigger `BEFORE INSERT OR UPDATE` (não GENERATED STORED — `CURRENT_DATE` não é IMMUTABLE no PostgreSQL); campo `transfer_peer_id` para par de transferência
- **Tabela `financial_movement_categories`** (split): trigger DEFERRED `validate_split_sum` garante que soma das linhas = total do movimento no COMMIT; constraint impede split em transferências
- **Tabela `movement_attachments`**: registro de comprovantes com `storage_path`
- **Bucket `movement-attachments`** (privado): path `{org_id}/{movement_id}/{filename}`
- **VIEW `account_current_balance`**: `initial_balance + receitas pagas - despesas pagas + transferências efetivadas recebidas - transferências efetivadas enviadas`
- **5 RPCs**: `list_financial_movements` (filtros: type, status, period_start/end, account_id, category_id), `get_financial_movement` (lançamento completo com split e anexos), `create_financial_movement` (com array de categories para split), `update_financial_movement`, `get_account_balances` (lê `account_current_balance`)

### Técnico
- GENERATED STORED para `status` descartado: trigger BEFORE INSERT OR UPDATE garante os 5 estados corretamente e mantém o índice `(organization_id, status)` populado com todos os valores (inclusive `atrasado`)
- Trigger DEFERRED `validate_split_sum` dispara ao COMMIT, não no INSERT — permite inserir linhas de split em múltiplos statements dentro da mesma transação
- Isolamento de snapshot de CTE: INSERTs em CTEs não são visíveis a SELECTs na mesma instrução — validações foram feitas em statements separados

---

## [v0.8.1] — 2026-05-13 · `onda2-st8.1-schema-base`

### Adicionado
- **Schema base da Onda 2 (financeiro)**: tabelas `projects` (stub para FK futura), `vendors`, `vendor_ratings`, `financial_accounts`, `categories`, `cost_centers`, `category_templates` — todas com RLS canônica e audit trigger
- **Enums**: `account_type` (7 valores) e `category_kind` (receita, despesa)
- **VIEW `categories_with_path`** com `security_invoker = true`: retorna `full_path` no formato "Pai > Filho" para uso em autocomplete e listagens
- **12 RPCs de CRUD**: `list/upsert/toggle_status` para contas financeiras, categorias e centros de custo; `list_category_templates`; `apply_category_template` (idempotente — duas passadas: pais → filhos)
- **Seed "Padrão Grupo Escoteiro 2026"** em `category_templates`: 35 categorias (14 receitas + 21 despesas) prontas para aplicação via RPC
- **Função `_set_updated_at()`** criada localmente na migration (não existia função genérica global no projeto)
- **Pattern `to_regclass`** nas RPCs de toggle_status: checagem de movimentações associadas ativada automaticamente quando `financial_movements` for criada na ST-8.2, sem alterar as RPCs

### Processo
- Adicionada regra ao `CLAUDE.md`: aprovação de plano do Lovable com ressalvas exige prompt escrito (`NNb-...-aprovacao.md`) — ressalva nunca pode ficar apenas no chat

---

## [v0.7.6] — 2026-05-12 · `config-plataforma-st7.6-perfil-notificacoes`

### Adicionado
- **Seção "Notificações"** em `/configuracoes/perfil`, independente do formulário principal (salva em `user_preferences` via `set_setting` com `p_level: "user"`)
- Campo WhatsApp: editável, formato E.164, validação inline, pré-preenchido com valor salvo
- Campo Telegram: read-only, exibe "Vinculado" / "Não vinculado" com base em `contact.telegram_chat_id`, instrução para vincular via @BussolaBot
- Nota de rodapé explicando escopo global das preferências

---

## [v0.7.5] — 2026-05-12 · `config-plataforma-st7.5-org-tabs`

### Adicionado
- **3 novas seções de integração** ao final de `/configuracoes/organizacao` (acesso admin da OSC)
  - **Google Drive**: JSON da conta de serviço (secret, não sobrescreve Vault quando em branco), ID da pasta de exportação e de importação
  - **WhatsApp Business**: Phone Number ID + token de acesso (secret, não sobrescreve quando em branco)
  - **Telegram por OSC**: Chat ID do grupo/canal
- Stubs funcionais: formulários salvam via `set_organization_settings_bulk`, backend ativo pendente
- Cada seção exibe nota "Esta integração ainda não está ativa..."

---

## [v0.7.4] — 2026-05-12 · `config-plataforma-st7.4-gotenberg-stubs`

### Adicionado
- **`GotenbergIntegrationPanel`**: URL, timeout (UI em segundos, salvo em ms), header de autenticação (secret), botão "Testar geração" com resultado inline (tempo em ms ou erro)
- **4 stubs funcionais** em `/superadmin/configuracoes`: Telegram, n8n, LLM/IA e S3/R2 — formulários com Salvar operacional, badge "Em breve" na sidebar
- `_stubShared.tsx`: `<StubNote>` e `<Field>` compartilhados entre os stubs

### Corrigido
- `storage.s3.access_key` era retornado como valor em claro pela RPC `read_platform_config_for_admin`; corrigido para `access_key_is_set: boolean` (Vault, nunca expõe o valor)
- `usePlatformConfig`: tipo `s3.access_key: string | null` atualizado para `access_key_is_set: boolean`
- Timeout do Gotenberg: UI exibia e recebia valor em segundos mas EF espera milissegundos; conversão explícita adicionada

---

## [v0.7.3] — 2026-05-12 · `config-plataforma-st7.3-email`

### Adicionado
- **`PlatformSettingsPage`** funcional em `/superadmin/configuracoes`: layout 2 colunas (sidebar + painel), hook `usePlatformConfig` (chama `read_platform_config_for_admin`), roteamento por integração selecionada
- **`IntegrationSidebar`** com badges de status por integração (ativo / config / erro / em breve)
- **`EmailIntegrationPanel`** com 3 subcards independentes: SMTP primário (6 campos + teste inline), Resend (API key + from), Padrões de e-mail (DPO, reply-to, fallback toggle)
- `IntegrationStatusBadge` + `computeStatus` + `formatRelativeTime`
- Botão "Testar envio" no subcard SMTP com resultado inline (✓ / ✗ + tempo em ms)

### Corrigido
- Bug crítico em `send_email/index.ts`: `SmtpConfig.secure` é `boolean` mas o banco armazenava `security: string`; `loadSmtpConfig` agora mapeia `security === 'SSL/TLS'` → `secure: true`

---

## [v0.7.2] — 2026-05-12 · `config-plataforma-st7.2-superadmin-layout`

### Adicionado
- **`SuperadminLayout`**: sidebar teal-dark, navegação `/superadmin/configuracoes`, `/superadmin/organizacoes`, `/superadmin/usuarios`
- **`SuperadminRoute`**: guard de acesso via RPC `read_platform_config_for_admin` como proxy de verificação de superadmin
- Hook `useIsSuperadmin` em `src/hooks/` (evita dependência invertida shared→features)
- Badge ⚡ no `TopNav` para superadmins
- Rotas `/superadmin/*` em `App.tsx`; páginas `/organizacoes` e `/usuarios` com `<ComingSoonPage>`

---

## [v0.7.1] — 2026-05-12 · `config-plataforma-st7.1-backend`

### Adicionado
- RPC `read_platform_config_for_admin` (VOLATILE, SECURITY DEFINER): retorna todas as configurações de plataforma com `is_set: boolean` para secrets (nunca expõe o valor)
- Template `test` no `send_email` para botão de teste de SMTP
- Edge Function `test_gotenberg`: dispara geração de PDF de teste e retorna `{ ok, ms }`

---

## [v0.6.7] — 2026-05-11 · `onda1-st6.7-gate-politica`

### Adicionado
- **Gate de aceite de política**: `RootRedirect` consulta `current_policy` + `user_consent`; redireciona para `/aceitar-politica` quando necessário (fail-open se RPC falhar)
- `AceitarPoliticaPage`: layout split teal/branco, reutiliza `<PolicyConsent>` e `<AuthBrandPanel>`, insert em `user_consent` com user_agent, redirect para `/` após aceite

---

## [v0.6.6] — 2026-05-11 · `onda1-st6.6-config-organizacao`

### Adicionado
- **`/configuracoes/organizacao`** completo (acesso admin): dados básicos da OSC (nome, CNPJ, contato, endereço, redes sociais), logo (bucket `organization-logos`, resize 512×512), configurações operacionais (moeda, timezone, ano fiscal), toggle de solicitações públicas (`accepts_public_signup`), permissões do papel Público
- RPC `set_organization_settings_bulk` para salvar múltiplas chaves de `organization_settings` em uma única chamada
- RPCs `read_organization_settings`, `update_organization_basic`, `update_organization_logo_path`
- Componente `OrgLogoUploader` (separado do `AvatarUploader` de perfil)

---

## [v0.6.5] — 2026-05-11 · `onda1-st6.5-usuarios-admin`

### Adicionado
- **`/configuracoes/usuarios`** completo (acesso admin): listagem de membros com filtros, busca e paginação client-side (cap 500); `AddUserDrawer` disparando EF `add_user_to_organization`; `MemberActionsMenu` com todas as transições válidas da máquina de estado (alterar papel, desativar, reativar, remover, cancelar convite, reenviar setup)
- `MemberAvatar` com signed URL (TTL 1h)
- `useIsActiveOrgAdmin` com fast-path JWT para superadmin
- `ConfiguracoesLayout` com sidebar adaptativa (aba "Usuários" visível apenas para admins)
- RPC `list_pending_org_requests` unificando `pending_organization_links` e `user_organization` pendentes, com identidade real via COALESCE

### Corrigido
- GRANT em `transition_user_organization_status` (estava REVOKE'd de `authenticated` desde ST-1)
- Nome nulo na listagem (COALESCE com `auth.users.raw_user_meta_data->>'full_name'`)
- Avatar no `TopNav` passou a ler `avatar_storage_path` de `user_profile`

---

## [v0.6.4] — 2026-05-08 · `onda1-st6.4-perfil`

### Adicionado
- **`/configuracoes/perfil`**: Identificação (nome + avatar), Contato (telefone E.164), Dados sensíveis (data de nascimento, CPF e RG cifrados no Vault), Ações (logout global + instruções LGPD)
- Tabela `user_profile` 1:1 com `auth.users`, RLS, trigger de auditoria com `audit_excluded_columns` para campos do Vault
- RPCs `set_user_profile_sensitive` + `get_user_profile_decrypted` (SECURITY DEFINER, Vault)
- Bucket `user-avatars` privado (2 MB, jpg/png/webp), `<AvatarUploader>` autônomo (resize 512×512 JPEG)
- `<ConfirmDialog>` em `shared/components/feedback/`
- `docs/lgpd-data-inventory.md`: 23 campos catalogados com base legal, prazo de retenção e mecanismo de anonimização

---

## [v0.6.3] — 2026-05-05 · `onda1-st6.3-setup-token`

### Adicionado
- **`/setup?token=...`** funcional: FSM com 10 estados (loading → ready → submitting → 4 terminais), validação Zod com react-hook-form, layout split idêntico ao `/login`
- `SetupPage` com tratamento diferenciado por `reason` retornado por `validate_setup_token`
- EF `dev_seed_setup_token` com duplo guard (`APP_ENV=dev` + service-role) para QA local
- Script `bin/seed-setup-token.sh` com listagem interativa de OSCs e indução dos 9 cenários da FSM

---

## [v0.6.2] — 2026-05-05 · `onda1-st6.2-criar-conta`

### Adicionado
- **`/criar-conta`** em dois modos: wizard anônimo de 3 passos (email → decisões → completar) e `LoggedNoOrgView` para usuário autenticado sem OSC
- EF `create_organization` com `createOrganizationWithSlug` (sufixo `-2`, `-3`...)
- `list_public_organizations()` SECURITY DEFINER
- Tradutor pt-BR de erros em `onboarding-errors.ts`

### Corrigido (OPSEC sweep — ADR-004)
- Removidos `details: err.message` em 27 pontos de 8 Edge Functions (ST-6.2 + retroativos em ST-4 e ST-5 + `send_email`) — zero vazamento de mensagem interna em respostas 500

---

## [v0.6.1] — 2026-05-05 · `onda1-st6.1-login-redirects`

### Adicionado
- **`/login`**: email/senha + Google OAuth, `RootRedirect` com 3 branches
- `useAuth` (combina `getSession` + `onAuthStateChange`), `useActiveOrganization`
- `OrgSwitcher` com selo de iniciais, dropdown de avatar com logout

---

## [v0.5.0] — 2026-05-05 · `onda1-st5-self-signup-and-links`

### Adicionado
- EFs `start_self_signup`, `complete_self_signup`, `request_organization_link`, `approve_organization_link`, `reject_organization_link`
- UPDATE atômico para evitar race em approve/reject
- `_shared/onboarding_common.ts` para reuso entre EFs

---

## [v0.4.1] — 2026-05-05 · `onda1-st4-onboarding-direct-with-resend`

### Adicionado
- EFs `add_user_to_organization`, `validate_setup_token`, `complete_setup`, `resend_setup_token`, `request_setup_resend`
- Schemas Zod, helpers compartilhados, configuração de `verify_jwt` por EF

---

## [v0.3.0] — 2026-05-05 · `onda1-st3-send-email-with-secrets`

### Adicionado
- Edge Function `send_email`: SMTP primário + Resend fallback, 6 templates, tabela `email_send_log`
- Integração com Vault via `set_setting`/`get_setting` com cifragem real (substituto de pgsodium)

---

## [v0.2.0] — 2026-05-05 · `onda1-st2-settings-policies`

### Adicionado
- 7 tabelas: `platform_settings`, `organization_settings`, `user_preferences`, `policies`, `user_consent`, `invitations`, `pending_organization_links`
- Auditoria com redação condicional para secrets
- Função `current_policy(type)`, `custom_access_token_hook` (não-ativável em Lovable Cloud — TODO operacional)

---

## [v0.1.0] — 2026-05-05 · `onda1-st1-schema-base`

### Adicionado
- Schema base PostgreSQL com RLS multi-tenant: funções `is_member_of`, `has_role_in`, `current_user_is_superadmin`
- Máquina de estado de `user_organization` com guard trigger (7 estados)
- `audit_log` + trigger genérico reutilizável
- Hardening: `search_path` fixo, `REVOKE EXECUTE` nas funções sensíveis

---

*Última atualização: 2026-05-13 · melhorias pós-Onda 2 (prompts 69–77)*
