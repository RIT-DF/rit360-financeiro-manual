---
layout: section
title: "Configurações — Fluxo de Aprovações"
permalink: /configuracoes/aprovacoes/
---

> Disponível para **Presidente (admin)** e **Tesoureiro**.

A página **Fluxo de Aprovações** define **quem pode aprovar** reembolsos e pedidos de pagamento da OSC, e **quantos votos são necessários** para aprovar. Acessada por **Configurações → Fluxo de Aprovações** (a URL é `/configuracoes/aprovacoes`).

[![Configurações — Fluxo de Aprovações](../assets/screenshots/config-workflow.png)](../assets/screenshots/config-workflow.png)
*Configurações — Fluxo de aprovações*

> 💡 **Por que isso importa**
> Em OSC sem regra clara de aprovação, ou ninguém aprova nada (e despesas acontecem por inércia, sem controle) ou todo mundo aprova tudo (e a aprovação vira carimbo automático, sem real avaliação). **O fluxo bem configurado** define exatamente quem tem mandato para autorizar saída de dinheiro, quantos precisam concordar, e como o sistema lida com casos atípicos (auto-aprovação, situações onde o solicitante é também aprovador). Isso protege a OSC de gastos não autorizados e protege os aprovadores de questionamento futuro.

A página tem dois blocos: configuração de reembolsos e configuração de pedidos de pagamento (cada um com regras próprias, mas mesma lógica).

## Aprovações necessárias (quórum)

Define quantos votos positivos são necessários para aprovar:

- **1 voto** — um aprovador elegível decide. Mais ágil; típico de OSC menor ou despesas de menor valor.
- **2 votos** — duas pessoas precisam aprovar. Mais controle; típico de OSC maior ou quando há regra estatutária de aprovação dupla.

> 📖 **Conceito · Quórum 2 e aprovação parcial**
> Com quórum 2, depois do primeiro voto positivo, o reembolso ou pedido entra em "Aguardando aprovação parcial" — os outros aprovadores elegíveis recebem notificação de que falta um voto. Quando o segundo voto positivo chega, o status muda para Aprovado. **Se um aprova e outro rejeita, prevalece a rejeição** (princípio conservador: na dúvida, não autoriza).

## Papéis elegíveis para aprovar

Lista de papéis que podem votar em aprovações. Default: **Presidente** e **Tesoureiro**.

A OSC pode optar por incluir outros papéis (Coordenador de Projeto, por exemplo) ou restringir (apenas Presidente). Depende da governança estatutária e da maturidade operacional.

## Pessoas específicas como aprovadores

Além dos papéis, você pode adicionar **pessoas individuais** como aprovadores — independentemente do papel atual delas. Útil para casos como:

- Conselheiro fiscal que não é tesoureiro mas precisa avaliar despesas
- Membro do comitê de finanças que aprova compras acima de certo valor
- Pessoa em transição entre papéis que precisa manter capacidade de aprovação temporariamente

> ✓ **Dica · Use papéis primeiro, exceções como exceções**
> A regra de "papéis aprovadores" cobre 95% dos casos da maioria das OSCs. **Pessoas específicas** são o mecanismo de exceção — use com parcimônia. Lista de aprovadores individuais com 8 nomes é sintoma de governança confusa: ou simplifique para papéis bem definidos, ou ajuste papéis no Cadastro de Usuários para cobrir esses casos.

## Quem pode solicitar pedidos de pagamento

Define quais papéis podem **criar** pedidos de pagamento. Default: Presidente, Tesoureiro, Coordenador de Projeto.

Voluntários não podem criar pedidos de pagamento (só reembolsos), por princípio: pedido de pagamento implica usar dinheiro da OSC, e voluntário sem papel específico não tem mandato para isso.

> 📖 **Conceito · Solicitante nunca aprova o próprio pedido**
> Independentemente da configuração de papéis aprovadores, a Bússola **bloqueia automaticamente** o solicitante de votar no próprio reembolso ou pedido — a aprovação é gesto de controle externo, faz sentido apenas se alguém **diferente** do solicitante revisa. A exceção é quando o solicitante é o único aprovador elegível (OSC muito pequena); aí a Bússola permite a auto-aprovação mas **marca explicitamente** no audit log como `self_approved` para revisão futura.

## Boas práticas

> ✓ **Dica · Comece simples, complique conforme cresce**
> OSC com 5 pessoas: quórum 1, Presidente + Tesoureiro como aprovadores. Decisão rápida, controle suficiente para o porte. Quando a OSC crescer para 20+ pessoas ou começar a movimentar valores maiores, então sim subir para quórum 2 e ampliar a lista de aprovadores. Quórum 2 numa OSC de 5 pessoas vira fricção sem ganho real de controle.

> ⚠️ **Atenção · Mudanças aqui se aplicam a partir de agora, não retroativamente**
> Reembolsos e pedidos **já aprovados** ficam como estavam. A nova configuração só afeta solicitações futuras. Se você quer alterar uma aprovação passada (ex: para revisar uma autorização questionável), use o mecanismo de **estorno** em Movimentações para reverter o lançamento financeiro correspondente, sem mexer no histórico de aprovações.

## Por onde seguir

- **Configurações → Usuários** — onde os papéis são atribuídos aos membros.
- **Reembolsos** e **Pedidos de Pagamento** — onde o fluxo configurado aqui é aplicado.
- **Papéis e Permissões** — para visão geral de quem pode fazer o quê.
