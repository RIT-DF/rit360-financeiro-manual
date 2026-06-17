---
title: "Painel"
nav_order: 1
parent: "Módulos"
permalink: /modulos/painel/
---

O **Painel** é a primeira tela após o login — a visão de cockpit da sua OSC. Em uma única página você vê quanto dinheiro tem disponível, o resumo do mês corrente e os atalhos para as pendências que precisam da sua atenção naquele momento, ajustados ao seu papel.

[![Painel](/assets/screenshots/manual-painel-pendencias.png)](/assets/screenshots/manual-painel-pendencias.png)
*Painel principal — saldos, resumo do mês, pendências de pagamento e projetos*

> 💡 **Por que isso importa**
>
> A maioria das ferramentas financeiras te despeja em uma lista enorme de lançamentos no login. O Painel inverte isso: **mostra primeiro o que importa para você decidir o próximo passo** — saldo, resumo, pendências por papel. Tesoureiro vê quantos reembolsos esperam pagamento; presidente vê pedidos aguardando aprovação; voluntário vê seus próprios reembolsos pendentes. Resultado: você gasta menos tempo procurando informação, mais tempo decidindo.

## Saldos por conta

Bloco com cada conta financeira da OSC (corrente, poupança, cartão, caixa interno, etc.) e o **saldo atual** de cada uma. No rodapé, o **saldo consolidado** soma todas as contas ativas.

> 📖 **Conceito · Como o saldo é calculado**
>
> O saldo é calculado em tempo real a partir das movimentações financeiras: soma de receitas pagas menos despesas pagas, considerando o saldo inicial da conta. **Movimentações pendentes não entram no saldo** — só somam quando você marca como pagas. Isso bate com a realidade do extrato bancário: o que você tem hoje é o que efetivamente entrou e ainda não saiu, não o que está previsto.

## Resumo do mês corrente

Três cards rápidos com:

- **Receitas** do mês — total de receitas com data de pagamento no mês atual
- **Despesas** do mês — total de despesas com data de pagamento no mês atual
- **Saldo do mês** — diferença entre as duas

Útil para responder de relance: "como foi o mês até agora?"

## Pendências de pagamento

Logo abaixo do resumo, **Pedidos de Pagamento** e **Reembolsos** aparecem **lado a lado**, cada um em um card único com suas pendências como linhas clicáveis. O que aparece depende do seu papel — você só vê pendências relacionadas ao que pode resolver. Clicar em uma linha leva direto à lista já filtrada pelo status correspondente.

### Pedidos de Pagamento

- **Solicitado por mim** — seus próprios pedidos pendentes (todos os papéis veem os próprios)
- **Aguardando minha aprovação** — somente para aprovadores elegíveis
- **Aprovados aguardando pagamento** — somente para o tesoureiro (e o presidente)

### Reembolsos

- **Meus reembolsos pendentes** — rascunhos e rejeitados aguardando reenvio (todos os papéis veem os próprios)
- **Aguardando minha aprovação** — somente para aprovadores elegíveis (Presidente, Tesoureiro e quem mais a OSC configurar)
- **Aguardando pagamento** — somente para o tesoureiro

> 📖 **Conceito · O Painel se adapta ao seu papel**
>
> Cada linha respeita o que você pode resolver. Um voluntário vê só "Solicitado por mim" / "Meus reembolsos pendentes"; um aprovador vê as linhas de aprovação; o tesoureiro vê também o que está "aguardando pagamento". Se um dos cards não tiver nenhuma linha para o seu papel, ele simplesmente não aparece. Cada seção do Painel ganhou ainda um ícone e um detalhe de cor para você localizar a informação mais rápido.

## Projetos

Quando a OSC usa o módulo de [Projetos](/modulos/projetos/), o Painel mostra, por último, um resumo: quantos **projetos ativos** existem, a **saúde dos ativos** (quantos saudáveis, em atenção e críticos) e um destaque para os que **precisam de atenção**. É a visão de portfólio em uma linha — para a diretoria saber, sem abrir projeto por projeto, se algo está pegando fogo.

> ✓ **Dica · Use o Painel como rotina de manhã**
>
> 5 minutos no Painel todo dia (ou toda segunda de manhã) substituem 1 hora de garimpo no final do mês. **Olhe saldo, leia pendências, confira a saúde dos projetos, decida o que precisa decidir, fecha.** Em OSC bem gerida, o Painel não tem cards com números altos parados ali há semanas — pendência só fica parada quando ninguém olhou.

## Por onde seguir

- **Movimentações** — para registrar novas entradas/saídas ou conferir movimentos do período.
- **Pagamentos e Reembolsos** — para resolver as pendências marcadas nos cards.
- **Projetos** — para acompanhar a saúde e o financeiro das iniciativas da OSC.
- **Meu Perfil → Notificações** — para receber alerta quando uma pendência sua aparecer (em vez de depender de abrir o sistema).
