---
title: "Cargos e Permissões"
nav_order: 3
parent: "Configurações da Organização"
permalink: /configuracoes/cargos/
---

> Disponível para **Presidente (admin)**.

A página **Cargos e permissões** vai além dos 6 cargos padrão da plataforma: além de **renomear** cada cargo, o Presidente pode **criar cargos novos** e **ajustar as permissões** com controle fino — por exemplo, um "Tesoureiro sem exclusão" que registra lançamentos mas não pode excluí-los.

[![Configurações — Cargos e permissões](/assets/screenshots/config-cargos.png)](/assets/screenshots/config-cargos.png)
*Editor de cargos — à esquerda a lista, à direita as permissões do cargo selecionado*

> 💡 **Por que isso importa**
>
> Cada OSC se organiza de um jeito. Os 6 papéis padrão cobrem a maioria dos casos, mas às vezes você precisa de uma função sob medida — um "Secretário" que só vê relatórios, um "Tesoureiro júnior" que lança mas não exclui, um "Captador de recursos" com acesso a reembolsos. Em vez de forçar a pessoa num papel que dá acesso demais (ou de menos), você monta o cargo certo e atribui. Tudo é validado **no servidor** — a tela só reflete o que a pessoa realmente pode fazer.

## Conceitos

> 📖 **Conceito · Cargo padrão × cargo personalizado**
>
> **Cargos padrão** são os 6 que já vêm na plataforma (Presidente, Tesoureiro, Diretor, Coord. de projeto, Comissão Fiscal, Voluntário) — aparecem com a etiqueta **Padrão**. **Cargos personalizados** são os que a sua OSC cria — etiqueta **Personalizado**. A diferença prática está na edição (veja abaixo): cargo padrão tem um piso de permissões que não sai; cargo personalizado é totalmente editável.

> 📖 **Conceito · Permissões essenciais e acréscimos**
>
> Cada cargo padrão tem um conjunto de **permissões essenciais** — o piso que define aquele papel e **não pode ser removido** (aparece travado, com a etiqueta "essencial"). O Presidente só pode **acrescentar** permissões sobre esse piso. Já um cargo personalizado não tem piso: todas as permissões são interruptores que você liga e desliga livremente.

> 📖 **Conceito · Permissão efetiva**
>
> Uma pessoa pode ter **mais de um cargo** ao mesmo tempo. O que ela pode fazer é a **soma** das permissões de todos os cargos dela. É essa permissão somada que o sistema usa para liberar ou barrar cada ação.

## As permissões

As permissões são organizadas por área, com as operações que importam separadas:

- **Movimentações** — Ver · Criar / editar · Excluir / estornar · Importar lançamentos
- **Reembolsos e pedidos de pagamento** — Ver · Aprovar · Pagar
- **Relatórios e auditoria** — Ver relatórios · Ver trilha de auditoria · Exportar dados (LGPD)
- **Configurações** — Config. financeira (contas e categorias) · Config. da OSC · Gerir membros e cargos

## Editar um cargo

Clique no cargo na lista à esquerda; as permissões aparecem à direita.

- Em **cargo personalizado**, cada permissão é um **interruptor** — ligue ou desligue à vontade.
- Em **cargo padrão**, as **essenciais** ficam travadas; os demais aparecem como interruptores que o Presidente pode **acrescentar**.
- Clique em **Salvar alterações** ao final. Em cargo padrão, salva só os acréscimos sobre o essencial.

[![Cargo personalizado — permissões editáveis](/assets/screenshots/config-cargos-custom.png)](/assets/screenshots/config-cargos-custom.png)
*Cargo personalizado: cada permissão é um interruptor (aqui, "Excluir / estornar" desligado)*

> ⚠️ **Atenção · Delegar poderes de administrador**
>
> Ao ligar **Config. da OSC** ou **Gerir membros e cargos**, o sistema avisa que você está concedendo **poderes de administrador**: quem tiver esse cargo passa a ter o mesmo controle que um Presidente sobre aquela área. Conceda apenas a quem você confia para administrar a organização.

## Comissão Fiscal: independência protegida

A **Comissão Fiscal** existe para fiscalizar as finanças com independência. Por isso, as permissões que **conflitam com a fiscalização** — operar, aprovar ou pagar finanças e gerir configuração — ficam **bloqueadas** no cargo Comissão Fiscal, **mesmo para o Presidente**. Acréscimos inofensivos (como exportar dados) são permitidos, com aviso.

A mesma regra vale na atribuição: se você tentar dar a uma pessoa da Comissão Fiscal um cargo que tem permissões conflitantes, o sistema **barra com explicação**.

> 💡 **Por que isso importa · Segregação de funções**
>
> Quem opera o dinheiro não pode ser quem fiscaliza o dinheiro — é o princípio que dá credibilidade ao conselho fiscal e costuma estar no estatuto da OSC. O Bússola protege isso automaticamente, para que a fiscalização nunca acabe auditando os próprios atos.

## Criar e clonar cargos

[![Diálogo de criar cargo personalizado](/assets/screenshots/config-cargos-criar.png)](/assets/screenshots/config-cargos-criar.png)
*Criar cargo: dê um nome e, opcionalmente, parta das permissões de um cargo existente*

- **Criar cargo** — botão no fim da lista. Dê um nome e escolha **começar do zero** ou **clonar** as permissões de um cargo existente. Depois ajuste os interruptores e salve.
- **Clonar** — disponível no cabeçalho de qualquer cargo: cria um personalizado já preenchido com as permissões daquele cargo, pronto para ajustar (ex.: clonar Tesoureiro e desligar "Excluir / estornar").

## Excluir um cargo personalizado

Cargos padrão não podem ser excluídos. Um cargo personalizado pode — **exceto se tiver membros**: nesse caso o sistema **bloqueia e mostra quem só tem aquele cargo**, para você reatribuir antes.

## Atribuir cargos às pessoas

A atribuição é feita em **Configurações → Usuários**: no menu de ações de cada pessoa, **Editar papéis** lista os cargos padrão **e** os personalizados; marque um ou vários (a pessoa acumula as permissões de todos).

[![Editar papéis — cargos padrão e personalizados](/assets/screenshots/config-usuarios-papeis.png)](/assets/screenshots/config-usuarios-papeis.png)
*Editar papéis: marque os cargos da pessoa (padrão e/ou personalizados)*

## Renomear o rótulo de um cargo

Você também pode trocar **como cada cargo é chamado** na sua OSC (onde o Bússola diz "Tesoureiro", a sua associação pode dizer "Diretor Financeiro") — sem mudar as permissões. O novo rótulo aparece em toda a aplicação.

## Por onde seguir

- **Configurações → Usuários** — para atribuir os cargos aos membros.
- **[Papéis e Permissões](/papeis/)** — a referência do que cada papel padrão pode ver e fazer.
