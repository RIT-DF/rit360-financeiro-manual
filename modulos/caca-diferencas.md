---
title: "Caça-diferenças"
nav_order: 3
parent: "Módulos"
permalink: /modulos/caca-diferencas/
task: conciliar-pelo-saldo-caca-diferencas
role: tesoureiro
routes: [/movimentacoes]
screenshots: [caca-diferencas-01-lupa, caca-diferencas-02-painel, caca-diferencas-03-hipoteses, caca-diferencas-04-conciliado]
source_docs: [BK-430]
last_verified: 2026-07-15
status: publicado
---

# Caça-diferenças

Toda OSC, uma hora ou outra, se depara com aquela pergunta incômoda: **"por que o saldo que o sistema mostra não é igual ao que está no meu banco?"**. O **Caça-diferenças** existe para responder isso em segundos. Você informa o saldo final que vê no extrato do banco, e o RIT360 Financeiro calcula a diferença para o saldo registrado e **aponta as causas mais prováveis** — com sugestões de correção em um clique.

> 💡 **Por que isso importa**
>
> Uma diferença de saldo raramente é "erro do sistema" — quase sempre é um lançamento **duplicado**, um pagamento que **ainda não foi registrado**, ou algo lançado na **conta errada**. Descobrir qual é, no meio de dezenas de movimentações, costuma tomar uma tarde inteira de conferência linha a linha. O Caça-diferenças faz esse trabalho de detetive por você: em vez de procurar no escuro, você recebe uma lista curta e ordenada de hipóteses, da mais provável para a menos provável. Conta conferida é prestação de contas tranquila e fechamento contábil sem sustos.

> 📖 **Conceito · Conciliação pelo saldo vs. pelo extrato**
>
> O RIT360 Financeiro oferece **dois jeitos** de conferir uma conta contra o banco. O **[Conciliar extrato](/modulos/movimentacoes/)** parte de um **arquivo OFX** (baixado do internet banking) e casa cada linha do extrato com os lançamentos do sistema — é o mais completo. O **Caça-diferenças** parte só do **saldo final** que você lê na tela do banco, **sem precisar de arquivo nenhum** — é a conferência rápida "pelo número". Use um ou outro conforme o que você tem em mãos; os dois levam ao mesmo lugar: sua conta batendo com o banco.

## Como abrir

Na tela de **Movimentações**, os cards de **Saldos por conta** ficam no topo. Cada card de conta tem um ícone de **lupa** 🔎 no canto superior direito. Clique na lupa da conta que você quer conferir.

[![Ícone de lupa no card de saldo de cada conta](/assets/screenshots/caca-diferencas-01-lupa.png)](/assets/screenshots/caca-diferencas-01-lupa.png)

> 📝 **Nota**
>
> A lupa aparece em **cada conta** (contas correntes, poupança, caixa e também **cartões de crédito** — útil para conferir a fatura, especialmente com compras internacionais, onde a cotação da moeda gera pequenas diferenças). Só o card **Líquido** (o consolidado de todas as contas) não tem lupa, porque o Caça-diferenças trabalha **uma conta por vez**.

## Passo a passo

1. Clique na **lupa** 🔎 do card da conta.
2. No painel que abre, informe o **Saldo do banco** — o valor final que aparece no extrato ou no app do seu banco — e a **Data de referência** (por padrão, hoje).

   [![Painel do Caça-diferenças com o saldo do app e a data de referência](/assets/screenshots/caca-diferencas-02-painel.png)](/assets/screenshots/caca-diferencas-02-painel.png)

3. O RIT360 Financeiro mostra na hora o **saldo do app naquela data** e a **diferença** (saldo do banco menos saldo do app). Abaixo, aparece a lista de **hipóteses**.

> 💡 **Dica · saldo negativo (cheque especial ou fatura de cartão)**
>
> Se a conta está no vermelho (cheque especial) ou você está conferindo a fatura de um cartão, informe o saldo **negativo** usando o sinal de **"−"** antes do valor (ex.: `−1.500,00`). O cálculo considera o sinal corretamente.

## Entendendo as hipóteses

O Caça-diferenças lista as causas prováveis **ordenadas** — as que fecham exatamente a diferença vêm primeiro; "faltante" vem por último. Cada hipótese traz um nível de confiança e, quando é seguro, um botão de ação.

[![Lista de hipóteses ranqueadas com ações de um clique](/assets/screenshots/caca-diferencas-03-hipoteses.png)](/assets/screenshots/caca-diferencas-03-hipoteses.png)

| Hipótese | O que significa | Ação sugerida |
|---|---|---|
| **Explica a diferença** | Existe um lançamento cujo valor bate exatamente com a diferença. | **Excluir lançamento** (se ele não deveria existir). |
| **Duplicata** | Dois lançamentos iguais (mesmo valor, datas próximas, descrição parecida) — provável lançamento em dobro. | **Excluir duplicata** (remove a segunda cópia). |
| **Pode estar na conta errada** | Um lançamento de **outra** conta que, se movido para esta, fecharia a diferença. | **Mover para esta conta**. |
| **Dois lançamentos combinados** | A soma de dois lançamentos explica a diferença. | Destaca os dois para você conferir. |
| **Valor quase igual** | Um lançamento com valor próximo — pode ter sido digitado errado. | **Abrir lançamento** para revisar. |
| **Provável lançamento faltando** | Nada no sistema explica a diferença — provavelmente há algo no extrato que ainda não foi registrado. | **Criar lançamento** (já pré-preenchido com o valor e a data). |

## Aplicando uma correção

As ações acontecem **em um clique** e, logo depois, a diferença é **recalculada automaticamente** para você ver o efeito.

- **Mover para esta conta** — troca a conta do lançamento. É reversível (você pode movê-lo de volta a qualquer momento pela edição do lançamento).
- **Excluir lançamento / Excluir duplicata** — remove o lançamento **de forma permanente**. Por isso, essa ação:
  - só aparece para quem tem **permissão de excluir movimentações** (tesoureiro, presidente ou papel equivalente);
  - sempre pede uma **confirmação** deixando claro que é definitiva.
- **Abrir lançamento** / **Criar lançamento** — atalhos que levam você à tela de edição ou de criação (já pré-preenchida), sem alterar nada sozinhos.

> ⚠️ **Atenção**
>
> A exclusão é definitiva e não tem "desfazer". Se você não tem certeza de que o lançamento é mesmo indevido, prefira **Abrir lançamento** e conferir antes. Uma duplicata real (o mesmo pagamento lançado duas vezes) é segura de excluir; um lançamento legítimo que só "por acaso" tem o valor da diferença, não.

## Quando está tudo certo

Se o saldo do banco que você informou **bate** com o do sistema, o Caça-diferenças mostra a diferença **R$ 0,00** e a mensagem **"Tudo certo — o saldo do app bate com o do banco nessa data"**. Conta conferida. ✅

[![Mensagem de conta conferida, com diferença zero](/assets/screenshots/caca-diferencas-04-conciliado.png)](/assets/screenshots/caca-diferencas-04-conciliado.png)

## Dicas

- **Confira uma conta por vez, na data do extrato.** Se o seu extrato é do fim do mês, use essa data de referência — assim o saldo do app considera só o que já tinha acontecido até lá.
- **Comece pela hipótese do topo.** A lista já vem ordenada pela probabilidade de fechar a diferença.
- **Diferença pequena e "redonda"?** Costuma ser digitação (um valor trocado) — a hipótese "valor quase igual" ajuda a achar.
- **Diferença que não fecha com nada?** Provavelmente falta registrar um lançamento que está no extrato (tarifa bancária, rendimento, uma doação que caiu direto na conta). Use **Criar lançamento**.
