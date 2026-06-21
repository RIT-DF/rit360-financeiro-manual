---
title: "FAQ"
nav_order: 10
permalink: /faq/
---

Respostas para dúvidas comuns. Se a sua pergunta não está aqui, use o botão **💬 Feedback** dentro do Bússola — sua dúvida ajuda este manual a melhorar.

## Acesso e conta

### Não recebi o e-mail de convite. O que faço?

Peça ao administrador da sua organização que reenvie o convite em **Configurações → Usuários → ações da sua linha → Reenviar convite**. Verifique também a caixa de spam/lixo eletrônico antes — convites são enviados a partir de domínio institucional e às vezes caem lá.

### Esqueci minha senha. Como redefino?

Na tela de login, clique em **Esqueci a senha**, informe o e-mail da sua conta e clique em **Enviar link de redefinição**.

[![Tela de recuperação de senha](/assets/screenshots/manual-recuperar-senha.png)](/assets/screenshots/manual-recuperar-senha.png)

Você receberá um e-mail com um link para definir uma nova senha. O link **vale por 1 hora e só pode ser usado uma vez**. Ao definir a nova senha, você volta para a tela de login e entra com ela.

Por segurança, a confirmação na tela é sempre a mesma, exista ou não uma conta para aquele e-mail (não revelamos quais e-mails têm cadastro). Se não receber, confira a caixa de spam. Se você cadastrou via Google no primeiro acesso, use **Continuar com Google** em vez de senha — contas só-Google não têm senha para redefinir.

### Posso usar o mesmo e-mail em mais de uma organização?

Sim. Sua conta no Bússola é única, atrelada ao seu e-mail, mas você pode ser membro de várias OSCs simultaneamente. Use o **seletor de organização** no topo da tela para alternar entre elas — toda a interface reage à organização ativa.

### Posso encerrar minhas sessões em outros dispositivos?

Sim. Em **Meu Perfil → Ações de Conta → Encerrar todas as sessões**. Útil se você perdeu um dispositivo ou suspeita de uso indevido. Atenção: isso te desconecta também do navegador atual; você precisa fazer login de novo.

## Navegação e papéis

### Onde encontro Configurações? Não vejo nenhum item no menu.

Configurações da organização está no **ícone de engrenagem** no canto superior direito da TopNav (entre o Feedback e o menu do avatar). O ícone só aparece para usuários com papel **Admin (Presidente)** ou **Tesoureiro** — voluntários e coordenadores não veem porque não têm acesso às configurações da OSC.

### Onde está "Meu Perfil"?

No **menu do avatar** (canto superior direito da tela) → **Meu perfil**. A rota é `/perfil`, separada das Configurações da organização porque o perfil é pessoal (não da OSC).

### Sou voluntário. Por que não vejo o módulo "Movimentações"?

Voluntários não têm acesso a Movimentações (lançamentos detalhados da OSC). Eles veem o Painel (com saldo geral), e a aba Reembolsos em Pagamentos e Reembolsos (para registrar os próprios reembolsos). Para ver Movimentações, é necessário papel Coordenador, Tesoureiro ou Presidente — fale com o administrador da OSC.

### O que significa "auto-aprovação"?

Quando você é o único aprovador elegível para o seu próprio reembolso ou pedido (caso comum em OSC pequena onde o presidente é o único aprovador e também é o solicitante), o Bússola **permite a auto-aprovação** para não travar o fluxo, mas marca explicitamente no audit log. Conforme a OSC ganha mais aprovadores cadastrados, auto-aprovações naturalmente diminuem.

## Movimentações

### O sistema registrou minha despesa com data errada. Posso corrigir?

Sim, desde que o lançamento ainda esteja com status **Pendente** ou **Atrasado**. Clique em **Editar** no detalhe da movimentação. Lançamentos já marcados como **Pago** não podem ter os dados principais alterados — para corrigir, use **Estornar** e crie um novo lançamento correto.

### Qual a diferença entre Cancelar e Excluir uma movimentação?

**Cancelar** mantém o lançamento no histórico com status "Cancelado" — útil para rastreabilidade ("essa despesa estava prevista mas não aconteceu"). **Excluir** apaga o lançamento de vez. O Bússola só permite excluir movimentações que já foram canceladas ou estornadas, justamente para evitar perda acidental. Para auditoria limpa, prefira sempre **cancelar** a excluir.

### Posso exportar os lançamentos?

Sim. Na lista de **Movimentações**, clique em **Exportar** e escolha PDF (formatado) ou Excel (planilha). A exportação inclui os filtros ativos no momento da exportação.

### Como funcionam as recorrências?

Ao criar uma movimentação, você pode escolher tipo **Recorrente**: define frequência (mensal, trimestral, etc.) e duração (data final, quantidade de ocorrências ou indefinido até cancelar). O Bússola cria as ocorrências automaticamente; cada uma é paga individualmente. Para encerrar uma série em andamento, abra o detalhe e use o cancelamento em 3 escopos (apenas esta / esta e futuras / série inteira).

### Posso informar o centro de custo ao importar lançamentos por planilha?

Sim. A planilha de importação tem a coluna `centro_de_custo` (opcional). Se o nome informado ainda não existir na OSC, ele aparece como **pendência** na tela de resumo, onde você escolhe **criar** o centro de custo, **mapear** para um existente ou **importar aquelas linhas sem** centro de custo — antes de confirmar. Em branco, o lançamento entra sem centro de custo.

### Anexei um arquivo ZIP a um lançamento. Os documentos de dentro aparecem na prestação de contas?

Sim. O Bússola **descompacta o ZIP automaticamente** e anexa cada arquivo de dentro como um anexo individual do lançamento — o pacote dá lugar aos arquivos, que passam a aparecer na pré-visualização e a entrar na prestação de contas. Vale também quando o comprovante chega por **link** na importação por CSV. Arquivos que não dá para exibir num PDF (planilhas, textos) ficam anexados, mas não aparecem no corpo do relatório.

## Reembolsos e Pedidos de Pagamento

### Meu reembolso foi rejeitado. Posso reenviar?

Sim. Abra o detalhe do reembolso rejeitado, clique em **Editar e reenviar**, corrija o que foi apontado pelo aprovador (motivo da rejeição aparece em destaque) e envie de novo. Não é preciso criar um reembolso novo — o mesmo volta para o fluxo de aprovação.

### O que acontece quando um reembolso é aprovado?

O Bússola cria automaticamente uma **movimentação financeira pendente** em Movimentações com origem `reimbursement`, vinculada ao reembolso. O tesoureiro entra em Movimentações, escolhe a conta de onde vai sair o dinheiro e marca como paga. O ciclo só fecha quando essa confirmação acontece.

### Posso anexar mais de um comprovante em um reembolso?

Sim. O formulário aceita múltiplos arquivos. Anexe nota fiscal, recibo, foto da despesa, comprovante de pagamento — quanto mais clareza, mais rápida a aprovação.

### Onde configuro minha chave PIX para receber reembolsos?

Em **Meu Perfil → Dados para Reembolso**. Configure uma vez; o formulário de nova solicitação preenche automaticamente em todas as próximas vezes.

### Qual a diferença entre Reembolso e Pedido de Pagamento?

**Reembolso** é para despesa que **já aconteceu**: você pagou do bolso e quer receber de volta. **Pedido de Pagamento** é para despesa que **ainda vai acontecer**: a OSC vai pagar (boleto, fornecedor, contrato) e a aprovação autoriza a saída de dinheiro.

### Posso criar um Pedido de Pagamento recorrente para o aluguel?

Sim. Ao criar um pedido, escolha tipo **Recorrente** e configure a frequência (mensal) e a duração (data final, quantidade de ocorrências ou indefinida até cancelar). A aprovação cria a série inteira; cada ocorrência é paga separadamente pelo tesoureiro. Veja a [seção de Pedidos de Pagamento](/modulos/pedidos-pagamento/) para detalhes.

## Projetos

### Como crio um projeto?

Em **Projetos → Novo projeto**. Um assistente de 4 passos (tipo e identidade, período, financeiro essencial, coordenador e equipe) conduz a criação, com textos de ajuda em cada etapa. O projeto nasce como rascunho "Em planejamento"; quando estiver pronto, você solicita a aprovação de abertura.

### Quem pode criar projetos?

Presidente, Tesoureiro e Coordenador podem criar diretamente. O **Voluntário** pode **propor** um projeto — ao ser aprovado, ele é promovido a coordenador daquele projeto. Veja o [Guia do Coordenador de Projetos](/guias/coordenador-projetos/).

### Como vinculo uma despesa (ou receita) a um projeto?

No formulário de lançamento, use o campo **Projeto** (opcional). O dinheiro continua sendo da OSC, nas mesmas contas — o projeto apenas **rotula** a movimentação, para você ver o recorte dele sem perder o todo. O mesmo vale para reembolsos e pedidos de pagamento.

### O que é a "saúde" do projeto (o semáforo)?

Um indicador (🟢 Saudável, 🟡 Atenção, 🔴 Crítico, com pontuação de 0 a 100) que combina **prazo**, **orçamento** e **riscos**. Ele aparece na lista de projetos e no Painel, para a diretoria ver de relance o que pede atenção.

### Onde vejo as lições de projetos anteriores?

Em **Projetos → Lições aprendidas** — um acervo da OSC com as lições e boas práticas registradas no encerramento de todos os projetos, com busca e filtros. Ao criar um novo projeto, o sistema ainda indica quantas lições existem para aquele tipo.

### Como encerro um projeto?

Na aba **Encerramento** do projeto, um assistente de avaliação conduz por perguntas (objetivos, critérios, engajamento, pontos altos, lições...). O Bússola monta o **relatório de encerramento** consolidado, exportável em PDF para a prestação de contas. Cada campo traz orientação e um exemplo de preenchimento.

### Qual a diferença entre meu papel na OSC e meu papel no projeto?

São independentes. Seu **papel na OSC** (Presidente, Tesoureiro, Voluntário...) define o acesso geral. Seu **papel no projeto** (Coordenador, integrante, observador) define o que você faz **dentro daquele projeto** — um voluntário pode ser coordenador de um projeto específico, e um tesoureiro pode ser só integrante de outro.

## Estornos

### Quando devo estornar e quando cancelar?

**Cancele** quando a movimentação **ainda não foi paga** e não vai mais acontecer (evento desmarcado, fornecedor desistiu). **Estorne** quando a movimentação **já foi paga** e precisa ser desfeita (depósito duplicado, doação devolvida pelo banco, refund). Estornar preserva o histórico e cria automaticamente um lançamento contrário; cancelar simplesmente marca como anulada.

### Estornei um lançamento por engano. Como desfazer?

Estorno não tem "desfazer estorno" automático no Bússola. Para reverter, você precisa **criar manualmente uma movimentação nova** com os mesmos dados do estornado, com data atual. Por isso a operação de estorno tem dialog de confirmação com campo de razão — para evitar engano no clique.

## Contas, categorias e configuração

### Minha conta bancária sumiu da lista. O que aconteceu?

Contas podem ser **desativadas** por um administrador (em Configurações → Contas Bancárias). Contas desativadas não aparecem em filtros e formulários, mas as movimentações históricas associadas a elas são preservadas. Verifique com o admin.

### Como começo do zero com as categorias? Não sei o que cadastrar.

Em **Configurações → Categorias**, clique em **Aplicar template** e escolha um modelo próximo ao perfil da sua OSC (ex: "Padrão Grupo Escoteiro 2026"). O template traz categorias típicas pré-configuradas. Depois você ajusta o que não bater com sua realidade — renomeia, exclui, adiciona.

## Integração com WooCommerce

### Posso conectar minha loja online ao Bússola?

Se sua loja usa **WooCommerce**, sim. Em **Configurações → Organização → seção WooCommerce**, configure URL da loja, Consumer Key e Consumer Secret. O Bússola sincroniza pedidos pagos como receitas automaticamente. A seção tem instruções passo a passo de como gerar as credenciais no admin do WooCommerce.

### Quando a sincronização com WooCommerce acontece?

**Automaticamente todo dia às 6h da manhã** (horário de Brasília), respeitando a frequência configurada por OSC: diária, semanal (segundas), mensal (dia 1) ou desligada. Você também pode disparar manualmente a qualquer momento em **Movimentações → Importar Lançamentos → aba WooCommerce → Importar agora**.

### Um pedido foi reembolsado no WooCommerce. O que acontece no Bússola?

A próxima sincronização detecta a mudança de status e **estorna automaticamente** a movimentação correspondente no Bússola — cria um lançamento contrário (despesa de igual valor que cancela a receita anterior) e ambos passam a exibir o badge "Estornado". Sem intervenção manual.

## Notificações

### Não quero receber tantos e-mails. Como reduzir?

Em **Meu Perfil → Notificações → Matriz**, você escolhe **por evento e por canal** quais notificações quer receber. Default é tudo ligado — desligue o que não interessa. Cuidado para não silenciar eventos críticos do seu papel (ex: aprovador deve manter "submetido" ligado para saber quando algo precisa do voto).

### Quero receber notificações por WhatsApp. Como faço?

Em **Meu Perfil → Notificações**, preencha seu número de WhatsApp em formato internacional (`+5511...`). Salve. A coluna WhatsApp na matriz fica habilitada para escolher quais eventos receber por esse canal.

### E Telegram?

Envie `/start` para `@BussolaBot` no Telegram. O bot vincula automaticamente seu Telegram à sua conta Bússola. Depois, a coluna Telegram na matriz de notificações fica habilitada.

### Como ativo notificações push no celular?

Em **Meu Perfil → Notificações**, toque no interruptor **"Ativar push neste dispositivo"** (acima da matriz). O navegador vai pedir permissão; autorize. A coluna **Push** na matriz fica habilitada para você escolher quais eventos receber por esse canal — funciona como aviso de banco, chega na tela mesmo com o Bússola fechado e abre direto na tela relevante ao tocar.

**Importante:** no **iPhone (Safari)**, push só funciona se você **instalou o Bússola como app** na tela de início — sem instalar, o interruptor fica desabilitado com instrução. Veja [Instalar como aplicativo](/instalar-como-app/). No **Android (Chrome / Edge)** e em **desktop (Chrome / Firefox / Edge)**, funciona direto sem precisar instalar como app.

A ativação é **por dispositivo**: pode ativar no celular pessoal e deixar desativado no celular do trabalho, sem afetar a configuração da sua conta.

## Guias por papel

### Existe um guia de como atuar no meu papel na OSC?

Sim. Além de explicar as telas, o manual traz **cartilhas de atuação** por papel — o que se espera de você, pontos de atenção e boas práticas, com exemplos de como o Bússola ajuda em cada aspecto:

- [Guia do Coordenador de Projetos](/guias/coordenador-projetos/) — escopo, prazo, recursos e pessoas.
- [Guia do Tesoureiro](/guias/tesoureiro/) — registrar, organizar, aprovar e prestar contas.
- [Guia da Comissão Fiscal](/guias/comissao-fiscal/) — fiscalização independente.
- [Guia do Presidente](/guias/presidente/) — responsabilidade com visão, delegação e acompanhamento tranquilo.

## Geral

### Tenho uma sugestão ou encontrei um erro. Como informo?

Use o botão **💬 Feedback** no menu superior. Está disponível para todos os usuários e envia sua mensagem direto para a equipe da RIT, com a versão do app e o seu contexto.

### Onde acompanho as novidades do Bússola?

Nas [Novidades](/changelog/) deste manual. Toda nova versão lançada é registrada lá com a lista de adições, correções e mudanças. As entregas significativas aparecem em destaque.

### Quero entender melhor um conceito que aparece no Bússola (fluxo de caixa, regime de caixa, estorno...). Onde leio?

Cada módulo deste manual tem uma seção **Conceitos essenciais** que cobre os termos relevantes em linguagem simples. Movimentações cobre regime de caixa e estorno; Reembolsos cobre quórum e auto-aprovação; Pedidos cobre recorrente vs parcelado.

### Posso usar o Bússola se não sou de OSC?

O Bússola é desenhado para OSCs (Organizações da Sociedade Civil) — terceiro setor. O fluxo de aprovação, os papéis e a linguagem refletem esse contexto. Outros tipos de organização (empresa, autônomo) podem usar tecnicamente, mas vão encontrar funcionalidades que não fazem sentido no contexto deles.
