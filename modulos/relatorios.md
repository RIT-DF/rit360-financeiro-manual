---
title: "Relatórios"
nav_order: 6
parent: "Módulos"
permalink: /modulos/relatorios/
---

O módulo de **Relatórios** consolida o que entra e o que sai da sua OSC em **análises gerenciais prontas para uso** — sem precisar exportar planilha, montar gráfico, copiar e colar. É onde a diretoria descobre quanto há em caixa, para onde o dinheiro está indo, o que merece atenção este mês e o que esperar dos próximos meses.

> 💡 **Por que isso importa**
>
> O dado que entra no sistema todo dia (lançamentos, reembolsos, pedidos) **só vale se vira informação para decidir**. OSC sem relatórios financeiros bem feitos toma decisões no escuro: contratar ou não contratar, gastar ou poupar, captar ou esperar. Relatório bom não é firula visual — é base para a diretoria escolher caminho com segurança e para a OSC prestar contas com transparência para conselho, financiadores e assembleia.

## Conceitos essenciais

Antes de entrar nos botões, vale firmar três conceitos que aparecem em todas as cinco abas.

> 📖 **Conceito · Regime de caixa**
>
> Toda análise dos Relatórios olha o **dinheiro que de fato entrou ou saiu** — não o que estava contratado ou previsto. Receita só conta quando a doação **caiu na conta**; despesa só conta quando o pagamento **saiu da conta**. Por isso a aba de Visão Geral mostra "Resultado do período" usando apenas movimentações com status **Pago**. Esse é o padrão usado por OSC para prestação de contas e bate com a forma como tesoureiros amadores enxergam o dinheiro: "quanto tem na conta hoje?".

> 📖 **Conceito · Período anterior equivalente**
>
> O toggle **Comparar com período anterior** no cabeçalho compara o período carregado com o **mesmo tamanho de janela imediatamente anterior**. Se você está olhando Abril/2026 completo, a comparação é com Março/2026 completo. Se você selecionou um intervalo personalizado de 12 dias, a comparação é com os 12 dias anteriores ao início. Quando o período é um **mês em andamento** (ex: Maio até hoje), a comparação é com o mesmo número de dias do mês anterior — não com o mês anterior inteiro. Isso evita que uma comparação "honesta" mostre o mês em curso "menor" só porque ainda não terminou.

> 📖 **Conceito · Histórico mínimo para anomalias e forecast**
>
> Algumas análises (anomalias na aba Atenção, projeção na aba Previsão) precisam de **histórico mínimo** da OSC para fazer sentido. Sem histórico, não há base de comparação. Por isso, regras de atenção que dependem de média podem ficar silenciadas em OSC nova, e a aba Previsão tem horizontes (3, 6 ou 12 meses) que só liberam à medida que sua OSC acumula meses de movimentação registrada. **Não é bug — é honestidade estatística**.

## Quem acessa

Acesso a Relatórios é restrito a três papéis:

- **Presidente** — visão completa
- **Tesoureiro** — visão completa
- **Comissão Fiscal** — visão completa (consulta; sem operação)

Voluntários e Coordenadores de Projeto têm acesso restrito a Relatórios no momento.

> 💡 **Novidade · Filtro por projeto**
>
> Com o módulo de [Projetos](/modulos/projetos/), os Relatórios ganharam um **filtro por projeto** no cabeçalho: selecione uma iniciativa e todas as abas passam a mostrar apenas receitas, despesas e gráficos daquele projeto — pronto para a prestação de contas específica de um financiador. Cada projeto também tem uma aba **Relatório** própria, com os mesmos números recortados.

## As cinco abas

[![Aba Visão Geral](/assets/screenshots/manual-relatorios-01-visao-geral.png)](/assets/screenshots/manual-relatorios-01-visao-geral.png)
*Visão Geral — resultado em destaque, evolução do saldo, cards por conta e top 5 categorias*

O módulo tem cinco abas, navegáveis dentro de uma mesma tela (`/relatorios`). Filtros e período do cabeçalho valem para todas — você troca de aba sem perder o recorte. **A URL reflete o estado completo** (período, filtros, aba ativa, comparativo ligado/desligado): copiar e enviar o link leva outra pessoa exatamente ao mesmo recorte.

### Visão Geral

Resumo executivo do período:

- **Resultado do período** — receitas menos despesas pagas, em destaque com cor semântica (verde se positivo, vermelho se negativo). Com comparativo ligado, mostra também variação em R$, em % e seta de tendência.
- **Evolução do saldo** — gráfico de linha mostrando a trajetória do saldo da OSC ao longo do período. Quando o comparativo está ligado, uma linha pontilhada sobrepõe a evolução do período anterior.
- **Saldos por conta** — cards com o saldo de cada conta financeira na **data final do período** (não "hoje"). Isso garante coerência com prestação de contas histórica: o saldo mostrado é o que de fato existia no fechamento daquele mês.
- **Top 5 receitas e Top 5 despesas por categoria** — leitura rápida do que mais pesou. Link "Ver todas" leva às abas detalhadas.

### Receitas e Despesas

[![Aba Receitas](/assets/screenshots/manual-relatorios-02-receitas.png)](/assets/screenshots/manual-relatorios-02-receitas.png)
*Receitas — gráfico por categoria + tabela completa*

Duas abas com a mesma estrutura, separadas por tipo:

- **Gráfico** por categoria (barras horizontais com top 10).
- **Tabela detalhada** com todas as categorias, valor absoluto e % do total. Mais de 10 categorias? Aparece linha **Outros** agregada — clique para expandir todas.
- Com **comparativo ligado**: colunas extras com valor do período anterior, variação em R$, variação em % e seta de tendência.
- **Drilldown** — clique em uma linha de categoria e a Bússola abre `/movimentacoes` já filtrado por essa categoria + o mesmo período. Você passa do agregado para o detalhe em um clique.

[![Aba Despesas](/assets/screenshots/manual-relatorios-03-despesas.png)](/assets/screenshots/manual-relatorios-03-despesas.png)
*Despesas — mesma estrutura aplicada ao outro lado da equação*

### Atenção

[![Aba Atenção](/assets/screenshots/manual-relatorios-04-atencao.png)](/assets/screenshots/manual-relatorios-04-atencao.png)
*Atenção — anomalias detectadas no período, ordenadas por severidade*

A Bússola monitora **cinco regras determinísticas** sobre os seus lançamentos e destaca o que parece fora do padrão da sua OSC:

1. **Despesa única concentrada** — um lançamento representa mais que X% do total do período
2. **Categoria com pico de despesa** — uma categoria gastou muito mais que sua média histórica
3. **Fornecedor novo com alto valor** — primeiro lançamento com um fornecedor, em valor relevante
4. **Categoria zerada que voltou** — categoria sem movimento há N meses recebeu lançamento
5. **Queda de receita** — receita do período caiu abaixo de um % da média histórica

Cada anomalia tem **severidade** (leve / moderada / alta) com cor semântica e **link de ação contextual** ("Abrir lançamento", "Ver categoria", "Ver fornecedor", "Ver detalhe das receitas"). Ordenação: do mais severo para o menos severo. Um badge no nome da aba mostra a contagem total.

> 📖 **Conceito · O que define severidade**
>
> Severidade não é categoria abstrata — é matemática. **Leve** = o evento ultrapassa o limite em até 25%. **Moderada** = 25% a 50% acima do limite. **Alta** = mais de 50% acima. Exemplo: se a regra de "despesa concentrada" está em 20% e um lançamento representa 28% do total do mês, severidade é **leve** (28/20 − 1 = 40% acima → moderada, na verdade). Quanto mais "fora do padrão", mais visível na lista.

> ⚠️ **Atenção · Regras silenciadas não são erro**
>
> Se uma OSC nova ainda não tem 6 meses de histórico, várias regras simplesmente não disparam — não dá para detectar "pico de categoria" sem média de 6 meses para comparar. A regra fica **silenciada automaticamente** até o histórico permitir. Não é bug: é a Bússola sendo honesta sobre o que pode ou não afirmar.

Os limites de cada regra são configuráveis em **Configurações → Relatórios** (ver mais abaixo). Quando a OSC tem **6+ meses de histórico**, há ainda a opção **Calibrar pelo histórico** que sugere limites personalizados baseados no padrão real da sua OSC — em vez de você adivinhar valores.

### Previsão (forecast)

[![Aba Previsão](/assets/screenshots/manual-relatorios-05-previsao.png)](/assets/screenshots/manual-relatorios-05-previsao.png)
*Previsão — saldo projetado mês a mês, com badge de origem por célula*

A aba **Previsão** projeta como a OSC tende a se comportar nos próximos meses. Útil quando a diretoria pergunta "vamos conseguir pagar o aluguel em agosto?" ou "tem espaço para contratar um voluntário remunerado em setembro?".

> 📖 **Conceito · O que é forecast (projeção financeira)?**
>
> Projeção financeira (em inglês, *forecast*) é a tentativa séria de responder "para onde meu saldo vai nos próximos meses, considerando o que já está combinado e o que costumo gastar?" — sem cair em adivinhação. Não é previsão do tempo nem chute. É **modelo matemático** que combina o que está cadastrado no sistema com o histórico real da OSC.

> 📖 **Conceito · Como a Bússola monta a projeção (modelo híbrido)**
>
> Para cada mês futuro e cada categoria, a Bússola soma duas fontes:
> - **Agendados** — lançamentos pendentes com data futura, ocorrências futuras de séries recorrentes ativas (ex: aluguel mensal), parcelas futuras de pedidos de pagamento aprovados. Tudo isso já está cadastrado no sistema.
> - **Estimados** — quando uma categoria não tem agendado no mês mas tem padrão histórico (≥ 3 meses), usa a média dos últimos 6 meses. Categorias com menos de 3 meses de histórico não são projetadas.
>
> Cada célula traz **badge de origem** indicando se o valor é agendado ou estimado — você não confunde "o que está realmente combinado" com "o que costuma acontecer".

**Mês corrente:** entra como **primeiro mês projetado** com marcador "em curso", indicando que é projeção parcial — o mês ainda não terminou.

**Horizonte** (3, 6 ou 12 meses) com pré-requisitos:

| Horizonte | Histórico mínimo | Ideal |
|---|---|---|
| 3 meses | 3 meses de movimentação | 6 meses |
| 6 meses | 6 meses | 12 meses |
| 12 meses | 12 meses | 24 meses |

Horizontes com histórico insuficiente ficam **desabilitados** no seletor com tooltip explicando o motivo. Histórico entre o mínimo e o ideal exibe um **banner de qualidade** acima do gráfico.

**Alerta de meses críticos:** quando algum mês projetado fica com saldo negativo, um bloco destacado em vermelho lista os meses problemáticos — é a hora de revisar planejamento, não no dia que o saldo zerar de fato.

**Drilldown:** clique em qualquer célula da tabela para abrir a composição por categoria. Para agendados, lista os lançamentos com link para abrir. Para estimados, explica em prosa: *"Média mensal dos últimos 6 meses para 'Aluguel': R$ X"*.

> ⚠️ **Atenção · Projeção não é certeza**
>
> Forecast é **estimativa baseada em padrões** — não previsão do futuro. Doação inesperada que entra em julho não aparece na projeção (porque não existe ainda). Despesa extraordinária do próximo mês também não aparece (idem). Use a aba como **alerta antecipado** ("vou ter problema?") e como **hipótese de trabalho** ("se mantiver o padrão, vou para onde?"), nunca como afirmação categórica.

> 💡 **Por que isso importa**
>
> A maioria das OSCs descobre que vai faltar dinheiro só quando o saldo já zerou. A aba Previsão muda esse jogo — você vê o vermelho aparecendo no horizonte de 3, 6, 12 meses e tem tempo de agir: revisar despesas, antecipar captação, conversar com financiador. **Esse "tempo de agir" é a diferença entre uma OSC que sobrevive e uma que entra em crise**.

## Filtros e período compartilhados

Filtros disponíveis na barra do cabeçalho:

- **Período** — presets (mês corrente, mês anterior, trimestre, semestre, ano em curso, ano anterior) + intervalo customizado. Default: último mês fechado.
- **Conta** (multi-select)
- **Categoria** (multi-select)
- **Tipo** (receita / despesa)
- **Centro de custo** (multi-select)

Aplicam-se a todas as abas. Trocar de aba preserva filtros e período. URL reflete o estado completo.

> 📖 **Conceito · Por que status não aparece como filtro**
>
> Relatórios usam **regime de caixa** (ver início desta página): consideram apenas movimentações com status `pago`, agregadas pela data de pagamento. Pendentes e cancelados não entram no cálculo — exceto na aba Previsão, onde lançamentos pendentes futuros contam como "agendados".

## Comparativo com período anterior

Toggle no cabeçalho. Quando ligado, cada bloco/tabela/gráfico das abas **Visão Geral**, **Receitas** e **Despesas** mostra também a variação contra o período anterior equivalente.

Nas abas **Atenção** e **Previsão**, o toggle fica visível mas inerte — comparar anomalias do período corrente ou projeção futura com passado não faz sentido conceitual.

## Exportação

[![Menu Exportar](/assets/screenshots/manual-relatorios-06-exportar.png)](/assets/screenshots/manual-relatorios-06-exportar.png)
*Menu Exportar com três opções*

Botão **Exportar** no cabeçalho. Três opções:

- **Exportar visão atual (PDF)** — apenas a aba ativa
- **Exportar relatório completo (PDF)** — todas as cinco abas em sequência, com sumário no topo
- **Exportar dados (Excel)** — planilha com uma worksheet por seção

Todos os exports trazem **cabeçalho identificador** padrão: nome da OSC, escopo, período, lista de filtros aplicados, estado do comparativo (ligado/desligado) e data/hora de geração. Aba Receitas/Despesas exporta **todas** as categorias (não só o top 10). Aba Atenção exporta a lista completa de anomalias com mensagem, severidade textual e regra. Aba Previsão exporta a tabela mês a mês com coluna "Origem" textual.

> 📖 **Sobre gráficos no PDF**
>
> A primeira versão da exportação traz **tabelas e blocos textuais** — sem reprodução de gráficos visuais. Para enxergar a curva de saldo ou o gráfico de categorias, use a interface da Bússola. Gráficos no PDF entram em versão futura.

## Configuração das regras de atenção

[![Configuração de regras](/assets/screenshots/manual-config-relatorios-regras.png)](/assets/screenshots/manual-config-relatorios-regras.png)
*Configurações → Relatórios — cinco cards editáveis, um por regra*

Acessível em **Configurações → Relatórios** (só Presidente). Cinco cards, um por regra, cada um com:

- **Toggle on/off** — ligar ou desligar a regra
- **Limite (threshold)** em campo numérico editável com unidade clara (%, ×, R$ ou meses)
- **Link "Restaurar padrão"** — volta ao valor default daquela regra

No rodapé: **Salvar alterações** (só habilita se houver mudança) e **Restaurar todas as regras ao padrão** (com confirmação modal).

### Calibrar pelo histórico

Quando a OSC tem **6 ou mais meses de movimentação registrada**, o botão **Calibrar pelo histórico** dispara uma análise estatística: para cada regra, a Bússola calcula um limite sugerido baseado no padrão real da sua OSC. Útil porque tesoureiros raramente sabem chutar bons valores ("20% é muito? 30%?") — calibração entrega valores ancorados no histórico real.

Cada sugestão vem com **nível de confiança** (alta / média / baixa, dependendo do volume de histórico) e **justificativa em linguagem natural** (ex: *"Sua maior despesa única costuma ser 27% do total — sugerimos alertar a partir de 30%"*).

Três opções na hora de revisar:

- **Aceitar todas as sugestões** — aplica em transação única (tudo ou nada; se uma falha, nenhuma é salva)
- **Editar individualmente** — fecha o diálogo deixando os valores propostos pré-preenchidos nos cards; admin ajusta e clica Salvar
- **Cancelar** — descarta sem aplicar

> ✓ **Dica · Comece pelos defaults e calibre só depois de 6 meses**
>
> Os limites default (20% / 2× / R$ 5.000 / 3 meses / 70%) foram escolhidos para serem **conservadores** — disparam pouco em OSC saudável, mas mostram sinais claros quando algo sai do padrão. Use os defaults nos primeiros 6 meses. Quando atingir o histórico mínimo, rode a calibração — os limites passam a ser **personalizados para a sua OSC**, não para uma OSC genérica.

## Boas práticas

> ✓ **Dica · Olhe Relatórios uma vez por mês, no dia 5**
>
> Reserve 30 minutos no dia 5 de cada mês para abrir Relatórios filtrado no mês anterior fechado. Resultado do período + Top 5 receitas + Top 5 despesas + aba Atenção em sequência. Em 5 minutos você sabe se houve algo fora do esperado. Em outros 25, você manda o PDF do "relatório completo" para a diretoria com filtros do mês fechado — virou prestação de contas mensal sem esforço.

> ✓ **Dica · Forecast antes de decisão grande**
>
> Antes de aprovar contratação, compra grande ou novo projeto, abra a aba Previsão com horizonte de 6 ou 12 meses. Veja se o gasto extra mantém o saldo positivo. Se o gráfico mostra vermelho aparecendo em algum mês, a decisão precisa de mais conversa antes — não menos.

> ⚠️ **Atenção · Comparativo só faz sentido se o período faz sentido**
>
> Comparar Abril/2026 (mês fechado) com Março/2026 é direto. Comparar "Maio até hoje" (10 dias) com "10 dias antes de maio" também — mesma janela. Mas comparar "Ano até hoje" com algo... não tem comparação intuitiva. Em períodos não-canônicos, leia a variação com cautela.

## Glossário rápido

- **Regime de caixa** — modelo em que o que vale é a data em que o dinheiro entrou/saiu da conta, não a data do contrato ou da fatura.
- **Período anterior equivalente** — janela imediatamente anterior, com a mesma duração do período carregado.
- **Comparativo** — toggle que adiciona variação versus período anterior em cada bloco.
- **Anomalia** — evento detectado por uma das 5 regras determinísticas; ranqueado por severidade.
- **Severidade** — leve / moderada / alta, derivada do quanto o evento ultrapassa o limite da regra.
- **Calibração** — análise estatística que sugere limites de regras personalizados ao padrão da sua OSC.
- **Forecast (projeção)** — estimativa do comportamento financeiro futuro, combinando agendados (já cadastrados) com estimados (média histórica).
- **Agendado** — lançamento pendente, ocorrência futura de série recorrente, ou parcela futura de pedido aprovado.
- **Estimado** — projeção por média móvel de 6 meses, usada para categorias sem agendado no mês.
- **Horizonte** — quantos meses adiante o forecast projeta (3, 6 ou 12).
- **Mês em curso** — mês corrente projetado como primeiro mês do forecast, com badge indicando que é projeção parcial.

## Por onde seguir

- **Movimentações** — onde estão os lançamentos que alimentam todas as análises.
- **Configurações → Categorias** — relatório bom depende de categorização consistente.
- **Configurações → Relatórios** (Presidente) — ajustar limites de pontos de atenção, calibrar pelo histórico.
