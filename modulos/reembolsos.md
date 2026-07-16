---
title: "Reembolsos"
nav_order: 4
parent: "Módulos"
permalink: /modulos/reembolsos/
---

O módulo de **Reembolsos** é onde voluntários, dirigentes e colaboradores **pedem de volta o dinheiro que tiraram do próprio bolso** para comprar alguma coisa em nome da OSC — combustível do voluntário que levou o material para o evento, lanche da reunião pago pela secretária, papelaria comprada pela coordenadora porque acabou no dia.

> Acesse pelo menu **Pagamentos e Reembolsos → aba Reembolsos**.

> 💡 **Por que isso importa**
>
> Reembolso parece uma operação simples — "fulano gastou, OSC paga de volta" — mas é o ponto onde **mais coisas dão errado em OSC sem controle**: gente que reembolsou e ninguém anotou, comprovante que sumiu, valor que ficou maior do que combinado, dirigente que aprovou para si mesmo sem registro. O módulo de Reembolsos resolve isso com um fluxo simples: **quem pediu, quem aprovou, quanto, com qual comprovante, e quando foi pago — tudo registrado, com auditoria**. Resultado: voluntário recebe rápido, a OSC tem transparência, a diretoria dorme em paz.

## Conceitos essenciais

> 📖 **Conceito · Reembolso ≠ Pedido de Pagamento**
>
> **Reembolso** é para despesa que **já aconteceu**: alguém gastou do bolso e quer receber de volta. **Pedido de Pagamento** é para despesa que **vai acontecer**: a OSC vai pagar uma conta de luz, um fornecedor, um boleto. Os dois fluxos têm aprovação, mas a lógica é diferente: no reembolso o dinheiro entrou no caixa de quem pagou, ele só quer ser ressarcido; no pedido o dinheiro ainda está na OSC, e a aprovação autoriza a saída. Use **Reembolso** quando a nota fiscal está em nome de uma pessoa física e o pagamento já aconteceu. Use **Pedido de Pagamento** quando o pagamento ainda vai ser feito (geralmente em nome da OSC).

> 📖 **Conceito · Quórum e papéis aprovadores**
>
> A OSC configura em **Configurações → Fluxo de Aprovações** quantos votos são necessários para aprovar um reembolso (1 ou 2) e quais papéis podem votar (Presidente, Diretor de Finanças, etc.) — opcionalmente também pessoas específicas além do papel. Com quórum **1**, o primeiro aprovador elegível que vota define a decisão. Com quórum **2**, são necessários dois votos positivos; se um aprova e outro rejeita, prevalece a rejeição. Solicitantes não votam nos próprios reembolsos (o RIT360 Financeiro bloqueia automaticamente quando há outros elegíveis).

> 📖 **Conceito · Auto-aprovação**
>
> Em OSCs pequenas, pode acontecer de o único aprovador elegível ser o próprio solicitante (ex: o presidente é também o único diretor financeiro e foi ele quem fez a compra). Nesses casos, o RIT360 Financeiro **permite a auto-aprovação** — caso contrário o fluxo trava — mas **marca explicitamente o evento** no histórico de auditoria como `self_approved`. A diretoria e auditoria conseguem identificar essas situações com filtro e responder se houve abuso. Conforme a OSC cresce, novos papéis aprovadores são cadastrados e auto-aprovações naturalmente diminuem.

> 📖 **Conceito · Status do reembolso**
>
> O ciclo de vida normal é **Rascunho → Aguardando aprovação → Aprovado → Pago**. **Rejeitado** é desvio do caminho aprovado — mas o solicitante pode editar e reenviar quantas vezes precisar.

| Status | Significado |
|---|---|
| ⬜ **Rascunho** | Salvo mas não enviado — só o solicitante vê |
| 🟡 **Aguardando aprovação** | Enviado, esperando voto dos aprovadores elegíveis |
| 🟢 **Aprovado** | Aprovado, aguardando confirmação de pagamento pelo tesoureiro |
| 🔴 **Rejeitado** | Reprovado com motivo registrado — pode ser editado e reenviado |
| 💙 **Pago** | Pagamento confirmado; movimentação financeira correspondente está em Movimentações |

## Lista de reembolsos

[![Lista de reembolsos](/assets/screenshots/manual-05-reembolsos-lista.png)](/assets/screenshots/manual-05-reembolsos-lista.png)
*Lista de reembolsos em desktop*

[![Reembolsos no celular](/assets/screenshots/mobile-reembolsos.png)](/assets/screenshots/mobile-reembolsos.png)
*Reembolsos no celular — cards de resumo em grade 2×2, sub-abas roláveis horizontalmente e lista em cards verticais*

A lista mostra todos os reembolsos da organização. Cada papel vê um recorte diferente:

- **Presidente, Tesoureiro e demais aprovadores** veem **todos** os reembolsos da OSC
- **Voluntários e solicitantes não-aprovadores** veem **apenas os próprios**

Cada aba mostra a contagem entre parênteses (ex: "Aguardando aprovação (3)") — útil para ver rapidamente o que está pendente.

**Colunas (desktop):** Data da despesa, Descrição, Valor, Status, Solicitante, Ações.

No **celular**, a lista vira **cards verticais** otimizados para toque, com toda a informação empilhada — descrição em destaque, valor à direita, data da despesa, solicitante, badge de status e botões de aprovar/reprovar quando aplicável. Sem precisar rolar lateralmente para ver o status ou as ações. Mesmo padrão usado em Movimentações e Pedidos de Pagamento.

### Cards de resumo no topo

Acima das abas de filtro de status, aparecem até quatro cards de resumo, exibidos **conforme o seu papel** (você só vê os que fazem sentido para você). Cada card é um **atalho clicável** para a lista filtrada correspondente. Útil para responder de relance: "o que precisa de atenção agora?".

- **Aguardando aprovação** — aparece para quem é aprovador elegível (Presidente, Tesoureiro e demais papéis configurados); conta os reembolsos da OSC que estão **na fila de aprovação** (não só os que dependem de você — a aprovação é por quórum e papel).
- **Aprovados aguardando pagamento** — aparece para o Tesoureiro e Administrador; conta reembolsos com status Aprovado que ainda não viraram movimentação paga.
- **Solicitado no período** — sempre visível; conta reembolsos submetidos no mês corrente.
- **Pago no período** — sempre visível; conta reembolsos pagos no mês corrente.

> ℹ️ **O card "Aguardando aprovação" mostra o mesmo número da aba de mesmo nome** — os reembolsos da OSC na fila de aprovação. Ele **não** é uma "fatia pessoal": como a aprovação é por **quórum e papel**, qualquer aprovador elegível pode votar. Para saber o que já foi votado e quanto falta, abra o **detalhe** de cada reembolso — lá aparece o progresso ("1 de 2 aprovações · falta 1").

### Ações inline na lista

Nas linhas com status "Aguardando aprovação", aprovadores elegíveis veem os botões ✓ **Aprovar** e ✕ **Rejeitar** diretamente na linha — para resolver pendências rápidas sem entrar no detalhe. O dialog de cada ação pede um campo: opcional para aprovar (comentário), obrigatório para rejeitar (motivo).

> ✓ **Dica · Use a aba "Aguardando aprovação" como caixa de entrada**
>
> Se você é aprovador, faça da aba "Aguardando aprovação" sua rotina diária de 5 minutos. Reembolso aprovado rápido é diferencial de OSC bem gerida — voluntário não fica de pires na mão esperando duas semanas para receber R$ 60 de combustível.

## Detalhe do reembolso

Clique em qualquer linha para abrir o detalhe completo. A página tem todas as informações necessárias para tomar uma decisão de aprovação consciente — sem precisar perguntar nada para ninguém.

### Aguardando aprovação

[![Reembolso aguardando aprovação](/assets/screenshots/manual-06-reembolso-aguardando.png)](/assets/screenshots/manual-06-reembolso-aguardando.png)
*Detalhe de reembolso aguardando aprovação*

- **Valor, Solicitante e Data da despesa** no topo
- **Status** em destaque no canto superior direito
- **Dados da solicitação**: descrição, categoria (sempre tipo despesa), projeto, centro de custo
- **Dados de pagamento**: método (PIX ou TED) e chave/conta — **visíveis apenas para aprovadores e tesoureiro** (voluntário não-aprovador vê só os próprios)
- **Comprovantes**: nota fiscal, recibo ou foto da despesa anexados pelo solicitante, com pré-visualização inline para imagens e PDFs (não precisa baixar)
- **Histórico de aprovações**: timeline de todos os votos com nome, papel e data, além do **progresso do quórum** (ex.: "1 de 2 aprovações · falta 1") enquanto o reembolso aguarda aprovação
- **Ações**: ✓ Aprovar / ✕ Rejeitar (somente para aprovadores; nunca para o próprio solicitante)

> 💡 **Por que isso importa**
>
> A timeline de aprovações é mais que registro contábil. É **proteção institucional**: meses depois, se alguém questionar "quem aprovou esse reembolso de R$ 800 do diretor?", a resposta está lá — quem votou, em qual data, com qual comentário. Em OSC com mudança rotativa de diretoria (eleição anual, troca de tesoureiro), esse registro é a diferença entre passagem de bastão tranquila e arenas de acusação.

### Rejeitado

[![Reembolso rejeitado](/assets/screenshots/manual-06b-reembolso-rejeitado.png)](/assets/screenshots/manual-06b-reembolso-rejeitado.png)
*Detalhe de reembolso rejeitado*

O motivo da rejeição aparece em destaque no topo da página. O solicitante (e somente o solicitante) vê o botão **Editar e reenviar** — clicando, os campos passam a ser editáveis na própria página, sem precisar criar um reembolso novo. Corrige o que foi apontado (valor errado, comprovante ausente, categoria trocada), reenvia, e o fluxo recomeça.

> ⚠️ **Atenção · Rejeição não é punição**
>
> Os motivos mais comuns de rejeição em OSC bem geridas são **práticos**, não pessoais: comprovante ilegível, valor sem nota, categoria que não bate. Quando rejeitar, **escreva motivo concreto e instrucional** ("anexar nota fiscal", "ajustar categoria para Combustível"), não vago ("revisar"). O solicitante reedita e reenvia em 2 minutos; conflito desnecessário evitado.

### Aprovado, aguardando pagamento

[![Reembolso aprovado](/assets/screenshots/manual-06c-reembolso-aprovado.png)](/assets/screenshots/manual-06c-reembolso-aprovado.png)
*Detalhe de reembolso aprovado, aguardando confirmação de pagamento*

Painel de Ações mostra: **"Aprovado — aguardando confirmação de pagamento pelo tesoureiro."**

> 📖 **Conceito · Aprovado vira movimentação pendente automaticamente**
>
> No momento em que o reembolso é aprovado, o RIT360 Financeiro cria automaticamente uma **movimentação financeira pendente** em Movimentações com origem `reimbursement` (origem reembolso), valor e categoria corretos, ainda sem conta financeira definida. Cabe ao tesoureiro entrar em Movimentações, clicar nessa linha, escolher a conta de onde o dinheiro vai sair e marcar como paga. O ciclo só fecha quando essa confirmação acontece. Na lista de Movimentações, o lançamento traz um link **"Ver pedido de reembolso →"** que volta direto ao detalhe original — útil para conferir comprovante antes de pagar.

### Pago

Quando o tesoureiro marca a movimentação financeira correspondente como paga, o reembolso aqui muda automaticamente para **Pago** (💙). O solicitante recebe notificação pelos canais que configurou no perfil. Ciclo encerrado.

## Nova solicitação de reembolso

[![Nova solicitação de reembolso](/assets/screenshots/manual-06d-novo-reembolso.png)](/assets/screenshots/manual-06d-novo-reembolso.png)
*Formulário de nova solicitação em desktop*

[![Nova solicitação de reembolso no celular](/assets/screenshots/mobile-novo-reembolso.png)](/assets/screenshots/mobile-novo-reembolso.png)
*Formulário no celular — destaque para o botão **Tirar foto** que abre a câmera traseira direto, e a barra de ações fixa no rodapé ("Cancelar / Salvar rascunho / Enviar para aprovação") ao alcance do polegar*

Clique em **+ Nova solicitação** para abrir o formulário.

**Campos obrigatórios:**

- **Data da despesa** — quando você efetivamente gastou
- **Valor** — total a ser reembolsado
- **Descrição** — o que foi comprado e para qual atividade (seja específico: "Combustível para transporte do material do bazar no sábado" vence "gasolina")
- **Forma de pagamento**: **PIX** ou **TED**, com a chave/dados bancários onde quer receber
- **Documentos**: nota fiscal, recibo, comprovante de pagamento ou foto da despesa

**Campos opcionais:**

- **Categoria** — sempre do tipo despesa (o RIT360 Financeiro só lista despesas aqui, não confunde com receita)
- **Projeto** e **Centro de custo** — para OSCs que separam o financeiro por iniciativa ou área
- **Observações** — contexto adicional para o aprovador

> ✓ **Dica · Configure dados de pagamento no perfil**
>
> Os dados de pagamento (PIX/TED) são pré-preenchidos automaticamente se você configurou o **Método de pagamento padrão** em **Meu Perfil → Dados para Reembolso**. Configura uma vez, todo reembolso futuro já vem com chave correta — você não erra e não precisa redigitar.

**Botões de ação:**

- **Salvar rascunho** — guarda sem enviar; você pode editar e enviar quando estiver pronto (útil quando você está esperando chegar a nota por e-mail, por exemplo)
- **Enviar para aprovação** — envia para os aprovadores elegíveis; status muda para "Aguardando aprovação" e os aprovadores recebem notificação pelos canais configurados

## Boas práticas

> ✓ **Dica · Reembolso curto, comprovante claro**
>
> A diferença entre reembolso aprovado no dia e reembolso que volta para correção: **descrição específica + comprovante legível**. Tire foto do recibo com boa luz, descreva no campo Descrição **o que** foi comprado e **para qual atividade** ("Lanche da reunião de planejamento dia 15"), e o aprovador resolve em 30 segundos sem nenhuma pergunta extra.

> ✓ **Dica · Tire a foto pelo próprio app no celular**
>
> Em mobile, o formulário oferece dois botões na seção **DOCUMENTOS**: **Tirar foto** e **Anexar arquivo**. **Tirar foto** abre a câmera traseira do celular direto, sem passar pela galeria; você enquadra o cupom, captura, vê a foto em tamanho grande e decide entre **Refazer** ou **Confirmar**. Útil para registrar a despesa no momento do gasto (no posto, na loja, na hora). O RIT360 Financeiro reduz automaticamente o tamanho da foto antes do envio — fica leve para subir mesmo em conexão móvel ruim, sem perder a legibilidade do cupom. Tipos aceitos pelo botão **Anexar arquivo**: imagens, PDF, XML (NFe) e ZIP.

> ⚠️ **Atenção · Comprovante é obrigatório, sem exceção**
>
> Reembolso sem comprovante é ponto de risco contábil e jurídico. Mesmo em compra pequena de R$ 10 — anexe o cupom fiscal ou ao menos uma foto da nota com data e estabelecimento. Reembolsos sem comprovação adequada são **a fonte número um de questionamento** em prestação de contas para financiadores e auditorias do terceiro setor.

> ⚠️ **Atenção · Não reembolse despesa de terceiro**
>
> O reembolso é para a pessoa que **pagou de verdade**. Se você levou um voluntário ao posto e ele pagou, o reembolso é dele, não seu. Reembolsar despesa de terceiro vira "doação disfarçada" — confunde a contabilidade, viola dever fiduciário, prejudica auditoria. Quando você não puder reembolsar a pessoa certa diretamente (ela não tem conta bancária, etc.), use um **Pedido de Pagamento** em nome dela como prestador, com seu CPF.

> ✓ **Dica · Aprovador, leia os comprovantes**
>
> O RIT360 Financeiro mostra os comprovantes em pré-visualização inline justamente para que o aprovador veja antes de votar — sem precisar baixar ou abrir programa externo. Aprovar sem ver o comprovante anula a função do controle. Reserve os 30 segundos para conferir; depois aprove com tranquilidade.

## Notificações dos eventos de reembolso

Cada usuário escolhe em **Meu Perfil → Notificações** quais eventos de reembolso quer receber, e por quais canais (e-mail e push). Eventos cobertos:

- **Reembolso submetido** — aprovadores elegíveis são avisados
- **Aprovação parcial** — em quórum 2, depois do primeiro voto positivo, demais aprovadores elegíveis são lembrados
- **Aprovado** — solicitante e tesoureiro são avisados
- **Rejeitado** — solicitante é avisado com o motivo
- **Pago** — solicitante é avisado

Padrão é tudo ligado; cada um silencia o que não quer receber.

## Glossário rápido

- **Reembolso** — solicitação para receber de volta dinheiro gasto do próprio bolso em nome da OSC.
- **Quórum** — número mínimo de aprovações necessárias para o reembolso ser aprovado (configurável: 1 ou 2).
- **Aprovador elegível** — usuário que pode votar em determinado reembolso pelo papel que ocupa ou por estar individualmente listado na configuração.
- **Auto-aprovação** — situação em que o solicitante é também o único aprovador elegível; permitida mas explicitamente marcada no audit log.
- **PIX/TED** — métodos de pagamento aceitos para crédito do reembolso aprovado.
- **Movimentação correspondente** — lançamento financeiro pendente criado automaticamente na aprovação, vinculado ao reembolso pelo campo origem.

## Por onde seguir

- **Pedidos de Pagamento** — para autorizar despesas que **ainda vão ser pagas** pela OSC (em vez de já ter pagado do bolso).
- **Movimentações** — para o tesoureiro confirmar o pagamento do reembolso aprovado e fechar o ciclo.
- **Meu Perfil → Dados para Reembolso** — para pré-preencher PIX/TED em futuras solicitações.
- **Configurações → Fluxo de Aprovações** — para a OSC ajustar quórum e papéis aprovadores.
- **Meu Perfil → Notificações** — para escolher quais eventos receber e em quais canais.
