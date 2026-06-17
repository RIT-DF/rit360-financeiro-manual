---
title: "Da Organização"
nav_order: 1
parent: "Primeiros Passos"
permalink: /primeiros-passos/organizacao/
---

Você acabou de **criar ou assumir uma organização** no Bússola. Antes de sair importando lançamentos e convidando gente, vale preparar a base — uns 20 a 30 minutos que evitam retrabalho e deixam a OSC pronta para operar com segurança. Esta página é o roteiro dessa preparação.

> 💡 **Por que a ordem importa**
>
> Lançamento financeiro precisa de uma **conta** e de uma **categoria** para fazer sentido; reembolso e pedido precisam de um **fluxo de aprovação** definido. Se você importar movimentações antes de ter essa base, vai gastar tempo corrigindo depois. A ordem abaixo monta a fundação primeiro e deixa a importação de dados por último.

## A ordem recomendada

1. **Dados da organização** — identidade da OSC.
2. **Contas bancárias** — onde o dinheiro está.
3. **Categorias** — como o dinheiro é classificado.
4. **Fluxo de aprovações** — quem autoriza saídas.
5. **Usuários e papéis** — quem acessa o quê.
6. **Integração com a loja (WooCommerce)** — opcional, se a OSC vende online.
7. **Importar os dados** — movimentações e usuários em lote.

Tudo isso fica no **ícone de engrenagem (Configurações)** no canto superior direito — visível para Presidente e Tesoureiro.

## 1. Complete os dados da organização

Comece pela identidade da OSC: nome, CNPJ, endereço, redes sociais e logo. É o que aparece em relatórios, e-mails e na prestação de contas.

→ **Configurações → Organização**. Detalhes em [Configurações da Organização](/configuracoes/organizacao/).

[![Configuração da organização](/assets/screenshots/manual-09c-config-organizacao.png)](/assets/screenshots/manual-09c-config-organizacao.png)

## 2. Cadastre as contas bancárias

Cadastre cada conta da OSC (corrente, poupança, dinheiro em caixa, cartão) com o **saldo inicial correto** na data em que você começa a usar o Bússola. O saldo de cada conta passa a ser calculado a partir daí.

→ **Configurações → Contas Bancárias**. Detalhes em [Contas Bancárias](/configuracoes/contas/).

> ⚠️ **Atenção · Saldo inicial**
>
> Acerte o saldo inicial **antes** de lançar ou importar movimentações. Depois que a conta tem lançamentos, o saldo inicial fica **protegido** contra alteração acidental (só a Presidência destrava) — justamente para não distorcer o saldo atual.

[![Configuração de contas bancárias](/assets/screenshots/manual-09d-config-contas.png)](/assets/screenshots/manual-09d-config-contas.png)

## 3. Revise as categorias

As categorias classificam receitas e despesas — são a base de todo relatório legível. Em vez de criar do zero, **aplique um template** próximo ao perfil da sua OSC e ajuste o que não bater (renomeie, exclua, adicione).

→ **Configurações → Categorias → Aplicar template**. Detalhes em [Categorias](/configuracoes/categorias/).

> 💡 **Por que caprichar aqui**
>
> Categorias bem pensadas hoje são relatórios que a diretoria entende amanhã. Categorias bagunçadas são a fonte número um de relatórios financeiros confusos. Vale os 10 minutos.

[![Configuração de categorias](/assets/screenshots/manual-09e-config-categorias.png)](/assets/screenshots/manual-09e-config-categorias.png)

## 4. Defina o fluxo de aprovações

Diga quem autoriza a saída de dinheiro: o **quórum** (1 ou 2 votos) e **quais papéis ou pessoas** aprovam reembolsos e pedidos de pagamento. O padrão é Presidente e Tesoureiro.

→ **Configurações → Fluxo de Aprovações**. Detalhes em [Fluxo de Aprovações](/configuracoes/aprovacoes/).

[![Configuração do fluxo de aprovações](/assets/screenshots/manual-09f-config-workflow.png)](/assets/screenshots/manual-09f-config-workflow.png)

## 5. Convide os usuários e atribua papéis

Agora chame a equipe. Cadastre cada pessoa, defina o **papel** dela (Presidente, Tesoureiro, Diretor, Coordenador, Voluntário, Comissão Fiscal) e envie o convite — o acesso só vale após o aceite. Para muita gente de uma vez, use a **importação por CSV**.

→ **Configurações → Usuários**. Detalhes em [Usuários](/configuracoes/usuarios/) e em [Papéis e Permissões](/papeis/).

> 📖 **Conceito · Dê o acesso certo a cada um**
>
> Papéis bem atribuídos protegem todo mundo: a Presidência delega sem perder controle, o Tesoureiro opera sem ter de configurar a OSC, o Voluntário pede o próprio reembolso sem ver dados que não são dele. Na dúvida, comece restritivo — é fácil ampliar depois.

[![Configuração de usuários](/assets/screenshots/manual-09b-config-usuarios.png)](/assets/screenshots/manual-09b-config-usuarios.png)

## 6. (Opcional) Conecte a loja online

Se a OSC vende ou recebe doações por uma loja **WooCommerce**, conecte-a para que os pedidos pagos virem receitas automaticamente.

→ **Configurações → Organização → seção WooCommerce** (a tela traz o passo a passo de como gerar as credenciais).

## 7. Agora sim: importe os dados

Com a base pronta, traga o histórico:

- **Movimentações** — em **Movimentações → Importar Lançamentos**, suba o CSV do seu histórico (a Bússola valida linha a linha antes de criar). Veja [Movimentações](/modulos/movimentacoes/).
- **Usuários em lote** — se ainda não cadastrou a equipe, **Configurações → Usuários → Importar** aceita uma planilha com pré-visualização classificada por status.

> ✓ **Pronto para operar**
>
> Com dados da OSC, contas, categorias, fluxo de aprovação e usuários configurados, a sua organização está pronta. A partir daqui, o dia a dia é lançar, aprovar, acompanhar o Painel e gerar relatórios — tudo coberto nas seções de **Módulos** deste manual.

## Próximo passo

- Conheça o passo a passo de cada pessoa em **[Primeiros Passos do Usuário](/primeiros-passos/)**.
- Veja a cartilha de atuação do seu papel em **[Guias por Papel](/guias/coordenador-projetos/)** (Coordenador, Tesoureiro, Comissão Fiscal, Presidente).
