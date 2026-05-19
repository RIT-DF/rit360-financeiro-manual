---
layout: section
title: Pedidos de Pagamento
permalink: /modulos/pedidos-pagamento/
---

O módulo de **Pedidos de Pagamento** é onde alguém da OSC **pede autorização** para pagar uma despesa **antes que o pagamento aconteça** — pagar o aluguel do salão, contratar o fornecedor do som do evento, quitar o boleto da energia. O fluxo tem aprovação por aprovadores elegíveis e termina com o tesoureiro confirmando o pagamento.

> Acesse pelo menu **Pagamentos e Reembolsos → aba Pedidos de Pagamento**.

> 💡 **Por que isso importa**
> Em OSC sem disciplina de pedido de pagamento, **acontece de gente sair pagando contas sem combinar com a diretoria** — desconfiando do saldo, criando despesas que nem todos sabiam, gerando o famoso "como? alguém pagou isso?". O pedido de pagamento resolve com fluxo simples: **antes de a OSC tirar dinheiro do caixa, alguém autoriza**. O autor da solicitação demonstra a despesa (descrição, fornecedor, comprovante), os aprovadores decidem com base em informação concreta, e o tesoureiro executa só o que foi autorizado. Resultado: controle sobre saídas, transparência, prevenção de despesas surpresa.

## Conceitos essenciais

> 📖 **Conceito · Pedido de Pagamento ≠ Reembolso**
> **Pedido de Pagamento** é para despesa que **ainda vai acontecer**: o dinheiro está na OSC e a aprovação autoriza que saia. **Reembolso** é para despesa que **já aconteceu**: alguém pagou do bolso e quer receber de volta. Use Pedido de Pagamento quando você tem a conta a pagar (boleto, fatura, nota de fornecedor) e o pagamento ainda não foi feito; o destinatário do dinheiro é o fornecedor/prestador, não você. Use Reembolso quando você já desembolsou e a conta está paga pelo seu CPF.

> 📖 **Conceito · Pedido único, recorrente ou parcelado**
> A Bússola permite três tipos de pedido de pagamento, escolhidos no momento da solicitação:
>
> - **Único** — pedido avulso, uma vez (o caso mais comum: pagar uma fatura, contratar um serviço pontual)
> - **Recorrente** — gera uma série que se repete em intervalo regular (mensal, trimestral, anual, etc.). Útil para aluguel, mensalidade de internet, contrato de manutenção. A aprovação cria a série inteira; cada ocorrência é paga individualmente pelo tesoureiro.
> - **Parcelado** — divide um valor único em N parcelas com datas e valores ajustáveis. Útil para compras parceladas (equipamento em 6×, contrato fechado em prestações). A aprovação cria as parcelas todas de uma vez.
>
> A duração de uma série recorrente pode ser **por data final**, **por quantidade de ocorrências** ou **indefinida até cancelar**.

> 📖 **Conceito · Quórum e fluxo de aprovação**
> A OSC configura em **Configurações → Fluxo de Aprovações** quantos votos são necessários (1 ou 2) e quais papéis podem aprovar. O solicitante nunca aprova o próprio pedido quando há outros aprovadores elegíveis — a Bússola bloqueia automaticamente. Quando o solicitante é o único aprovador (caso de OSCs muito pequenas), a auto-aprovação é permitida mas explicitamente registrada no audit log como `self_approved`.

> 📖 **Conceito · Status do pedido**
> O ciclo normal é **Rascunho → Aguardando aprovação → Aprovado → Pago**. **Rejeitado** é desvio do caminho aprovado — solicitante pode editar e reenviar.

| Status | Significado |
|---|---|
| ⬜ **Rascunho** | Salvo mas não enviado — só o solicitante vê |
| 🟡 **Aguardando aprovação** | Esperando voto dos aprovadores elegíveis |
| 🟢 **Aprovado** | Aprovado; movimentação financeira pendente criada automaticamente |
| 🔴 **Rejeitado** | Reprovado com motivo registrado — pode ser editado e reenviado |
| 💙 **Pago** | Tesoureiro confirmou o pagamento na movimentação correspondente |

## Lista de pedidos de pagamento

[![Lista de pedidos](../../assets/screenshots/manual-07-pedidos-lista.png)](../../assets/screenshots/manual-07-pedidos-lista.png)
*Lista de pedidos de pagamento*

A lista exibe todos os pedidos com colunas Descrição, Destinatário, Valor, Data da despesa, Solicitante e Status.

### Cards de resumo no topo

De acordo com seu papel, você vê cards que viram atalhos para as listas filtradas:

- **Aguardando minha aprovação** — para aprovadores (Presidente, Tesoureiro)
- **Aprovados aguardando pagamento** — para o Tesoureiro
- **Solicitado por mim** — para todos os papéis

### Tipos visíveis na linha

Ao lado da descrição, badges discretos indicam o tipo do pedido:

- **Recorrente** — pedido que gerou série recorrente
- **Parcela X de N** — uma parcela específica de um pedido parcelado

Pedidos únicos aparecem sem badge adicional.

## Detalhe do pedido

### Aguardando aprovação

[![Pedido aguardando aprovação](../../assets/screenshots/manual-08-pedido-aguardando.png)](../../assets/screenshots/manual-08-pedido-aguardando.png)
*Detalhe de pedido aguardando aprovação*

- **Valor, Destinatário, Solicitante e Data da despesa** no topo
- **Tipo do pedido** (único / recorrente / parcelado) com configuração da série/parcelas, quando aplicável
- **Dados do pedido**: descrição, categoria, projeto, centro de custo
- **Dados de pagamento do destinatário** (PIX, TED ou Boleto) — visíveis apenas para aprovadores e tesoureiro
- **Documentos**: orçamento, nota fiscal, contrato ou outros anexos
- **Histórico de aprovações**: timeline de todos os votos
- **Ações**: ✓ Aprovar / ✕ Reprovar (somente para aprovadores; nunca para o próprio solicitante)

Pedidos recorrentes mostram aqui uma seção **Ocorrências** com a lista de cada ocorrência prevista, seu status individual e ações específicas (marcar como pago, cancelar essa ocorrência, ver movimento gerado).

### Rejeitado

[![Pedido rejeitado](../../assets/screenshots/manual-08b-pedido-rejeitado.png)](../../assets/screenshots/manual-08b-pedido-rejeitado.png)
*Detalhe de pedido rejeitado*

O motivo da rejeição aparece em destaque no topo. O solicitante pode editar os campos e reenviar para nova rodada de aprovação.

### Aprovado, aguardando pagamento

[![Pedido aprovado](../../assets/screenshots/manual-08c-pedido-aprovado.png)](../../assets/screenshots/manual-08c-pedido-aprovado.png)
*Detalhe de pedido aprovado, aguardando pagamento*

Painel de Ações mostra: **"Aprovado — aguardando confirmação de pagamento pelo tesoureiro."**

> 📖 **Conceito · Aprovado vira movimentação automaticamente**
> No momento da aprovação, a Bússola cria automaticamente a **movimentação financeira pendente** (ou várias, no caso de parcelado e recorrente) com origem `purchase_order` (pedido de pagamento). O tesoureiro entra em Movimentações, escolhe a conta de saída e marca como paga. Cada ocorrência de uma série recorrente gera um movimento individual no momento programado, pago separadamente. O lançamento em Movimentações tem o link **"Ver pedido de pagamento →"** que volta ao detalhe original para conferência.

### Cancelar série (recorrente / parcelado)

Para séries (recorrentes ou parceladas), o detalhe permite **cancelar com 3 escopos diferentes**, escolhidos no momento do cancelamento:

- **Apenas esta ocorrência** — cancela só a parcela/ocorrência específica
- **Esta e todas as futuras** — encerra a série a partir de uma data
- **Série inteira** — cancela tudo (apenas ocorrências ainda não pagas)

Ocorrências já pagas não podem ser canceladas (preservação de auditoria) — apenas estornadas via Movimentações.

## Novo pedido de pagamento

[![Novo pedido](../../assets/screenshots/manual-08d-novo-pedido.png)](../../assets/screenshots/manual-08d-novo-pedido.png)
*Formulário de novo pedido*

Clique em **+ Nova solicitação** para abrir o formulário.

**Campos obrigatórios:**

- **Data da despesa** — data prevista de pagamento ou da nota fiscal
- **Valor**
- **Destinatário** — nome do fornecedor ou prestador de serviços
- **Descrição** — o que está sendo pago e para qual finalidade
- **Dados de pagamento do destinatário**: PIX, TED ou Boleto (chave/conta/código de barras)

**Campos opcionais:** Categoria, Projeto, Centro de custo, Observações, Documentos (orçamento, nota fiscal, contrato).

> ⚠️ **Atenção · Dados são do destinatário, não do solicitante**
> No reembolso, a chave PIX é a sua. No Pedido de Pagamento, é a do **fornecedor**. Não há pré-preenchimento automático — informe corretamente os dados do destinatário a cada solicitação (ou cadastre o fornecedor nos seus contatos e copie). Erro nesses dados significa transferência para destino errado.

### Tipo do pedido (Único / Recorrente / Parcelado)

Toggle no formulário escolhe entre os três tipos. Para **Recorrente** ou **Parcelado**, campos adicionais aparecem:

- Recorrente: frequência (semanal, quinzenal, mensal, bimestral, trimestral, semestral, anual) + duração (data final / quantidade de ocorrências / indefinido até cancelar)
- Parcelado: tabela editável com data e valor de cada parcela; valor total = soma das parcelas

> ⚠️ **Atenção · Anexo é obrigatório no envio**
> Salvar como rascunho não exige anexo, mas **enviar para aprovação exige pelo menos 1 documento anexado**. A Bússola bloqueia o envio se faltar comprovante. Motivo: aprovação sem documento é aprovação no escuro — vira ponto de risco contábil. Sempre anexe a nota, contrato ou orçamento antes de enviar.

**Botões de ação:**

- **Salvar rascunho** — guarda sem enviar
- **Enviar para aprovação** — envia para aprovadores elegíveis (status muda para "Aguardando aprovação")

## Boas práticas

> ✓ **Dica · Pedido com 1 mês de antecedência poupa noite mal dormida**
> Aluguel vence dia 5? Crie o Pedido de Pagamento no dia 20 do mês anterior. Aprovadores votam com calma, tesoureiro programa o pagamento, ninguém entra em pânico no último dia. **Recorrência é seu aliado** — cria pedido de aluguel mensal recorrente uma vez, todo mês cai pra aprovação automaticamente.

> ✓ **Dica · Descrição clara economiza ida e volta**
> "Fornecedor X — Y" é vago. "Aluguel da quadra para treino dos novatos, mensal, contrato firmado em janeiro/2026" responde tudo. Aprovadores votam mais rápido quando a história está completa.

> ⚠️ **Atenção · Pagou sem aprovar? Volta no fluxo**
> Se a urgência levou alguém a pagar antes de ter aprovação, **registre como reembolso retroativo** (a pessoa pagou do bolso) e justifique a urgência. Não tente "burlar" criando um pedido de pagamento de despesa que já foi paga em nome da pessoa. A confusão contábil que sai disso é maior que o ganho.

## Notificações dos eventos de pedidos

Cada usuário escolhe em **Meu Perfil → Notificações** quais eventos receber e por quais canais:

- **Pedido submetido** — aprovadores elegíveis são avisados
- **Aprovação parcial** — em quórum 2, após primeiro voto, demais aprovadores são lembrados
- **Aprovado** — solicitante e tesoureiro são avisados
- **Rejeitado** — solicitante é avisado com o motivo
- **Pago** — solicitante é avisado

## Glossário rápido

- **Pedido de Pagamento** — solicitação para a OSC pagar uma despesa que ainda vai acontecer.
- **Destinatário** — quem recebe o dinheiro (fornecedor, prestador, locador).
- **Tipo do pedido** — único, recorrente ou parcelado.
- **Ocorrência** — uma das execuções programadas de um pedido recorrente.
- **Parcela** — uma das partes de um pedido parcelado.
- **Cancelar série** — encerrar pedido recorrente/parcelado em um dos 3 escopos (apenas uma / esta e futuras / série inteira).

## Por onde seguir

- **Reembolsos** — para despesas que **já foram pagas** do bolso e querem ressarcimento.
- **Movimentações** — para o tesoureiro confirmar o pagamento do pedido aprovado.
- **Configurações → Fluxo de Aprovações** — para a OSC ajustar quórum e papéis aprovadores.
- **Meu Perfil → Notificações** — para configurar canais e eventos das notificações de pedido.
