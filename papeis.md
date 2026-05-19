---
layout: page
title: Papéis e Permissões
permalink: /papeis/
---

O Bússola tem **quatro papéis** que um usuário pode ocupar dentro de uma organização. Cada papel define o que aquele usuário **pode ver e pode fazer** no sistema — sempre dentro da OSC à qual está vinculado.

> 💡 **Por que isso importa**
> Em OSC, função financeira não é "tudo ou nada". O presidente quer ter visão geral, autorizar saídas grandes, mas não necessariamente lançar cada conta de luz. O tesoureiro precisa operacionalizar o financeiro mas talvez não tenha por que mexer no cadastro de papéis. O voluntário só quer registrar seu reembolso, não ver dados de outras pessoas. **Papéis bem desenhados protegem todo mundo**: o presidente delega sem perder controle, o tesoureiro opera sem ter responsabilidade por configurar a OSC, o voluntário pede reembolso sem expor dados financeiros que não são dele saber.

## Os quatro papéis

| Papel | Pode aprovar? | O que faz no dia a dia |
|---|---|---|
| **Presidente** (admin) | ✓ Sim | Tudo: configurações da OSC, gerenciamento de usuários, aprovações, lançamentos, conta bancária, categorias |
| **Tesoureiro** | ✓ Sim | Lançar movimentações, aprovar reembolsos e pedidos, confirmar pagamentos, configurar contas bancárias e categorias |
| **Coordenador de Projeto** | — | Solicitar reembolsos e pedidos de pagamento, ver movimentações |
| **Voluntário** | — | Solicitar reembolsos (apenas os próprios), ver o painel |

## Regras importantes

- **Voluntários** não podem solicitar pedidos de pagamento (só reembolsos). Pedido de pagamento envolve dispor de dinheiro da OSC; reembolso é só ressarcimento.
- **Voluntários** não veem dados de pagamento (PIX/TED/conta) de outros membros nos reembolsos. Só veem os próprios dados.
- **Configurações da Organização** (gerenciamento de usuários, dados da OSC, integrações, etc.) é restrita a **Presidente e Tesoureiro** — o ícone de engrenagem só aparece para esses papéis na barra superior.
- **Tesoureiro** vê uma sub-nav reduzida em Configurações: Contas Bancárias, Categorias e Fluxo de Aprovações. Presidente vê os 5 itens (acima + Organização + Usuários).
- **Aprovadores não aprovam a si mesmos** — a Bússola bloqueia automaticamente quando há outros aprovadores elegíveis no fluxo.

> 📖 **Conceito · Auto-aprovação quando solicitante é o único aprovador**
> Em OSC muito pequena, pode acontecer de o único aprovador elegível ser o próprio solicitante (ex: o presidente é também o único diretor financeiro e foi ele quem fez a compra). Nesses casos, a Bússola **permite a auto-aprovação para não travar o fluxo**, mas **marca explicitamente** no histórico de auditoria como `self_approved`. A diretoria e auditoria conseguem filtrar esses casos para revisão. Conforme a OSC cresce e mais papéis aprovadores são cadastrados, auto-aprovações naturalmente diminuem.

## Quem aprova reembolsos e pedidos?

O fluxo de aprovação é **configurável** pelo Presidente em [Configurações → Fluxo de Aprovações](configuracoes/workflow/). Default: Presidente e Tesoureiro são os aprovadores elegíveis, com quórum 1 (basta um voto positivo).

A configuração permite:

- Escolher quantos votos são necessários (1 ou 2)
- Selecionar quais papéis podem aprovar (Presidente, Tesoureiro, ou outros que a OSC cadastrar)
- Adicionar pessoas específicas como aprovadores além do papel (útil para incluir um conselheiro ou membro do comitê fiscal sem dar-lhe papel completo de tesoureiro)

## Alterar o papel de um usuário

Apenas o **Presidente** pode alterar papéis. Acesse [Configurações → Usuários](configuracoes/usuarios/), localize o membro, use o menu de ações da linha e selecione **Alterar papel**.

> ⚠️ **Atenção · Mudança de papel é mudança de poder**
> Promover alguém para Tesoureiro dá acesso à aprovação de despesas — pense bem antes de ampliar. Conversão "voluntário ↔ tesoureiro" deve passar pela diretoria, não ser unilateral. Em OSC com governança formal (estatuto, assembleia), a mudança pode até ter requisito formal de ata ou eleição. O sistema não bloqueia a mudança, mas ela fica registrada no audit log.

## Quando criar papel novo (Coordenador) faz sentido?

OSC pequena geralmente opera com 3 papéis: Presidente, Tesoureiro, Voluntário. **Coordenador de Projeto** entra quando a OSC tem **projetos específicos com responsável próprio** que precisa pedir pagamentos sem ser tesoureiro nem voluntário comum — coordenador de campanha, líder de evento, gestor de iniciativa pontual.

Use coordenador quando: a pessoa não opera o financeiro consolidado, mas pede saídas para o projeto dela; precisa ver movimentações da OSC mas não autoriza outros pedidos.

## Por onde seguir

- **Configurações → Usuários** — para adicionar pessoas e atribuir papéis.
- **Configurações → Fluxo de Aprovações** — para ajustar quórum, papéis aprovadores e aprovadores individuais.
- **Primeiros Passos** — orientações práticas para quem está começando.
