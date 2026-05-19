---
layout: page
title: Roadmap
permalink: /roadmap/
---

Esta página mostra **o que já existe**, **o que está em construção** e **o que está planejado** no Bússola Financeira. A ordem dentro de cada bloco é planejada — pode haver ajustes conforme aprendemos com OSCs no piloto.

> 💡 **Por que esta página existe**
> Toda OSC tem necessidades específicas, e queremos ser honestos sobre o que o Bússola entrega hoje e o que ainda está por vir. Antes de adotar o sistema, dá para conferir aqui se a funcionalidade que sua OSC precisa já está pronta, está perto ou vai demorar — sem suposição. Se algo importante para a sua OSC não está aqui, escreva pelo botão **💬 Feedback** dentro do sistema; ouvimos.

## Já disponível

Funcionalidades operacionais e testadas no Bússola.

### Núcleo financeiro

- **Movimentações** — receitas, despesas, transferências, com filtros por período contábil, ordenação por coluna, exportação PDF/Excel
- **Estornos** — reversão preservativa de lançamentos pagos
- **Recorrentes e parcelados** — séries que se repetem automaticamente, com 3 escopos de cancelamento
- **Importação CSV** — migração de planilhas históricas para o sistema

### Reembolsos e pedidos de pagamento

- **Reembolsos** — fluxo completo de solicitação, aprovação por quórum configurável, geração automática de movimentação, confirmação de pagamento
- **Pedidos de Pagamento** — fluxo simétrico ao reembolso para despesas que ainda vão acontecer
- **Pedidos recorrentes e parcelados** — aluguel mensal, compra em prestações, contratos fechados
- **Estorno automático** em pedidos rejeitados após pagamento

### Gestão de organização e usuários

- **Multi-organização** — uma conta de usuário em várias OSCs, com seletor de organização
- **Papéis** — Presidente, Tesoureiro, Coordenador, Voluntário, com permissões diferenciadas
- **Fluxo de aprovações configurável** — quórum 1 ou 2, papéis aprovadores e pessoas individuais
- **Convite por e-mail** com aceite formal, controle de acesso ativo/inativo
- **Auto-aprovação rastreável** quando solicitante é único aprovador

### Perfil do usuário

- **Identificação** com foto, telefone, CPF/RG cifrados
- **Dados para reembolso** com pré-preenchimento automático nas solicitações
- **Matriz granular de notificações** — 10 eventos × 3 canais (e-mail, WhatsApp, Telegram)
- **Vinculação ao Telegram via bot oficial**

### Integrações

- **WooCommerce** — sincronização automática de pedidos pagos como receitas; estorno automático em refunds
- **Auditoria completa** — timeline de eventos em cada movimentação, com nome do responsável e data/hora

### Infraestrutura

- **LGPD** — política de privacidade e termos de uso versionados; aceite formal; dados sensíveis cifrados; exclusão de dados sob demanda
- **Documentação pública** — esta documentação que você está lendo, sempre atualizada

## Em construção (próximas entregas)

Em ordem aproximada de chegada. Algumas podem mudar de prioridade conforme as OSCs no piloto sinalizem necessidades urgentes.

### Próximos meses

- **Aceite combinado de privacidade e termos** — refinamento do fluxo de aceite com versionamento independente dos dois documentos legais
- **Reorganização da tela de perfil** — quatro caixas consolidadas com botões internos padronizados *(parcialmente entregue)*
- **Atalhos contábeis nas listas de reembolsos e pedidos** — atalhos de período (mês atual, trimestre etc.) replicando o que já existe em Movimentações

### Onda 5 — Projetos

- **Cadastro de projetos** com nome, descrição, período, orçamento previsto, equipe responsável
- **Vinculação automática** entre projetos e movimentações, reembolsos, pedidos de pagamento
- **Visão consolidada por projeto** — orçamento previsto × realizado, lançamentos vinculados
- **Relatórios prontos para prestação de contas** por projeto (financiadores, conselho)

### Onda 6 — Relatórios

- **Fluxo de caixa** projetado e realizado
- **Comparativos por categoria** — para onde o dinheiro vai e de onde vem
- **Evolução do saldo** — gráficos mês a mês
- **Comparativos período × período** — mês a mês, ano a ano
- **Formatos prontos** para diretoria, conselho, assembleia, financiadores

### Onda 7 — Voluntários (módulo básico)

- **Cadastro de voluntários** com papel, vinculação a projetos, dados de contato
- **Histórico de participação**

### Onda 8 — Fornecedores

- **Cadastro de fornecedores e prestadores** com dados completos
- **Avaliação por OSC** (recomendação interna entre OSCs da rede)
- **Histórico de lançamentos por fornecedor**

### Onda 9 — Plano de Contas Contábil

- **PCG** — Plano de Contas Geral mapeado a partir das categorias operacionais
- **Suporte a ECD/ECF** — formatos contábeis brasileiros oficiais

### Onda 10 — Privacidade e LGPD avançado

- **Exportação de dados pessoais** sob demanda (direito de portabilidade)
- **Anonimização automática** sob solicitação (direito ao esquecimento)

## V2 (médio prazo)

Funcionalidades planejadas para após o MVP completo. Algumas dependem de validação com piloto.

- **Monetização** — planos com período gratuito, OSCs RIT em plano Pro gratuito, OSCs fora da rede em plano pago, portal de cobrança
- **Orçamento anual** — planejamento por categoria/projeto com controle de desvios
- **Voluntários — módulo avançado** — ATVs escoteiras, especialidades, progressão
- **Solicitação de compras com cotação** — ≥ 1 fornecedores, fluxo de aprovação, lançamento automático ao aprovar
- **Gestão de associados** — contribuintes, planos de contribuição, vínculo financeiro
- **Portal do Associado** — área pública sem senha, segunda via, histórico
- **Doações e Campanhas** — recibos PDF, página pública `/doe/<slug>`, campanhas com meta e prazo
- **IA — sugestão de categoria + OCR de comprovantes** — extração automática de valor/data/fornecedor; sugestão de categoria por LLM
- **Auditoria visual** — viewer da audit_log com filtros e exportação
- **Conciliação bancária** — importação OFX/CNAB, matching automático

## V3 (longo prazo)

Mais distante no horizonte.

- **Integração Asaas** — pagamentos PIX/boleto/cartão recorrente como gateway primário; webhook que atualiza `payment_date` automaticamente
- **Inadimplência** — controle e régua de cobrança automática (D+7, D+15, D+30)
- **Gateways avançados** — split de pagamento, múltiplos gateways
- **Documentos institucionais** — atas, certidões, contratos com controle de validade

## Como acompanhar

- **[Changelog](changelog/)** registra cada versão lançada com a lista detalhada de adições, correções e mudanças.
- **Botão 💬 Feedback** dentro do Bússola — sua mensagem é lida pela equipe da RIT e pode acelerar a priorização de algo que você precisa.

## Observação importante

> ⚠️ **Roadmap não é compromisso de data**
> Esta página descreve **intenção e ordem**, não datas firmes. Software se constrói no mundo real, com restrições reais (equipe, recursos, feedback de piloto). Alguns itens podem antecipar; outros podem atrasar. O que **garantimos** é que o Bússola continua sendo desenvolvido ativamente e que toda mudança fica registrada no [Changelog](changelog/).
