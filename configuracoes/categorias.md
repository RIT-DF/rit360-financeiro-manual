---
title: "Categorias"
nav_order: 5
parent: "Configurações da Organização"
permalink: /configuracoes/categorias/
---

> Disponível para **Presidente (admin)** e **Tesoureiro**.

A página **Categorias** organiza as categorias contábeis e os centros de custo da OSC — o esqueleto da sua contabilidade gerencial.

[![Configurações — Categorias](/assets/screenshots/config-categorias.png)](/assets/screenshots/config-categorias.png)
*Configurações — Categorias e centros de custo*

> 💡 **Por que isso importa**
>
> Categoria é o que **faz o relatório financeiro fazer sentido**. Sem categoria, você tem 200 lançamentos no mês e nenhuma resposta sobre "para onde vai o dinheiro?". Com categoria ruim (inconsistente, duplicada, vaga), o relatório engana mais do que ajuda. Com categoria boa (enxuta, consistente, semântica), o relatório responde sozinho — você vê em 30 segundos quanto a OSC gastou com aluguel, quanto com material, quanto recebeu de doação, quanto de mensalidade. **Tempo investido em organizar categorias é o investimento de melhor retorno** que uma OSC pode fazer no Bússola.

A página tem 3 abas: **Receitas**, **Despesas** e **Centros de custo**.

## Receitas

Categorias para classificar entradas financeiras. Exemplos típicos de OSC:

- Doações
- Mensalidades de associados
- Subvenções e editais
- Arrecadação de eventos
- Venda de produtos (lojinha)
- Patrocínio
- Rendimentos financeiros

## Despesas

Categorias para classificar saídas. Exemplos:

- Aluguel
- Conta de luz, água, internet
- Material didático
- Material de escritório
- Combustível e transporte
- Alimentação
- Salários e encargos
- Manutenção
- Marketing e comunicação

## Centros de custo

> 📖 **Conceito · Categoria vs Centro de custo**
>
> **Categoria** classifica a *natureza* do lançamento (o que foi gasto/recebido): "aluguel", "doação", "combustível". **Centro de custo** classifica a *origem ou destino organizacional*: "Sede", "Filial Norte", "Coordenação de Eventos", "Diretoria de Comunicação". Os dois são independentes — um lançamento pode ter categoria "Combustível" e centro de custo "Filial Norte" simultaneamente. Centro de custo é opcional na maioria dos lançamentos; categoria é (quase sempre) obrigatória.

OSC pequena geralmente não precisa de centros de custo. OSC com **múltiplas frentes operacionais** (sede + filiais; várias coordenações; diretorias com orçamentos separados) ganha muito ao usar.

## Template de categorias

Para começar rapidamente, clique em **Aplicar template**. O Bússola tem modelos prontos por tipo de OSC — há templates para **Grupo Escoteiro, Associação, Instituto, Fundação, ONG, Coletivo e Cooperativa**, cada um com as categorias de receita e despesa típicas daquele perfil. Escolha o modelo mais próximo da sua organização; aplicar o template importa as categorias do modelo para a sua OSC, sem apagar o que você já tinha.

> ✓ **Dica · Comece com template, depois afine**
>
> Você nunca acerta a lista perfeita de categorias na primeira tentativa. Comece com um template próximo ao perfil da sua OSC, opere por 1-2 meses, e ajuste o que **não bater** com sua realidade: renomeie categorias confusas, una categorias que viraram redundantes, crie categoria nova quando 5+ lançamentos foram para "Outros". Lista enxuta vence lista exaustiva — categoria que aparece 2× no ano não vale ter como categoria separada.

> ⚠️ **Atenção · Cuidado ao renomear categoria em uso**
>
> Renomear uma categoria atinge **retroativamente** todos os lançamentos que já a usavam — eles passam a aparecer com o novo nome em relatórios e listagens. Geralmente isso é o que você quer (ajustou o nome para algo mais claro), mas pense duas vezes antes de renomear uma categoria que já foi referenciada em prestação de contas externa.

## Hierarquia de categorias

O Bússola suporta **categorias-mãe com sub-categorias** — útil para agrupar afins sem perder granularidade. Exemplo:

- Loja Virtual (categoria-mãe)
  - Camisetas
  - Canecas
  - Doações pelo site

O modo automático de integração com WooCommerce (em Configurações → Organização) usa exatamente esse padrão: cria sub-categorias sob a categoria-mãe escolhida para cada categoria do WC.

## Por onde seguir

- **Movimentações** — onde as categorias aparecem nos formulários de novo lançamento e nos filtros da lista.
- **Reembolsos** e **Pedidos de Pagamento** — onde as categorias de despesa são usadas para classificar as solicitações.
- **Configurações → Organização → Integrações** — onde a categoria-mãe do WooCommerce é configurada.
