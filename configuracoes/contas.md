---
title: "Contas Bancárias"
nav_order: 4
parent: "Configurações da Organização"
permalink: /configuracoes/contas/
---

> Disponível para **Presidente (admin)** e **Tesoureiro**.

A página **Contas Bancárias** lista as contas financeiras da sua OSC e permite cadastrar novas, editar dados existentes e desativar contas que saíram de uso.

[![Configurações — Contas](/assets/screenshots/config-contas.png)](/assets/screenshots/config-contas.png)
*Configurações — Contas financeiras*

> 💡 **Por que isso importa**
>
> "Conta financeira" no Bússola não é só **conta bancária**. É qualquer lugar onde a OSC guarda dinheiro: a conta corrente do banco, a poupança, o caixa interno em dinheiro vivo, o cartão de crédito da OSC, a conta no Mercado Pago para recebimentos online, o saldo no PayPal. Cada um desses é uma "conta" diferente, e mantê-los separados no Bússola **faz a contabilidade bater com a realidade** — você sabe quanto tem em cada lugar, e o saldo total consolidado reflete a posição real da OSC.

## Tipos de conta suportados

- **Corrente** — conta bancária de uso geral
- **Poupança** — conta poupança vinculada
- **Caixa** — caixa interno físico (notas e moedas guardadas na sede)
- **Cartão Pré-pago** — quando há saldo pré-pago vinculado
- **Investimento** — aplicações, CDB
- **Fundo** — cotas de fundos de investimento
- **Outro** — para casos não cobertos (PayPal, Mercado Pago, gateway de pagamento, etc.)

## Adicionar nova conta

Clique em **+ Nova conta**. Preencha:

- **Nome** — descritivo (ex: "Banco do Brasil — CC", "Mercado Pago — Vendas WC")
- **Tipo** — da lista acima
- **Saldo inicial** — quanto tem na conta no momento do cadastro
- **Data de abertura** — quando a conta começou a ser usada pela OSC (não a data de criação no Bússola)
- **Conta padrão da organização** (opcional) — ver a seção **Conta padrão**, abaixo
- **Dados bancários** (opcional, recolhível) — banco, agência e demais dados, quando aplicável
- **Personalização** (opcional, recolhível) — uma **cor** e um **ícone** para a conta; ver a seção **Personalização**, abaixo

[![Editar conta — conta padrão e personalização](/assets/screenshots/config-contas-editar.png)](/assets/screenshots/config-contas-editar.png)
*Cadastro/edição de conta — alternar conta padrão e definir cor e ícone*

> 📖 **Conceito · Saldo inicial e data de abertura**
>
> Quando você cadastra uma conta nova no Bússola, ela precisa saber qual era o saldo no momento em que sua OSC começou a usá-la no sistema. **Não é o saldo de hoje** — é o saldo na data de abertura. O Bússola usa esse valor como ponto de partida para calcular saldos futuros somando receitas e subtraindo despesas pagas. Se você está migrando de planilha para o Bússola, **a data de abertura é o dia que você começa a registrar no Bússola**, e o saldo inicial é o que estava na conta naquele dia.

## Ações por conta

- **Definir padrão / Remover padrão** — marca (ou desmarca) a conta como **padrão da organização**; ver abaixo
- **Editar** — alterar nome, banco, tipo, cor e ícone (não o saldo — saldo só muda via movimentações)
- **Desativar / Reativar** — uma conta desativada não aparece em filtros e formulários, mas seu histórico permanece preservado

> ⚠️ **Atenção · Conta com movimentações não pode ser excluída**
>
> O Bússola **não permite excluir conta que tem movimentações registradas** — só desativar. Motivo: excluir destruiria a história contábil dessas movimentações ("essa receita foi para qual conta?"). Para "encerrar" uma conta na prática, **desative**. As movimentações ficam intactas no histórico, e a conta desativada não aparece nos formulários de novo lançamento.

## Conta padrão

Uma das contas pode ser marcada como **conta padrão da organização**. A conta padrão é **pré-selecionada automaticamente ao criar um novo lançamento** — assim, quem registra movimentações não precisa escolher a conta toda vez (é só mudar quando for outra).

- **Apenas uma** conta pode ser a padrão por vez. Ao definir uma nova padrão, a anterior deixa de ser.
- Marque pela ação **Definir padrão** na lista, ou pelo interruptor **Conta padrão da organização** ao criar/editar a conta.
- A conta padrão exibe o selo **Padrão** na lista de contas.
- Se você **desativar** a conta que era a padrão, ela deixa de ser padrão automaticamente — defina outra.

> ✓ **Dica · Aponte para a conta que mais movimenta**
>
> Defina como padrão a conta por onde passa o grosso do dia a dia (geralmente a conta corrente principal). Como ela já vem selecionada no novo lançamento, você economiza um passo na maioria dos registros e reduz o risco de lançar na conta errada por desatenção.

## Personalização (cor e ícone)

Na seção **Personalização** do cadastro da conta, você pode definir uma **cor** (em hexadecimal) e um **ícone** para a conta. A cor vira um **acento visual** nos cartões de saldo — no **Painel**, na lista de movimentações e nos relatórios —, ajudando a distinguir as contas de relance.

> ✓ **Dica · Cores ajudam a bater o olho**
>
> Dar a cada conta uma cor própria (azul para o banco, verde para o caixa, roxo para a poupança) faz o Painel ficar legível num instante — você identifica de qual conta é cada saldo sem precisar ler o nome. É opcional, mas vale o minuto de configuração.

## Saldo em tempo real

Cada conta na lista mostra o **saldo atual**, calculado em tempo real a partir das movimentações pagas. Quando você marca uma receita ou despesa como paga em Movimentações, o saldo aqui atualiza imediatamente.

> ✓ **Dica · Concilie mensalmente contra o extrato bancário**
>
> No final de cada mês, abra o extrato do banco e o saldo da conta correspondente aqui no Bússola. Eles devem bater **centavos por centavos**. Diferenças apontam para lançamento esquecido, valor digitado errado, ou taxa que não foi registrada. Corrigir mensalmente é fácil; descobrir 6 meses depois é pesadelo.

## Por onde seguir

- **Movimentações** — onde as contas aparecem como destino/origem dos lançamentos.
- **Painel** — onde os saldos consolidados das contas ativas aparecem.
- **Configurações → Organização → Integrações → WooCommerce** — onde você define qual conta recebe receitas da loja online.
