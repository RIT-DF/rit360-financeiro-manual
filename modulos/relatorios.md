---
layout: section
title: Relatórios
permalink: /modulos/relatorios/
---

O módulo de **Relatórios** consolida a informação financeira da OSC em **análises gerenciais prontas para uso** — sem precisar exportar planilha, montar gráfico, copiar e colar.

> 💡 **Por que isso importa**
> O dado que entra no sistema todo dia (lançamentos, reembolsos, pedidos) **só vale se vira informação para decidir**. OSC sem relatórios financeiros bem feitos toma decisões no escuro: contratar ou não contratar, gastar ou poupar, captar ou esperar. Relatório bom não é firula visual — é base para a diretoria escolher caminho com segurança e para a OSC prestar contas com transparência.

## Quem acessa

Acesso a **Relatórios** é restrito a três papéis:

- **Presidente** — visão completa
- **Tesoureiro** — visão completa
- **Comissão Fiscal** — visão completa (consulta; sem operação)

Voluntários e Coordenadores de Projeto **não acessam** Relatórios no momento. (Quando o módulo de Projetos chegar, Coordenadores terão visão restrita aos próprios projetos.)

## As cinco abas

O módulo tem cinco abas, navegáveis dentro de uma mesma tela (`/relatorios`). Filtros e período aplicados no cabeçalho valem para todas as abas — você troca de aba sem perder o recorte que montou.

### Visão Geral

Resumo executivo do período:

- **Resultado do período** — receitas menos despesas pagas, em destaque (verde se positivo, vermelho se negativo)
- **Evolução do saldo** — gráfico de linha mostrando a trajetória do saldo da OSC ao longo do período
- **Saldos por conta** — cards com o saldo de cada conta na data final do período (não "hoje" — coerência com prestação de contas histórica)
- **Top 5 receitas e despesas por categoria** — para uma leitura rápida do que pesou mais

### Receitas e Despesas

Duas abas com a mesma estrutura, separadas por tipo:

- **Gráfico** por categoria (barras horizontais com top 10)
- **Tabela detalhada** com todas as categorias, valor absoluto e % do total. Mais de 10 categorias? Aparece linha "Outros" agregada — clique para expandir todas.
- **Drilldown** — clique em uma linha de categoria e o sistema abre `/movimentacoes` já filtrado por essa categoria + o mesmo período

### Atenção

Lista anomalias detectadas no período por **cinco regras configuráveis**:

1. **Despesa única concentrada** — um lançamento representa mais que X% do total do período
2. **Categoria com pico de despesa** — uma categoria gastou muito mais que sua média histórica
3. **Fornecedor novo com alto valor** — primeiro lançamento com um fornecedor, em valor relevante
4. **Categoria zerada que voltou** — categoria sem movimento há N meses recebeu lançamento
5. **Queda de receita** — receita do período caiu abaixo de um % da média histórica

Cada anomalia tem severidade (leve / moderada / alta) com cor semântica e link de ação contextual ("Abrir lançamento", "Ver categoria", "Ver fornecedor", "Ver detalhe das receitas").

A configuração das regras vive em [Configurações → Relatórios](/configuracoes/), restrita ao Presidente. Lá é possível ligar/desligar regras, ajustar thresholds manualmente, restaurar os defaults, e usar o botão **"Calibrar pelo histórico"** para que o sistema sugira valores baseados no padrão real da sua OSC (disponível a partir de 6 meses de movimentação registrada).

### Previsão

Forecast híbrido de fluxo de caixa para os próximos **3, 6 ou 12 meses**, combinando:

- **Lançamentos já cadastrados** com data futura (pendentes, ocorrências de séries recorrentes ativas, parcelas de pedidos de pagamento aprovados) — chamados **agendados**
- **Extrapolação por média móvel** dos últimos 6 meses por categoria — preenche o que ainda não está cadastrado mas tem padrão histórico — chamados **estimados**

Cada célula da tabela traz **badge de origem** indicando se o valor é agendado ou estimado. O mês corrente entra como primeiro mês projetado com marcador "em curso" — projeção parcial. Drilldown ao clicar numa célula mostra a composição: para agendados, a lista de lançamentos com link de detalhe; para estimados, a explicação em prosa da média usada.

Quando a projeção indica saldo negativo em algum mês, um alerta destacado lista os meses críticos.

Cada horizonte exige um mínimo de histórico (3 → 3 meses, 6 → 6 meses, 12 → 12 meses). Histórico entre o mínimo e o ideal aparece com um banner de qualidade explicativo.

## Filtros e período

Filtros disponíveis na barra:

- **Período** (presets: mês corrente, mês anterior, trimestre, semestre, ano em curso, ano anterior, ou intervalo customizado)
- **Conta** (multi-select)
- **Categoria** (multi-select)
- **Fornecedor** (multi-select)
- **Tipo** (receita / despesa)
- **Centro de custo** (multi-select)

Os filtros aplicam-se a todas as abas. Trocar de aba preserva os filtros e o período. A URL reflete o estado completo — copiar e enviar o link leva outra pessoa ao mesmo recorte.

> 📖 **Por que o status não aparece como filtro**
> Relatórios usam **regime de caixa**: consideram apenas movimentações com status `pago`, agregadas pela data de pagamento. Pendentes e cancelados não entram no cálculo — exceto na aba Previsão, onde lançamentos pendentes futuros contam como "agendados".

## Comparativo com período anterior

Toggle no cabeçalho. Quando ligado, cada bloco/tabela/gráfico das abas Visão Geral, Receitas e Despesas mostra também a variação contra o período anterior equivalente: variação em R$, variação em %, seta de tendência.

A definição do "período anterior equivalente" segue a granularidade:

- **Mês completo** → mês anterior completo
- **Trimestre/semestre/ano completo** → bloco equivalente anterior completo
- **Mês corrente em andamento ou intervalo customizado** → mesma duração imediatamente antes do início do período atual

Nas abas Atenção e Previsão, o toggle fica visível mas inerte — comparar anomalias do período corrente ou projeção futura com passado não faz sentido conceitual.

## Exportação

Botão **Exportar** no cabeçalho, três opções:

- **Exportar visão atual (PDF)** — apenas a aba ativa
- **Exportar relatório completo (PDF)** — todas as cinco abas em sequência, com sumário no topo
- **Exportar dados (Excel)** — planilha com uma worksheet por seção

Todos os exports trazem cabeçalho identificador: nome da OSC, escopo, período, lista de filtros aplicados, estado do comparativo (ligado/desligado), e data/hora de geração. Aba Receitas/Despesas exporta **todas** as categorias (não só o top 10). Aba Atenção exporta a lista completa de anomalias com mensagem, severidade textual e regra. Aba Previsão exporta a tabela mês a mês com coluna "Origem" textual.

> 📖 **Sobre gráficos no PDF**
> A primeira versão da exportação traz **tabelas e blocos textuais** — sem reprodução de gráficos visuais. Para enxergar a curva de saldo ou o gráfico de categorias, use a interface da Bússola. Gráficos no PDF entram em versão futura.

## Por onde seguir

- **Configurações → Relatórios** (Presidente) — ajustar as regras de pontos de atenção; calibrar pelo histórico
- **Movimentações** — onde estão os lançamentos que alimentam todas as análises
- **Configurações → Categorias** — relatório bom depende de categorização consistente
