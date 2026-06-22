---
title: "Meu Perfil"
nav_order: 6
permalink: /configuracoes/perfil/
---

A página **Meu Perfil** concentra **seus** dados pessoais e preferências dentro do Bússola — não os dados da organização. Disponível para todos os usuários autenticados, acessada pelo menu do avatar (canto superior direito → **Meu perfil**) ou diretamente pela rota `/perfil`.

[![Página Meu Perfil](/assets/screenshots/config-perfil.png)](/assets/screenshots/config-perfil.png)
*Página Meu Perfil — boxes consolidados de dados e preferências*

> 💡 **Por que isso importa**
>
> Perfil bem configurado tem dois efeitos práticos: (1) **reembolsos mais rápidos** porque a chave PIX/TED já vem pré-preenchida; (2) **menos ruído no dia a dia** porque você só recebe as notificações que importam para você, nos canais que prefere. 5 minutos de configuração inicial economizam horas ao longo dos meses.

A página tem cinco boxes consolidados: **Identificação**, **Dados para Reembolso**, **Notificações**, **Meus dados (LGPD)** e **Ações de Conta**.

## Identificação

- **Foto de perfil** — JPG, PNG ou WebP, até 2 MB. A imagem é redimensionada para 512×512 antes do envio.
- **Nome completo** — como aparece em audit logs, aprovações, registros.
- **Telefone** — digite no formato brasileiro `(11) 99999-9999` (o campo formata sozinho enquanto você digita); o Bússola guarda em formato internacional (com `+55`).
- **Data de nascimento** — opcional.
- **CPF** e **RG** — opcionais; o **CPF** é formatado automaticamente (`000.000.000-00`). Armazenados **cifrados em repouso** (chave de criptografia gerenciada separadamente do banco). Usados apenas para emissão de comprovantes quando exigido por lei.

Botão **Salvar alterações** ao final do box salva tudo de uma vez.

> ⚠️ **Atenção · CPF e RG são dados sensíveis pela LGPD**
>
> Você só precisa preencher CPF/RG se a sua OSC vai emitir documento que exija (recibo formal, declaração para imposto de renda, etc.). Se você não tem certeza se precisa, deixe em branco — o Bússola não exige esses dados para operar.

## Dados para Reembolso

Configure aqui sua **chave PIX** ou **dados bancários para TED**. Quando você criar um Reembolso, o Bússola preenche automaticamente esses dados — você não precisa redigitar a cada solicitação, e não corre risco de errar a chave.

> ✓ **Dica · Use chave PIX preferencialmente**
>
> PIX simplifica a vida do tesoureiro: pagamento imediato, sem custo, sem necessidade de TED programada. Se sua conta tem chave PIX configurada, use-a aqui em vez dos dados bancários completos. A OSC paga mais rápido, você recebe mais rápido.

Se você nunca pede reembolso, pode deixar em branco — só preencha quando for fazer a primeira solicitação.

## Notificações

Três grupos de configuração:

### Canais de notificação

- **Número de WhatsApp** — para receber alertas. Formato internacional (`+5511999999999`).
- **Telegram** — vinculação via bot. Envie `/start` para `@BussolaBot` no Telegram para vincular seu Telegram à sua conta Bússola. O campo aqui aparece como "Não vinculado" até você fazer a vinculação pelo bot.

E-mail é o canal default — sempre disponível, sem configuração adicional.

### Push (avisos no celular ou no navegador)

A partir da versão **v0.19.0**, **Push** é o 4º canal de notificações. Funciona como aviso de banco: você recebe um alerta na tela mesmo com o Bússola fechado, toca, e abre direto na tela relevante (reembolso aprovado, pedido pendente de seu voto, etc.).

A ativação é **por dispositivo**, com um interruptor mestre **"Ativar push neste dispositivo"** logo acima da matriz. Pode ativar no celular pessoal e desativar no do trabalho sem afetar a configuração da sua conta — cada dispositivo é independente.

**Como ativar:**

1. Toque (ou clique) no interruptor **"Ativar push neste dispositivo"**.
2. O navegador vai pedir permissão para enviar notificações — autorize.
3. Pelos toggles da matriz logo abaixo, defina quais eventos quer receber por push neste device.

**Requisitos por plataforma:**

- **Android (Chrome / Edge / outro navegador moderno):** funciona direto, sem precisar instalar. Apenas autorize quando perguntar.
- **iOS (Safari):** push só funciona se o Bússola estiver **instalado como app** na sua tela de início. Sem isso, o iOS não permite push e o interruptor fica desabilitado com instrução. Veja **[Instalar como app](/instalar-como-app/)** se ainda não fez.
- **Desktop (Chrome / Firefox / Edge):** funciona como no celular. Útil para receber avisos quando você está com outro aplicativo em primeiro plano.

**Múltiplas OSCs:** se você participa de mais de uma OSC, recebe push de eventos de todas. A OSC aparece no corpo do aviso para identificação da origem.

> 🔒 **Privacidade**
>
> O endpoint do seu dispositivo é armazenado da mesma forma que outros dados de contato (número de WhatsApp, ID do Telegram). Você pode desativar a qualquer momento no master switch ou pedir exclusão completa pelo fluxo LGPD em **Ações de Conta**.

### Matriz granular de preferências

Tabela que cruza **eventos × 4 canais** (E-mail, WhatsApp, Telegram, Push) e permite controle fino sobre quais notificações receber e por onde. Os eventos estão agrupados por área:

- **Reembolsos** (5): submetido, aprovação parcial, aprovado, rejeitado, pago.
- **Pedidos de Pagamento** (5): submetido, aprovação parcial, aprovado, rejeitado, pago.
- **Feedback** (2): novo feedback enviado, feedback resolvido.
- **Projetos**: comentários no mural, hora de publicar status, marcos atingidos ou perdidos, riscos materializados, tarefas atribuídas ou vencendo, resumo diário, e as aprovações de abertura/alteração e seus resultados.

Para cada par (evento, canal), um switch on/off. **Default é tudo ligado** — você silencia o que não quer receber.

> 📖 **Conceito · Canal desabilitado vs canal não cadastrado**
>
> Se a coluna WhatsApp, Telegram ou Push aparece **desabilitada** com tooltip ("Cadastre seu número primeiro" ou "Ative push neste dispositivo"), é porque você ainda não cumpriu o pré-requisito do canal. Cumpra-o e salve — na próxima abertura da página, a coluna fica habilitada para escolher quais eventos receber por esse canal.

> ✓ **Dica · Calibre por papel**
>
> Se você é aprovador, mantenha "submetido" ligado para ser avisado quando um reembolso/pedido precisa do seu voto. Se você é solicitante e não aprovador, "submetido" não te interessa — pode desligar e manter só "aprovado", "rejeitado" e "pago". Tesoureiro deve manter "aprovado" e "pago" sempre ligados para acompanhar o ciclo de pagamento.

## Meus dados (LGPD)

Você pode **baixar uma cópia dos seus dados pessoais** no Bússola a qualquer momento — é o seu direito de acesso e portabilidade previsto na LGPD.

[![Meus dados (LGPD) e ações de conta](/assets/screenshots/config-perfil-lgpd.png)](/assets/screenshots/config-perfil-lgpd.png)
*Box "Meus dados (LGPD)" para baixar seus dados, e box "Ações de conta"*

- Clique em **Baixar meus dados**. O pacote é um arquivo **JSON** com seu perfil, preferências, consentimentos, vínculos com organizações e as referências dos registros que você criou.
- A geração roda **em segundo plano**. Você recebe um **e-mail com o link de download** (válido por **7 dias**) assim que o pacote fica pronto. O último pedido fica listado na seção, pronto para baixar enquanto o link estiver válido.

## Ações de Conta

Ações administrativas sobre sua própria conta, cada uma com botão independente:

- **Alterar senha** — campos de nova senha e confirmação; clique em "Alterar senha" para confirmar. Senha forte (8+ caracteres, mix de letras, números e símbolos) é exigida.
- **Encerrar todas as sessões** — desconecta sua conta de todos os dispositivos onde está logada. Útil se você perdeu acesso a um celular ou suspeita de uso indevido.
- **Excluir minha conta (LGPD)** — exerce o **direito ao esquecimento**. Ao confirmar, sua conta entra em uma **carência de 30 dias**; passado o prazo, seus dados pessoais (nome, e-mail, telefone, CPF, RG, avatar) são **anonimizados de forma irreversível**. Por obrigação legal, **registros financeiros e de auditoria são retidos por 5 anos sem identificação pessoal**.

### Como excluir a conta

[![Confirmação de exclusão da conta](/assets/screenshots/config-perfil-excluir.png)](/assets/screenshots/config-perfil-excluir.png)
*Confirmação de exclusão — exige a senha atual e digitar "EXCLUIR"*

Por ser uma ação séria, a confirmação pede duas coisas: **sua senha atual** e digitar a palavra **EXCLUIR**. Ao confirmar, você é **desconectado de todos os dispositivos** e **não consegue mais entrar**. Dentro da janela de 30 dias, a **reativação** só é possível pelo DPO (`dpo@rit.org.br`) — não há autosserviço para reativar.

> ⚠️ **Atenção · Encerrar sessões te desconecta também**
>
> "Encerrar todas as sessões" inclui o navegador atual. Você vai precisar fazer login de novo. Útil principalmente em situação de risco (perdeu celular, suspeita de acesso indevido). Em uso normal, não há motivo para usar.

## Por onde seguir

- **Reembolsos** — onde os dados de reembolso configurados aqui são usados automaticamente.
- **Configurações → Usuários** — para o admin gerenciar acesso de outros membros.
