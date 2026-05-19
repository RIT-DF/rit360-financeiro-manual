---
layout: page
title: Roadmap
permalink: /roadmap/
---

Esta página mostra **o estado de cada funcionalidade** do Bússola Financeira — o que já está em produção, o que está sendo desenvolvido agora, e o que está planejado para mais à frente.

> 💡 **Por que esta página existe**
> Toda OSC tem necessidades diferentes. Antes de adotar o sistema ou planejar como vai usar, dá para conferir aqui se a funcionalidade que você precisa **já está pronta, está perto ou ainda vai demorar** — sem suposição. Se algo importante para a sua OSC não está aqui, escreva pelo botão **💬 Feedback** dentro do Bússola; ouvimos.

> ⚠️ **Sobre datas e ordem**
> Esta página descreve **intenção e estado**, não datas firmes. O que está em **Em construção** está sendo trabalhado agora; o que está em **Planejado** vai chegar — mas a ordem pode mudar conforme as OSCs no piloto sinalizem necessidades urgentes. Cada nova versão entregue aparece no [Changelog](/changelog/) com os detalhes específicos.

---

## 💸 Financeiro (Movimentações, Painel e Relatórios)

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Lançamento manual de receita, despesa e transferência | Registrar cada entrada e saída com data de vencimento, data de pagamento, conta, categoria, beneficiário, anexos | ✓ | | |
| Atalhos contábeis no filtro de período | Mês atual, mês anterior, trimestre atual/anterior, semestre, ano YTD, ano anterior | ✓ | | |
| Lançamentos recorrentes | Séries que se repetem automaticamente em frequência configurável; duração por data, contagem ou indefinida até cancelar | ✓ | | |
| Lançamentos parcelados | Valor total dividido em N parcelas com datas e valores ajustáveis | ✓ | | |
| Cancelamento de série em 3 escopos | Cancelar apenas uma ocorrência, esta e futuras, ou série inteira | ✓ | | |
| Estorno preservativo | Reverter lançamento pago criando lançamento contrário automaticamente; histórico preservado | ✓ | | |
| Auditoria por movimentação (timeline) | Registro de todas as ações no lançamento (criação, pagamento, estorno) com responsável e data/hora | ✓ | | |
| Comprovantes anexáveis com pré-visualização inline | Anexar nota fiscal, recibo, foto; pré-visualizar imagem e PDF sem baixar | ✓ | | |
| Distribuição entre múltiplas categorias | Dividir um valor único por mais de uma categoria contábil | ✓ | | |
| Vinculação a projeto e centro de custo | Campo opcional em cada lançamento para análise gerencial | ✓ | | |
| Importação por CSV | Migrar histórico de planilhas com validação linha a linha antes de criar | ✓ | | |
| Importação automática do WooCommerce | Pedidos pagos da loja online viram receitas; refunds disparam estorno automático | ✓ | | |
| Painel com saldos por conta e saldo consolidado | Tela inicial com cockpit financeiro | ✓ | | |
| Resumo do mês corrente no Painel | Receitas, despesas e saldo do mês atual em destaque | ✓ | | |
| Cards de pendências no Painel por papel | Reembolsos pendentes, pedidos aguardando aprovação, aprovados aguardando pagamento | ✓ | | |
| Exportação em PDF e Excel | Lista filtrada exportável; PDF formatado com cabeçalho e totais, Excel com todas as colunas | ✓ | | |
| Relatórios consolidados (módulo dedicado) | Fluxo de caixa, comparativo por categoria, evolução de saldo, comparativo período × período | | ✓ | |
| Conciliação bancária | Importação OFX/CNAB com matching automático e resolução de divergências | | | ✓ |
| OCR de comprovantes | Extração automática de valor, data e fornecedor a partir da foto da nota | | | ✓ |
| Sugestão de categoria por IA | Categorização automática com base em descrição e histórico | | | ✓ |

---

## 🔄 Reembolsos

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Solicitação de reembolso | Voluntário ou diretor registra despesa paga do bolso com comprovante | ✓ | | |
| Aprovação com quórum configurável (1 ou 2 votos) | Quórum e papéis aprovadores definidos pela OSC | ✓ | | |
| Aprovação ou rejeição inline na lista | Aprovar sem precisar entrar no detalhe | ✓ | | |
| Edição inline pós-rejeição | Corrigir e reenviar na mesma página, sem criar nova solicitação | ✓ | | |
| Pré-preenchimento de PIX/TED do perfil | Dados de pagamento configurados uma vez no perfil entram automaticamente nas solicitações | ✓ | | |
| Geração automática de movimentação ao aprovar | Reembolso aprovado vira lançamento pendente para o tesoureiro confirmar pagamento | ✓ | | |
| Link cruzado com a movimentação correspondente | Detalhe do movimento traz link "Ver pedido de reembolso" | ✓ | | |
| Auto-aprovação rastreável | Quando solicitante é único aprovador, permitida mas marcada explicitamente no audit log | ✓ | | |
| Reembolso parcial (aprovar valor diferente do solicitado) | Aprovador pode aprovar valor menor com justificativa | | | ✓ |
| Atalhos contábeis de período na lista | Mesmos atalhos já existentes em Movimentações | | ✓ | |

---

## 📋 Pedidos de Pagamento

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Solicitação de pagamento a fornecedor | Autorizar despesa que ainda vai acontecer com dados do destinatário (PIX/TED/Boleto) | ✓ | | |
| Pedido único, recorrente ou parcelado | Toggle no formulário escolhe entre os 3 tipos | ✓ | | |
| Aprovação com quórum configurável | Mesma lógica de Reembolsos | ✓ | | |
| Geração automática de movimentação ao aprovar | Cria movimentação pendente (ou várias, se série); tesoureiro confirma o pagamento | ✓ | | |
| Cancelamento de série em 3 escopos | Cancelar uma ocorrência, esta e futuras, ou série inteira | ✓ | | |
| Anexo obrigatório no envio para aprovação | Sem orçamento/nota anexo, sistema bloqueia envio | ✓ | | |
| Atalhos contábeis de período na lista | Mesmos atalhos já existentes em Movimentações | | ✓ | |
| Solicitação de compras com cotação | Fluxo com ≥ 1 fornecedores comparados antes da aprovação | | | ✓ |

---

## 📁 Projetos

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Campo "Projeto" disponível nos formulários | Vincular movimentações, reembolsos e pedidos de pagamento a um projeto pelo nome | ✓ | | |
| Cadastro de projetos com nome, descrição, período, orçamento, equipe | Módulo dedicado para registrar projetos com metadados completos | | ✓ | |
| Vinculação automática entre projetos, categorias, centros de custo e lançamentos | A partir do cadastro do projeto, classificação ganha consistência cruzada | | ✓ | |
| Visão consolidada por projeto (orçamento × realizado) | Painel específico do projeto com saldo previsto e gasto | | ✓ | |
| Relatórios prontos por projeto | Prestação de contas formatada para financiadores e conselho | | ✓ | |
| Templates de projeto reutilizáveis | Modelos pré-configurados (ex: "Acampamento escoteiro") | | | ✓ |
| Cronograma visual (Gantt) | Visualização gráfica de tarefas e dependências | | | ✓ |
| Dependências entre tarefas | "Tarefa B inicia quando A termina" com cálculo de caminho crítico | | | ✓ |
| Inventário de recursos e materiais do projeto | Controle de empréstimo e agendamento de uso | | | ✓ |

---

## 👥 Voluntários e Associados

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Cadastro de voluntários | Nome, contato, papel, vinculação a projetos, histórico de participação | | | ✓ |
| Gestão de associados contribuintes | Cadastro de membros pagantes, planos de contribuição, vínculo financeiro | | | ✓ |
| Portal do Associado (área pública por token) | Associado consulta situação financeira e histórico sem precisar de login | | | ✓ |
| Acordos de trabalho e termos com voluntários | Registro de termos de participação, assinatura digital, histórico por voluntário | | | ✓ |

---

## 🏪 Fornecedores

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Cadastro de fornecedores e prestadores | Nome, CNPJ/CPF, contato, dados de pagamento, histórico | | | ✓ |
| Avaliação por OSC | Estrelas e comentários para recomendação interna entre OSCs da rede | | | ✓ |
| Histórico de lançamentos por fornecedor | Todas as movimentações associadas, com filtros e exportação | | | ✓ |

---

## 💰 Doações e Campanhas

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Doações via WooCommerce | "Doações" como produto na loja online sincronizam para Movimentações | ✓ | | |
| Campanhas de arrecadação | Página pública `/doe/<slug>` com meta, prazo e barra de progresso | | | ✓ |
| Personalização da página pública de transparência | Configurar o que aparece — indicadores resumidos, gráficos, fotos | | | ✓ |

---

## 🏢 Configurações da Organização

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Cadastro de dados da OSC | Nome, CNPJ, endereço, redes sociais, logo | ✓ | | |
| Multi-organização (uma conta em várias OSCs) | Seletor de organização no topo da tela | ✓ | | |
| Gestão de usuários e papéis | Adicionar membros, alterar papel, desativar acesso, reenviar convite | ✓ | | |
| Convite por e-mail com aceite | Acesso só após aceite formal pelo destinatário | ✓ | | |
| Acesso público de vínculo (opcional) | Link público permite solicitações espontâneas que admin aprova | ✓ | | |
| Cadastro de contas bancárias | Corrente, poupança, dinheiro, cartão, outros; saldo em tempo real | ✓ | | |
| Categorias de receita, despesa e centros de custo | Estrutura editável com templates iniciais por tipo de OSC | ✓ | | |
| Hierarquia de categorias (mãe + filhas) | Subcategorias para organização contábil mais granular | ✓ | | |
| Fluxo de aprovações configurável | Quórum 1 ou 2, papéis aprovadores, pessoas individuais como aprovadores | ✓ | | |
| Status "Em estruturação → Em funcionamento" | Transição automática por critérios objetivos (membros, contas, etc.) | | | ✓ |
| Status "Suspensa" para organizações | Acesso temporariamente bloqueado, dados preservados | | | ✓ |
| Gestão de papéis customizável por OSC | Renomear papéis, criar papéis novos, matriz de permissões | | | ✓ |
| Suporte a múltiplas lojas WooCommerce por OSC | Configuração de mais de uma loja online conectada | | | ✓ |

---

## 👤 Meu Perfil

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Identificação completa | Foto, nome, telefone, data de nascimento, CPF, RG (cifrados em repouso) | ✓ | | |
| Dados para reembolso (PIX/TED) | Pré-preenchimento automático nas solicitações de reembolso | ✓ | | |
| Notificações granulares por evento e canal | Matriz 10 eventos × 3 canais (e-mail, WhatsApp, Telegram) com switches individuais | ✓ | | |
| Vinculação ao Telegram via bot oficial | Bot `@BussolaBot` vincula contato automaticamente | ✓ | | |
| Alteração de senha | Mudança autosserviço pelo próprio usuário | ✓ | | |
| Encerramento de todas as sessões ativas | Útil em casos de perda de dispositivo ou suspeita de uso indevido | ✓ | | |
| Solicitação de exclusão de dados (LGPD) | Fluxo de direito ao esquecimento previsto na LGPD | ✓ | | |

---

## 🔌 Integrações Externas

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| WooCommerce — sincronização de pedidos pagos | Cron diário automático + manual sob demanda; configuração por OSC | ✓ | | |
| WooCommerce — mapeamento de categorias automático ou manual | Categoria-mãe + filhas auto-criadas, ou mapeamento explícito | ✓ | | |
| WooCommerce — estorno automático em refunds | Pedido refundado dispara estorno na próxima sync | ✓ | | |
| WooCommerce — badge clicável que abre o pedido no admin | Visual roxo na lista de movimentações | ✓ | | |
| WhatsApp Business API | Envio oficial de notificações pela conta WhatsApp Business da OSC | | | ✓ |
| Telegram para grupos e canais da OSC | Envio para grupo/canal além de usuário individual | | | ✓ |
| Google Drive | Sincronização de anexos com Drive da OSC | | | ✓ |
| API pública REST (OpenAPI / Swagger) | Acesso programático aos dados da OSC, habilitado por OSC via superadmin | | | ✓ |
| Integração com sistemas contábeis (NIBO, ContaAzul) | Exportação automática de lançamentos para o ERP contábil | | | ✓ |
| Webhook em tempo real para WooCommerce | Sincronização instantânea ao invés de diária | | | ✓ |
| Conciliação com extrato bancário (OFX/CNAB) | Importação de extrato com matching automático | | | ✓ |

---

## 🏷️ Plano de Contas e Compliance Contábil

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Plano de contas contábil formal (PCG) | Mapeamento das categorias operacionais para o Plano de Contas Geral | | | ✓ |
| Suporte a ECF e ECD | Formatos contábeis brasileiros oficiais para Receita Federal | | | ✓ |
| Orçamento anual com controle de desvios | Cadastro de orçamento por categoria/projeto/período, alertas por desvio | | | ✓ |
| Hash chain na audit_log | Detecção forense de tampering | | | ✓ |
| Imutabilidade real da audit_log | Revogação de UPDATE/DELETE no banco em produção | | | ✓ |
| Certificado digital ICP-Brasil | Assinatura digital de documentos e relatórios | | | ✓ |

---

## 🤖 Inteligência Artificial

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Sugestão automática de categoria | LLM sugere categoria com base em descrição e histórico | | | ✓ |
| OCR de comprovantes | Extração de valor, data e fornecedor a partir da foto da nota | | | ✓ |
| Relatório gerencial mensal gerado por IA | Resumo escrito em prosa do mês para diretoria | | | ✓ |

---

## 🔒 Acesso, Segurança e LGPD

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Login com e-mail e senha | Cadastro via convite, senha forte exigida | ✓ | | |
| Login com Google | Continuar com Google na tela de login e no setup inicial | ✓ | | |
| Aceite formal de política de privacidade | Versionada, registrada por usuário com data | ✓ | | |
| Aceite formal de termos de uso | Versionada, registrada por usuário com data | ✓ | | |
| Dados sensíveis cifrados em repouso | CPF e RG cifrados; chave gerenciada separadamente | ✓ | | |
| Multi-tenancy por RLS (isolamento por OSC) | Cada OSC enxerga apenas seus próprios dados | ✓ | | |
| Auditoria completa em todas as ações | Audit log de criação, edição, aprovação, pagamento, estorno | ✓ | | |
| Aceite combinado privacy + terms | Fluxo único de aceite com versionamento independente dos dois | | ✓ | |
| Exportação de dados pessoais sob demanda | Direito de portabilidade da LGPD | | | ✓ |
| Anonimização automática | Direito ao esquecimento; PII vira placeholders mantendo integridade contábil | | | ✓ |

---

## 💵 Monetização e Cobrança

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Free trial de 30 dias | Acesso completo durante o período inicial | | | ✓ |
| Plano Pro para OSCs RIT (gratuito) | Acesso completo mediante validação de vínculo | | | ✓ |
| Plano Pro para OSCs fora da rede (pago) | Cobrança recorrente PIX/boleto/cartão | | | ✓ |
| Régua de cobrança automática (inadimplência) | D+7, D+15, D+30; bloqueio configurável | | | ✓ |
| Cota de armazenamento e usuários por plano | Limites configuráveis por nível de plano | | | ✓ |

---

## ⚙️ Operação e Suporte

| Funcionalidade | Descrição | Disponível | Em Construção | Planejado |
|---|---|:---:|:---:|:---:|
| Botão de Feedback dentro do app | Mensagem direto para a equipe RIT com versão e contexto | ✓ | | |
| Manual público em `docs.bf.rit.org.br` | Esta documentação que você está lendo | ✓ | | |
| Changelog versionado | Lista de alterações por versão; atualizado a cada release | ✓ | | |
| Modo claro / escuro | Toggle de tema no perfil do usuário | | | ✓ |
| Cronograma automático de relatórios periódicos | Envio mensal/trimestral para destinatários configurados | | | ✓ |
| Monitoramento (Sentry, Logflare) | Captura de erros e logs estruturados | | | ✓ |
| Disaster recovery documentado e testado | Procedimento anual de teste de recuperação | | | ✓ |
| Internacionalização (i18n) | Suporte a idiomas além de pt-BR | | | ✓ |

---

## Acompanhe as entregas

- **[Changelog](/changelog/)** lista cada versão lançada com adições, correções e mudanças específicas.
- **Botão 💬 Feedback** dentro do Bússola — sua mensagem é lida pela equipe da RIT e pode acelerar a priorização de algo que você precisa.
