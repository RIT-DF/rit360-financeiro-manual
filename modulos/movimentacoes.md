---
layout: section
title: Movimentações Financeiras
permalink: /modulos/movimentacoes/
---

O módulo de **Movimentações** é onde sua OSC registra cada entrada e saída de dinheiro — doação recebida, conta de luz paga, repasse entre contas, reembolso de combustível do voluntário. É o coração do sistema porque todos os outros módulos (Reembolsos, Pedidos de Pagamento, Relatórios, Conciliação) acabam alimentando ou se apoiando nessa lista.

> 💡 **Por que isso importa**
> Uma OSC que registra suas movimentações com disciplina **sabe a qualquer momento quanto tem em caixa, para onde o dinheiro está indo e quais despesas estão por vencer**. Sem esse registro, você descobre que o dinheiro acabou só quando o banco recusa o boleto — geralmente perto do fim do mês, sem tempo para resolver. Movimentações registradas em dia são a base para fluxo de caixa, relatórios para a diretoria, prestação de contas para financiadores e tranquilidade no fechamento contábil anual.

## Conceitos essenciais

Antes de entrar nos botões, vale firmar três conceitos que você vai ver em toda a Bússola.

> 📖 **Conceito · Receita, despesa e transferência**
> **Receita** é todo dinheiro que entra na OSC (doação, venda da lojinha, mensalidade de associado, repasse de edital). **Despesa** é todo dinheiro que sai (aluguel, conta de luz, compra de material, reembolso para voluntário). **Transferência** é movimento *interno* entre contas da própria OSC (do banco para a poupança, do dinheiro do caixinha para a conta corrente) — não é nem receita nem despesa, porque o dinheiro continua sendo seu, só muda de lugar. A distinção parece óbvia, mas misturá-las nas categorias é a fonte número um de relatórios financeiros distorcidos.

> 📖 **Conceito · Regime de caixa**
> A Bússola opera por **regime de caixa**: o que vale para o seu saldo e seus relatórios é a *data em que o dinheiro entrou ou saiu da conta*, não a data em que você assinou o contrato ou recebeu a fatura. Por isso a movimentação tem dois campos de data: **vencimento** (quando *deveria* acontecer) e **pagamento** (quando *aconteceu de fato*). Enquanto a data de pagamento não estiver preenchida, o dinheiro ainda não mexeu no seu saldo — ele está "previsto", não "realizado". Esse é o jeito mais simples e direto de acompanhar uma OSC e bate com a forma como a maioria das prestações de contas é feita.

> 📖 **Conceito · Status do lançamento**
> Cada movimentação tem um status que conta sua história. O ciclo de vida normal é **Pendente → Pago**. Quando o vencimento passa e nada foi pago, vira **Atrasado**. Quando uma movimentação não vai mais acontecer (ex: cancelaram o evento que pagaria o aluguel do salão), você a **Cancela**. Quando ela já estava paga mas precisa ser desfeita (ex: depósito caiu duplicado e o banco devolveu o segundo), você a **Estorna** — a Bússola cria um lançamento contrário automaticamente para preservar a história.

| Status | Significado | Quando aparece |
|---|---|---|
| 🟡 **Pendente** | Lançado, ainda não pago, dentro do prazo | Você registrou a conta de luz que vence dia 15; hoje é dia 10. |
| 🔴 **Atrasado** | Data de vencimento passou sem pagamento | Mesma conta de luz; hoje é dia 18 e ninguém marcou como paga. |
| 🟢 **Pago** | Confirmado como pago | Você marcou a conta como paga, anexou o comprovante. |
| 🟣 **Estornado** | Pagamento desfeito por inversão | Cliente devolveu uma doação; saída espelha a entrada original. |
| ⬛ **Cancelado** | Lançamento foi anulado manualmente | Lançou por engano ou o evento foi cancelado antes do pagamento. |

## Lista de movimentações

[![Lista de movimentações](../../assets/screenshots/manual-02-movimentacoes-lista.png)](../../assets/screenshots/manual-02-movimentacoes-lista.png)
*Lista de movimentações*

A lista mostra todas as movimentações com as colunas **Vencimento**, **Pagamento**, **Lançamento** (título e beneficiário), **Conta**, **Categoria**, **Status** e **Valor**.

Ao abrir a tela, ela já vem filtrada pelo **mês corrente** — o que você está operando agora. Para ver períodos anteriores ou outros recortes, use o filtro de período.

### Filtros e período contábil

Você pode filtrar por:

- **Período** — atalhos contábeis prontos (Mês atual, Mês anterior, Trimestre atual, Trimestre anterior, Semestre atual, Ano atual até hoje, Ano anterior) + opção **Personalizado** para definir intervalo livre + **Todos** para ver tudo
- **Conta** financeira
- **Categoria**
- **Status**

> 💡 **Por que isso importa**
> Atalhos contábeis (trimestre, semestre, ano) parecem detalhe, mas eles existem porque **prestação de contas e análise gerencial seguem esses recortes**, não os meses corridos. Quando a diretoria pergunta "como foi o primeiro trimestre?", você seleciona "Trimestre anterior" e o relatório está pronto — sem precisar configurar datas no calendário toda vez.

Quando há filtros ativos, uma linha "Filtrado por: …" aparece abaixo dos totais. O botão **Limpar filtros** remove todos de uma vez.

### Abas por tipo

A lista tem abas para filtrar por tipo: **Todas**, **Receitas**, **Despesas**, **Transferências**, **Estornadas** e **Canceladas**. Cada aba mostra a contagem entre parênteses (ex: "Receitas (12)") — útil para ver de relance o volume de cada tipo no período.

Na barra inferior aparecem os **totais do período filtrado**: receitas, despesas e saldo (receitas menos despesas).

### Identificadores visuais no título

Ao lado do título de cada movimentação, badges contam mais sobre a origem e a história dela:

- **Recorrente** — lançamento gerado por uma série recorrente (ex: aluguel mensal)
- **Parcela X de N** — uma parcela de um lançamento parcelado (ex: 3/6 de uma compra parcelada)
- **Estornado** — aparece tanto no lançamento original quanto no contrário gerado pelo estorno
- **WooCommerce** (roxo) — pedido importado automaticamente da sua loja online; clique no badge abre o pedido no admin do WooCommerce em nova aba

### Ordenação

Clique no cabeçalho de qualquer coluna para ordenar. Um segundo clique inverte a ordem; um terceiro remove a ordenação.

### Ações por linha

Cada linha tem ícones de ação que mudam conforme o status:

- ✏️ **Editar** — disponível para movimentações pendentes ou atrasadas
- 💲 **Marcar como pago** — disponível para pendentes e atrasadas (atalho rápido sem entrar no detalhe)
- ✕ **Cancelar** — disponível para pendentes e atrasadas
- ↩ **Estornar** — disponível para pagas
- 🗑 **Excluir** — disponível apenas para canceladas e estornadas

> ⚠️ **Atenção · Cancelar não é a mesma coisa que excluir**
> **Cancelar** marca o lançamento como anulado mas mantém o histórico — útil quando algo registrado não vai mais acontecer (evento desmarcado, fornecedor desistiu) e você quer rastreabilidade. **Excluir** apaga o lançamento de vez. A Bússola só permite excluir quem já foi cancelada ou estornada justamente para evitar perda acidental. Para auditoria limpa, prefira sempre **cancelar** a excluir.

### Seleção em lote

Marque o checkbox no início das linhas para selecionar várias movimentações. A barra de ações em lote aparece no rodapé com as opções **Marcar como pago** e **Excluir**.

### Exportação

O botão **Exportar** permite exportar para:

- **PDF** — relatório formatado com cabeçalho, filtros ativos e totais (bom para imprimir / enviar para diretoria)
- **Excel** — planilha com todas as colunas (bom para análises customizadas)

## Detalhe de uma movimentação

[![Detalhe de movimentação](../../assets/screenshots/manual-03-movimentacao-detalhe.png)](../../assets/screenshots/manual-03-movimentacao-detalhe.png)
*Detalhe de uma despesa*

Clique em qualquer linha da lista para abrir o detalhe completo, organizado em duas colunas no desktop:

**Coluna principal:**

- Tipo e status (chips coloridos no topo)
- Título e valor em destaque
- Dados do lançamento: vencimento, pagamento, conta, categoria, beneficiário/fornecedor, forma de pagamento, projeto, centro de custo
- Distribuição entre categorias (se o valor foi dividido)
- Observações
- Documentos: comprovantes e notas fiscais anexados, com pré-visualização inline para imagens e PDFs
- Quando o lançamento veio de outro módulo, links cruzados aparecem aqui:
  - **Ver pedido de pagamento** — para movimentações geradas a partir de uma solicitação de pagamento aprovada
  - **Ver pedido de reembolso** — para movimentações que pagaram um reembolso

**Coluna de auditoria (à direita no desktop, abaixo no mobile):**

Linha do tempo com todas as ações sobre o lançamento — quem criou, quem marcou como pago, quem estornou, quando, em qual ordem. Cada evento mostra ícone, nome do responsável e data/hora.

> 💡 **Por que isso importa**
> A timeline de auditoria não é firula. Em OSC, é comum a função financeira ser rotativa (passa de um voluntário para outro a cada ano) e questões surgem meses ou anos depois — *"essa despesa foi paga ou não?", "quem autorizou esse estorno?"*. A linha do tempo responde sem ambiguidade e protege todo mundo: o tesoureiro atual, o anterior, a diretoria que vai prestar contas.

## Registrar novo lançamento

[![Formulário de novo lançamento](../../assets/screenshots/manual-04-novo-lancamento.png)](../../assets/screenshots/manual-04-novo-lancamento.png)
*Formulário de novo lançamento*

Clique em **+ Novo lançamento** no topo da lista.

**Campos obrigatórios:**

- **Tipo** — Receita, Despesa ou Transferência
- **Título** — descrição breve (ex: "Conta de luz - março", "Doação Família Silva")
- **Data de vencimento**
- **Valor total**
- **Conta** — qual conta financeira movimenta
- **Categoria** — não obrigatória para Transferências (porque transferência é só mudança de lugar)

**Campos opcionais:**

- **Data de pagamento** — se preenchida no momento da criação, o lançamento já entra como **Pago**; se vazia, entra como **Pendente** e você confirma o pagamento depois
- **Projeto** e **Centro de custo** — para OSCs que dividem o financeiro por projeto/área
- **Distribuir valor entre categorias** — divide um único valor por várias categorias (ex: uma compra de R$ 500 que vai 60% para "Material didático" e 40% para "Manutenção")

> ✓ **Dica · Categorias consistentes valem ouro nos relatórios**
> Categoria é o que faz seus relatórios mensais e anuais terem sentido. Se metade dos lançamentos de combustível foi para "Transporte" e a outra metade para "Combustível", o relatório vai mostrar dois grupos pequenos em vez de um grupo real. Defina as categorias da sua OSC com cuidado em **Configurações → Categorias**, deixe a lista enxuta, e treine quem registra para usar sempre a mesma.

### Tipo de repetição

A barra lateral direita também controla a repetição do lançamento:

- **Único** — lançamento avulso (default para a maioria dos casos)
- **Parcelado** — divide um valor único em N parcelas com datas distintas (ex: compra de equipamento em 6×). A aprovação cria as parcelas todas de uma vez; cada uma tem sua data e pode ser paga individualmente.
- **Recorrente** — cria uma série que se repete automaticamente em intervalo regular (semanal, quinzenal, mensal, bimestral, trimestral, semestral, anual). A duração pode ser **por data final**, **por quantidade de ocorrências** ou **indefinida até cancelar**.

> 📖 **Conceito · Parcelado × Recorrente — qual usar?**
> Use **Parcelado** quando você sabe o valor total e quantas vezes vai pagar (compra de notebook em 6×, contrato fechado em 12 prestações). Use **Recorrente** quando o lançamento se repete por tempo indeterminado ou até segunda ordem (aluguel mensal, mensalidade de internet, doação fixa do mantenedor). A diferença é mais que cosmética: parcelas dividem **um valor único**, enquanto recorrências são **lançamentos independentes que repetem**. Cancelar uma recorrência para no mês escolhido; cancelar uma parcela cria uma pendência no plano de pagamento.

### Anexos e comprovantes

Você pode anexar arquivos (comprovantes, notas fiscais, contratos) ao lançamento. PDFs e imagens ganham pré-visualização inline no detalhe.

> ✓ **Dica · Anexe sempre, anexe na hora**
> Comprovante anexado na criação do lançamento custa 10 segundos. Procurar um comprovante de 8 meses atrás na pasta de e-mails do diretor anterior custa horas e às vezes não dá certo. **Adote como regra: nenhum lançamento sem comprovante.** Sua diretoria, sua auditoria contábil e seu eu do futuro vão agradecer.

## Estornar um lançamento

[![Dialog de estorno](../../assets/screenshots/manual-04c-estornar-dialog.png)](../../assets/screenshots/manual-04c-estornar-dialog.png)
*Dialog de estorno — informe a razão antes de confirmar*

Estornar é diferente de cancelar. Estorno é a forma contábil correta de reverter um lançamento **que já foi pago**.

> 📖 **Conceito · O que acontece quando você estorna**
> A Bússola não apaga o lançamento original. Em vez disso, cria automaticamente um **lançamento contrário** com a mesma data, o mesmo valor e a categoria/conta espelhadas — uma receita estornada vira uma despesa de igual valor, e vice-versa. Os dois ficam vinculados na timeline e ambos exibem o badge "Estornado". O resultado no saldo é o mesmo que se nada tivesse acontecido, mas **a história fica preservada**: você consegue mostrar, anos depois, que aquele depósito chegou, foi estornado, e por quê.

Para estornar: vá no detalhe do lançamento → botão **Estornar** → informe a razão. O lançamento contrário é criado e ambos ficam marcados na lista.

> ⚠️ **Atenção · Estorno preserva, exclusão apaga**
> Estornos podem ser feitos por motivos legítimos — devolução bancária, depósito duplicado, doação devolvida. Em todos esses casos, **estornar é o caminho correto, não excluir**. Excluir um lançamento pago não é nem permitido pela Bússola justamente para preservar a integridade da prestação de contas.

## Importar lançamentos

[![Importar Lançamentos com 2 fontes](../../assets/screenshots/manual-04b-importar-lancamentos.png)](../../assets/screenshots/manual-04b-importar-lancamentos.png)
*Importar Lançamentos — duas fontes disponíveis: CSV e WooCommerce*

Em vez de digitar lançamento por lançamento, você pode importar de duas fontes:

**Acesso:** botão **Importar Lançamentos** no topo da lista de movimentações.

### Importação por CSV

Útil para migrar histórico de planilhas (a base mais comum quando uma OSC começa a usar a Bússola). Faça download do template, preencha as linhas com seus lançamentos antigos, faça upload. A Bússola mostra um **preview** com erros por linha antes de criar nada; você confirma e os lançamentos são criados em lote.

### Importação do WooCommerce

Se sua OSC tem loja online em WooCommerce (venda de produtos, doações online, ingressos), pode conectar a loja à Bússola em **Configurações → Organização → WooCommerce**. Uma vez configurada, pedidos pagos viram receitas automaticamente — diariamente via sincronização programada ou sob demanda pelo botão **Importar agora** desta tela.

Mais detalhes na seção de configurações.

## Boas práticas

> ✓ **Dica · Adote uma rotina semanal de 15 minutos**
> A maior dor de OSCs amadoras na função financeira é deixar tudo acumular para o fim do mês. Aí cada lançamento exige resgatar comprovante, lembrar contexto, perguntar para gente que já esqueceu. **Reserve 15 minutos uma vez por semana** (toda terça de manhã, por exemplo) para registrar a movimentação da semana. É a diferença entre ter a contabilidade da OSC sempre pronta e viver apagando incêndio no dia 25.

> ✓ **Dica · Confira a lista contra o extrato bancário todo mês**
> No final do mês, abra o extrato do banco e a lista de movimentações da Bússola filtrada pelo mês. Cada linha do extrato deve ter um lançamento correspondente. Diferenças vão aparecer (taxa que você esqueceu, transferência que veio sem aviso) — corrigir essas diferenças mensalmente é mil vezes mais fácil do que descobrir 6 meses depois.

> ⚠️ **Atenção · Cuidado com transferências entre contas**
> Quando você move R$ 5.000 do banco para a poupança, **não é despesa nem receita** — é transferência. Se você lançar errado como despesa em "Banco" e como receita em "Poupança", o relatório vai mostrar que sua OSC gastou R$ 5.000 e ganhou R$ 5.000 do nada. Sempre use o tipo **Transferência** nesses casos; ele preserva o saldo geral e mantém os relatórios limpos.

## Glossário rápido

- **Receita** — dinheiro entrando na OSC.
- **Despesa** — dinheiro saindo da OSC.
- **Transferência** — movimento interno entre contas da própria OSC; não afeta o saldo total.
- **Vencimento** — data prevista para o pagamento (campo planejado).
- **Pagamento** — data em que o pagamento foi efetivamente realizado (campo realizado).
- **Categoria** — classificação contábil do lançamento (ex: Aluguel, Material didático, Doações).
- **Centro de custo** — agrupamento gerencial paralelo à categoria (ex: Sede, Filial-Norte).
- **Projeto** — agrupamento por iniciativa (ex: Acampamento 2026, Campanha do Agasalho).
- **Estorno** — reversão de um lançamento já pago, com criação automática de lançamento contrário.
- **Recorrente** — lançamento que se repete automaticamente em intervalo fixo.
- **Parcelado** — valor único dividido em parcelas com datas distintas.
- **Regime de caixa** — modelo contábil em que o que vale é a data de entrada/saída do dinheiro, não a data do contrato.

## Por onde seguir

- **Reembolsos** — para registrar despesas pagas com dinheiro próprio por voluntários ou diretores.
- **Pedidos de Pagamento** — para pedir aprovação antes de uma despesa ser paga.
- **Relatórios** — para visualizar fluxo de caixa, comparativos por categoria, evolução do saldo.
- **Configurações → Categorias** — para deixar suas categorias enxutas e consistentes.
