---
title: "Guia de Migração"
nav_order: 3
permalink: /migracao/
---

Trazer a vida financeira da sua OSC de outro lugar — uma planilha, um sistema antigo, ou o caderno — para a Bússola não precisa ser um salto no escuro. Esta página é o **roteiro de migração**: o que decidir antes, em que ordem montar a base, como importar o histórico e como virar a chave com segurança, sem perder nada no caminho.

> 💡 **Para quem é este guia**
>
> Para quem vai colocar a OSC na Bússola pela primeira vez e quer trazer o histórico financeiro. Se você está só conhecendo a ferramenta, comece pelos **[Primeiros Passos](/primeiros-passos/)**. Se já montou a organização e só quer entender a tela de importação, pule para **[Importar lançamentos](/modulos/movimentacoes/#importar-lançamentos)**.

## De onde você está vindo?

A migração tem um caminho comum (a **espinha**, mais abaixo), mas o ponto de partida muda o tamanho do trabalho. Encontre o seu cenário:

### Vindo do zero (caderno, cabeça, nada digital)

Você não tem histórico para importar — tem um **saldo atual** e daqui pra frente lança na Bússola. É o cenário mais simples: pule a parte de importação e vá direto montar a base.

→ Siga **[Primeiros Passos da Organização](/primeiros-passos/organizacao/)**: cadastre a OSC, as contas (com o **saldo de abertura** na data em que você começa), as categorias e os usuários. Pronto — a partir daí é só operar.

### Vindo de uma planilha (o caso mais comum)

Você tem um Excel ou Google Sheets com o histórico de entradas e saídas. Esse é o **núcleo deste guia**: a Bússola importa planilha via CSV, validando linha a linha antes de criar qualquer coisa. Siga a espinha inteira abaixo.

### Vindo de outro sistema (ERP, app financeiro, contabilidade)

Quase todo sistema exporta os lançamentos para **CSV ou Excel**. Exporte de lá, ajuste as colunas para o formato da Bússola (a tabela está em [Importar o histórico](#4-importe-o-historico-csv)) e siga a espinha como quem vem de planilha.

> ⚠️ **Atenção · Não cancele o sistema antigo cedo demais**
>
> Mantenha o acesso ao sistema anterior até ter **conferido** que tudo entrou certo na Bússola (etapa de reconciliação, mais abaixo). Contrato cancelado às pressas costuma levar junto o acesso ao histórico que você ainda vai precisar conferir. Vire a chave só depois de bater os saldos.

## A espinha da migração

Independentemente de onde você vem, o caminho é este — e a **ordem importa**:

1. **Defina o ponto de corte** — até onde trazer histórico.
2. **Monte a base, na ordem certa** — organização → contas → categorias → usuários.
3. **Prepare a planilha** — no formato que a Bússola entende.
4. **Importe o histórico** — CSV com validação linha a linha.
5. **Anexe comprovantes** (o que precisar) — manualmente, depois.
6. **Confira e reconcilie** — bata os saldos contra o banco.
7. **Rode em paralelo e vire a chave** — sem susto.

### 1. Defina o ponto de corte

Você raramente precisa trazer **toda** a história da OSC. Decida um corte sensato:

- **Padrão recomendado:** cadastre o **saldo inicial de cada conta** numa data de corte (ex.: 1º de janeiro do ano corrente) e importe só os lançamentos **a partir dessa data**. Você fica com o ano corrente detalhado e os saldos corretos, sem carregar anos de histórico.
- **Quer mais histórico?** Nada impede importar anos anteriores — só lembre que cada lançamento antigo é uma linha a mais para preparar e conferir.

> 💡 **Por que o saldo inicial é a peça-chave**
>
> A Bússola calcula o saldo de cada conta a partir do **saldo de abertura** mais os lançamentos. Se você acerta o saldo de abertura na data de corte e importa os lançamentos seguintes, o saldo atual bate sozinho. Errar o saldo de abertura é a causa nº 1 de "os números não fecham" depois da migração.

### 2. Monte a base, na ordem certa

Um lançamento só faz sentido com uma **conta** e uma **categoria** por trás; uma transferência precisa de **duas contas**; um vínculo de projeto precisa do **projeto** já criado. Por isso a base vem **antes** da importação:

1. **Organização** — dados da OSC. → **Configurações → Organização**.
2. **Contas bancárias** — cada conta (corrente, poupança, caixa, cartão) com o **saldo de abertura** na data de corte. → **Configurações → Contas Bancárias**.
3. **Categorias** — aplique um template próximo ao perfil da OSC e ajuste. → **Configurações → Categorias**.
4. **Projetos** (se for vincular lançamentos a projetos) — crie os projetos antes de importar. → **Projetos**.
5. **Usuários e papéis** — convide a equipe (ou importe em lote por CSV). → **Configurações → Usuários**.

> ⚠️ **Atenção · Saldo de abertura antes de qualquer lançamento**
>
> Acerte o saldo de abertura de cada conta **antes** de importar. Depois que a conta tem lançamentos, o saldo de abertura fica **protegido** contra alteração acidental (só a Presidência destrava) — exatamente para não distorcer o saldo atual. Acertar antes evita esse retrabalho.

O roteiro detalhado dessa preparação está em **[Primeiros Passos da Organização](/primeiros-passos/organizacao/)**.

### 3. Prepare a planilha

Em **Movimentações → Importar Lançamentos**, baixe o **template CSV** e use-o como molde. Cada linha é um lançamento. As regras de formato:

- **Separador:** ponto-e-vírgula (`;`).
- **Valor:** em reais com **vírgula decimal** — `1500,00`. O ponto pode separar milhar (`1.500,00`). *Não* use ponto como decimal (`1500.00`) — veja o alerta abaixo.
- **Data:** `DD/MM/AAAA` (ex.: `20/05/2026`). O formato `AAAA-MM-DD` (`2026-05-20`), usado nos exemplos do template, também é aceito.
- **Codificação:** UTF-8 (o template já vem assim; acentos funcionam).

> ⚠️ **Atenção · Vírgula é o separador decimal**
>
> No Brasil, `1.500,00` é mil e quinhentos. Escreva os valores assim. Evite o formato com ponto decimal (`1500.00`), comum em exportações de sistemas em inglês — converta para vírgula antes de importar. A Bússola avisa quando o valor é ambíguo, mas o certo é já mandar no formato brasileiro.

#### As colunas, uma a uma

| Coluna | Obrigatória? | O que vai aqui |
|---|---|---|
| `data` | Sim | Data do lançamento — `DD/MM/AAAA`. |
| `valor` | Sim | Valor em reais, vírgula decimal — `1500,00`. Sempre positivo; o **tipo** define entrada ou saída. |
| `descricao` | Sim | Descrição curta do lançamento. |
| `tipo` | Sim | `receita`, `despesa` ou `transferencia`. |
| `conta` | Sim | Nome da conta (de origem). Deve existir na OSC. |
| `categoria` | Sim (exceto transferência) | Nome da categoria, compatível com o tipo. **Transferência não tem categoria** — deixe em branco. |
| `conta_destino` | Só em transferência | Conta que **recebe** a transferência. Obrigatória quando `tipo=transferencia`; precisa ser **diferente** da conta de origem. Ignorada nos demais tipos. |
| `projeto` | Não | Nome de um **projeto aberto** para vincular o lançamento. Vale para qualquer tipo. |
| `data_pagamento` | Não | Data em que o pagamento foi efetivado (`DD/MM/AAAA`). Em branco = lançamento pendente. |
| `beneficiario` | Não | Quem recebeu / pagou. |
| `forma_pagamento` | Não | `pix`, `cartão`, `dinheiro`, `transferencia`, etc. |
| `observacoes` | Não | Texto livre. |

> 💡 **Conceito · Transferência é uma linha só**
>
> Para mover dinheiro entre duas contas da própria OSC, use **uma única linha** com `tipo=transferencia`, a conta de origem em `conta` e a de destino em `conta_destino`. Não lance como uma despesa numa conta e uma receita na outra — isso infla os relatórios. A transferência preserva o saldo total e mantém os relatórios limpos.

> 💡 **Conceito · Vincular a um projeto**
>
> Preencha `projeto` com o nome de um projeto **aberto** para amarrar o lançamento a ele. Se o nome não bater com nenhum projeto aberto (projeto fechado, cancelado ou inexistente), o lançamento **é importado mesmo assim, sem o vínculo**, com um aviso na linha — o vínculo é opcional e nunca bloqueia a importação. Se o projeto restringe categorias, a categoria da linha precisa ser uma das permitidas.

> 💡 **Dica · O template já traz exemplos prontos**
>
> O template oferecido para download já inclui todas as colunas acima e linhas de exemplo — inclusive uma de **transferência** (com `conta_destino` preenchida e sem categoria) e uma com **`projeto`** vinculado. Use-as como referência: apague os exemplos e preencha com os seus lançamentos.

> 💡 **O que ainda não vai por CSV**
>
> **Parcelas e lançamentos recorrentes** não têm coluna no CSV — crie-os pelo formulário do app, que monta a série automaticamente. **Comprovantes** (anexos) também não entram por CSV; veja a etapa 5.

### 4. Importe o histórico (CSV)

[![Importar Lançamentos](/assets/screenshots/manual-04b-importar-lancamentos.png)](/assets/screenshots/manual-04b-importar-lancamentos.png)

Em **Movimentações → Importar Lançamentos → CSV**, suba o arquivo. A Bússola não cria nada de imediato — primeiro mostra um **preview** validado:

- Cada linha aparece com o **valor interpretado em R$**, a conta, a categoria, o projeto e o status.
- Linhas com **erro** (ex.: transferência sem destino, destino igual à origem, categoria não permitida no projeto) são marcadas e **ignoradas** na importação — o resto entra normalmente.
- Linhas válidas mostram **OK**; vínculos de projeto que não casaram aparecem como **aviso** (entram sem o vínculo).

#### Quando um nome não existe ainda: resolução na hora

Se a planilha cita uma **conta** ou **categoria** que ainda não existe na OSC, você não precisa cancelar, ir cadastrar e recomeçar. A tela de resumo abre um painel de **Pendências a resolver**:

- **Categoria desconhecida** → você pode **criar a categoria** ali mesmo (a Bússola sugere o tipo) ou **mapear** para uma categoria existente.
- **Conta desconhecida** → **mapear** para uma conta existente, ou **deixar de fora** as linhas daquela conta (você cadastra a conta com o saldo de abertura correto depois e reimporta só essas linhas — sem criar conta meia-boca no meio da importação).
- O casamento de nomes ignora **acentos, maiúsculas/minúsculas e espaços extras** — "doações", "Doações" e "DOAÇÕES " são a mesma categoria.

Só depois de resolver as pendências o botão de confirmar libera. Aí sim os lançamentos são criados em lote.

> ✓ **Dica · Comece com um lote pequeno**
>
> Na primeira importação, suba uma planilha com **5 a 10 linhas** representativas (uma receita, uma despesa, uma transferência, uma com projeto). Confira o preview, confirme, veja como ficou na lista. Pegando o jeito, importe o histórico completo com confiança.

### 5. Anexe os comprovantes (o que precisar)

Comprovantes (notas, recibos, prints) **não entram pelo CSV** — são arquivos. Depois da importação, abra os lançamentos que precisam de comprovante e anexe pelo detalhe de cada um. Na prática, você raramente precisa anexar comprovante a **todo** o histórico — foque no que a prestação de contas exige daqui pra frente.

### 6. Confira e reconcilie

Importou? Agora **bata os números** antes de confiar:

- Abra o **Painel** e confira o **saldo de cada conta** contra o saldo real (extrato do banco, saldo do caixa) na data de hoje.
- Se bater, a migração foi fiel. Se não bater, a diferença quase sempre é **saldo de abertura errado** ou **uma linha que ficou de fora** (erro no preview que você não notou).
- Filtre a lista de **Movimentações** pelo período importado e confira por amostragem contra a planilha de origem.

> ✓ **Dica · Reconciliar é a etapa que dá segurança**
>
> A reconciliação não é burocracia — é o momento em que você prova para si mesmo (e para a diretoria) que os números da Bússola são confiáveis. Cinco minutos conferindo o saldo de cada conta valem mais do que qualquer relatório bonito sobre dados que ninguém checou.

### 7. Rode em paralelo e vire a chave

Por **um ciclo** (uma a quatro semanas, ou um mês de fechamento), mantenha o registro antigo **e** a Bússola lado a lado:

- Lance as novas movimentações nos dois.
- No fim do ciclo, **reconcilie** os dois: se os saldos batem, a Bússola está fiel e você pode parar de manter o antigo.
- A partir daí, a Bússola é a **fonte da verdade**. Só então cancele assinaturas ou arquive a planilha antiga (mantendo uma cópia de segurança do histórico).

## Checklist de migração

Copie e marque conforme avança:

```
[ ] Ponto de corte definido (data + saldo de abertura por conta)
[ ] Organização cadastrada
[ ] Contas bancárias com saldo de abertura correto
[ ] Categorias revisadas (template aplicado e ajustado)
[ ] Projetos criados (se for vincular lançamentos)
[ ] Usuários convidados com os papéis certos
[ ] Planilha preparada no formato da Bússola (separador ;, valor com vírgula, data DD/MM/AAAA)
[ ] Lote pequeno importado e conferido no preview
[ ] Histórico completo importado (pendências resolvidas)
[ ] Comprovantes essenciais anexados
[ ] Saldos reconciliados contra banco/caixa
[ ] Ciclo em paralelo concluído e batido
[ ] Chave virada: Bússola é a fonte da verdade
```

## Perguntas frequentes da migração

**Preciso trazer todo o histórico da OSC?**
Não. O recomendado é cadastrar o saldo de abertura numa data de corte e importar a partir dali. Mais histórico é opcional.

**Errei o saldo de abertura e já importei. E agora?**
Se a conta já tem lançamentos, o saldo de abertura fica protegido — a Presidência consegue destravar para corrigir. Corrija o saldo de abertura (não saia criando lançamentos de "ajuste") e reconcilie de novo.

**Importei uma linha errada. Como desfaço?**
Cada lançamento pode ser editado, cancelado ou estornado individualmente pela lista de Movimentações. Não há "desfazer a importação inteira" — por isso o preview e o lote pequeno existem: para errar antes de criar.

**Minha planilha tem conta/categoria que não cadastrei. Trava a importação?**
Não. A tela de resumo resolve na hora: criar a categoria que falta, mapear para uma existente, ou deixar as linhas daquela conta de fora para reimportar depois. Veja [Quando um nome não existe ainda](#4-importe-o-histórico-csv).

**Transferências entre contas, como importo?**
Uma linha por transferência, `tipo=transferencia`, com `conta` (origem) e `conta_destino` (destino) — sem categoria. Veja a tabela de colunas.

**E parcelamentos e recorrências?**
Não entram por CSV. Crie pelo formulário do app, que gera a série de parcelas/repetições automaticamente.

## Por onde seguir

- **[Primeiros Passos da Organização](/primeiros-passos/organizacao/)** — o roteiro de montar a base, passo a passo.
- **[Movimentações](/modulos/movimentacoes/)** — a tela de importação e o dia a dia dos lançamentos.
- **[Configurações → Contas Bancárias](/configuracoes/contas/)** — onde acertar o saldo de abertura.
- **[FAQ](/faq/)** — dúvidas gerais sobre a Bússola.
