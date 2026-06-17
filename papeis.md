---
title: "Papéis e Permissões"
nav_order: 8
permalink: /papeis/
---

O Bússola tem **seis papéis** que um usuário pode ocupar dentro de uma organização. Cada papel define o que aquele usuário **pode ver e pode fazer** no sistema — sempre dentro da OSC à qual está vinculado. Um usuário pode acumular **mais de um papel** na mesma OSC (ver "Múltiplos papéis", abaixo).

> 💡 **Por que isso importa**
>
> Em OSC, função financeira não é "tudo ou nada". O presidente quer ter visão geral, autorizar saídas grandes, mas não necessariamente lançar cada conta de luz. O tesoureiro precisa operacionalizar o financeiro mas talvez não tenha por que mexer no cadastro de papéis. O voluntário só quer registrar seu reembolso, não ver dados de outras pessoas. **Papéis bem desenhados protegem todo mundo**: o presidente delega sem perder controle, o tesoureiro opera sem ter responsabilidade por configurar a OSC, o voluntário pede reembolso sem expor dados financeiros que não são dele saber.

## Os seis papéis

| Papel | Pode aprovar? | O que faz no dia a dia |
|---|---|---|
| **Presidente** (admin) | ✓ Sim | Tudo: configurações da OSC, gerenciamento de usuários, aprovações, lançamentos, conta bancária, categorias |
| **Tesoureiro** | ✓ Sim | Lançar movimentações, aprovar reembolsos e pedidos, confirmar pagamentos, configurar contas bancárias e categorias |
| **Diretor** | — | Membro da diretoria com **visão ampla de supervisão**: vê movimentações, relatórios e projetos para acompanhar, mas **não opera** (não lança, não aprova). Pode solicitar reembolso próprio |
| **Coordenador de Projeto** | — | Solicitar reembolsos e pedidos de pagamento, ver movimentações |
| **Voluntário** | — | Solicitar reembolsos (apenas os próprios), ver o painel |
| **Comissão Fiscal** | — | Lê tudo (movimentações, reembolsos, pedidos de pagamento, auditoria) **sem operar, aprovar ou solicitar pedidos de pagamento**. Pode solicitar reembolso próprio |

> 💡 O papel **Diretor** era chamado "Dirigente" em versões anteriores — é o mesmo papel, só o nome na tela mudou (versão 0.23.0).

## Quadro de permissões por papel

Visão rápida do que cada papel pode fazer. **✓** = pode operar · **👁** = só leitura · **—** = sem acesso. A coluna Presidente vale também para o Superadmin da plataforma.

| O que pode fazer | Presidente | Tesoureiro | Diretor | Comissão Fiscal | Coordenador | Voluntário |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Ver o financeiro (movimentações, relatórios) | ✓ | ✓ | 👁 | 👁 | 👁 | — |
| Lançar / editar / estornar movimentação | ✓ | ✓ | — | — | — | — |
| Cadastrar contas bancárias e categorias | ✓ | ✓ | — | — | — | — |
| Configurar a OSC (dados, usuários, papéis, fluxo de aprovação) | ✓ | — | — | — | — | — |
| Aprovar reembolsos / pedidos | conforme o fluxo | conforme o fluxo | — | — | conforme o fluxo | conforme o fluxo |
| Solicitar pedido de pagamento | ✓ | ✓ | — | — | ✓ | — |
| Solicitar o **próprio** reembolso | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Coordenar um projeto (do qual é coordenador) | ✓ | ✓ | — | — | ✓ | — |

> "Conforme o fluxo" = depende do que a OSC configurou em Fluxo de Aprovações (padrão: Presidente e Tesoureiro). Diretor e Comissão Fiscal **nunca** são aprovadores.

## Regras importantes

- **Voluntários** não podem solicitar pedidos de pagamento (só reembolsos). Pedido de pagamento envolve dispor de dinheiro da OSC; reembolso é só ressarcimento.
- **Voluntários** não veem dados de pagamento (PIX/TED/conta) de outros membros nos reembolsos. Só veem os próprios dados.
- **Diretor** é um papel de **supervisão, somente leitura**: enxerga movimentações, relatórios, projetos e a trilha de auditoria para acompanhar a OSC, mas **não opera** — não lança, não aprova, não configura. Pode solicitar o próprio reembolso, como qualquer membro. **Não acessa Configurações da OSC.**
- **Comissão Fiscal** tem leitura ampla de todos os dados financeiros mas não realiza nenhuma operação, não participa de fluxos de aprovação e não solicita pedidos de pagamento. Pode solicitar reembolso próprio (mesma regra dos demais membros). **Não acessa Configurações da OSC** — o papel é de fiscalização, separado da gestão.
- **Configurações da Organização** se divide por papel: **Presidente** acessa tudo (dados da OSC, usuários, papéis, contas bancárias, categorias, fluxo de aprovações, relatórios); **Tesoureiro** acessa apenas **Contas Bancárias e Categorias** (o cadastro financeiro). O Fluxo de Aprovações, por ser configuração de governança, é **só do Presidente**. O ícone de engrenagem aparece para Presidente e Tesoureiro; ao clicar, cada um vai para a primeira seção que pode acessar.
- **Aprovadores não aprovam a si mesmos** — a Bússola bloqueia automaticamente quando há outros aprovadores elegíveis no fluxo.

## Múltiplos papéis no mesmo vínculo

Um usuário pode ter **mais de um papel** dentro da mesma OSC. As capacidades se somam — quem tem dois papéis pode fazer tudo que qualquer um dos dois permite. Exemplos comuns:

- **Coordenador de Projeto + Comissão Fiscal** — coordena um projeto específico e ao mesmo tempo fiscaliza as contas da OSC.
- **Tesoureiro + Coordenador de Projeto** — opera o financeiro consolidado e também responde por um projeto específico.
- **Diretor + Coordenador de Projeto** — acompanha a OSC como diretoria (leitura) e, no projeto que coordena, pode operar.
- **Voluntário + Comissão Fiscal** — atua como voluntário regular e fiscaliza as contas (o papel de fiscal já cobre tudo que voluntário pode fazer).

> ⚠️ **Restrição · Comissão Fiscal não acumula com Presidente ou Tesoureiro**
>
> Por princípio de fiscalização independente, **Comissão Fiscal não pode ser combinada com Presidente nem com Tesoureiro**. Quem opera o financeiro (Presidente, Tesoureiro) não pode fiscalizar a si mesmo. O sistema bloqueia essa combinação no editor de papéis e no backend.

> 📖 **Conceito · Auto-aprovação quando solicitante é o único aprovador**
>
> Em OSC muito pequena, pode acontecer de o único aprovador elegível ser o próprio solicitante (ex: o presidente é também o único diretor financeiro e foi ele quem fez a compra). Nesses casos, a Bússola **permite a auto-aprovação para não travar o fluxo**, mas **marca explicitamente** no histórico de auditoria como `self_approved`. A diretoria e auditoria conseguem filtrar esses casos para revisão. Conforme a OSC cresce e mais papéis aprovadores são cadastrados, auto-aprovações naturalmente diminuem.

## Quem aprova reembolsos e pedidos?

O fluxo de aprovação é **configurável** pelo Presidente em [Configurações → Fluxo de Aprovações](/configuracoes/aprovacoes/). Default: Presidente e Tesoureiro são os aprovadores elegíveis, com quórum 1 (basta um voto positivo).

A configuração permite:

- Escolher quantos votos são necessários (1 ou 2)
- Selecionar quais papéis podem aprovar (Presidente, Tesoureiro, ou outros que a OSC cadastrar)
- Adicionar pessoas específicas como aprovadores além do papel (útil para incluir um conselheiro ou membro do comitê fiscal sem dar-lhe papel completo de tesoureiro)

## Alterar os papéis de um usuário

Apenas o **Presidente** pode alterar papéis. Acesse [Configurações → Usuários](/configuracoes/usuarios/), localize o membro, use o menu de ações da linha e selecione **Editar papéis**. Abrirá um painel lateral com checkboxes para os papéis disponíveis (Presidente, Tesoureiro, Diretor, Coordenador de Projeto, Comissão Fiscal e Voluntário). Marque os papéis desejados e clique em "Salvar". Pelo menos 1 papel é obrigatório.

> ⚠️ **Atenção · Mudança de papel é mudança de poder**
>
> Promover alguém para Tesoureiro dá acesso à aprovação de despesas — pense bem antes de ampliar. Conversão "voluntário ↔ tesoureiro" deve passar pela diretoria, não ser unilateral. Em OSC com governança formal (estatuto, assembleia), a mudança pode até ter requisito formal de ata ou eleição. O sistema não bloqueia a mudança, mas ela fica registrada no audit log.

## Quando criar papel novo (Coordenador) faz sentido?

OSC pequena geralmente opera com 3 papéis: Presidente, Tesoureiro, Voluntário. **Coordenador de Projeto** entra quando a OSC tem **projetos específicos com responsável próprio** que precisa pedir pagamentos sem ser tesoureiro nem voluntário comum — coordenador de campanha, líder de evento, gestor de iniciativa pontual.

Use coordenador quando: a pessoa não opera o financeiro consolidado, mas pede saídas para o projeto dela; precisa ver movimentações da OSC mas não autoriza outros pedidos.

## Por onde seguir

- **Configurações → Usuários** — para adicionar pessoas e atribuir papéis.
- **Configurações → Fluxo de Aprovações** — para ajustar quórum, papéis aprovadores e aprovadores individuais.
- **Primeiros Passos** — orientações práticas para quem está começando.
