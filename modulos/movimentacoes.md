---
title: "Movimentações"
nav_order: 2
parent: "Módulos"
permalink: /modulos/movimentacoes/
---

O módulo de **Movimentações** é onde sua OSC registra cada entrada e saída de dinheiro — doação recebida, conta de luz paga, repasse entre contas, reembolso de combustível do voluntário. É o coração do sistema porque todos os outros módulos (Reembolsos, Pedidos de Pagamento, Relatórios, Conciliação) acabam alimentando ou se apoiando nessa lista.

> 💡 **Por que isso importa**
>
> Uma OSC que registra suas movimentações com disciplina **sabe a qualquer momento quanto tem em caixa, para onde o dinheiro está indo e quais despesas estão por vencer**. Sem esse registro, você descobre que o dinheiro acabou só quando o banco recusa o boleto — geralmente perto do fim do mês, sem tempo para resolver. Movimentações registradas em dia são a base para fluxo de caixa, relatórios para a diretoria, prestação de contas para financiadores e tranquilidade no fechamento contábil anual.

## Conceitos essenciais

Antes de entrar nos botões, vale firmar três conceitos que você vai ver em toda o RIT360 Financeiro.

> 📖 **Conceito · Receita, despesa e transferência**
>
> **Receita** é todo dinheiro que entra na OSC (doação, venda da lojinha, mensalidade de associado, repasse de edital). **Despesa** é todo dinheiro que sai (aluguel, conta de luz, compra de material, reembolso para voluntário). **Transferência** é movimento *interno* entre contas da própria OSC (do banco para a poupança, do dinheiro do caixinha para a conta corrente) — não é nem receita nem despesa, porque o dinheiro continua sendo seu, só muda de lugar. A distinção parece óbvia, mas misturá-las nas categorias é a fonte número um de relatórios financeiros distorcidos.

> 📖 **Conceito · Regime de caixa**
>
> O RIT360 Financeiro opera por **regime de caixa**: o que vale para o seu saldo e seus relatórios é a *data em que o dinheiro entrou ou saiu da conta*, não a data em que você assinou o contrato ou recebeu a fatura. Por isso a movimentação tem dois campos de data: **vencimento** (quando *deveria* acontecer) e **pagamento** (quando *aconteceu de fato*). Enquanto a data de pagamento não estiver preenchida, o dinheiro ainda não mexeu no seu saldo — ele está "previsto", não "realizado". Esse é o jeito mais simples e direto de acompanhar uma OSC e bate com a forma como a maioria das prestações de contas é feita.

> 📖 **Conceito · Status do lançamento**
>
> Cada movimentação tem um status que conta sua história. O ciclo de vida normal é **Pendente → Pago**. Quando o vencimento passa e nada foi pago, vira **Atrasado**. Quando uma movimentação não vai mais acontecer (ex: cancelaram o evento que pagaria o aluguel do salão), você a **Cancela**. Quando ela já estava paga mas precisa ser desfeita (ex: depósito caiu duplicado e o banco devolveu o segundo), você a **Estorna** — o RIT360 Financeiro cria um lançamento contrário automaticamente para preservar a história.

| Status | Significado | Quando aparece |
|---|---|---|
| 🟡 **Pendente** | Lançado, ainda não pago, dentro do prazo | Você registrou a conta de luz que vence dia 15; hoje é dia 10. |
| 🔴 **Atrasado** | Data de vencimento passou sem pagamento | Mesma conta de luz; hoje é dia 18 e ninguém marcou como paga. |
| 🟢 **Pago** | Confirmado como pago | Você marcou a conta como paga, anexou o comprovante. |
| 🟣 **Estornado** | Pagamento desfeito por inversão | Cliente devolveu uma doação; saída espelha a entrada original. |
| ⬛ **Cancelado** | Lançamento foi anulado manualmente | Lançou por engano ou o evento foi cancelado antes do pagamento. |

## Lista de movimentações

[![Lista de movimentações](/assets/screenshots/manual-02-movimentacoes-lista.png)](/assets/screenshots/manual-02-movimentacoes-lista.png)
*Lista de movimentações em desktop — tabela com todas as colunas*

A lista mostra todas as movimentações com as colunas **Vencimento**, **Pagamento**, **Lançamento** (descrição e contraparte), **Conta**, **Categoria**, **Status** e **Valor**.

No **celular** ou em telas estreitas (abaixo de 1024 px de largura), a tabela vira uma **lista de cards** com a mesma informação organizada verticalmente — descrição em destaque, valor colorido, data, contraparte, conta, categoria, status e menu de ações:

[![Lista de movimentações no celular](/assets/screenshots/mobile-movimentacoes-cards.png)](/assets/screenshots/mobile-movimentacoes-cards.png)
*Lista de movimentações no celular — cada lançamento como card*

Para ordenar a lista no celular, use o seletor **"Ordenar por"** logo acima dos cards.

Ao abrir a tela, ela já vem filtrada pelo **mês corrente** — o que você está operando agora. Para ver períodos anteriores ou outros recortes, use o filtro de período.

### Filtros e período contábil

Você pode filtrar por:

- **Período** — atalhos contábeis prontos (Mês atual, Mês anterior, Trimestre atual, Trimestre anterior, Semestre atual, Ano atual até hoje, Ano anterior) + opção **Personalizado** para definir intervalo livre + **Todos** para ver tudo
- **Conta** financeira
- **Categoria**
- **Status**

> 💡 **Por que isso importa**
>
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
- 🗑 **Excluir** — disponível apenas para canceladas (estornos são preservados e **não** podem ser excluídos)

> ⚠️ **Atenção · Cancelar não é a mesma coisa que excluir**
>
> **Cancelar** marca o lançamento como anulado mas mantém o histórico — útil quando algo registrado não vai mais acontecer (evento desmarcado, fornecedor desistiu) e você quer rastreabilidade. **Excluir** apaga o lançamento de vez. O RIT360 Financeiro só permite excluir lançamentos já **cancelados**, justamente para evitar perda acidental; **estornos são preservados** (não podem ser excluídos) para manter a prestação de contas íntegra. Para auditoria limpa, prefira sempre **cancelar** a excluir.

### Seleção em lote

Marque o checkbox no início das linhas para selecionar várias movimentações. A barra de ações em lote aparece no rodapé com as opções **Marcar como pago** e **Excluir**.

### Exportação

O botão **Exportar** oferece três saídas:

- **PDF** — relatório formatado com cabeçalho, filtros ativos e totais (bom para imprimir / enviar para diretoria)
- **Excel** — planilha para análises customizadas
- **Prestação de contas** — o documento contábil completo do período, em regime de caixa, com os comprovantes anexados (ver a seção **Prestação de contas** abaixo)

Ao escolher **PDF** ou **Excel**, antes de gerar o arquivo o RIT360 Financeiro abre um **seletor de colunas**: marque ou desmarque o que deve aparecer no relatório. Vêm marcadas por padrão oito colunas — Vencimento, Pagamento, Pagador/Beneficiário, Lançamento, Conta, Categoria, Status e Valor — e você pode acrescentar **Tipo**, **Forma de pagamento**, **Observações** e **Nº de anexos**. A seleção é **lembrada para a próxima exportação**, separada por organização (cada OSC mantém o formato que prefere). É preciso deixar pelo menos uma coluna marcada.

## Detalhe de uma movimentação

[![Detalhe de movimentação](/assets/screenshots/manual-03-movimentacao-detalhe.png)](/assets/screenshots/manual-03-movimentacao-detalhe.png)
*Detalhe de uma despesa*

Clique em qualquer linha da lista para abrir o detalhe completo, organizado em duas colunas no desktop:

**Coluna principal:**

- Tipo e status (chips coloridos no topo)
- Título e valor em destaque
- Dados do lançamento: vencimento, pagamento, conta, categoria, beneficiário/fornecedor, forma de pagamento, projeto, centro de custo
- **Dados de pagamento** — quando o lançamento tem chave PIX ou dados bancários do destinatário, um card mostra esses dados para efetivar o pagamento sem abrir a solicitação de origem. Vale tanto para lançamentos vindos de **reembolso/pedido de pagamento** quanto para **despesas lançadas à mão** (ver "Forma de pagamento" no formulário). Aparece apenas para quem tem permissão de ver esses dados (tesoureiro, aprovadores e administradores)
- Distribuição entre categorias (se o valor foi dividido)
- Observações
- Documentos: comprovantes e notas fiscais anexados, com pré-visualização inline para imagens e PDFs
- Quando o lançamento veio de outro módulo, links cruzados aparecem aqui:
  - **Ver pedido de pagamento** — para movimentações geradas a partir de uma solicitação de pagamento aprovada
  - **Ver pedido de reembolso** — para movimentações que pagaram um reembolso

**Coluna de auditoria (à direita no desktop, abaixo no mobile):**

Linha do tempo com todas as ações sobre o lançamento — quem criou, quem marcou como pago, quem estornou, quando, em qual ordem. Cada evento mostra ícone, nome do responsável e data/hora.

> 💡 **Por que isso importa**
>
> A timeline de auditoria não é firula. Em OSC, é comum a função financeira ser rotativa (passa de um voluntário para outro a cada ano) e questões surgem meses ou anos depois — *"essa despesa foi paga ou não?", "quem autorizou esse estorno?"*. A linha do tempo responde sem ambiguidade e protege todo mundo: o tesoureiro atual, o anterior, a diretoria que vai prestar contas.

## Registrar novo lançamento

[![Formulário de novo lançamento](/assets/screenshots/manual-04-novo-lancamento.png)](/assets/screenshots/manual-04-novo-lancamento.png)
*Formulário de novo lançamento*

Clique em **+ Novo lançamento** no topo da lista. O formulário abre em **página própria**, com um resumo e um checklist do lado direito que vão se preenchendo conforme você digita.

**Campos obrigatórios:**

- **Tipo** — Receita, Despesa ou Transferência (define o resto do formulário)
- **Descrição** — descrição breve do lançamento (ex: "Conta de luz - março", "Doação Família Silva")
- **Data de vencimento**
- **Valor total**
- **Conta** — qual conta financeira movimenta. Já vem **pré-selecionada com a [conta padrão](/configuracoes/contas/#conta-padrão)** da OSC; troque se for outra
- **Categoria** — não pedida para Transferências (porque transferência é só mudança de lugar)

**Campos opcionais:**

- **Beneficiário / Pagador** — quem recebeu o pagamento (em Despesa, "Beneficiário") ou de quem veio o dinheiro (em Receita, "Pagador"). Fica no topo do formulário, logo após o tipo
- **Tipo de documento fiscal** e **Número do documento** — para registrar a nota/recibo que originou o lançamento
- **Data de pagamento** — se preenchida no momento da criação, o lançamento já entra como **Pago**; se vazia, entra como **Pendente** e você confirma o pagamento depois
- **Projeto** e **Centro de custo** — para OSCs que dividem o financeiro por projeto/área
- **Forma de pagamento** (em Despesa) — como o pagamento será feito. Ao escolher **PIX**, o formulário abre os campos da **chave PIX** (tipo e chave); ao escolher **Transferência bancária**, abre os **dados bancários** do destinatário (banco, agência, conta e titular); **Boleto** e as demais formas não pedem campos extras. Esses dados são opcionais e ficam guardados no lançamento — úteis para quem for efetivar o pagamento depois
- **Distribuir valor entre categorias** — divide um único valor por várias categorias (ex: uma compra de R$ 500 que vai 60% para "Material didático" e 40% para "Manutenção")

> 📖 **Conceito · O formulário se adapta ao tipo**
>
> Ao escolher **Transferência**, o RIT360 Financeiro **oculta os campos que não fazem sentido** para um movimento interno entre contas — Beneficiário, Categoria e os campos de documento fiscal somem, e aparece o campo de **conta de destino**. Você só vê o que precisa preencher para cada tipo de lançamento. Da mesma forma, os campos de destinatário (chave PIX / dados bancários) só aparecem em **Despesa**, conforme a forma de pagamento escolhida.

No **celular**, o mesmo formulário se organiza em uma coluna única, na ordem em que você preenche — desenhado para registrar um lançamento de pé, em campo, sem zoom nem rolagem horizontal:

[![Novo lançamento no celular](/assets/screenshots/mobile-novo-lancamento.png)](/assets/screenshots/mobile-novo-lancamento.png)
*Novo lançamento no celular — coluna única, campos na ordem de preenchimento*

> ✓ **Dica · Categorias consistentes valem ouro nos relatórios**
>
> Categoria é o que faz seus relatórios mensais e anuais terem sentido. Se metade dos lançamentos de combustível foi para "Transporte" e a outra metade para "Combustível", o relatório vai mostrar dois grupos pequenos em vez de um grupo real. Defina as categorias da sua OSC com cuidado em **Configurações → Categorias**, deixe a lista enxuta, e treine quem registra para usar sempre a mesma.

### Tipo de repetição

A barra lateral direita também controla a repetição do lançamento:

- **Único** — lançamento avulso (default para a maioria dos casos)
- **Parcelado** — divide um valor único em N parcelas com datas distintas (ex: compra de equipamento em 6×). A aprovação cria as parcelas todas de uma vez; cada uma tem sua data e pode ser paga individualmente.
- **Recorrente** — cria uma série que se repete automaticamente em intervalo regular (semanal, quinzenal, mensal, bimestral, trimestral, semestral, anual). A duração pode ser **por data final**, **por quantidade de ocorrências** ou **indefinida até cancelar**.

> 📖 **Conceito · Parcelado × Recorrente — qual usar?**
>
> Use **Parcelado** quando você sabe o valor total e quantas vezes vai pagar (compra de notebook em 6×, contrato fechado em 12 prestações). Use **Recorrente** quando o lançamento se repete por tempo indeterminado ou até segunda ordem (aluguel mensal, mensalidade de internet, doação fixa do mantenedor). A diferença é mais que cosmética: parcelas dividem **um valor único**, enquanto recorrências são **lançamentos independentes que repetem**. Cancelar uma recorrência para no mês escolhido; cancelar uma parcela cria uma pendência no plano de pagamento.

### Anexos e comprovantes

Você pode anexar arquivos (comprovantes, notas fiscais, contratos) ao lançamento. Anexo é **opcional** — lançamento sem comprovante continua válido — mas é fortemente recomendado para qualquer movimentação que tenha origem em compra, serviço contratado ou pagamento de terceiro. PDFs e imagens ganham pré-visualização inline na página de detalhe.

**Em mobile**, a seção **DOCUMENTOS** exibe dois botões: **Tirar foto** (abre a câmera traseira do celular direto, com preview **Refazer** ou **Confirmar** antes de subir) e **Anexar arquivo** (aceita imagens, PDF, XML de NFe e ZIP). O RIT360 Financeiro reduz a foto automaticamente antes do upload — fica leve mesmo em conexão móvel ruim, sem perder a legibilidade do cupom para auditoria humana ou para extração automática futura via IA.

**Em desktop**, a seção mostra uma área para arrastar arquivos ou clicar para selecionar — o botão "Tirar foto" não aparece nesse contexto (webcam de laptop não serve para fotografar comprovante apoiado na mesa).

**Anexou um arquivo ZIP?** O RIT360 Financeiro **descompacta o pacote automaticamente** e anexa cada documento de dentro como um anexo individual do lançamento — o ZIP some da lista, dando lugar aos arquivos. Assim, cada comprovante que estava no pacote ganha pré-visualização e **entra na prestação de contas** (um ZIP, por ser um pacote fechado, não poderia ser exibido no relatório). A expansão roda em segundo plano, em segundos, e vale também quando o comprovante chega por **link** na importação por CSV. Arquivos que não dá para exibir num PDF (planilhas, documentos de texto) ficam anexados, mas não aparecem no corpo do relatório.

**Em Novo Lançamento nos modos Recorrente e Parcelado**, a seção de anexo é ocultada na criação da série — não há um lançamento único ao qual associar o documento. Uma nota explicativa orienta a anexar individualmente em cada lançamento depois que a série for criada. Em **Editar Lançamento**, a seção funciona normalmente, pois você sempre edita um movimento individual.

> ✓ **Dica · Anexe sempre, anexe na hora**
>
> Comprovante anexado na criação do lançamento custa 10 segundos. Procurar um comprovante de 8 meses atrás na pasta de e-mails do diretor anterior custa horas e às vezes não dá certo. **Adote como regra: nenhum lançamento sem comprovante.** Sua diretoria, sua auditoria contábil e seu eu do futuro vão agradecer.

> ✓ **Dica · Tesoureiro em campo, câmera direto no app**
>
> Tesoureiro voluntário em viagem com o grupo, pagou combustível no posto: abre o RIT360 Financeiro instalado no celular, **Novo Lançamento → Tirar foto**, fotografa o cupom fiscal, confirma. Quatro toques contra os oito tradicionais de tirar foto pelo app de câmera, salvar na galeria, abrir o RIT360 Financeiro, navegar, selecionar.

## Estornar um lançamento

[![Dialog de estorno](/assets/screenshots/manual-04c-estornar-dialog.png)](/assets/screenshots/manual-04c-estornar-dialog.png)
*Dialog de estorno — informe a razão antes de confirmar*

Estornar é diferente de cancelar. Estorno é a forma contábil correta de reverter um lançamento **que já foi pago**.

> 📖 **Conceito · O que acontece quando você estorna**
>
> O RIT360 Financeiro não apaga o lançamento original. Em vez disso, cria automaticamente um **lançamento contrário** com a mesma data, o mesmo valor e a categoria/conta espelhadas — uma receita estornada vira uma despesa de igual valor, e vice-versa. Os dois ficam vinculados na timeline e ambos exibem o badge "Estornado". O resultado no saldo é o mesmo que se nada tivesse acontecido, mas **a história fica preservada**: você consegue mostrar, anos depois, que aquele depósito chegou, foi estornado, e por quê.

Para estornar: vá no detalhe do lançamento → botão **Estornar** → informe a razão. O lançamento contrário é criado e ambos ficam marcados na lista.

> ⚠️ **Atenção · Estorno preserva, exclusão apaga**
>
> Estornos podem ser feitos por motivos legítimos — devolução bancária, depósito duplicado, doação devolvida. Em todos esses casos, **estornar é o caminho correto, não excluir**. Excluir um lançamento pago não é nem permitido pelo RIT360 Financeiro justamente para preservar a integridade da prestação de contas.

## Corrigir os dados de pagamento de um lançamento pago

Às vezes a data ou a conta registradas no pagamento saem diferentes do que aconteceu no banco — você pagou num dia e lançou no outro, ou marcou a conta errada. Antes era preciso estornar e refazer; agora dá para **corrigir direto**, sem desfazer o lançamento.

[![Diálogo de edição dos dados de pagamento](/assets/screenshots/mov-editar-pagamento-01.png)](/assets/screenshots/mov-editar-pagamento-01.png)
*Editar dados de pagamento — ajuste data e/ou conta e informe o motivo*

**Quem pode:** os responsáveis financeiros — o mesmo perfil que marca lançamentos como pagos e faz estornos.

Para corrigir:

1. Abra o **detalhe** do lançamento (ele precisa estar com status **Pago**).
2. Clique em **Editar dados de pagamento**.
3. Ajuste a **data de pagamento** e/ou a **conta financeira** e escreva um **motivo** — o motivo é obrigatório e fica guardado no histórico da movimentação.
4. Salve. Se você trocou a conta, os **saldos das contas envolvidas são recalculados** automaticamente.

> ⚠️ **Atenção · Só data e conta**
>
> Por aqui você corrige apenas a **data de pagamento** e a **conta**. Valor, categoria e status permanecem intactos. Para corrigir o **valor** de um lançamento pago, o caminho continua sendo o **Estorno**. Transferências não usam essa correção.

## Importar lançamentos

[![Importar Lançamentos com 2 fontes](/assets/screenshots/manual-04b-importar-lancamentos.png)](/assets/screenshots/manual-04b-importar-lancamentos.png)
*Importar Lançamentos — duas fontes disponíveis: CSV e WooCommerce*

Em vez de digitar lançamento por lançamento, você pode importar de duas fontes:

**Acesso:** botão **Importar Lançamentos** no topo da lista de movimentações.

### Importação por CSV

Útil para migrar histórico de planilhas (a base mais comum quando uma OSC começa a usar o RIT360 Financeiro). Faça download do template, preencha as linhas com seus lançamentos antigos, faça upload. O RIT360 Financeiro mostra um **preview** com erros por linha antes de criar nada; você confirma e os lançamentos são criados em lote.

**Formato:** separador ponto-e-vírgula (`;`); valor em reais com vírgula decimal (`1500,00`); data `DD/MM/AAAA`.

**Colunas aceitas:**

| Coluna | Obrigatória? | Conteúdo |
|---|---|---|
| `data` | Sim | Data do lançamento. |
| `valor` | Sim | Valor em reais, vírgula decimal. Sempre positivo; o tipo define entrada/saída. |
| `descricao` | Sim | Descrição curta. |
| `tipo` | Sim | `receita`, `despesa` ou `transferencia`. |
| `conta` | Sim | Conta de origem (deve existir na OSC). |
| `categoria` | Sim (exceto transferência) | Categoria compatível com o tipo. Transferência não tem categoria. |
| `conta_destino` | Só em transferência | Conta que recebe; obrigatória e diferente da origem. |
| `projeto` | Não | Projeto **aberto** para vincular (qualquer tipo). |
| `centro_de_custo` | Não | Centro de custo para vincular (qualquer tipo). |
| `data_pagamento` | Não | Data de efetivação. Em branco = pendente. |
| `beneficiario` | Não | Quem recebeu/pagou. |
| `forma_pagamento` | Não | `pix`, `cartão`, `dinheiro`, etc. |
| `observacoes` | Não | Texto livre. |

- **Transferência** entre contas da OSC é **uma linha** (`tipo=transferencia`, `conta` + `conta_destino`, sem categoria) — preserva o saldo total.
- **Projeto** não encontrado (fechado/inexistente) → o lançamento entra **sem o vínculo**, com aviso; nunca bloqueia.
- **Conta ou categoria que ainda não existe** na OSC vira uma **pendência resolvida na própria tela de resumo**: criar a categoria que falta, mapear para uma existente, ou deixar as linhas daquela conta de fora para reimportar depois. O casamento de nomes ignora acentos, maiúsculas/minúsculas e espaços.
- **Centro de custo que ainda não existe** também vira **pendência na tela de resumo**, com três opções por nome: **criar** o centro de custo, **mapear** para um existente, ou **importar aquelas linhas sem** centro de custo. Centro de custo em branco (ou coluna ausente) → o lançamento entra sem centro de custo, sem aviso.

> 💡 **Migrando de uma planilha ou de outro sistema?**
>
> O **[Guia de Migração](/migracao/)** cobre o caminho completo — ponto de corte, ordem de montar a base, formato da planilha coluna a coluna, reconciliação e como virar a chave com segurança.

O **template baixável** já vem com todas essas colunas e linhas de exemplo — inclusive uma transferência, uma com projeto vinculado e uma com centro de custo. Baixe, apague os exemplos e preencha com os seus lançamentos.

Parcelas e recorrências não entram por CSV — crie pelo formulário. **Comprovantes, sim:** a planilha tem uma coluna `comprovante` onde você informa o **link** do arquivo (vários links na mesma célula, separados por vírgula, barra vertical ou espaço). Ao importar, os lançamentos são criados na hora e os comprovantes são **baixados em segundo plano** e anexados — você recebe um aviso ao concluir, e qualquer link que não baixar fica registrado na **observação** do lançamento. Use o **link direto** do arquivo; links de compartilhamento de nuvem que abrem uma página (em vez de baixar o arquivo) não funcionam.

### Importação do WooCommerce

Se sua OSC tem loja online em WooCommerce (venda de produtos, doações online, ingressos), pode conectar a loja ao RIT360 Financeiro em **Configurações → Organização → WooCommerce**. Uma vez configurada, pedidos pagos viram receitas automaticamente — diariamente via sincronização programada ou sob demanda pelo botão **Importar agora** desta tela. A sincronização roda **em segundo plano**: a tela responde na hora, você acompanha o andamento pelo histórico e recebe um aviso ao concluir; importações grandes se completam sozinhas, em um único disparo.

Mais detalhes na seção de configurações.

## Conciliação bancária (extrato OFX)

Se você baixa o **extrato do banco em formato OFX** (a maioria dos bancos oferece), pode conciliá-lo com seus lançamentos no RIT360 Financeiro — em vez de marcar conta por conta como paga.

**Acesso:** tela de **Conciliação**, a partir das movimentações.

**Como funciona:**

1. Escolha a **conta** e suba o arquivo `.ofx`.
2. O RIT360 Financeiro lê cada transação do extrato e **procura o lançamento correspondente** (por valor e proximidade de data), organizando tudo em quatro grupos:
   - **Conciliados** — alta confiança no casamento; já vêm pré-marcados.
   - **Em revisão** — casamento provável, mas com alguns dias de diferença; você confirma ou recusa.
   - **Novos** — transações sem lançamento correspondente; você pode **criar** o lançamento (escolhendo a categoria) ou ignorar.
   - **Já conciliados** — transações que você já processou antes (apenas informativo).
3. Ao **confirmar**, os lançamentos conciliados/aceitos são marcados como **pagos** com a data do extrato e ficam vinculados à conciliação; os "novos" que você escolher viram lançamentos.

**Reimportar o mesmo extrato não duplica nada** — cada transação é reconhecida pelo identificador único do banco.

> 💡 **Por que isso importa**
> Conciliar pelo extrato substitui a conferência manual lançamento a lançamento, reduz erro e dá confiança de que o que está registrado no RIT360 Financeiro bate com o banco.

> 🔎 **Não tem o arquivo OFX?** Se você só tem o **saldo final** que aparece na tela do banco, use o **[Caça-diferenças](/modulos/caca-diferencas/)**: informe o saldo e ele aponta na hora onde está a diferença, com correção em um clique. É a conferência rápida "pelo número", complementar a esta conciliação por extrato.

## Prestação de contas

[![Diálogo de prestação de contas](/assets/screenshots/manual-mov-prestacao-contas.png)](/assets/screenshots/manual-mov-prestacao-contas.png)
*Em Exportar → Prestação de contas: escolha o período e, opcionalmente, anexe documentos complementares*

A **prestação de contas** é um documento em PDF, no padrão visual do RIT360 Financeiro, que reúne **tudo o que a organização precisa apresentar de um período** — para a diretoria, o conselho fiscal, a assembleia de associados, um financiador ou um órgão público. Diferente do *Exportar PDF* (que é a lista de lançamentos), a prestação de contas é um **relatório contábil completo, em regime de caixa**, pronto para entregar. Está disponível para a **diretoria/tesouraria** e a **comissão fiscal** da organização.

### O que o documento traz

- **Capa e termo de abertura** — identidade da OSC (razão social, CNPJ), período e regime.
- **Demonstração de receitas e despesas** — totais por categoria, com **gráficos** por grupo e o resultado do período (superávit ou déficit).
- **Posição de caixa por conta** — saldo inicial, créditos, débitos e saldo final de cada conta, com o total geral que reconcilia.
- **Demonstrativo analítico** — lançamento a lançamento, **separado em Receitas, Despesas e Transferências** e agrupado por categoria, com os valores sinalizados e coloridos (entradas em verde com `+`, saídas em vermelho com `−`), no mesmo padrão do extrato. As transferências aparecem com a conta de origem e a de destino.
- **Extrato por conta** — a movimentação cronológica de cada conta, com saldo corrente.
- **Comprovantes** — as imagens e PDFs anexados aos lançamentos, **mesclados ao final** do documento e organizados em três grupos (**Despesas, Receitas e Transferências**), na ordem dos lançamentos; os lançamentos sem comprovante ficam listados à parte.
- **Documentos complementares** (opcional) — outros documentos que você anexar na hora de gerar (extrato bancário, parecer da comissão fiscal, notas explicativas), incluídos **no fim do PDF**, cada um precedido de uma folha com título e descrição.
- **Termo de encerramento** — com os nomes do **Presidente** e do **Tesoureiro** e um bloco de **autenticação eletrônica** (data/hora de geração e um código de verificação único do documento).

### Documentos complementares (opcional)

Além dos comprovantes dos lançamentos, você pode **anexar outros documentos** ao relatório no momento de gerar — por exemplo, o **extrato bancário** do período, o **parecer da comissão fiscal** ou **notas explicativas**. O objetivo é entregar a prestação de contas **completa em um único PDF**, sem precisar mandar anexos soltos por e-mail depois.

Os documentos ficam **vinculados àquele período**: se você gerar o mesmo período de novo, eles **reaparecem já anexados**, prontos para complementar ou remover. No PDF, entram **no fim, depois dos comprovantes**, cada um precedido de uma folha com o título e a descrição que você informou.

Para anexar, na seção **Documentos complementares** do diálogo: escolha o arquivo (PDF ou imagem), preencha o **título** (obrigatório) e uma **descrição** opcional, e clique em **Anexar este documento**. Repita para quantos documentos quiser.

> ⚠️ Escolher o arquivo **não basta** — é o botão **Anexar este documento** que efetiva o anexo. Se você clicar em *Gerar PDF* com um arquivo escolhido mas ainda não anexado, o RIT360 Financeiro anexa automaticamente (quando há título) ou avisa para você concluir antes.

### Como gerar

1. Em **Movimentações**, clique em **Exportar → Prestação de contas**.
2. Escolha o período:
   - **Mês** — um mês específico já **fechado** (o mês corrente, ainda em andamento, não fica disponível);
   - **Ano (acumulado)** — de janeiro até o último mês fechado daquele ano (ou o ano inteiro, se for um ano anterior).
3. Clique em **Gerar PDF**. A geração roda **em segundo plano**: você pode continuar trabalhando, e **o link do PDF chega no seu e-mail** assim que ficar pronto (a montagem com gráficos e comprovantes pode levar de alguns segundos a poucos minutos). Se algo falhar, você é avisado por e-mail e por notificação no app.

> 💡 **Por que isso importa · Transparência e governança não são burocracia**
>
> Em uma OSC, **prestar contas é o que sustenta a confiança** — de quem doa, de quem fiscaliza, de quem assina junto. Um relatório completo, com os comprovantes anexados e a posição de caixa que reconcilia, responde de uma vez às perguntas que sempre voltam: *"para onde foi o dinheiro?", "esse gasto tem nota?", "o saldo bate?"*. Gerar a prestação de contas a cada mês fechado — e o acumulado para a assembleia anual — cria um **histórico íntegro e fácil de auditar**, protege a diretoria atual e a futura, e transforma a prestação de contas de uma correria de fim de ano em um clique.

> ⚠️ **Atenção · O PDF reflete o que está registrado**
>
> A prestação de contas só é tão boa quanto os dados que a alimentam. Lançamentos sem categoria, despesas sem comprovante anexado ou contas desatualizadas aparecem assim no relatório. Use a rotina semanal e a conferência mensal contra o extrato para chegar ao fim do período com a prestação pronta — e **anexe os comprovantes na hora de lançar**.

## Boas práticas

> ✓ **Dica · Adote uma rotina semanal de 15 minutos**
>
> A maior dor de OSCs amadoras na função financeira é deixar tudo acumular para o fim do mês. Aí cada lançamento exige resgatar comprovante, lembrar contexto, perguntar para gente que já esqueceu. **Reserve 15 minutos uma vez por semana** (toda terça de manhã, por exemplo) para registrar a movimentação da semana. É a diferença entre ter a contabilidade da OSC sempre pronta e viver apagando incêndio no dia 25.

> ✓ **Dica · Confira a lista contra o extrato bancário todo mês**
>
> No final do mês, abra o extrato do banco e a lista de movimentações do RIT360 Financeiro filtrada pelo mês. Cada linha do extrato deve ter um lançamento correspondente. Diferenças vão aparecer (taxa que você esqueceu, transferência que veio sem aviso) — corrigir essas diferenças mensalmente é mil vezes mais fácil do que descobrir 6 meses depois.

> ⚠️ **Atenção · Cuidado com transferências entre contas**
>
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
