---
layout: section
title: Changelog
permalink: /changelog/
---

# Changelog — Bússola Financeira

Todas as mudanças relevantes do projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/){:target="_blank" rel="noopener noreferrer"}.

---

## [0.26.1] — 2026-06-12

O e-mail de redefinição de senha agora chega em português e com a identidade da Bússola.

### Melhorado

- **E-mail de redefinição de senha:** o link de "Esqueci a senha" passa a chegar em **português**, com o visual da Bússola, em vez do modelo padrão em inglês. O fluxo continua o mesmo — você pede o link, define a nova senha e entra com ela.

---

## [0.26.0] — 2026-06-11

Recuperação de senha por e-mail no login.

### Adicionado

- **"Esqueci a senha":** a tela de login passa a ter a opção **Esqueci a senha** — você informa o e-mail e recebe um link para definir uma nova senha, com as mesmas regras de senha forte do cadastro. Por segurança, a confirmação é sempre neutra (não revela se o e-mail tem conta). Quem entra pelo Google continua usando **Continuar com Google**.

---

## [0.25.4] — 2026-06-11

Mensagem mais clara ao vincular uma movimentação a um projeto.

### Corrigido

- **Vínculo de projeto na movimentação:** quando a organização não tem projetos abertos, o campo "Projeto" do lançamento passa a informar claramente que não há projetos a vincular, em vez de exibir "Em breve" — que dava a impressão equivocada de que a funcionalidade ainda não existia. Para organizações com projetos, o campo já funcionava normalmente.

---

## [0.25.3] — 2026-06-11

Ajuste visual no cadastro de movimentação pelo celular.

### Corrigido

- **Botões de tipo no celular:** na tela de novo lançamento, os botões Receita / Despesa / Transferência passam a exibir um ícone e a caber corretamente em telas pequenas, sem o texto de "Transferência" sair do lugar.

---

## [0.25.2] — 2026-06-11

A tela de Lições Aprendidas fica mais compacta e fácil de percorrer.

### Melhorado

- **Lições Aprendidas em lista:** o acervo passa a ser exibido como tabela (no computador) e linhas compactas (no celular), no lugar dos cards — mais lições visíveis de uma vez, mantendo a categoria, o texto integral, o projeto e a data, além da busca e dos filtros.

---

## [0.25.1] — 2026-06-11

Orientações e exemplos ajudam a preencher melhor a avaliação de encerramento de projetos.

### Melhorado

- **Orientação no encerramento de projetos:** cada campo de texto da avaliação de encerramento — objetivos, critérios de sucesso, engajamento, imprevistos, pontos altos, pontos a melhorar, lição mais importante e recomendação — passa a mostrar uma orientação curta e um exemplo, ajudando a coordenação a registrar aprendizados mais úteis para a organização (e que alimentam o acervo de Lições Aprendidas).

---

## [0.25.0] — 2026-06-11

Nova tela de Lições Aprendidas reúne, em um só lugar, os aprendizados de todos os projetos encerrados da organização.

### Adicionado

- **Lições Aprendidas da organização:** uma nova tela, dentro de Projetos, reúne as lições e boas práticas registradas no encerramento de todos os projetos da organização — acessível a qualquer membro. Dá para filtrar por tipo de projeto e por categoria (boa prática, lição, ponto a melhorar, recomendação) e buscar pelo texto.
- **Sugestão de lições ao criar um projeto:** ao escolher o tipo de projeto no começo da criação, o sistema mostra quantas lições já existem para projetos daquele tipo e oferece um atalho para consultá-las — ajudando a aproveitar a experiência de projetos anteriores.

---

## [0.24.7] — 2026-06-11

Rotinas automáticas de projetos e a sincronização diária voltam a rodar nos horários programados.

### Corrigido

- **Avisos e rotinas automáticas:** os lembretes e avisos automáticos de projetos (atualização de status, tarefas e marcos atrasados) e a sincronização diária com a loja (WooCommerce) passam a ser executados de forma confiável nos horários programados.

---

## [0.24.5] — 2026-06-11

Valores financeiros se ajustam melhor à tela no celular.

### Melhorado

- **Números dos cards financeiros no celular:** em telas pequenas, os valores nos cards — saldos por conta, totais de movimentações, indicadores do painel e os resumos de Reembolsos e Pedidos de pagamento — passam a usar um tamanho de fonte que se ajusta à largura do card, evitando que valores altos "saiam" do card. No computador a aparência continua a mesma.

---

## [0.24.3] — 2026-06-11

A Tesouraria passa a acessar a calibração de Relatórios nas Configurações.

### Corrigido

- **Tesoureiro acessa "Relatórios" nas Configurações:** o item "Relatórios" (calibração das regras de atenção dos relatórios) agora aparece e funciona também para a Tesouraria, e não só para a Presidência — alinhando esse acesso ao que já vale para as demais configurações financeiras (Contas e Categorias).

---

## [0.24.2] — 2026-06-11

O saldo inicial de uma conta passa a ficar protegido depois que ela já tem lançamentos.

### Corrigido

- **Saldo inicial protegido após o primeiro lançamento:** ao editar uma conta que já possui lançamentos, o campo "Saldo inicial" fica bloqueado, evitando que uma alteração acidental distorça o saldo atual exibido. Os demais dados da conta continuam editáveis normalmente. Caso seja realmente necessário corrigir o saldo inicial nesse caso, isso pode ser feito pela Presidência.

---

## [0.24.1] — 2026-06-11

Digitação de valores em reais agora é igual em todo o sistema, com formatação automática.

### Melhorado

- **Campos de valor com formatação automática:** ao digitar qualquer valor em reais — em Movimentações, Reembolsos, Pedidos de pagamento, Parcelas, Contas e Projetos — o campo já mostra o número formatado enquanto você digita (por exemplo, `1.500,00`), do mesmo jeito em todas as telas.

### Corrigido

- **Orçamento de projeto não salva mais zerado por engano:** ao informar um valor com separador de milhar (como `1.500,00`), o orçamento passa a ser gravado com o valor correto, em vez de ser salvo como R$ 0 sem aviso. O mesmo cuidado vale agora para os campos de valor de Reembolsos e Pedidos de pagamento.

---

## [0.24.0] — 2026-06-11

Reforço de segurança no cadastro feito por conta própria.

### Adicionado

- **Confirmação de e-mail no cadastro:** ao criar a própria conta (link "Criar agora" na tela de login), você recebe um **código de 6 dígitos por e-mail** e o informa para concluir o cadastro — com opção de reenviar o código. Quem já tem conta é levado direto ao **login**, em vez de criar outra.

### Segurança

- Reforço no fluxo de criação de conta: a definição de senha agora exige a confirmação do e-mail por código.

---

## [0.23.1] — 2026-06-11

Correções de exibição e de permissões identificadas em testes por papel.

### Corrigido

- **Diretor agora apenas consulta as Movimentações**: para o papel Diretor, deixaram de aparecer os botões de operação (lançar, importar, editar, cancelar, estornar, excluir, marcar como pago) na lista e no detalhe, e também a edição do projeto vinculado a um lançamento. O papel é de supervisão, somente leitura.
- **Menu "Mais" no celular**: a opção de Configurações passa a aparecer somente para quem tem acesso às configurações, e leva cada perfil à seção permitida (antes era exibida também para perfis sem acesso).
- **Painel — seção Projetos**: voltou a carregar corretamente para perfis operacionais (como o Voluntário), que antes viam a seção falhar ao abrir o Painel.

---

## [0.23.0] — 2026-06-10

Uniformização das permissões por papel: o papel "Dirigente" passa a se chamar "Diretor", o Tesoureiro ganha a gestão de cadastros e há reforços internos de controle de acesso.

### Alterado

- **Papel "Diretor"** (antes "Dirigente"): renomeado para um termo mais usual em OSCs. Passa a ser um papel de **supervisão, somente leitura** — vê Movimentações, Relatórios e Projetos para acompanhamento, sem operar (não lança nem aprova).

### Melhorado

- **Tesoureiro gerencia cadastros**: o Tesoureiro passa a poder criar e editar Contas Bancárias e Categorias diretamente (antes restrito ao Presidente).
- **Reforços internos de segurança e de controle de acesso por papel**, sem mudança no uso do dia a dia.

---

## [0.22.1] — 2026-06-10

Lote de correções e reforços após uma auditoria de qualidade: datas corretas nas exportações, app mais rápido de abrir e mais privacidade em dispositivos compartilhados.

### Corrigido

- **Datas corretas nas exportações e no parcelamento**: planilhas de movimentações, relatórios em PDF e o resumo ao criar um parcelamento passaram a mostrar a data exata (antes, em alguns casos, apareciam um dia antes).
- **Aviso ao remover anexos**: se a remoção de um comprovante de reembolso falhar, agora aparece um aviso, em vez de falhar sem explicação.
- **Lembretes e sincronizações automáticas** (lembretes de projeto e sincronização do catálogo WooCommerce) passam a rodar corretamente nos horários programados.

### Melhorado

- **Abertura mais rápida**: o app passou a carregar telas e recursos de exportação sob demanda, deixando a primeira abertura mais leve — especialmente no celular.
- **Privacidade em dispositivos compartilhados**: ao sair da conta, os comprovantes visualizados deixam de ficar guardados no navegador.
- **Reforços internos de segurança e controle de acesso**, sem mudança no uso do dia a dia.
- **Card de compartilhamento próprio**: ao compartilhar o link do app, o card passa a exibir a imagem e a identidade da Bússola.

---

## [0.22.0] — 2026-06-10

Melhorias de usabilidade nos projetos: ações mais diretas, layout da execução em colunas e um novo filtro por data no mural.

### Adicionado

- **Filtro por data no mural do projeto**: na aba Execução, o mural de comunicação ganhou um filtro por período (Últimos 7 dias, Últimos 30 dias, Este mês ou um intervalo personalizado), que combina com o filtro por tipo (eventos, comentários, status updates).

### Melhorado

- **Botões de ação diretos nos blocos do projeto**: as ações dos itens (editar, remover e ações específicas como "marcar marco como atingido" ou "marcar risco como materializado") agora aparecem como botões diretos no item, em vez de escondidas atrás de um menu de três pontos — nos blocos de Marcos, Riscos, Stakeholders, Tarefas, Evidências e Mural.
- **Aba Execução em duas colunas (desktop)**: Tarefas ocupa a coluna principal à esquerda e Comunicação + Evidências ficam à direita, reduzindo a rolagem. No celular, continua em seções recolhíveis.
- **Logo clicável**: clicar no logo da Bússola no topo leva você de volta ao Painel.
- **Ações de tarefa mais claras**: em tarefas já concluídas ou abandonadas, agora aparece apenas "Reabrir" (além de Editar e Remover), em vez de vários botões redundantes. Mover uma tarefa entre qualquer status continua possível arrastando no quadro ou pela edição.

---

## [0.21.0] — 2026-06-10

Correções de acabamento logo após a estreia do módulo de Projetos, mais um novo filtro por período na lista de projetos.

### Adicionado

- **Filtro por período na lista de projetos**: filtre os projetos por mês, trimestre, ano ou por um intervalo de datas personalizado. O filtro mostra os projetos cujo período acontece — mesmo que parcialmente — dentro do intervalo escolhido, e combina com os filtros de status, tipo, saúde e busca.

### Corrigido

- **Produtos do WooCommerce nos projetos**: o bloco de produtos no financeiro do projeto voltou a carregar e a listar corretamente os produtos sincronizados da loja.
- **Sincronização do catálogo WooCommerce**: a data da última sincronização do catálogo agora permanece visível ao recarregar a página ou navegar entre telas.
- **Aceite da Política de Privacidade**: corrigido um caso em que o aceite podia ser registrado mais de uma vez e gerar um aviso no carregamento inicial do app.
- **Troca de organização**: ao trocar de OSC enquanto visualizava o detalhe de uma movimentação, reembolso, pedido de pagamento ou projeto, o app agora abre automaticamente a lista correta da nova organização — sem precisar recarregar a página.

### Melhorado

- **Produtos do WooCommerce no projeto**: o bloco de produtos passou a aparecer na visão geral do financeiro do projeto (antes ficava só dentro de "Calcular taxa"), tornando mais simples associar produtos da loja ao projeto.

---

## [0.20.0] — 2026-06-10

Estreia do **módulo de Projetos** — o maior incremento da plataforma até aqui. Agora a OSC planeja, executa, acompanha e encerra seus projetos dentro da Bússola, com financeiro vinculado, indicador de saúde e relatório de encerramento.

### Adicionado

- **Módulo de Projetos** (novo item no menu): crie e gerencie os projetos da OSC, cada um com seu coordenador e equipe. Cada pessoa tem um papel dentro do projeto e o acesso respeita esse papel. Os projetos passam por um ciclo de vida — da criação ao encerramento —, com uma etapa de **aprovação configurável** pela OSC.
- **Criação guiada por assistente**: um passo a passo de 4 etapas (tipo e identidade · período · financeiro · coordenador) cria o projeto com as informações certas, adaptando-se ao tipo escolhido (Projeto, Evento ou Voluntário).
- **Planejamento**: defina o **escopo**, monte a **equipe**, registre o **orçamento** previsto por categoria, planeje **marcos**, mapeie **riscos** (probabilidade × impacto) e cadastre **partes interessadas**.
- **Execução**:
  - **Tarefas** em lista e em quadro **Kanban**, com responsável, prazo e vínculo a marcos.
  - **Mural de comunicação**: linha do tempo dos acontecimentos do projeto + comentários com menção a pessoas (`@`).
  - **Status updates** do coordenador, com lembrete automático quando o projeto fica muito tempo sem atualização.
  - **Evidências** (arquivos e vídeos) anexáveis ao projeto.
- **Financeiro do projeto**:
  - **Movimentações vinculadas** ao projeto, com visão de previsto × realizado.
  - **Registrar despesa** do projeto abrindo um reembolso ou pedido de pagamento já vinculado, que segue o fluxo normal de aprovação da OSC.
  - **Produtos do WooCommerce por projeto**: vincule produtos da loja a um projeto para que as vendas entrem como receita dele.
  - **Calculadora de taxa de evento**: simule a taxa por participante considerando custos, fundo de reserva, isentos, voluntários e a regra de pagamento; adote uma taxa oficial ou marque o evento como gratuito.
- **Acompanhamento**:
  - **Indicador de saúde** (semáforo verde / amarelo / vermelho) por projeto — na lista e em um card no **Painel**.
  - **Filtro por projeto nos Relatórios** e uma aba de **Relatório** dentro do próprio projeto.
- **Encerramento do projeto**: assistente de avaliação (objetivos, critérios, engajamento), **relatório de encerramento** completo, exportação em **PDF**, registro de **lições aprendidas** e a opção de gerar um **relatório parcial** antes da finalização.

### Melhorado

- **Painel reorganizado**: a ordem das seções ficou mais coerente (resumo financeiro do mês → pendências de pagamento → projetos); **Pedidos de Pagamento** e **Reembolsos** agora aparecem lado a lado, cada um em um card único com suas pendências como linhas clicáveis; e cada seção ganhou um ícone e um detalhe de cor para facilitar a leitura.
- **Lista de Projetos em tabela no computador**: no desktop a lista abre em formato de tabela (como os demais módulos), mantendo os cards no celular.
- **Severidade de risco**: o card de cada risco passa a mostrar uma severidade calculada (probabilidade × impacto), ajudando a priorizar o que merece atenção.
- **Pendências visíveis no financeiro do projeto**: reembolsos e pedidos ainda não aprovados aparecem em uma seção "Aguardando aprovação", evitando solicitar o mesmo pagamento duas vezes.

### Corrigido

- **Concordância de gênero na matriz de risco**: os níveis de **Impacto** agora aparecem no masculino (Alto / Médio / Baixo), enquanto a Probabilidade permanece no feminino.

---

## [0.19.4] — 2026-05-22

Bump consolidado de 8 entregas focadas em **consistência visual em mobile/PWA**, **navegação inferior** e **estabilidade do ciclo de atualização do app**.

### Adicionado

- **Relatórios na barra inferior do app em mobile** (BK-219): a barra inferior agora tem 5 itens fixos — **Painel · Movim. · Pag./Reemb. · Relatórios · Mais**. O botão `+` central, que era circular e prometia abrir um novo lançamento mas não funcionava, foi removido. As ações de criar lançamento, reembolso e pedido continuam no botão **Novo** do header de cada lista.
- **Manual, Privacidade e Termos no menu "Mais"** (BK-222): em mobile (onde o rodapé fica oculto pra dar espaço à barra inferior), o sheet aberto pelo botão **Mais** agora inclui links diretos para **Manual do Usuário**, **Política de Privacidade** e **Termos de Uso** — sempre acessíveis na palma da mão.

### Corrigido

- **Campo de valor em Reembolsos e Pedidos de Pagamento se comportava diferente de Movimentações** (BK-218): nas telas de Reembolsos e Pedidos, ao digitar `100` o campo exibia `R$ 1,00` (tratava cada dígito como centavo). Em Movimentações o mesmo `100` virava `R$ 100,00`. Foi corrigido. Agora todos os campos de valor do app se comportam igual: digitar números resulta no valor inteiro; centavos só são incluídos se você usar vírgula explicitamente (ex.: `100,50` → `R$ 100,50`). Cobre Reembolso novo/editar, Pedido novo/editar (modos único, recorrente e parcelado).
- **Calibração automática de pontos de atenção falhava com erro técnico** (BK-224): em **Configurações → Regras de pontos de atenção**, clicar em **Calibrar pelo histórico** (disponível pra OSCs com 6+ meses de movimentação) disparava um erro técnico e o fluxo não completava. Foi corrigido. A calibração agora roda até o fim e propõe os novos limites pra cada regra com base no histórico real da OSC.
- **App em mobile precisava limpar dados do navegador a cada nova versão** (BK-212 — 2ª iteração): o aviso "Nova versão disponível" aparecia, mas tocar em **Atualizar** não tinha efeito e o app continuava na versão antiga — a única forma de subir era ir nas configurações do Chrome, excluir todos os dados de site e refazer login. Foi corrigido. Agora tocar em **Atualizar** mostra rapidamente o aviso "Atualizando..." e recarrega o app já na versão nova, em mobile e desktop.

### Melhorado

- **Botões do header das listas em mobile** (BK-220, BK-223): nas telas de Reembolsos, Pedidos de Pagamento, Configurações (Contas, Categorias, Usuários, Relatórios), Superadmin (Organizações) e empty states, os botões de ação no topo agora exibem só ícones em mobile (em vez de texto longo que quebrava o layout em telas pequenas), com toque confortável e descrição acessível pra leitor de tela. Em desktop continua ícone + texto, como antes. A página de Configurações de Usuários ganhou outra simplificação no mobile: o bloco flutuante na parte de baixo da tela foi removido — os mesmos botões agora ficam só no topo, sem duplicação.
- **Tabs internas de Configurações em mobile** (BK-221): as tabs **Organização**, **Usuários**, **Contas Bancárias**, **Categorias**, **Fluxo de Aprovações** e **Relatórios** passaram a exibir só ícone em mobile (antes alguns rótulos longos como "Contas Bancárias" quebravam em duas linhas e bagunçavam o layout). Em desktop continuam com ícone + texto.

### Observações de uso

- **Esta é a primeira release onde o ciclo de atualização do app funciona automaticamente em mobile e desktop.** Quem está em v0.19.3 vai receber o aviso "Nova versão disponível" e, ao tocar em **Atualizar**, o app subirá pra v0.19.4 sem precisar de hard refresh nem limpar cache. Daqui pra frente, esse passo é automático em toda nova versão.

---

## [0.19.3] — 2026-05-21

### Adicionado

- **Superadministradores avisados em tempo real quando você envia um feedback** (BK-217): ao usar o botão **Feedback** no topo do app, todos os superadmins ativos recebem aviso imediato pelos canais que tiverem habilitado em **Meu Perfil → Notificações** (e-mail por padrão; push se a Bússola estiver instalada como app). Resposta administrativa fica muito mais ágil — antes, dependia do superadmin abrir a tela de feedbacks pra ver o que tinha de novo.

### Observações de uso

- A configuração desse aviso fica em **Meu Perfil → Notificações → seção Feedback → linha "Quando um usuário envia novo feedback"**. A linha aparece apenas para superadministradores. Defaults: e-mail e push ligados; WhatsApp e Telegram desligados (canais menos comuns para uso administrativo).

---

## [0.19.2] — 2026-05-21

Bump consolidado de 6 entregas pós-piloto: 3 correções de bugs reportados pelos testadores, 2 melhorias de navegação e 1 nova funcionalidade administrativa.

### Adicionado

- **Resposta ao usuário quando seu feedback é resolvido** (BK-215): em **Superadmin → Feedbacks**, ao marcar um feedback como **Resolvido**, abre uma tela onde o administrador pode escrever uma mensagem opcional pro usuário que reportou. Se escolher enviar, a mensagem chega ao usuário pelo canal que ele tem habilitado em **Meu Perfil → Notificações** (e-mail por padrão). Se preferir só resolver sem enviar nada, basta o botão **Marcar como resolvido sem enviar**. A mensagem fica guardada na linha do feedback (ícone de envelope ao lado do status) pra histórico e revisão.
- **Cards de saldos por conta na aba Movimentações** (BK-211): a página de Movimentações agora exibe, acima da lista de lançamentos, os cards com o saldo de cada conta (Consolidado + uma card por conta operacional ativa) — o mesmo bloco que já existia no Painel e em Relatórios. Saldos atualizam ao vivo, independente dos filtros que você aplicar na lista.
- **Cards de aprovação clicáveis em Pedidos e Reembolsos** (BK-213): os 4 cards no topo das listas de **Pedidos de Pagamento** e **Reembolsos** ("Aguardando minha aprovação", "Aprovados aguardando pagamento", "Solicitado no período", "Pago no período") agora são clicáveis — clicar leva direto à sub-aba filtrada pelo status correspondente. Antes eram puramente informativos.

### Corrigido

- **Saldos no Painel não atualizavam após transferência entre contas** (BK-210): ao registrar uma transferência marcada como já efetivada (Data de pagamento preenchida no formulário), os cards de saldo do Painel, da página de Contas e do dropdown de seleção continuavam mostrando os valores antigos — só atualizavam após hard refresh (Ctrl+Shift+R) ou nova sessão. Foi corrigido. Agora qualquer transferência marcada como paga reflete imediatamente nos saldos em todas as telas. Transferências antigas que estavam contabilizadas errado também foram corrigidas retroativamente — o saldo total consolidado da OSC foi preservado (transferências não criam nem destroem dinheiro, só redistribuem entre as contas).
- **Reprovação de pedidos de pagamento dava erro e não era registrada** (BK-214): ao tentar reprovar um pedido aguardando aprovação, o sistema retornava o erro técnico "Edge Function returned a non-2xx status code" e a reprovação não era registrada — o pedido ficava preso em "aguardando" sem possibilidade de avançar. Foi corrigido. Aprovadores agora conseguem reprovar com motivo e o pedido vai pra status "Rejeitado" normalmente, com a entrada visível no histórico de aprovações com a cor e o rótulo certos. Reprovação de reembolsos continuava funcionando — apenas o fluxo de pedidos estava afetado.
- **Atualizações do app em desktop exigiam hard refresh em cada página** (BK-212): em navegador comum (não-PWA instalado), o aviso "Nova versão disponível" só aparecia depois de o tesoureiro fechar e reabrir a aba — quem deixava a Bússola aberta o dia inteiro nunca via o aviso e continuava na versão antiga. Foi corrigido. Agora o app verifica versão nova a cada minuto, quando você volta o foco pra aba da Bússola, e quando reconecta após perder rede. Quando você toca em **Atualizar**, todas as abas abertas se atualizam juntas.

### Observações de uso

- **Bootstrap chato (uma vez só):** quem está em v0.19.1 ainda precisa fazer um último hard refresh manual (Ctrl+Shift+R) para subir para v0.19.2 — depois disso o ciclo automático de atualização (BK-212) passa a valer e nenhum hard refresh será mais necessário.
- Esta release fecha a fila de bugs e melhorias reportados pelos testadores na fase de pré-teste.

---

## [0.19.1] — 2026-05-21

Versão dedicada à **estabilização da experiência no celular** e à correção de um bug crítico que estava impedindo as atualizações do app de chegarem aos usuários. Os 6 ajustes desta versão não trazem funcionalidade nova — refinam o que já existia para deixar a Bússola pronta para uso diário no smartphone.

### Corrigido

- **Atualizações do app agora chegam direito ao celular**: nas versões anteriores, quando uma nova versão era publicada e o aviso "Nova versão disponível" aparecia no celular, tocar em **Atualizar** não trocava de versão — só funcionava após limpar manualmente os dados do navegador (Configurações do Chrome → Privacidade e segurança → Limpar dados). Foi corrigido. A partir desta versão, tocar em "Atualizar" recarrega o app na versão nova automaticamente. **Importante:** este fix só passa a valer **a partir desta versão (v0.19.1)** — quem está em v0.19.0 ou anterior precisa, uma última vez, fazer aquele procedimento manual de limpar dados pra subir para v0.19.1 e ganhar o comportamento correto dali em diante.
- **Filtros de status em Reembolsos**: tocar em "Rascunho", "Aguardando aprovação", "Aprovado", "Rejeitado" ou "Pago" dentro da aba **Reembolsos** estava levando o usuário pra aba **Pedidos de Pagamento**. Agora o filtro funciona dentro da própria aba Reembolsos.
- **Cabeçalho de Movimentações no celular**: os botões "Exportar / Importar Lançamentos / Novo lançamento" no topo da página vazavam ligeiramente para fora da tela. Foram ajustados para caber certinho.

### Modificado

- **Listas de Pedidos e Reembolsos no celular agora aparecem como cartões**: em vez da tabela com colunas que precisavam de rolagem lateral, cada solicitação vira um cartão vertical com todos os campos visíveis sem precisar rolar — mesmo padrão que **Movimentações** já tinha desde a v0.18.0. Em desktop, a tabela tradicional continua sendo usada.
- **Formulários de Nova Solicitação otimizados para celular**: nos formulários de **Novo Reembolso** e **Novo Pedido de Pagamento** (e nos modos de edição), a barra de ações ("Cancelar / Salvar rascunho / Enviar para aprovação") agora aparece em um rodapé fixo na parte de baixo da tela do celular, ao alcance do polegar — padrão familiar de apps nativos. Os campos também ganham mais espaço horizontal: em vez de 3 colunas apertadas (Categoria / Projeto / Centro de custo), passam a empilhar em coluna única no celular. Em desktop o visual continua exatamente como antes.
- **Rodapé do app oculto no celular**: a barra de rodapé (versão do app + links de Política / Termos / Manual) só aparece em telas grandes. No celular, esses links continuam disponíveis pelo menu **Mais** da barra inferior.

### Observações de uso

- Esta versão é resultado de uma varredura sistemática pós-PWA: testamos as 12 rotas principais do app em viewport de 375px (smartphones pequenos como iPhone SE) para garantir zero conteúdo cortado e fluxo de toque consistente.
- Quem usa o Bússola só no desktop não vai notar mudança nenhuma — todas as alterações desta versão são especificamente para refinar a experiência no celular.
- Próximas versões voltam o foco para novas funcionalidades (em particular, aceite combinado da Política de Privacidade e Termos de Uso).

---

## [0.19.0] — 2026-05-20

Esta versão adiciona um novo canal de notificações: **push direto no celular ou no navegador**. Você passa a receber avisos da Bússola mesmo com o app fechado, como em qualquer aplicativo de banco — ao tocar no aviso, abre direto na tela relevante (reembolso aprovado, pedido pendente de seu voto, etc.). Push é o 4º canal da matriz de preferências, ao lado de E-mail, WhatsApp e Telegram.

### Adicionado

- **Push como 4º canal na matriz de notificações** (BK-199): a tabela de preferências em **Meu Perfil → Notificações** ganha uma coluna **Push** ao lado de E-mail, WhatsApp e Telegram. Cada par (evento × canal) continua sendo um toggle independente — você decide por qual caminho quer ser avisado de cada tipo de evento. Default vem com tudo ligado; você silencia o que não quer.
- **Ativação por dispositivo** (BK-199): um interruptor mestre **"Ativar push neste dispositivo"** acima da matriz controla se este celular/computador específico recebe push. Pode ativar no celular pessoal e desativar no do trabalho sem afetar a configuração da sua conta — cada dispositivo é independente.
- **Avisos chegam mesmo com o app fechado** (BK-199): a integração com os serviços nativos de notificação dos sistemas (Google no Android, Apple no iOS) faz o aviso chegar como o de WhatsApp ou e-mail — não depende de você estar com a Bússola aberta.
- **Toque no aviso abre a tela correspondente** (BK-199): tocar em "Reembolso aprovado" abre direto no detalhe daquele reembolso; tocar em "Pedido pendente de aprovação" abre direto no detalhe do pedido — sem navegar por menu.

### Observações de uso

- **Android (Chrome / Edge / outro navegador moderno):** funciona direto, sem precisar instalar. Apenas autorize quando o navegador perguntar.
- **iOS (Safari):** push só funciona se a Bússola estiver **instalada como app** na tela de início (toque em **Compartilhar → Adicionar à Tela de Início**). Sem isso o iOS não permite push, e o interruptor fica desabilitado com instrução. Veja **[Instalar como app](/instalar-como-app/)** se ainda não fez.
- **Desktop (Chrome / Firefox / Edge):** funciona como no celular. Útil para receber avisos quando você está com outro aplicativo em primeiro plano.
- **Múltiplas OSCs:** quem participa de mais de uma OSC recebe push de eventos de todas elas. A OSC aparece no corpo do aviso para identificação da origem.
- **Privacidade:** o endpoint do seu dispositivo é armazenado da mesma forma que os outros dados de contato (número de WhatsApp, ID do Telegram). Você pode desativar a qualquer momento no master switch ou pedir exclusão completa pelo fluxo LGPD em **Ações de Conta**.

---

## [0.18.0] — 2026-05-20

Release consolidando duas frentes: a **captura de documentos pela câmera no celular** (BK-200, principal novidade) e um pacote de **estabilização mobile + polimentos** que vinha acumulando desde a entrega do PWA (v0.17.0). O salto de versão de v0.17.2 direto para v0.18.0 (sem v0.17.3 intermediária) reflete essa consolidação — todas as melhorias chegam juntas ao usuário.

### Adicionado
- **Capturar documento com a câmera do celular** (BK-200): em **Nova Movimentação**, **Novo Reembolso** e **Novo Pedido de Pagamento** (e nas variantes de edição de Reembolso/Pedido), o celular agora exibe um botão **Tirar foto** ao lado de **Anexar arquivo**. Tocar abre a câmera traseira direto; após capturar, você vê a foto em tamanho grande e decide entre **Refazer** ou **Confirmar**. Caso de uso primário: tesoureiro registra a despesa de campo (gasolina, material, lanche) no momento do gasto, sem precisar abrir a câmera do celular, salvar na galeria e depois selecionar.
- **Anexar comprovante em lançamentos diretos** (BK-200): até a versão anterior, só Reembolsos e Pedidos de Pagamento permitiam anexar nota fiscal/recibo/boleto. Agora **Movimentação** também aceita anexo (opcional — lançamento sem comprovante continua válido). O comprovante aparece na página de detalhe do lançamento e fica disponível para auditoria. Em modo recorrente/parcelado a seção fica oculta na criação da série e ganha uma nota explicativa: você anexa depois acessando cada lançamento individualmente.
- **Troca de organização (OSC) no celular** (BK-201, originalmente em v0.17.2 — refinamento incremental aqui): no painel **Mais** da barra inferior, o bloco da OSC ativa permanece sólido e funcional.

### Modificado
- **Vocabulário uniformizado em todos os formulários financeiros** (BK-200): a seção de anexos passa a se chamar **DOCUMENTOS** em todos os 6 formulários (Reembolso novo/editar, Pedido novo/editar, Movimentação novo/editar). Texto auxiliar único — "Nota fiscal, recibo, boleto, orçamento, contrato ou outro documento". Mensagem de erro padronizada — "Inclua ao menos um documento." (substitui "Inclua ao menos um comprovante.").
- **Tipos de arquivo aceitos restritos a imagens, PDF, XML (NFe) e ZIP** (BK-200): o seletor nativo do dispositivo passa a esconder tipos fora dessa lista, reduzindo upload de arquivos inválidos.
- **Fotos da câmera são reduzidas automaticamente** antes do upload (BK-200): legibilidade preservada para humano (e para extração automática futura via IA), com economia significativa de armazenamento da OSC — cada foto chega ao servidor com 200-500 KB em vez dos 5-10 MB típicos de smartphone moderno.
- **Botão de submit muda conforme o modo no Novo Lançamento** (carona BK-200): "Salvar lançamento" em modo Único; "Criar série" em modo Recorrente/Parcelado. Comunica melhor o que vai acontecer.

### Corrigido
- **Inconsistência visual de obrigatoriedade no Pedido de Pagamento** (BK-200): a label "DOCUMENTOS" passa a exibir o asterisco vermelho de campo obrigatório, alinhando com Reembolso (a regra no servidor já era a mesma — só a UI não comunicava).
- **App no celular agora rola normalmente ao arrastar com o dedo** (BK-193): em Android Chrome e iOS Safari, a tela não rolava por toque — o conteúdo ficava cortado e o usuário precisava esticar/zoom para chegar no rodapé. A altura fixa que travava o documento foi substituída por altura mínima, liberando o browser a criar a área scrollável virtual. Em desktop continua funcionando como antes.
- **Tabela de Movimentações em celular agora exibe os lançamentos como cartões** (BK-194): a tabela de 9 colunas era cortada em viewport mobile (só 2 colunas visíveis em 322px). Agora, em telas menores que 1024px, cada lançamento aparece como um cartão com todos os campos visíveis sem rolagem horizontal — padrão familiar de apps financeiros (Nubank, Conta Azul). Em telas maiores, a tabela tradicional continua sendo usada.
- **Scrollbar horizontal indesejada no body em mobile** (BK-195): em `/pagamentos`, `/reembolsos`, `/movimentacoes` e `/relatorios`, a página inteira oferecia rolagem horizontal de até 342px em mobile, dando sensação de "tela quebrada". Corrigido globalmente; containers de tabs ficam responsáveis por sua própria rolagem horizontal quando precisarem. Resta uma regressão residual de 47px em `/movimentacoes` mascarada pelo fix global — rastreada em BK-202 para tratamento futuro.
- **Sino de notificações sem funcionalidade removido da barra superior** (BK-174): o ícone de sino próximo ao avatar não estava ligado a nenhum fluxo de notificações no app — clicar não fazia nada. Foi removido para não passar expectativa errada ao usuário. Quando a feature de notificações no app for implementada, o sino volta junto.
- **Filtro de Fornecedor removido da barra de Relatórios** (BK-176): decisão de produto — no contexto de prestação de contas e visão gerencial agregada, Tipo, Conta, Categoria e Centro de custo já cobrem o essencial. Filtro permanece intacto em `/movimentacoes` e demais telas.
- **Meses em português em todo o módulo Relatórios** (BK-177): alerta de meses negativos na aba Previsão exibia "Atenção: saldo projetado negativo em May/2026" em vez de "Maio/2026". Todos os pontos de formatação de mês no módulo (alerta de Previsão, gráficos, tabelas, cabeçalho) passaram a usar o português.
- **Importação de movimentações via CSV agora aceita seis formatos de data** (BK-171): planilhas brasileiras (com data em `dd/mm/aaaa` ou `dd-mm-aaaa`) eram rejeitadas pelo importador, que aceitava apenas ISO. Agora o parser reconhece automaticamente `aaaa-mm-dd`, `aaaa/mm/dd`, `dd-mm-aaaa`, `dd/mm/aaaa`, `dd-mm-aa`, `dd/mm/aa` e converte internamente antes de salvar.

### Observações de uso
- Validação E2E foi feita via Playwright em produção em 2026-05-20: dois botões em mobile, dropzone preservada em desktop, captura por câmera com preview, compressão, modos Único/Recorrente/Parcelado da Movimentação. Teste manual com upload de CSV em formato brasileiro ainda recomendado pelo administrador antes de migrar planilhas antigas em larga escala.
- Câmera é exclusiva do celular — em desktop o botão "Tirar foto" não aparece (webcam frontal de laptop não serve para fotografar comprovante apoiado na mesa).
- Modos Recorrente e Parcelado de **Novo Lançamento** ocultam a seção de anexo na criação da série; uma nota explicativa orienta o usuário a anexar individualmente em cada lançamento após salvar.

---

## [0.17.2] — 2026-05-19

### Corrigido
- **Abas de Movimentações no celular voltaram a ser acessíveis** (BK-197): as abas iniciais (**Todas** e **Receitas**) ficavam invisíveis à esquerda e o usuário não conseguia rolar a barra de abas para alcançá-las — só era possível rolar para a direita para ver as últimas. Agora a rolagem funciona em ambas as direções nas abas de **Movimentações**, **Pagamentos e Reembolsos**, **Relatórios** e demais telas que usam abas em mobile (8 telas mapeadas e corrigidas via componente compartilhado).
- **Rótulo "Pag./Reemb." na navegação do celular** (BK-198): a barra inferior do app instalado mostrava só "Reemb." no terceiro botão, ocultando que o módulo cobre também Pedidos de Pagamento. Agora aparece **Pag./Reemb.** e leva para `/pagamentos` (a tela raiz do módulo).

### Adicionado
- **Troca de organização (OSC) agora disponível no celular** (BK-201): no celular, usuários com acesso a mais de uma OSC (superadmin, voluntários cross-OSC, contadores) não tinham como trocar de organização — o seletor existia só no cabeçalho desktop, escondido em mobile. Agora, no painel **Mais** (barra inferior), aparece no topo um bloco com a **OSC ativa** (logo + nome). Quando há múltiplas OSCs, tocar nesse bloco expande a lista de organizações disponíveis dentro do próprio painel; tocar em uma delas troca de OSC e fecha o painel. Se o usuário tem só uma OSC, o bloco aparece apenas como informação ("você está na OSC X").

---

## [0.17.1] — 2026-05-19

### Corrigido
- **Filtros de Relatórios voltaram a funcionar** (BK-183): os filtros **Conta**, **Categoria** e **Centro de custo** estavam exibindo botões vazios e não filtravam nada (só **Tipo** funcionava). Agora todos os filtros listam as opções com nome legível e aplicam o filtro corretamente em todas as abas (Visão Geral, Receitas, Despesas, Atenção, Previsão).
- **Menu "Mais" no celular não cai mais em 404** (BK-187): ao tocar em **Mais** na barra inferior do app instalado no celular, agora abre um painel deslizante com **Pagamentos e Reembolsos**, **Projetos**, **Relatórios**, **Configurações da organização**, **Meu perfil** e **Sair** — em vez de mostrar página de erro.
- **Banner de instalação não bloqueia mais a navegação no celular** (BK-188): o banner "Instale o Bússola como app" subiu para acima da barra de navegação inferior. Tesoureiros agora conseguem usar a navegação livremente mesmo com o banner visível.
- **Banner de instalação só aparece no celular** (BK-186): em computadores desktop, o banner sumiu — Chrome/Edge já têm o ícone "Instalar" próprio na barra de endereços, então o banner era redundante e ocupava espaço.
- **Página de erro 404 agora em português** (BK-189): ao acessar uma rota inexistente, a Bússola exibe **"Página não encontrada"** com a identidade visual da marca (logo, paleta teal, fonte Exo 2) em vez do texto genérico "Oops! Page not found" em inglês.
- **Atualizações voltam ao modelo de aviso** (BK-185): a v0.17.0 saiu com modo de auto-atualização forçada (necessário para destravar quem ficou com a versão quebrada do dia anterior). A v0.17.1 retoma o comportamento padrão — você vê uma notificação "Nova versão disponível" e decide quando aplicar.

### Em validação (Android)
- **Bússola virou app instalável de verdade no Android** (BK-191): instalar a Bússola pelo Chrome Android agora cria um aplicativo standalone com ícone próprio (não mais um simples atalho que abre dentro do Chrome). **Validado em produção em 2026-05-19.** Veja como instalar em [Instalar como aplicativo](/instalar-como-app/).

---

## [0.17.0] — 2026-05-19

### Adicionado
- **Bússola instalável como aplicativo no celular** (BK-179): Android Chrome agora oferece **Instalar aplicativo** no menu de três pontos. No iPhone, **Compartilhar → Adicionar à Tela de Início** instala a Bússola como app de verdade. No desktop (Chrome/Edge), aparece um ícone de **Instalar** na barra de endereços. App instalado abre em janela própria, sem barra do navegador, com splash em Verde Teal e ícone próprio da marca.
- **Logo oficial em todas as telas** (BK-179): símbolo + nome **BÚSSOLA** lado a lado substituem a pseudo-logo de texto improvisada que aparecia no cabeçalho, na tela de login e no painel de autenticação. Mesmo símbolo é usado como ícone do app quando instalado no celular.
- **Manual público com logo oficial** (BK-179): cabeçalho da documentação (`bussola-docs`) passa a exibir **RIT** + **Bússola Financeira** lado a lado.

### Alterado
- **Fonte Exo 2 self-hostada** (BK-179): tipografia oficial do design system agora é servida pelo próprio domínio da Bússola, sem depender mais do Google Fonts. Resultados: carregamento mais rápido, funciona em redes que bloqueiam CDN externa, e nenhum dado de IP do usuário vai para a infraestrutura do Google (privacy-by-design).
- **Atualização sob seu controle** (BK-179): quando uma nova versão da Bússola for publicada, você verá uma notificação discreta perguntando se quer atualizar agora ou depois — em vez de o app trocar de versão sem aviso enquanto você usa.

---

## [0.16.1] — 2026-05-19

### Corrigido
- **Relatórios: filtro "Todos" agora exibe os dados completos** (BK-180): ao escolher o preset **Todos** na Visão Geral de `/relatorios`, o Resultado do Período, Evolução do Saldo, Saldos por Conta e Top 5 receitas/despesas voltam a exibir todos os valores reais do histórico da OSC, em vez de zerar tudo como se não houvesse movimentações. As demais abas (Receitas, Despesas, Atenção, Previsão) seguem a mesma lógica.

---

## [0.16.0] — 2026-05-19

### Adicionado
- **Importação de usuários em lote por CSV** (BK-178): nova opção **Importar usuários** em **Configurações → Usuários**, ao lado de "Adicionar usuário". Admin pode trazer dezenas ou centenas de membros de uma vez a partir de uma planilha CSV — útil para OSCs migrando de outro sistema ou cadastrando todo o quadro associativo de uma vez.
- **Template CSV pré-formatado** (BK-178): botão "Baixar template" entrega um arquivo com cabeçalho e exemplos. Campos obrigatórios: nome completo, e-mail e papel. Opcionais: telefone, WhatsApp, Telegram, data de nascimento, CPF e RG.
- **Pré-visualização com classificação por status** (BK-178): após upload, a Bússola mostra cada linha como **novo** (vai receber convite), **já cadastrado** (cria vínculo direto), **vínculo ativo na OSC** (atualiza só campos vazios do perfil), ou **com erro** (será pulada, com motivo explícito). Botão "Importar" só fica ativo se houver linhas válidas.
- **Convite por e-mail mantido para novos cadastros** (BK-178): cada e-mail novo recebe o mesmo template de convite usado quando o admin cadastra individualmente. Senha continua sendo definida pelo próprio usuário no link de setup — admin nunca vê nem digita senha alheia.
- **Upsert seletivo de perfil** (BK-178): para e-mails já cadastrados, a Bússola preenche apenas os campos do perfil que estão vazios. Nenhum dado existente é substituído. Útil para enriquecer cadastros sem risco de sobrescrever dados que o membro já cadastrou no próprio perfil.
- **CPF e RG via Vault** (BK-178): se a planilha incluir CPF/RG, esses dados vão para o cofre seguro (Vault) do Supabase, com a mesma proteção que o cadastro individual recebe. Nunca persistem em coluna clara.
- **Resumo final por categoria** (BK-178): ao concluir, a Bússola mostra contagens por tipo (convites enviados, convites com e-mail pendente quando o envio falhou, vínculos novos, perfis atualizados, linhas com erro). Linhas com erro ficam disponíveis para download em CSV separado com coluna de motivo, facilitando correção.

### Observações de uso
- Multi-papel não entra via planilha — cada linha atribui exatamente 1 papel. Para acumular papéis, usar **Editar papéis** no menu de ações do membro após importar.
- Dados de pagamento (PIX/banco/conta) **não entram** na planilha por decisão de segurança e simplicidade. Cada membro preenche no próprio perfil.

## [0.15.0] — 2026-05-19

### Adicionado
- **Módulo de Relatórios** (BK-070, Onda 5): novo item "Relatórios" na barra superior, restrito a **Presidente, Tesoureiro e Comissão Fiscal**. Consolida toda a informação financeira da OSC em análises gerenciais navegáveis em **cinco abas**: Visão Geral, Receitas, Despesas, Atenção e Previsão. Voluntários e Coordenadores de Projeto não acessam no momento.
- **Visão Geral** (BK-070): resultado do período em destaque (receitas menos despesas pagas), gráfico de evolução do saldo, cards com saldo de cada conta na **data final do período** (não "hoje" — coerência com prestação de contas histórica), top 5 receitas e top 5 despesas por categoria com link para a aba detalhada.
- **Receitas e Despesas** (BK-070): gráfico por categoria + tabela detalhada com todas as categorias e percentual do total; quando há mais de 10 categorias, linha "Outros" agregada com expansão inline. Clique em qualquer linha abre `/movimentacoes` filtrado pela categoria + período.
- **Aba Atenção** (BK-070): lista anomalias detectadas no período por **cinco regras configuráveis** — despesa única concentrada, categoria com pico, fornecedor novo com alto valor, categoria zerada que voltou, queda de receita. Cada anomalia tem severidade (leve/moderada/alta) e link de ação contextual. Badge na aba mostra a contagem total.
- **Aba Previsão** (BK-070): forecast híbrido de fluxo de caixa para os próximos 3, 6 ou 12 meses combinando lançamentos já cadastrados (pendentes, ocorrências futuras de séries recorrentes, parcelas futuras de pedidos aprovados — "agendados") com extrapolação por média móvel de 6 meses por categoria ("estimados"). Mês corrente entra como primeiro mês projetado com marcador "em curso". Cada célula traz badge de origem (agendado/estimado). Drilldown mostra a composição. Alerta destacado quando há mês com saldo projetado negativo.
- **Comparativo com período anterior** (BK-070): toggle no cabeçalho ativa comparação em todas as abas onde faz sentido (Visão Geral, Receitas, Despesas). Granularidade automática: mês completo compara com mês anterior completo; mês em andamento ou intervalo customizado compara com janela de mesma duração imediatamente antes.
- **Configuração das regras de atenção** (BK-070): nova seção em **Configurações → Relatórios** (restrita ao Presidente). Cards editáveis com toggle on/off, threshold em campo numérico com unidade clara, link "Restaurar padrão" individual e link "Restaurar todas as regras ao padrão".
- **Calibrar pelo histórico** (BK-070): botão na tela de configuração de regras (habilitado a partir de 6 meses de movimentação registrada) que dispara análise estatística do histórico da OSC e sugere thresholds personalizados para cada uma das cinco regras, com nível de confiança (alta/média/baixa) e justificativa em linguagem natural. Admin pode aceitar todas, editar individualmente antes de salvar, ou cancelar. Aplicação atômica em transação única.
- **Exportação dos relatórios** (BK-070): botão Exportar com três opções — PDF da aba ativa, PDF completo (todas as cinco abas + sumário) e Excel multi-sheet. Cabeçalho identificador padrão em todos os formatos: nome da OSC, escopo, período, filtros aplicados, estado do comparativo, data/hora de geração. Receitas/despesas exportadas trazem todas as categorias (não só top 10).
- **Filtros e período compartilhados entre abas** (BK-070): conta, categoria, fornecedor, tipo, centro de custo — todos multi-select. Período com presets (mês, trimestre, semestre, ano) + intervalo customizado. Default: último mês fechado. Estado completo persistido em query params da URL — link compartilhável reconstrói o recorte.

### Corrigido
- **Bloco "Resultado do período" zerado** (BK-173): bloco hero da aba Visão Geral exibia R$ 0,00 enquanto os demais blocos da mesma tela (gráfico, saldos por conta, top 5) mostravam dados reais. RPC `report_overview` foi corrigida para alinhar lógica de filtros com as demais RPCs do módulo.

### Observações de uso
- Cálculo dos relatórios é **regime de caixa**: considera apenas movimentações com status **pago**, agregadas pela data de pagamento. A aba Previsão é exceção — lançamentos pendentes futuros entram como "agendados".
- Relatórios são leitura pura — gerar um relatório não altera nenhum dado financeiro.
- PDF da primeira versão usa **tabelas e blocos textuais** — sem reprodução de gráficos visuais. Reprodução visual em PDF entra em versão futura.

## [0.14.0] — 2026-05-19

### Adicionado
- **Múltiplos papéis por usuário em uma mesma OSC** (BK-166): um membro agora pode acumular papéis no mesmo vínculo — por exemplo, ser **Coordenador de Projeto** e **Comissão Fiscal** ao mesmo tempo. As capacidades se somam: o usuário faz tudo que qualquer um dos seus papéis permite. Útil em OSCs pequenas onde a mesma pessoa cumpre mais de uma função.
- **Editor de papéis dedicado** (BK-166): em Configurações → Usuários, o menu de ações ganhou o item **"Editar papéis"** que abre um painel lateral com checkboxes para os 6 papéis disponíveis. Marcar/desmarcar é livre, com **uma restrição visível**: Comissão Fiscal não pode ser combinada com Presidente nem Tesoureiro (conflito de interesse — o fiscal não pode fiscalizar a si mesmo). O sistema desabilita visualmente as opções incompatíveis e mostra mensagem explicativa.
- **Confirmações sensíveis preservadas** (BK-166): adicionar ou remover o papel de Presidente continua exibindo o diálogo de confirmação ("Promover a administrador" / "Remover privilégios de administrador") antes de salvar. Outras mudanças de papel salvam direto.
- **Lista de membros com todas as pills de papel** (BK-166): a tabela e os cards de membros agora exibem **todas as pills de papel** lado a lado, na ordem hierárquica (Presidente → Tesoureiro → Dirigente → Coordenador de Projeto → Comissão Fiscal → Voluntário). A visão do superadmin recebeu a mesma atualização para manter consistência.

### Observações de uso
- Invariante "último administrador ativo" preservada: o sistema continua bloqueando a remoção do papel de Presidente do último admin ativo da OSC.
- O fluxo de **convite** de novos membros não muda — convite continua atribuindo um único papel (default: Voluntário); papéis adicionais são atribuídos depois via edição do membro.

## [0.13.1] — 2026-05-19

### Adicionado
- **Papel "Comissão Fiscal"** como 5º papel disponível (BK-165): novo papel destinado a membros eleitos da comissão fiscal estatutária da OSC. Capacidades: leitura ampla de todas as movimentações, reembolsos, pedidos de pagamento e log de auditoria. **Não opera, não aprova e não solicita pedidos de pagamento** — pode solicitar reembolso próprio, como qualquer outro membro. Configurações da OSC ficam inacessíveis (mesma regra de Coordenador/Voluntário).
- **Filtros de papel em Configurações → Fluxo de Aprovações** (BK-165): seletor de papéis aprovadores **não exibe** Comissão Fiscal como opção. Tentativas de configurar via API direta são rejeitadas pelo backend com erro explícito.
- **Defesa em profundidade** (BK-165): bloqueio de mutações financeiras por Comissão Fiscal aplicado em três camadas — guard de rota, ocultação de botão na UI e validação no backend. Mesmo que algum passo falhe, os demais continuam protegendo.

### Corrigido
- **Regressão na ST-165.2** (BK-170): Comissão Fiscal aparecia indevidamente como opção de **solicitante de pedido de pagamento** em Configurações → Fluxo de Aprovações. Corrigido — apenas Presidente, Tesoureiro e Coordenador de Projeto solicitam pedidos de pagamento.

## [0.13.0] — 2026-05-18

### Adicionado
- **Integração com WooCommerce** (BK-149): a Bússola agora sincroniza automaticamente os pedidos pagos da loja online da sua OSC como receitas em Movimentações. Cada pedido `completed` vira um lançamento financeiro com data, valor, cliente, método de pagamento e categoria — sem intervenção manual.
- **Configuração da integração** (BK-149): nova seção "WooCommerce" em **Configurações → Organização**. Admin informa URL da loja, Consumer Key e Consumer Secret (com instruções passo a passo de como gerar no admin do WooCommerce, sem suposições), escolhe a frequência da sincronização (diária / semanal / mensal / desligada), a conta financeira destino, a data de corte para o backfill inicial e o modo de mapeamento de categorias (automático com categoria-mãe ou manual explícito).
- **Sincronização automática diária** (BK-149): todas as OSCs com integração ativa têm seus pedidos sincronizados automaticamente todo dia às 06:00 (horário de Brasília). A frequência efetiva por OSC respeita a configuração escolhida — uma OSC em "Semanal" só roda nas segundas; em "Mensal" só no dia 1; em "Desligada" pula completamente.
- **Importação manual sob demanda** (BK-149): além do cron automático, a página **Movimentações → Importar Lançamentos** (renomeada de "Importar CSV") agora tem duas fontes — CSV (existente) e WooCommerce (nova). Na aba WooCommerce, o admin escolhe o período (Desde a última sincronização / Últimos 7 dias / Últimos 30 dias / Personalizado com 2 datas) e clica "Importar agora".
- **Estorno automático em refunds** (BK-149): se um pedido importado pela Bússola virar `refunded` ou `cancelled` no WooCommerce depois, a próxima sincronização cria automaticamente um lançamento contrário (padrão de estorno do BK-156) e ambos os lançamentos passam a exibir o badge "Estornado". A OSC não precisa fazer nada manualmente — a reconciliação contábil acontece sozinha.
- **Badge "WooCommerce" na lista de movimentações** (BK-149): lançamentos importados da loja online ganham um badge clicável ao lado do título. Clicar abre o pedido original no admin do WooCommerce em nova aba (útil para conferir o pedido completo, falar com o cliente, etc.).
- **Mapeamento inteligente de categorias** (BK-149): no modo automático, a Bússola lê as categorias dos produtos da loja e cria sub-categorias correspondentes sob a categoria-mãe escolhida (ex: "Loja Online" → "Camisetas", "Livros", "Doações"). Renomeação manual prevalece em sincronizações futuras — a Bússola não sobrescreve o nome que a OSC ajustou. No modo manual, o admin mapeia explicitamente cada categoria do WooCommerce para uma categoria contábil da Bússola.
- **Detalhe rico no lançamento** (BK-149): cada movimento importado traz nas observações a lista dos itens comprados, o método de pagamento, o status no WooCommerce, dados do cliente e um link direto para abrir o pedido no admin da loja.
- **Histórico de sincronizações** (BK-149): nova área dentro da configuração da integração mostra as últimas 20 execuções (data, modo, totais de novos/estornados/erros, status). Útil para diagnosticar problemas e acompanhar a saúde da integração.
- **Notificação de falha** (BK-149): se uma sincronização falhar por credenciais inválidas, loja fora do ar ou outro erro grave, os administradores da OSC recebem notificação imediatamente (pelos canais habilitados na matriz de notificações do perfil).

### Observações de uso
- Sem alteração nos fluxos existentes de Reembolsos, Pedidos de Pagamento, Movimentações manuais ou CSV — a integração WooCommerce é totalmente aditiva.
- Pendente para versões futuras: webhook em tempo real (hoje sync é cron + manual), split por método de pagamento, cálculo automático de taxa do gateway, reconciliação com extrato bancário e múltiplas lojas por OSC.

## [0.12.0] — 2026-05-18

### Adicionado
- **Perfil do usuário em rota própria** (BK-154 + BK-139): a tela de perfil foi separada de Configurações e ganhou rota standalone `/perfil`, acessível a qualquer usuário autenticado pelo item "Meu perfil" no menu do avatar. Quatro boxes consolidados — **Identificação** (foto, nome completo, telefone, data de nascimento, CPF, RG), **Dados para Reembolso**, **Notificações** e **Ações de Conta** — cada um com seu próprio botão de salvar interno (exceto Ações de Conta, com botões por ação).
- **Configurações da organização via ícone de engrenagem na TopNav** (BK-139): o item de texto "Configurações" da TopNav foi substituído por um ícone de engrenagem próximo ao sino de notificações, visível apenas para administradores e tesoureiros (e superadmin). Libera espaço horizontal na barra e torna explícito que Configurações é restrita por papel.
- **Sub-nav de Configurações reorganizada** (BK-154): nova ordem e nomenclatura — Organização → Usuários → **Contas Bancárias** (renomeada de "Contas") → Categorias → **Fluxo de Aprovações** (renomeada de "Pagamentos e Reembolsos"). A URL antiga `/configuracoes/reembolsos` passa a ser `/configuracoes/aprovacoes`. A sub-nav filtra itens pelo papel: tesoureiro vê 3 (Contas Bancárias, Categorias, Fluxo de Aprovações); admin/superadmin veem todos os 5.
- **Matriz granular de preferências de notificação por usuário** (BK-154): novo bloco na seção "Notificações" do perfil com matriz de 10 eventos × 3 canais (e-mail, WhatsApp, Telegram). Eventos cobertos: 5 de reembolso (submetido, aprovação parcial, aprovado, rejeitado, pago) e 5 de pedidos de pagamento (mesmos estados). Default: tudo ligado. Quando o usuário não tem WhatsApp ou Telegram cadastrado, a coluna correspondente aparece desabilitada visualmente com orientação para cadastrar o contato. As notificações disparadas por reembolsos e pedidos de pagamento agora respeitam estritamente essas preferências — silenciam exatamente os pares `(evento, canal)` desligados pelo usuário.
- **Redirects automáticos preservando query params**: bookmarks e links antigos `/configuracoes/perfil?qs` redirecionam para `/perfil?qs`, e `/configuracoes/reembolsos?qs` para `/configuracoes/aprovacoes?qs` — query string e fragmento são preservados.

### Corrigido
- **Race condition no guard de Configurações** (descoberto em QA pós-implementação): acessar qualquer subrota de `/configuracoes/*` por URL direta (refresh, bookmark, link colado no navegador) bloqueava admin e tesoureiro com toast "Acesso restrito" mesmo tendo permissão. O guard agora aguarda o carregamento dos papéis do usuário antes de avaliar — array vazio durante loading não dispara mais redirect indevido.
- **Falha silenciosa ao salvar Notificações com WhatsApp vazio** (descoberto em QA pós-implementação): salvar a seção Notificações sem número de WhatsApp cadastrado falhava silenciosamente no servidor (a matriz salvava, a chamada de contato dava erro 400 invisível ao usuário). A função de preferências passou a tratar valor nulo como remoção da chave; o formulário só envia a chamada de contato quando o valor de fato muda.

## [0.11.0] — 2026-05-18

### Adicionado
- **Pedidos de pagamento recorrentes** (BK-155): agora é possível solicitar pagamentos que se repetem ao longo do tempo (ex: conta de energia, internet, mensalidade). Ao criar uma solicitação, o usuário escolhe entre três tipos — único, recorrente ou parcelado — e configura a frequência (mensal, semanal, quinzenal, bimestral, trimestral, semestral, anual) e a duração (data final, quantidade de ocorrências ou indefinido até cancelar). A aprovação cria a série inteira e o tesoureiro paga ocorrência a ocorrência via Movimentações.
- **Pedidos de pagamento parcelados** (BK-155): solicitação parcelada (ex: compra em 6×) com aprovação única; cada parcela vira um lançamento pendente com data e valor ajustáveis individualmente no momento da criação. Útil para compras de equipamentos ou contratos divididos em prestações.
- **Movimentações recorrentes com duração indefinida** (BK-155): admin e tesoureiro agora podem criar lançamentos recorrentes diretos sem precisar definir data final ou quantidade — opção "Indefinido até cancelar" no fim da série. Gera lote inicial de 12 ocorrências; renovação manual fica como tech debt explícito.
- **Detalhe do pedido recorrente/parcelado com seção "Ocorrências"** (BK-155): lista todas as ocorrências geradas com data prevista, valor estimado, valor real, status individual, conta e data de pagamento. Cada linha tem ações contextuais (Marcar como paga, Ver movimento, Cancelar esta ocorrência) conforme status e papel do usuário.
- **Cancelamento de série com 3 escopos** (BK-155): admin e tesoureiro podem cancelar uma ocorrência específica, todas as ocorrências futuras a partir de uma data, ou a série inteira. Ocorrências já pagas não podem ser canceladas (apenas estornadas via Movimentações).
- **Link cruzado entre lançamentos e pedidos** (BK-155): o detalhe de uma movimentação que veio de um pedido de pagamento aprovado exibe link "Ver pedido de pagamento" para navegação direta ao detalhe da solicitação original.
- **Lista de Pagamentos type-aware** (BK-155): cada linha exibe indicador discreto do tipo (Recorrente · mensal, Parcelado · 6×) e a coluna de valor mostra a representação adequada (R$ X/mês · est. R$ Y para recorrente; R$ X/parcela · total R$ Y para parcelado).
- **Paleta semântica de badges de status** (parte de BK-155): badges de status passaram a usar cores semânticas distintas — teal sólido para pago/aprovado, laranja para pendente/aguardando, vermelho para atrasado/rejeitado, roxo para estornado, cinza para cancelado/rascunho. Facilita leitura rápida das listagens.

### Corrigido
- **Anexos obrigatórios para envio de pedido** (BK-155): submeter um pedido de pagamento para aprovação sem nenhum comprovante anexado passa a ser bloqueado, com mensagem clara. Salvar como rascunho continua sem essa exigência. Validação reforçada tanto no formulário quanto na função de servidor.
- **Solicitante não vê mais Aprovar/Reprovar no próprio pedido** (BK-155): no detalhe e na lista de pedidos, o autor da solicitação não vê mais os botões de aprovação ou reprovação na própria solicitação — comportamento alinhado com o já existente em Reembolsos.

## [0.10.8] — 2026-05-18

### Adicionado
- **Histórico de auditoria na página de detalhe do lançamento** (BK-161): a página de detalhe em `/movimentacoes` foi reorganizada em duas colunas — conteúdo principal à esquerda e um card "Auditoria" à direita com a timeline de eventos do lançamento (quem criou, marcou como pago, estornou, cancelou, etc.), com nome do responsável e data/hora de cada ação. Em mobile as colunas empilham verticalmente. A seção "Criado em / Criado por" anterior foi removida — a informação agora aparece na timeline. Lançamentos sem eventos registrados exibem mensagem de fallback.

## [0.10.7] — 2026-05-18

### Adicionado
- **Contagem de itens nas abas de `/reembolsos`** (BK-097, conclusão): abas de `/reembolsos` passam a exibir contagem entre parênteses, completando a implementação iniciada na v0.10.6. A query passou a carregar todos os reembolsos da OSC de uma vez; filtragem por aba e contagens são derivadas client-side via `useMemo`. O recorte por papel do usuário continua transparente via RLS.

## [0.10.6] — 2026-05-18

### Adicionado
- **Contagem de itens nas abas de listagem** (BK-097, parcial): as abas de status em `/movimentacoes`, `/pagamentos` e `/superadmin/organizacoes` passam a exibir o total de itens entre parênteses ao lado do rótulo — ex: "Pendente (5)", "Pago (30)". As contagens são derivadas dos dados já carregados no cliente, sem queries adicionais. Em `/movimentacoes` a contagem considera os filtros de período e busca ativos.

### Corrigido
- **Tipo de organização exibido como snake_case em `/superadmin/organizacoes`** (BK-097): a coluna Tipo agora exibe labels legíveis (`grupo_escoteiro` → "Grupo Escoteiro", `associacao` → "Associação", etc.) com fallback para titlecase em valores desconhecidos.

## [0.10.5] — 2026-05-18

### Adicionado
- **Flag de auditoria para auto-aprovações** (BK-105): quando o solicitante aprova o próprio pedido por ser o único aprovador elegível — situação permitida pelo sistema — as EFs `approve_reimbursement` e `approve_purchase_order` passam a gravar uma linha adicional no `audit_log` com `metadata.self_approved = true`. Aprovações normais seguem sem essa marca. Facilita a revisão pela comissão fiscal sem necessidade de cruzar manualmente os dados de solicitante e aprovador.

## [0.10.4] — 2026-05-18

### Corrigido
- **Auto-aprovação em pedidos de pagamento** (BK-127): confirmado que a EF `approve_purchase_order` já valida a elegibilidade antes de qualquer gravação no banco — a auto-aprovação é bloqueada quando existem outros aprovadores elegíveis, e permitida quando o solicitante é o único. Comportamento idêntico ao módulo de reembolsos. Nenhuma alteração de código necessária; bump de versão para registrar a validação.
- **Link "Meu perfil" no menu do avatar** (BK-162): o menu dropdown do avatar no menu superior agora exibe "Meu perfil" (navega para Configurações → Perfil) além de "Sair".
- **Título da aba de workflow de aprovação** (BK-147): rótulo corrigido de "Workflow de aprovação de reembolsos" para "Fluxo de aprovação de pagamentos e reembolsos", refletindo que a aba controla o fluxo de ambos os módulos.
- **Fotos de usuários na lista de Configurações → Usuários** (BK-163): avatares na listagem de membros passam a exibir a foto cadastrada; iniciais continuam como fallback quando não há foto. Mesma correção já aplicada ao avatar do menu superior na v0.10.1.

## [0.10.3] — 2026-05-18

### Adicionado
- **Atalhos de período no filtro de Movimentações** (BK-145): além de escolher datas customizadas, o filtro agora oferece atalhos contábeis em um clique — Mês atual, Mês anterior, Trimestre atual, Trimestre anterior, Semestre atual, Ano atual (YTD), Ano anterior, Personalizado e Todos. Cálculo baseado em trimestres e semestres calendário (T1: jan-mar, T2: abr-jun, etc.). Selecionar um atalho preenche as datas automaticamente; editar manualmente as datas troca o filtro para "Personalizado".

### Modificado
- **Filtro de Movimentações abre por padrão em "Mês atual"** em vez de "Todos" — visão operacional do dia a dia é mais comum no fluxo do tesoureiro.

## [0.10.2] — 2026-05-18

### Corrigido
- **Badge "Estornado" volta a aparecer também no lançamento contrário** (BK-160, regressão da v0.10.1): a release anterior introduziu o badge no lançamento original mas a regra de detecção não cobria o lançamento contrário gerado pelo estorno; agora ambos exibem o badge corretamente.

## [0.10.1] — 2026-05-18

Primeira release versionada após a transição de `v0.10 (beta)` para semver puro. Consolida correções de UX no módulo de Movimentações, melhorias no menu superior, publicação dos documentos legais e do manual em domínio próprio, e a primeira preparação do fluxo Google em `/setup` para auto-conclusão (validação E2E pendente). A partir desta versão, marcadores como "(beta)" não fazem mais parte da string da versão.

### Adicionado
- **Avatar do usuário no menu superior** (BK-141): a foto cadastrada em Configurações → Perfil agora aparece no avatar do menu superior em qualquer cenário em que a tela de perfil também exibe a foto; ao trocar a foto, o menu superior atualiza imediatamente sem precisar de F5. Iniciais continuam como fallback quando não há foto.
- **Badge "Recorrente" em lançamentos recorrentes** (BK-158): movimentos pertencentes a uma série recorrente não-parcelada passam a exibir um badge "Recorrente" ao lado do título, em `/movimentacoes` (lista e detalhe). Visibilidade rápida do contexto sem precisar abrir o detalhe.
- **Manual do Usuário publicado** (BK-137): novo manual público em `https://docs.bf.rit.org.br/` cobrindo primeiros passos, movimentações, reembolsos, pagamentos, configurações da OSC, papéis e FAQ. Link no rodapé da aplicação.
- **Política de Privacidade e Termos de Uso publicados** (BK-094): documentos legais publicados em `https://docs.bf.rit.org.br/privacidade/` e `/termos/`. Links discretos no rodapé da aplicação.
- **Documentação em domínio próprio** (BK-153): substituído o domínio padrão do GitHub Pages por `docs.bf.rit.org.br` (Cloudflare DNS + custom domain + HTTPS ativo). Links de Política, Termos e Manual no rodapé já apontam para o novo domínio.

### Corrigido
- **Troca de OSC pelo seletor agora atualiza a tela automaticamente** (BK-151): selecionar outra OSC no menu superior recarrega imediatamente todas as páginas (painel, movimentações, reembolsos, pagamentos, configurações) sem precisar de F5. Antes, a página atual mantinha os dados da OSC anterior até refresh manual.
- **Badge "Parcela X de N" voltou a aparecer** (BK-157): em lançamentos parcelados, o badge "Parcela X de N" deixou de ser exibido em algum refactor recente; foi restaurado. Causa raiz: a fonte de dados parou de expor a informação da série parcelada.
- **Badge "Estornado" agora aparece em ambos os lançamentos** (BK-156): ao estornar um pagamento, tanto o lançamento original quanto o contrário (gerado pelo estorno) passam a exibir o badge "Estornado". Antes só o contrário recebia o badge, dando a falsa impressão de que o original ainda estava "pago" sem indicação. O status no banco do lançamento original permanece "pago" — só a visualização ganha o badge adicional.
- **"Continuar com Google" em `/setup` redireciona corretamente para o painel** (BK-144): no fluxo de configuração inicial via convite, o usuário que escolhia "Continuar com Google" voltava para o formulário de senha em vez de seguir para o painel; agora o cadastro é concluído automaticamente com o nome e a foto do perfil Google e o usuário entra direto no painel. **Validação E2E com convite real pendente em BK-152 antes de declarar verificado.**
- **Link "Manual do Usuário" no rodapé** apontava para `/manual` (404); corrigido para apontar para a raiz do site de docs.

### Modificado
- **Formato da string da versão**: passou de `v0.10 (beta)` para `v0.10.1`. Padronizado em semver puro (MAJOR.MINOR.PATCH); marcadores como "(beta)" não fazem mais parte da string da versão exibida no rodapé e nos feedbacks. A natureza piloto/beta do projeto passa a ser sinalizada (quando necessário) fora da string da versão.

---

### Adicionado (Documentação pública — 2026-05-15)
- **Site de documentação multi-página** em `https://rit-df.github.io/bussola-docs/`: substituído o manual em página única por site Jekyll com navegação por abas (Início, Primeiros Passos, Módulos, Configurações, Papéis, FAQ, Changelog, Legal); cada módulo e aba de configurações tem página dedicada
- **Sub-navegação por seção**: pills de navegação abaixo do título em todas as páginas de Módulos, Configurações e Legal, permitindo navegar entre páginas da seção sem sair da tela
- **Screenshots de configurações** sem dados pessoais: Organização, Contas, Categorias, Fluxo de Aprovação — imagens capturadas com dados fictícios; abas Perfil e Usuários sem screenshot (dados reais visíveis)

### Corrigido (Documentação pública — 2026-05-15)
- **Links absolutos quebrados no GitHub Pages**: 10 links com caminhos absolutos (`/configuracoes/perfil/` etc.) geravam 404; convertidos para caminhos relativos em 8 arquivos
- **Screenshot de perfil com dados pessoais reais**: `manual-09-config-perfil.png` continha telefone, e-mail e CPF reais; arquivo removido e referência eliminada da página de perfil

### Adicionado (Onda 4 — Pedidos de Pagamento)
- **Módulo de Pedidos de Pagamento**: novo módulo completo para solicitação formal de pagamentos a fornecedores e prestadores externos, com fluxo de aprovação configurável e lançamento automático em `financial_movements`; tabelas `purchase_orders`, `purchase_order_approvals`, `purchase_order_attachments`; EFs `submit_purchase_order`, `reject_purchase_order`, `approve_purchase_order`, `pay_purchase_order`; `movement_origin` estendido com valor `purchase_order`
- **Página `/pagamentos` unificada**: abas "Pedidos de pagamento" e "Reembolsos" (aba de reembolsos reutiliza componente existente sem alteração); sub-abas por status (Todos / Rascunho / Aguardando aprovação / Aprovado / Rejeitado / Pago); cards-resumo condicionais ao papel (aprovador, tesoureiro, todos); coluna Ações com botões Aprovar / Reprovar condicionais ao papel e status; ícone "Marcar como pago" não aparece na lista — pagamento é confirmado via `/movimentacoes` (igual a Reembolsos)
- **"Boleto" como forma de pagamento** (pós-lançamento Onda 4): formulário de criação e edição inline do pedido oferecem três opções — PIX, TED, Boleto; selecionar Boleto não exibe campos extras (o arquivo é anexado na seção Documentos); `vendor_payment_info` grava `{ method: 'boleto' }` sem campos adicionais
- **Redirect `/reembolsos`**: rota redireciona automaticamente para `/pagamentos?tab=reembolsos`; links existentes e rotas `/reembolsos/novo` e `/reembolsos/:id` permanecem funcionais
- **Formulário `/pagamentos/novo`**: criação e edição de rascunho com CRUD direto via Supabase client; carregamento de rascunho via `?id=` na URL; campos PIX/TED do fornecedor (sem pré-população do perfil do usuário); uploader com prefixo `purchase-orders/`; botões "Salvar rascunho" e "Enviar para aprovação" com validação por campo
- **Página `/pagamentos/:id`**: detalhe completo com 4 zonas (header, dados, documentos, timeline + ações); preview inline de imagens (thumbnails clicáveis, fallback) e PDF (iframe lazy); ações condicionais — "Editar e reenviar" (solicitante), "Aprovar" / "Reprovar" (aprovador elegível); dados PIX/TED do fornecedor ocultos para voluntários; seção de anexos denominada "Documentos"
- **TopNav**: item "Reembolsos" renomeado para "Pagamentos e Reembolsos"; badge soma pedidos de pagamento aguardando + reembolsos aguardando (ambos os módulos); RPC `count_pending_purchase_orders_for_user` criada
- **Configurações**: aba "Reembolsos" renomeada para "Pagamentos e Reembolsos"; nova subseção "Quem pode solicitar pagamentos" com checkboxes por papel (persiste em `reimbursement_workflow.allowed_requester_roles`; default: Presidente, Tesoureiro, Coordenador de Projeto)
- **Painel**: nova seção "Pedidos de pagamento" com cards condicionais ao papel (aguardando aprovação, aprovados aguardando pagamento, solicitado por mim)

### Adicionado
- **"Continuar com Google" em `/setup`**: usuários convidados podem concluir o primeiro acesso autenticando via Google OAuth em vez de definir senha; botão visível e habilitado somente após aceite da política de privacidade; `setup_token` e versão da política preservados em `sessionStorage` através do redirect OAuth; `complete_setup` valida `claims.sub === uo.user_id` para garantir que a conta Google corresponde ao convite; campo "Nome completo" pré-populado com o nome do perfil Google (editável); campos de senha ocultados no fluxo Google
- **Upsert de `full_name` em `user_profile` ao concluir setup**: `complete_setup` agora grava `user_profile.full_name` em ambos os fluxos (senha e Google) após transição bem-sucedida; fechou lacuna pré-existente onde o nome era salvo apenas em `auth.user_metadata`
- **Canal de feedback de usuários — chip no TopNav**: botão/badge laranja "💬 Feedback" no TopNav, visível para todos os papéis autenticados; abre o `FeedbackModal` ao ser clicado
- **`FeedbackModal`**: modal com grade 2×2 de tiles de categoria (🐛 Bug / 💡 Sugestão / 👍 Elogio / ❓ Outro), textarea de mensagem livre, rodapé com identidade do usuário ("Enviado como [nome] · [e-mail]") e insert direto em `user_feedback` via Supabase client (RLS); toast de confirmação ao enviar; campos limpos ao reabrir
- **Tabela `user_feedback`**: armazena feedbacks com `user_id`, `organization_id`, `category`, `message`, `resolved` (default `false`), `resolved_at`; RLS: INSERT para qualquer autenticado com `user_id = auth.uid()`; SELECT e UPDATE restritos ao superadmin
- **Página `/superadmin/feedbacks`**: tabela com colunas Data, Categoria (badge colorido), Mensagem, Usuário (nome + e-mail), OSC, Resolvido; ordenação automática (não-resolvidos mais novos primeiro, resolvidos ao final); checkbox "Resolvido" executa UPDATE + re-fetch; linha resolvida fica tachada e com opacidade reduzida; contador de itens pendentes no topo
- **Seção "Alterar senha" em `/configuracoes/perfil`**: campos "Nova senha" e "Confirmar nova senha", botão "Alterar senha"; chama `supabase.auth.updateUser({ password })`; erro `weak_password` (HIBP) exibido inline abaixo do campo; sucesso limpa os campos e exibe toast de confirmação
- **Orientação de criação de senha** em `/setup` e em `/configuracoes/perfil`: texto estático "Use ao menos 8 caracteres combinando letras maiúsculas, minúsculas, números e símbolos. Evite senhas comuns." abaixo do campo de senha; substituído por erro inline quando há falha de validação
- **Seção "Dados para reembolso" em `/configuracoes/perfil`**: seletor PIX ou TED, campos condicionais (tipo de chave + valor para PIX; banco/agência/conta para TED), todos opcionais, botão de salvar próprio desabilitado quando não há alteração; lê e grava em `user_profile.default_payment_info` (JSONB) via `useUpdateProfile`; formato compatível com `paymentFromProfile` no formulário de reembolso — prefill automático funciona sem alteração adicional

### Corrigido (pós-lançamento Onda 4 — 2026-05-15)
- **EF `approve_purchase_order` retornava HTTP 500 em toda tentativa de aprovação** (BK-132): a CHECK constraint `fm_account_required_unless_pending_reimbursement` em `financial_movements` só permitia `account_id = NULL` para `origin = 'reimbursement'`; pedidos de pagamento aprovados (origin `purchase_order`) sem conta definida violavam a constraint ao criar o movimento financeiro; corrigido via migration que estendeu a constraint para também aceitar `purchase_order` pendente sem `account_id` — mesmo comportamento já permitido para reembolsos; a EF já passava todos os campos corretamente (prompt #134)
- **Card "AGUARDANDO MINHA APROVAÇÃO" exibia `[object Object][object Object]`** (BK-129): renderização incorreta do retorno da RPC `count_pending_purchase_orders_for_user` no componente de card; corrigido para extrair corretamente o campo numérico (prompt #131)
- **Layout do formulário de pedido de pagamento divergia do formulário de reembolso** (BK-133): DESCRIÇÃO aparecia como textarea grande no topo, antes de DATA DA DESPESA e VALOR; reordenado para DATA DA DESPESA + VALOR no topo, DESTINATÁRIO, DESCRIÇÃO (campo de linha única), CATEGORIA/PROJETO/CENTRO DE CUSTO, DADOS DE PAGAMENTO, OBSERVAÇÕES, DOCUMENTOS — igual ao padrão de `/reembolsos/novo` (prompt #135)

### Modificado (pós-lançamento Onda 4 — 2026-05-15)
- **Rótulo da seção de anexos em pedidos de pagamento**: "COMPROVANTES / NF" substituído por "Documentos" em todos os contextos do módulo (formulário de criação, formulário de edição inline, página de detalhe) — mesma terminologia de Reembolsos (prompt #133)
- **Fluxo de confirmação de pagamento de pedidos**: botão "Confirmar pagamento" removido da coluna AÇÕES da lista `/pagamentos`; o tesoureiro confirma o pagamento diretamente na movimentação financeira gerada em `/movimentacoes` (ícone "Marcar como pago"), igual ao fluxo de Reembolsos; a EF `pay_purchase_order` permanece deployada mas sem ponto de entrada no frontend atual (prompt #133)

### Corrigido
- **Botões "Aprovar"/"Reprovar" não apareciam para aprovadores elegíveis na lista de reembolsos** (BK-123): query do workflow de aprovação (`wfQ`, `organization_settings?key=eq.reimbursement_workflow`) não disparava na `ReembolsosListPage` por problema de timing do React Query — `enabled: !!activeOrganizationId` nunca transitava para `true` a tempo; corrigido para aguardar o `activeOrganizationId` antes de executar o fetch; `isEligibleApprover` agora calcula sobre os dados reais da OSC em vez do `EMPTY_WORKFLOW` padrão; regra de auto-aprovação (não ver botões no próprio reembolso) preservada (prompt #119)
- **Badge de reembolsos pendentes na TopNav não atualizava após aprovação/rejeição** (BK-125): mutations de aprovação e rejeição não invalidavam a query que alimenta o badge; corrigido para invalidar também essa query ao concluir cada mutation com sucesso (prompt #122)
- **Dialog "Reprovar solicitação" — botão habilitado sem motivo** (BK-124): o botão "Confirmar reprovação" estava habilitado mesmo com o campo "Motivo" vazio; corrigido para desabilitar enquanto o campo estiver vazio ou só com espaços (prompt #121)
- **Datas exibidas com 1 dia a menos** (BK-121): `formatDate()` em `shared/lib/format.ts` convertia strings ISO date-only (`"YYYY-MM-DD"`) via `new Date(value)`, que o JavaScript interpreta como UTC midnight; em UTC-3, isso recuava a exibição para o dia anterior. Corrigido detectando o padrão `YYYY-MM-DD` e construindo o `Date` com componentes locais (sem conversão de timezone). Afetava: coluna "Data da despesa" em `/reembolsos`, detalhe do reembolso (`/reembolsos/:id`) e campos Vencimento/Pagamento/Competência em `/movimentacoes/:id`. A lista de movimentações não era afetada (usava `parseISO` do date-fns) (prompt #120)
- **E-mail de convite não chegava ao usuário convidado**: `add_user_to_organization` chamava `send_email` com `Authorization: Bearer SERVICE_ROLE_KEY`; após migração do Supabase para chaves `sb_secret_*` (não-JWT), o gateway rejeitava com 401 antes do código rodar — invitation era criada mas `email_send_log` ficava vazio; corrigido com autenticação Bearer correta + try/catch que grava `failed_all` em `email_send_log` em caso de qualquer falha de chamada
- **`send_email` rejeita chamadas sem JWT**: `verify_jwt = false` declarado explicitamente em `config.toml` para `send_email` e `complete_setup`; autenticação manual aceita Bearer == `SUPABASE_SERVICE_ROLE_KEY` (server-to-server) ou JWT com `app_metadata.is_superadmin = true` (página de teste)
- **Cancelar convite retornava "Não foi possível aplicar a alteração"**: transição `active_pending_setup → removed` estava ausente dos pares válidos na função SQL `_valid_uo_transition`; adicionada via migration; handler do `MemberActionsMenu` agora também marca `invitations.status = revoked` após a transição
- **Botão "Reenviar e-mail de convite" não era clicável**: condição de `disabled` ausente ou incorreta no `MemberActionsMenu` para membros em `active_pending_setup`; corrigido com `disabled={busy}` explícito durante a chamada; `resend_setup_token` usa o mesmo helper `invokeSendEmail` de `add_user_to_organization` com try/catch + `logEmailAttempt('failed_all')` para rastreabilidade em `email_send_log`
- **`complete_setup` retornava "Erro inesperado" para senha rejeitada pelo HIBP**: EF mascarava o `error_code` real do Supabase Auth como 500 genérico; agora propaga o `error_code` original (incluindo `weak_password` com status 422 e mensagem em pt-BR); demais erros do GoTrue também passam adiante o `error_code` real
- **Nome preenchido no setup não era salvo**: `complete_setup` não executava `UPDATE user_profile SET full_name` após a transição; corrigido para gravar o nome enviado no payload
- **Nome não persistia em `/configuracoes/perfil`** (toast de sucesso mas campo voltava vazio ao recarregar): `UPDATE` em `user_profile` retornava 0 linhas — linha ausente ou RLS bloqueando silenciosamente; corrigido com upsert e/ou ajuste de policy
- **Tela em branco em `/configuracoes/reembolsos`** após 1-2 segundos de exibição: violação das Rules of Hooks — `useMemo` e `memberById` estavam declarados após early returns no `ConfiguracoesReembolsosPage`, causando contagem diferente de hooks entre renders e desmonte da árvore pelo React; corrigido movendo todos os hooks para antes de qualquer `return` condicional
- **Tela em branco em `/reembolsos/:id`** ao navegar via SPA (funcionava com F5): efeito cascata do bug anterior — o estado degradado do React contaminava navegações subsequentes na mesma sessão; resolvido com a correção do bug de Rules of Hooks acima

---

### Adicionado (Onda 2 — melhorias pós-lançamento)
- **Botão "Salvar e fazer outro"** no formulário de novo lançamento (`/movimentacoes/novo`): salva e reinicia o formulário mantendo tipo e conta — sem redirecionar para a lista; útil para lançamentos em sequência (prompt 69)
- **Indicação de filtros ativos** abaixo dos cards de totais: quando qualquer filtro está ativo (`isDefault = false`), exibe linha discreta "Filtrado por: [rótulos]" concatenados com " · "; desaparece ao limpar filtros (prompt 70)
- **Ordenação por coluna** na tabela de movimentações: Vencimento, Valor, Status e Conta ordenáveis com ciclo ASC → DESC → sem ordenação; indicador de direção no header ativo; ordenação client-side preservada ao trocar aba ou filtro (prompt 71)
- **EF `delete_movements`**: substitui `bulk_update_movements` com `p_action: 'delete'` para exclusão de lançamentos; coleta `storage_path` de `financial_movement_attachments`, remove arquivos do bucket `movement-attachments` (falha individual não aborta), deleta lançamentos por CASCADE; retorna `{ ok, deleted, storage_cleaned }`; validação de ownership e limite de 500 IDs por chamada (prompt 72)
- **Coluna "Pagamento"** na tabela de movimentações, entre "Vencimento" e "Lançamento": exibe `payment_date` formatada; "—" quando não pago; ordenável com nulos por último no ASC (prompt 73)
- **Ordenação por Categoria** na tabela de movimentações: ordena pelo nome da primeira categoria; splits com múltiplas categorias usam a primeira como critério (prompt 73)
- **Ícones de ação por linha** na tabela de movimentações: coluna "Ações" ao final da tabela (após Valor), sempre visível sem hover; ícone de lápis (editar) em todas as linhas; ícone contextual por status — cancelar (`pendente`/`atrasado`), estorno (`pago`/`efetivado`), lixeira (`cancelado`/`estornado`); clicar abre o mesmo fluxo de confirmação existente (prompt 74)

### Corrigido
- `canDelete()` em `movementActions.ts` expandido para incluir `cancelado` e `estornado` — lançamentos finalizados podem ser excluídos (prompt 75)
- Texto do dialog de confirmação de exclusão em lote corrigido: não menciona mais restrição de status (herdado da RPC antiga) (prompt 75)
- Botão "Excluir" na tela de detalhe (`/movimentacoes/:id`) movido para fora do bloco condicional `!finalized`, tornando-o visível e habilitado para lançamentos `cancelado` e `estornado` (prompt 77)
- Tooltip do botão "Excluir" para lançamentos `pago` atualizado para mensagem coerente com a nova lógica de elegibilidade (prompt 77)

### Modificado
- **Exportação Excel**: pacote `xlsx` (SheetJS, abandonado, vulnerabilidades Prototype Pollution + ReDoS) substituído por `exceljs` (mantido ativamente); comportamento idêntico — mesmo arquivo, colunas e formatação (prompt 76)
- **Ícone de olho (visualizar)** removido das linhas da tabela de movimentações — redundante com o clique na linha; mantido apenas o lápis (editar) (prompt 74)
- **Exclusão de lançamentos** (individual e em lote) migrada da RPC `bulk_update_movements` para a EF `delete_movements`; `bulk_update_movements` continua sendo usada exclusivamente para `mark_paid` (prompt 72)

---

## [v0.9.11] — 2026-05-14 · `onda3-st9.11-configuracoes-reembolsos`

### Adicionado
- **Aba "Reembolsos" em `/configuracoes`** (admin-only): seletor de aprovações necessárias (1 ou 2), checkboxes de papéis elegíveis (Dirigente, Tesoureiro), busca de pessoas específicas como aprovadores independente de papel, lista consolidada "Quem pode aprovar" com origem indicada (papel/pessoa), alerta âmbar quando nenhum aprovador configurado
- Botão Salvar habilitado apenas quando há alteração (`isDirty`) e ao menos um aprovador; mensagem inline "Selecione ao menos um papel ou uma pessoa aprovadora" quando inválido
- Persistência via `set_organization_settings_bulk` com chave `reimbursement_workflow`; leitura via `read_organization_settings` com query própria e filtro client-side

---

## [v0.9.10] — 2026-05-14 · `onda3-st9.10-painel-badge`

### Adicionado
- **Seção "Reembolsos" no `/painel`**: até 3 cards condicionais por papel — "Meus reembolsos pendentes" (rascunhos + rejeitados), "Aguardando minha aprovação" (aprovadores elegíveis) e "Aguardando pagamento" (tesoureiros); cada card clicável navega para `/reembolsos?tab=<status>`
- **Badge real no TopNav**: exibe contagem com prioridade aprovador→tesoureiro→voluntário; oculto quando a contagem relevante = 0
- **RPC `count_pending_reimbursements_for_user(p_org_id)`** (SECURITY DEFINER): retorna `{ volunteer_pending, approver_pending, treasurer_pending }` para o caller autenticado; lê `reimbursement_workflow` para determinar elegibilidade do aprovador
- **Hook `useReimbursementsCounts`** compartilhado entre `/painel` e TopNav (`staleTime: 30s`); elimina chamada dupla à RPC

---

## [v0.9.9] — 2026-05-14 · `onda3-st9.9-edicao-inline-rejeicao`

### Adicionado
- **Edição inline após rejeição** em `/reembolsos/:id`: botão "Editar e reenviar" habilitado para requester quando status = `rejeitado`; expande `EditAndResubmitForm` inline com motivo da rejeição em destaque, campos pré-populados do reembolso e gestão de comprovantes sem ensureDraft
- Sequência de salvamento: `update_reimbursement` → `submit_reimbursement`; em sucesso, página recarrega em `aguardando_aprovacao`
- Botão "Cancelar" recolhe sem salvar; `EditAndResubmitForm` isolado em `Card` próprio abaixo do grid

---

## [v0.9.8] — 2026-05-14 · `onda3-st9.8-preview-comprovantes`

### Adicionado
- **Preview inline de comprovantes** em `/reembolsos/:id`: thumbnails automáticos para imagens (clicáveis para ampliar, fallback textual), botão lazy "Visualizar/Ocultar PDF" com iframe; outros tipos mantêm apenas download
- **Botão "Editar rascunho"** (correção de gap — prompt 85b): em `/reembolsos/:id` com status = `rascunho`, requester navega para `/reembolsos/novo?id=<uuid>`; formulário carrega dados existentes, reutiliza o mesmo ID para uploads e salvamentos

---

## [v0.9.7] — 2026-05-14 · `onda3-st9.7-pay-reimbursement`

### Adicionado
- **EF `pay_reimbursement`**: tesoureiro confirma pagamento; cria `financial_movement` com `origin = 'reimbursement'`; salva `paid_movement_id` no reembolso (link reverso); rollback best-effort do movimento em caso de falha posterior; notifica solicitante via `send_notification`
- **Ação "Confirmar pagamento"** em `/reembolsos/:id`: select de conta financeira + data de pagamento; coordenado com Aprovar/Rejeitar; invalida caches de `financial-movements` e `account-balances`

---

## [v0.9.6] — 2026-05-14 · `onda3-st9.6-approve-reimbursement`

### Adicionado
- **EF `approve_reimbursement`**: voto duplo retorna 409; suporta quorum parcial (notifica aprovadores restantes) e quorum final (notifica solicitante + tesoureiros); voto prévio do mesmo aprovador bloqueia com 409 distinto
- **Ação "Aprovar"** em `/reembolsos/:id`: comentário opcional, detecção de voto prévio desabilita botão, toasts diferenciados para aprovação parcial e final

---

## [v0.9.5] — 2026-05-14 · `onda3-st9.5-detalhe-rejeicao`

### Adicionado
- **Página `/reembolsos/:id`**: 4 zonas — header (status, solicitante, valor), dados (campos + dados de pagamento condicionais por papel), comprovantes e timeline + ações
- **EF `reject_reimbursement`**: registra motivo em `reimbursement_approvals`, transiciona para `rejeitado`, notifica solicitante; motivo obrigatório
- **`lib/eligibility.ts`**: helper reutilizável com `isApprover(roles, userId, workflow)` e `canSeePayment` — única fonte da verdade para elegibilidade na UI (reutilizado em ST-9.6, ST-9.7, ST-9.10 e ST-9.11)
- Dados de pagamento PIX/TED ocultos para voluntários; visíveis apenas para aprovadores elegíveis e tesoureiro

---

## [v0.9.4] — 2026-05-14 · `onda3-st9.4-formulario-submit`

### Adicionado
- **Formulário `/reembolsos/novo`**: data, valor, descrição, categoria, projeto, centro de custo, observações, método de pagamento PIX/TED com campos condicionais; dados pré-populados do perfil com checkbox "Salvar como padrão"; uploader com auto-create de registro rascunho
- **RPCs `create_reimbursement` / `update_reimbursement`** (SECURITY INVOKER): criação e edição de reembolsos com validação de organização
- **EF `submit_reimbursement`**: valida diff vs. snapshot da rejeição anterior, limpa `reimbursement_approvals` da rodada, transiciona para `aguardando_aprovacao`, notifica aprovadores elegíveis
- 3 storage policies para prefixo `reimbursements/{org_id}/{reimbursement_id}/` no bucket `movement-attachments`

### Corrigido
- Rotas `/reembolsos`, `/reembolsos/novo` e `/reembolsos/:id` ausentes do `App.tsx` após ST-9.3 — registradas via prompt de continuação 81c

---

## [v0.9.3] — 2026-05-14 · `onda3-st9.3-rotas-lista`

### Adicionado
- **Listagem `/reembolsos`**: 6 tabs por status (todos, rascunho, aguardando_aprovacao, aprovado, rejeitado, pago) persistidas via `?tab=`; coluna "Solicitante" condicional ao papel; item "Reembolsos" com badge no TopNav (placeholder — badge real na ST-9.10)
- Rotas `/reembolsos`, `/reembolsos/novo` e `/reembolsos/:id` registradas em `App.tsx`

---

## [v0.9.2] — 2026-05-14 · `onda3-st9.2-send-notification`

### Adicionado
- **EF `send_notification`** (infraestrutura global reutilizável por todos os módulos): e-mail ativo via `nodemailer@6.9.14`/STARTTLS reutilizando `_shared/smtp.ts`; push/Telegram/WhatsApp como stubs; despacho paralelo por destinatário e canal; `audit_log` por par (destinatário, canal); HTTP 200 exceto 400 de validação de input
- Interface: `{ organization_id, event_type, recipients: [{ user_id, channels? }], payload: { title, body, link?, data? } }`
- Default quando `notification_preferences` ausente: todos os canais habilitados; skip silencioso quando preferência é false ou dado de contato ausente no perfil

---

## [v0.9.1] — 2026-05-14 · `onda3-st9.1-schema-base`

### Adicionado
- **Schema base de reembolsos**: enum `reimbursement_status` (rascunho → aguardando_aprovacao → aprovado → rejeitado → pago); tabelas `reimbursements`, `reimbursement_approvals`, `reimbursement_attachments` com triggers `updated_at` e auditoria (reuso das funções existentes); RLS role-aware (voluntário vê apenas os próprios; dirigente/tesoureiro/admin/comissão veem todos da OSC)
- **Chave `reimbursement_workflow`** em `organization_settings` (padrão EAV): `{ required_approvals, allowed_approver_roles, allowed_approver_user_ids }`; padrão `{ required_approvals: 1, allowed_approver_roles: ["dirigente"], allowed_approver_user_ids: [] }`
- Campo `default_payment_info` (JSONB) em `user_profile` para dados de pagamento padrão do usuário: `{ payment_method, pix_key_type, pix_key, bank_name, bank_agency, bank_account }`; UI adicionada em `/configuracoes/perfil` na correção pós-Onda 3

---

## [v0.8.18] — 2026-05-13 · `onda2-st8.18-cancelamento`

### Adicionado
- **Cancelamento de lançamentos**: status `cancelado` suportado pelo trigger `_fm_set_defaults_and_status`; colunas `cancelled_at`, `cancelled_by`, `cancelled_reason` em `financial_movements`; índice parcial em `organization_id WHERE cancelled_at IS NOT NULL`
- **EF `cancel_movement`**: suporta três escopos — `this` (lançamento isolado), `this_and_future` (a partir da posição na série), `all` (toda a série recorrente); filtra apenas elegíveis (`pendente` ou `atrasado`) e retorna `{ cancelled_count, skipped_count }` sem erro para os ignorados; motivo obrigatório
- **Modal de cancelamento** em `/movimentacoes/:id`: campo de justificativa obrigatório, seleção de escopo para séries/parcelamentos, exibição de erro inline quando EF recusa
- **Card de auditoria de cancelamento** na tela de detalhe: exibe data, motivo e nome do responsável (resolvido via `get_user_display_names`)
- **Aba "Cancelados"** na lista de movimentações: tab dedicada com filtro de status `cancelado`; lançamentos cancelados excluídos dos totais das demais abas
- **RPC `get_user_display_names(UUID[])`**: SECURITY DEFINER com verificação de co-membership por organização; retorna `{ id, display_name }` preferindo `full_name` do perfil, depois `email`, depois `—`; usada para resolver `cancelled_by` e `reversed_by` na tela de detalhe
- **Hook `useUserDisplayNames`**: chamada única com array de IDs deduplicados, `staleTime` de 5 min, evita N+1

### Adicionado (habilitação contextual de ações — ST-8.18.1)
- **Helper `movementActions.ts`**: única fonte da verdade para elegibilidade de ações por status — `canDelete`, `canCancel`, `canReverse`, `canMarkPaid`; `disabledReason(action, status)` para tooltips individuais; `bulkEligibility(rows, action)` para ações em lote
- **Matriz de elegibilidade aplicada** em `MovimentoDetailPage` e `BulkActionsBar`: botões Excluir, Cancelar, Estornar e Marcar como pago ficam visíveis mas desabilitados quando a ação não é permitida para o status atual; tooltip explicativo ao passar o cursor; lançamentos `cancelado`/`estornado` não exibem nenhuma ação
- **Regra de lote**: cada botão de ação em lote só habilita se TODOS os selecionados forem elegíveis; tooltip contextual quando desabilitado por seleção mista
- **Botão "Estornar" em lote**: adicionado à `BulkActionsBar`; abre modal com motivo obrigatório; chama `reverse_movement` por ID via `Promise.all`

### Corrigido
- `computeTotals` excluía status `estornado` do cálculo mas não `cancelado` — corrigido para ambos
- `filtersToPayload` não tratava a tab `canceladas` — adicionado override de status análogo ao de `estornadas`

---

## [v0.8.17] — 2026-05-13 · `onda2-st8.17-exportacao`

### Adicionado
- **Botão "Exportar"** na barra de ações da lista com dropdown "Exportar PDF" e "Exportar Excel"; aplica os filtros ativos no momento da exportação
- **Exportação PDF**: EF `export_movements_pdf` chama Gotenberg com HTML renderizado no servidor; inclui cabeçalho (nome da OSC + período + filtros), tabela completa e rodapé com totais; download automático no browser
- **Exportação Excel**: geração client-side via `lib/exportExcel.ts`; colunas Vencimento, Pagamento, Título, Tipo, Status, Conta, Categoria(s), Valor (R$, numérico), Fornecedor, Observações; `derivePeriodLabel` para nome do arquivo (inicialmente SheetJS; migrado para `exceljs` em prompt 76)
- **`lib/periodLabel.ts`**: função `derivePeriodLabel` que infere rótulo legível a partir dos filtros de período ativos (ex: "maio-2026")

### Corrigido
- EF `export_movements_pdf` chamava `list_financial_movements` via service_role, que retorna `auth.uid() = NULL` internamente — corrigido para usar padrão `callerClient` das demais EFs que dependem de `auth.uid()`

---

## [v0.8.16] — 2026-05-13 · `onda2-st8.16-parcelamentos`

### Adicionado
- **Modo "Parcelado" no toggle 3-vias** do formulário de novo lançamento: número de parcelas (2–120), frequência, data da 1ª parcela
- **Tabela de parcelas** editável: datas calculadas pela frequência; valor por parcela editável com validação de soma em tempo real; diferença de centavos alocada na última parcela; linha de soma com indicador vermelho/verde; botão Salvar desabilitado enquanto soma divergir
- **Modal de confirmação**: resumo com count e intervalo de datas antes de criar
- **EF `create_installment_series`**: cria `recurring_series` com `is_installment = TRUE`; cria N `financial_movements` com `origin = 'installment'`, `series_position` e `total_amount` individual; valida que `SUM(installment_amounts) === total_amount` quando editado manualmente (tolerância de centavos); rollback total em caso de erro
- **Edição de parcelamentos via `update_recurring_series`**: escopo `all`/`this_and_future` preserva `total_amount` individual por parcela (sem achatar em valor único)

---

## [v0.8.15] — 2026-05-13 · `onda2-st8.15-acoes-em-lote`

### Adicionado
- **Seleção múltipla na lista de movimentações**: checkbox por linha + checkbox de seleção geral no header (com estado indeterminate); seleção limpa ao trocar de tab, filtro ou organização
- **Barra de ações em lote**: aparece quando ≥ 1 lançamento selecionado; exibe contador "N lançamentos selecionados", botão "Limpar seleção", "Marcar como pago" e "Excluir"
- **Ação "Marcar como pago"**: define `payment_date = hoje` nos selecionados com status `pendente` ou `atrasado`; ignora os demais com aviso no toast (ex.: "3 marcados como pagos. 1 ignorado.")
- **Ação "Excluir"**: confirmação destrutiva com count; exclui apenas `pendente` ou `atrasado`; toast com counts de excluídos e ignorados
- **RPC `bulk_update_movements(p_org_id, p_ids, p_action)`**: executa em transação única; valida membership e `organization_id` por linha; ação `mark_paid` ou `delete`; retorna `{ updated, ignored }`; `REVOKE ALL` + `GRANT EXECUTE TO authenticated`

> **Limitação conhecida:** bulk delete remove registros de `financial_movement_attachments` via CASCADE mas não exclui os arquivos do bucket `movement-attachments` (RPCs não têm acesso ao Storage). Arquivos órfãos serão endereçados em manutenção futura.

---

## [v0.8.13b] — 2026-05-13 · `onda2-melhorias-documentos`

### Adicionado
- **Indicador de documentos na lista** (`/movimentacoes`): ícone de clipe (paperclip) discreto na linha do lançamento quando `attachment_count > 0`; lançamentos sem documentos não exibem nada; campo `attachment_count` adicionado à RPC `list_financial_movements` via subquery `COUNT(*) FROM financial_movement_attachments`

### Modificado
- **Formatos de upload ampliados**: zona de upload aceita qualquer formato exceto executáveis e scripts (`.exe`, `.bat`, `.cmd`, `.msi`, `.sh`, `.ps1`, `.vbs`, `.jar` e similares); limite de 10 MB mantido; mensagem de erro inline "Tipo de arquivo não permitido por segurança." para formatos bloqueados
- **Renomeação "Comprovantes" → "Documentos"**: título do card, estado vazio, mensagem de carregamento e toasts em `MovimentoDetailPage`

### Corrigido
- **Lista de movimentações vazia após adição do `attachment_count`**: `list_financial_movements` usava `row_to_jsonb(x)` que falha com tipos anônimos de subquery em PostgreSQL; substituído por `to_jsonb(x)` (compatível com qualquer tipo, incluindo anônimos)

---

## [v0.8.13] — 2026-05-13 · `onda2-st8.13-comprovantes`

### Adicionado
- **Card "Documentos"** funcional em `/movimentacoes/:id`: lista de anexos com nome do arquivo, tamanho formatado e data de envio; botão "Baixar" (URL assinada temporária do Storage) e botão "Remover" (com confirmação inline que exclui do banco e do bucket)
- **Zona de upload** drag-and-drop e clicável: limite de 10 MB; validação de formato e tamanho com mensagem de erro inline; spinner durante envio; upload para bucket `movement-attachments` no caminho `{org_id}/{movement_id}/{filename}` com sufixo numérico em caso de colisão de nome; registro em `financial_movement_attachments` e atualização da lista sem reload
- Substituição do stub "Nenhum documento anexado" pelo componente funcional; comportamento idêntico para lançamentos de qualquer status

---

## [v0.8.12b] — 2026-05-13 · `onda2-st8.12b-bugfixes-recorrencia`

### Corrigido
- **Substituição de categorias em série**: `replaceCategories` fazia DELETE + INSERT em duas transações separadas; o trigger DEFERRED `validate_split_sum` disparava no commit do DELETE (sum=0) antes do INSERT reinserir as linhas — erro `split_sum_mismatch`. Solução: nova RPC `replace_movement_categories_bulk` que executa DELETE + INSERT atomicamente em uma única função PL/pgSQL.
- **Data de vencimento em edição de série**: `scope='all'` e `scope='this_and_future'` aplicavam o valor absoluto de `due_date` a todos os lançamentos, achatando a distribuição temporal. Solução: cálculo de delta em dias entre a data informada e a `due_date` do lançamento de referência, aplicado individualmente por linha; `payment_date` preservada.

---

## [v0.8.12] — 2026-05-13 · `onda2-st8.12-edicao-recorrencia`

### Adicionado
- **Rota `/movimentacoes/:id/editar`** com `EditarMovimentoPage` e `EditarMovimentoFormPage`
- Formulário de edição pré-preenchido via `get_financial_movement`; reutiliza `CategoriesSplitTable` e helpers de opções do formulário de criação; sem toggle de tipo nem bloco de recorrência
- Guard de status: se o movimento carregado não for 'pendente' ou 'atrasado', redireciona imediatamente para `/movimentacoes/:id` com toast "Este lançamento não pode ser editado."
- Banner discreto no topo indicando o escopo da edição ('apenas este lançamento', 'este e os próximos', 'toda a série')
- Modal de escopo em `MovimentoDetailPage`: RadioGroup com 3 opções ('Apenas este lançamento', 'Este e os próximos', 'Toda a série'), padrão `this`; lançamentos sem `recurring_series_id` navegam direto sem modal
- **EF `update_recurring_series`**: operação atômica para os 3 escopos — `this` aplica dados e desvincula da série em uma única transação; `this_and_future` cria nova `recurring_series` com os movimentos afetados reposicionados; `all` atualiza `template_jsonb` e todos os movimentos da série; a mutation do frontend usa sempre a EF para todos os escopos

---

## [v0.8.11] — 2026-05-13 · `onda2-st8.11-recorrencias`

### Adicionado
- Toggle 3-vias (Único / Parcelado stub / Recorrente) no formulário de novo lançamento
- Bloco de configuração de recorrência: frequência (diária, semanal, quinzenal, mensal, bimestral, trimestral, semestral, anual), data de início, modo de término (por nº de ocorrências ou data-fim)
- Preview dinâmico das próximas datas no bloco de recorrência
- Modal de confirmação antes de salvar série recorrente, com resumo do que será criado
- **EF `create_recurring_series`**: cria `recurring_series` + N `financial_movements` com datas calculadas em UTC; rollback em 3 camadas em caso de erro; suporte a `is_installment` e `total_installment_amount`

---

## [v0.8.10] — 2026-05-13 · `onda2-st8.10-estorno`

### Adicionado
- Modal de estorno em `/movimentacoes/:id` com campo de motivo obrigatório, gate no botão "Confirmar" e exibição de erro inline
- Defesa contra estorno de transferências (bloqueio via validação na EF)
- **EF `reverse_movement`**: validações (não estornado, não transferência), insert do movimento inverso com `origin='reversal'` e `status='pago'`, cópia dos splits, atualização do original com `reversed_at` / `reversed_by_movement_id` / `reversed_reason`, rollback manual em caso de erro; erros 403 e 422 mapeados corretamente

---

## [v0.8.9] — 2026-05-13 · `onda2-st8.9-detalhe-lancamento`

### Adicionado
- **`/movimentacoes/:id`** (detalhe do lançamento): header com tipo, status, título e valor; seções condicionais para split com percentuais, info de recorrência, estorno bidirecional e comprovantes placeholder
- Seção de auditoria com datas de criação, atualização e campos de origem
- Botões contextuais por status: "Editar" visível para 'pendente'/'atrasado'; "Estornar" visível para 'pago' não estornado

---

## [v0.8.8] — 2026-05-13 · `onda2-st8.8-split-categorias`

### Adicionado
- Toggle "Distribuir valor entre categorias" no formulário de novo lançamento
- Tabela de split com linhas editáveis de categoria + valor; validação de soma com tolerância de 0,005; gate do botão "Salvar" enquanto soma inválida
- Pré-população automática ao ligar o toggle (distribuição igualitária pelas categorias existentes) e limpeza ao desligar

---

## [v0.8.7] — 2026-05-13 · `onda2-st8.7-novo-lancamento` + hotfixes de RPC

### Corrigido
- **`row_to_jsonb` → `to_jsonb`** em 4 RPCs da Onda 2: `list_financial_movements`, `get_financial_movement`, `get_account_balances`, `create_financial_movement` — PostgreSQL rejeitava `row_to_jsonb(record)` quando usado com alias de subquery; substituído por `to_jsonb` que aceita `record` anônimo (via migration)
- **Payload de categorias em `create_financial_movement`**: formulário enviava `category_id` como campo top-level; corrigido para `categories: [{ category_id, amount }]` conforme a RPC exige
- **Toast de erro genérico**: adicionado log completo do erro Supabase (`code`, `message`, `details`) antes de exibir toast, para facilitar diagnóstico futuro

---

## [v0.8.7] — 2026-05-13 · `onda2-st8.7-novo-lancamento`

### Adicionado
- **`/movimentacoes/novo`** (formulário básico de criação de lançamento)
- Toggle de tipo (Receita/Despesa/Transferência) com cores funcionais; adapta campos dinamicamente: exibe/oculta Categoria e Conta de destino conforme tipo selecionado
- Campos principais: título, data de vencimento, data de pagamento (opcional), valor total com máscara BRL, select de conta com saldo atual (`get_account_balances`), select de categoria com `full_path` (`list_categories`)
- Campos de contexto: Projeto (desabilitado "Em breve" quando vazio), Centro de custo (`list_cost_centers`)
- Seção colapsável "Mais opções": forma de pagamento, beneficiário/pagador, referência bancária, documento fiscal, tags, observações — inputs sempre montados para preservar estado RHF
- Sidebar reativa com resumo dinâmico (badge de tipo, título, valor, conta, categoria, vencimento) e checklist de preenchimento via `useWatch`
- Validações inline: valor > 0, categoria obrigatória para receita/despesa, contas distintas para transferência; botão "Salvar" desabilitado enquanto inválido
- Submissão via `create_financial_movement`; sucesso invalida cache `['movements', orgId]` e navega para `/movimentacoes`
- Schema Zod discriminado por tipo; `buildCreatePayload` converte datas para ISO e campos vazios para `null`

---

## [v0.8.6] — 2026-05-13 · `onda2-st8.6-lista-movimentacoes`

### Adicionado
- **`/movimentacoes`** (lista completa): substituição do stub pela lista funcional
- Filtros-chip persistidos em `sessionStorage` por orgId: Período (padrão: mês corrente), Conta, Categoria (com `full_path`), Status — cada chip com X individual e botão "Limpar filtros"
- 5 tabs por tipo: Todas, Receitas, Despesas, Transferências, Estornadas; tab "Estornadas" desabilita chip de Status e força `status: 'estornado'` no payload
- Tabela com colunas: Vencimento, Lançamento (título + meta), Conta, Categoria (`full_path` ou "N categorias"), Status (badge colorido), Valor (cor por tipo)
- Hover na linha: ícones Eye e Pencil navegam para `/movimentacoes/:id`; linha inteira clicável para o mesmo destino
- Linha de totais calculada client-side: receitas, despesas, saldo do período (ou total único para tabs Transferências/Estornadas); saldo colorido por sinal
- Skeleton de 8 linhas e estado vazio com botão "Limpar filtros"
- Hook `useMovementFilters` + `useMovementsList` (TanStack Query); helpers `filtersToPayload`, `movementLabels`, `computeTotals`

---

## [v0.8.5] — 2026-05-13 · `onda2-st8.5-configuracoes-categorias`

### Adicionado
- **`/configuracoes/categorias`** (acesso admin): 3 tabs — Receitas, Despesas (árvore 2 níveis com indentação), Centros de custo (lista plana)
- Reordenamento via botões ▲/▼ com persistência de `display_order` via `upsert_category` em `Promise.all`
- Slideover criar/editar categoria: kind travado ao da tab ativa na criação; texto fixo na edição; select de pai limitado a raízes do mesmo kind; desabilitado em categorias que já têm filhos
- Slideover criar/editar centro de custo: nome + descrição, via `upsert_cost_center`
- Diálogos de ativar/desativar para categorias e centros de custo, com toast de erro descritivo da RPC
- **Modal "Aplicar template"**: lista templates via `list_category_templates`, preview de categorias por kind, aplicação via `apply_category_template` com toast de contagem; segunda aplicação exibe "Nenhuma categoria nova" (comportamento idempotente)
- Aba "Categorias" na sidebar do `ConfiguracoesLayout` (admin-only, ícone Tag)
- Helpers puros `buildCategoryTree` e `swapDisplayOrder`

---

## [v0.8.4] — 2026-05-13 · `onda2-st8.4-configuracoes-contas`

### Adicionado
- **`/configuracoes/contas`** (acesso admin): lista de contas com saldo atual via VIEW `account_current_balance`, badge de status, opacidade reduzida em contas inativas, estado vazio
- **Slideover de criar/editar conta**: campos obrigatórios (nome, tipo, saldo inicial, data de abertura) + seções colapsáveis "Dados bancários" e "Personalização" (cor, ícone); salva via `upsert_financial_account`
- **Diálogo de ativar/desativar**: confirmação antes de agir; erro da RPC exibido como toast descritivo; usa `toggle_account_status`
- Aba "Contas" adicionada à sidebar do `ConfiguracoesLayout` (visível apenas para admins, ícone Wallet)
- `accountTypeLabels.ts` com mapa enum→label PT para os 7 tipos de conta

---

## [v0.8.3] — 2026-05-13 · `onda2-st8.3-painel-rotas`

### Adicionado
- **`PainelPage`** funcional: bloco de saldos por conta (VIEW `account_current_balance`, apenas contas ativas, saldo total no rodapé, estado vazio com link para `/configuracoes/contas`) + bloco de KPIs do mês corrente via RPC `list_financial_movements` (receitas, despesas, saldo do mês com cor por sinal)
- **`RequireAuth`** em `src/features/auth/components/`: wrapper de rota que verifica sessão via `useAuth()`, exibe spinner durante carregamento e redireciona para `/login` se não autenticado
- **4 rotas stub** registradas em `App.tsx` sob `RequireAuth`: `/movimentacoes`, `/movimentacoes/novo`, `/movimentacoes/importar`, `/movimentacoes/:id`
- Skeleton nos blocos do painel durante carregamento de dados

---

## [v0.8.2] — 2026-05-13 · `onda2-st8.2-schema-movimentacoes`

### Adicionado
- **Enums**: `movement_type` (receita, despesa, transferencia), `movement_origin` (manual, recurring, installment, contribution), `movement_status` (pendente, pago, atrasado, estornado, efetivado)
- **Tabela `recurring_series`**: RLS canônica, suporte a parcelamentos via `is_installment BOOLEAN` + `total_installment_amount`
- **Tabela `financial_movements`**: FK para `financial_accounts`, `recurring_series`, `projects`, `vendors`; coluna `status` controlada por trigger `BEFORE INSERT OR UPDATE` (não GENERATED STORED — `CURRENT_DATE` não é IMMUTABLE no PostgreSQL); campo `transfer_peer_id` para par de transferência
- **Tabela `financial_movement_categories`** (split): trigger DEFERRED `validate_split_sum` garante que soma das linhas = total do movimento no COMMIT; constraint impede split em transferências
- **Tabela `movement_attachments`**: registro de comprovantes com `storage_path`
- **Bucket `movement-attachments`** (privado): path `{org_id}/{movement_id}/{filename}`
- **VIEW `account_current_balance`**: `initial_balance + receitas pagas - despesas pagas + transferências efetivadas recebidas - transferências efetivadas enviadas`
- **5 RPCs**: `list_financial_movements` (filtros: type, status, period_start/end, account_id, category_id), `get_financial_movement` (lançamento completo com split e anexos), `create_financial_movement` (com array de categories para split), `update_financial_movement`, `get_account_balances` (lê `account_current_balance`)

### Técnico
- GENERATED STORED para `status` descartado: trigger BEFORE INSERT OR UPDATE garante os 5 estados corretamente e mantém o índice `(organization_id, status)` populado com todos os valores (inclusive `atrasado`)
- Trigger DEFERRED `validate_split_sum` dispara ao COMMIT, não no INSERT — permite inserir linhas de split em múltiplos statements dentro da mesma transação
- Isolamento de snapshot de CTE: INSERTs em CTEs não são visíveis a SELECTs na mesma instrução — validações foram feitas em statements separados

---

## [v0.8.1] — 2026-05-13 · `onda2-st8.1-schema-base`

### Adicionado
- **Schema base da Onda 2 (financeiro)**: tabelas `projects` (stub para FK futura), `vendors`, `vendor_ratings`, `financial_accounts`, `categories`, `cost_centers`, `category_templates` — todas com RLS canônica e audit trigger
- **Enums**: `account_type` (7 valores) e `category_kind` (receita, despesa)
- **VIEW `categories_with_path`** com `security_invoker = true`: retorna `full_path` no formato "Pai > Filho" para uso em autocomplete e listagens
- **12 RPCs de CRUD**: `list/upsert/toggle_status` para contas financeiras, categorias e centros de custo; `list_category_templates`; `apply_category_template` (idempotente — duas passadas: pais → filhos)
- **Seed "Padrão Grupo Escoteiro 2026"** em `category_templates`: 35 categorias (14 receitas + 21 despesas) prontas para aplicação via RPC
- **Função `_set_updated_at()`** criada localmente na migration (não existia função genérica global no projeto)
- **Pattern `to_regclass`** nas RPCs de toggle_status: checagem de movimentações associadas ativada automaticamente quando `financial_movements` for criada na ST-8.2, sem alterar as RPCs

### Processo
- Adicionada regra ao `CLAUDE.md`: aprovação de plano do Lovable com ressalvas exige prompt escrito (`NNb-...-aprovacao.md`) — ressalva nunca pode ficar apenas no chat

---

## [v0.7.6] — 2026-05-12 · `config-plataforma-st7.6-perfil-notificacoes`

### Adicionado
- **Seção "Notificações"** em `/configuracoes/perfil`, independente do formulário principal (salva em `user_preferences` via `set_setting` com `p_level: "user"`)
- Campo WhatsApp: editável, formato E.164, validação inline, pré-preenchido com valor salvo
- Campo Telegram: read-only, exibe "Vinculado" / "Não vinculado" com base em `contact.telegram_chat_id`, instrução para vincular via @BussolaBot
- Nota de rodapé explicando escopo global das preferências

---

## [v0.7.5] — 2026-05-12 · `config-plataforma-st7.5-org-tabs`

### Adicionado
- **3 novas seções de integração** ao final de `/configuracoes/organizacao` (acesso admin da OSC)
  - **Google Drive**: JSON da conta de serviço (secret, não sobrescreve Vault quando em branco), ID da pasta de exportação e de importação
  - **WhatsApp Business**: Phone Number ID + token de acesso (secret, não sobrescreve quando em branco)
  - **Telegram por OSC**: Chat ID do grupo/canal
- Stubs funcionais: formulários salvam via `set_organization_settings_bulk`, backend ativo pendente
- Cada seção exibe nota "Esta integração ainda não está ativa..."

---

## [v0.7.4] — 2026-05-12 · `config-plataforma-st7.4-gotenberg-stubs`

### Adicionado
- **`GotenbergIntegrationPanel`**: URL, timeout (UI em segundos, salvo em ms), header de autenticação (secret), botão "Testar geração" com resultado inline (tempo em ms ou erro)
- **4 stubs funcionais** em `/superadmin/configuracoes`: Telegram, n8n, LLM/IA e S3/R2 — formulários com Salvar operacional, badge "Em breve" na sidebar
- `_stubShared.tsx`: `<StubNote>` e `<Field>` compartilhados entre os stubs

### Corrigido
- `storage.s3.access_key` era retornado como valor em claro pela RPC `read_platform_config_for_admin`; corrigido para `access_key_is_set: boolean` (Vault, nunca expõe o valor)
- `usePlatformConfig`: tipo `s3.access_key: string | null` atualizado para `access_key_is_set: boolean`
- Timeout do Gotenberg: UI exibia e recebia valor em segundos mas EF espera milissegundos; conversão explícita adicionada

---

## [v0.7.3] — 2026-05-12 · `config-plataforma-st7.3-email`

### Adicionado
- **`PlatformSettingsPage`** funcional em `/superadmin/configuracoes`: layout 2 colunas (sidebar + painel), hook `usePlatformConfig` (chama `read_platform_config_for_admin`), roteamento por integração selecionada
- **`IntegrationSidebar`** com badges de status por integração (ativo / config / erro / em breve)
- **`EmailIntegrationPanel`** com 3 subcards independentes: SMTP primário (6 campos + teste inline), Resend (API key + from), Padrões de e-mail (DPO, reply-to, fallback toggle)
- `IntegrationStatusBadge` + `computeStatus` + `formatRelativeTime`
- Botão "Testar envio" no subcard SMTP com resultado inline (✓ / ✗ + tempo em ms)

### Corrigido
- Bug crítico em `send_email/index.ts`: `SmtpConfig.secure` é `boolean` mas o banco armazenava `security: string`; `loadSmtpConfig` agora mapeia `security === 'SSL/TLS'` → `secure: true`

---

## [v0.7.2] — 2026-05-12 · `config-plataforma-st7.2-superadmin-layout`

### Adicionado
- **`SuperadminLayout`**: sidebar teal-dark, navegação `/superadmin/configuracoes`, `/superadmin/organizacoes`, `/superadmin/usuarios`
- **`SuperadminRoute`**: guard de acesso via RPC `read_platform_config_for_admin` como proxy de verificação de superadmin
- Hook `useIsSuperadmin` em `src/hooks/` (evita dependência invertida shared→features)
- Badge ⚡ no `TopNav` para superadmins
- Rotas `/superadmin/*` em `App.tsx`; páginas `/organizacoes` e `/usuarios` com `<ComingSoonPage>`

---

## [v0.7.1] — 2026-05-12 · `config-plataforma-st7.1-backend`

### Adicionado
- RPC `read_platform_config_for_admin` (VOLATILE, SECURITY DEFINER): retorna todas as configurações de plataforma com `is_set: boolean` para secrets (nunca expõe o valor)
- Template `test` no `send_email` para botão de teste de SMTP
- Edge Function `test_gotenberg`: dispara geração de PDF de teste e retorna `{ ok, ms }`

---

## [v0.6.7] — 2026-05-11 · `onda1-st6.7-gate-politica`

### Adicionado
- **Gate de aceite de política**: `RootRedirect` consulta `current_policy` + `user_consent`; redireciona para `/aceitar-politica` quando necessário (fail-open se RPC falhar)
- `AceitarPoliticaPage`: layout split teal/branco, reutiliza `<PolicyConsent>` e `<AuthBrandPanel>`, insert em `user_consent` com user_agent, redirect para `/` após aceite

---

## [v0.6.6] — 2026-05-11 · `onda1-st6.6-config-organizacao`

### Adicionado
- **`/configuracoes/organizacao`** completo (acesso admin): dados básicos da OSC (nome, CNPJ, contato, endereço, redes sociais), logo (bucket `organization-logos`, resize 512×512), configurações operacionais (moeda, timezone, ano fiscal), toggle de solicitações públicas (`accepts_public_signup`), permissões do papel Público
- RPC `set_organization_settings_bulk` para salvar múltiplas chaves de `organization_settings` em uma única chamada
- RPCs `read_organization_settings`, `update_organization_basic`, `update_organization_logo_path`
- Componente `OrgLogoUploader` (separado do `AvatarUploader` de perfil)

---

## [v0.6.5] — 2026-05-11 · `onda1-st6.5-usuarios-admin`

### Adicionado
- **`/configuracoes/usuarios`** completo (acesso admin): listagem de membros com filtros, busca e paginação client-side (cap 500); `AddUserDrawer` disparando EF `add_user_to_organization`; `MemberActionsMenu` com todas as transições válidas da máquina de estado (alterar papel, desativar, reativar, remover, cancelar convite, reenviar setup)
- `MemberAvatar` com signed URL (TTL 1h)
- `useIsActiveOrgAdmin` com fast-path JWT para superadmin
- `ConfiguracoesLayout` com sidebar adaptativa (aba "Usuários" visível apenas para admins)
- RPC `list_pending_org_requests` unificando `pending_organization_links` e `user_organization` pendentes, com identidade real via COALESCE

### Corrigido
- GRANT em `transition_user_organization_status` (estava REVOKE'd de `authenticated` desde ST-1)
- Nome nulo na listagem (COALESCE com `auth.users.raw_user_meta_data->>'full_name'`)
- Avatar no `TopNav` passou a ler `avatar_storage_path` de `user_profile`

---

## [v0.6.4] — 2026-05-08 · `onda1-st6.4-perfil`

### Adicionado
- **`/configuracoes/perfil`**: Identificação (nome + avatar), Contato (telefone E.164), Dados sensíveis (data de nascimento, CPF e RG cifrados no Vault), Ações (logout global + instruções LGPD)
- Tabela `user_profile` 1:1 com `auth.users`, RLS, trigger de auditoria com `audit_excluded_columns` para campos do Vault
- RPCs `set_user_profile_sensitive` + `get_user_profile_decrypted` (SECURITY DEFINER, Vault)
- Bucket `user-avatars` privado (2 MB, jpg/png/webp), `<AvatarUploader>` autônomo (resize 512×512 JPEG)
- `<ConfirmDialog>` em `shared/components/feedback/`
- `docs/lgpd-data-inventory.md`: 23 campos catalogados com base legal, prazo de retenção e mecanismo de anonimização

---

## [v0.6.3] — 2026-05-05 · `onda1-st6.3-setup-token`

### Adicionado
- **`/setup?token=...`** funcional: FSM com 10 estados (loading → ready → submitting → 4 terminais), validação Zod com react-hook-form, layout split idêntico ao `/login`
- `SetupPage` com tratamento diferenciado por `reason` retornado por `validate_setup_token`
- EF `dev_seed_setup_token` com duplo guard (`APP_ENV=dev` + service-role) para QA local
- Script `bin/seed-setup-token.sh` com listagem interativa de OSCs e indução dos 9 cenários da FSM

---

## [v0.6.2] — 2026-05-05 · `onda1-st6.2-criar-conta`

### Adicionado
- **`/criar-conta`** em dois modos: wizard anônimo de 3 passos (email → decisões → completar) e `LoggedNoOrgView` para usuário autenticado sem OSC
- EF `create_organization` com `createOrganizationWithSlug` (sufixo `-2`, `-3`...)
- `list_public_organizations()` SECURITY DEFINER
- Tradutor pt-BR de erros em `onboarding-errors.ts`

### Corrigido (OPSEC sweep — ADR-004)
- Removidos `details: err.message` em 27 pontos de 8 Edge Functions (ST-6.2 + retroativos em ST-4 e ST-5 + `send_email`) — zero vazamento de mensagem interna em respostas 500

---

## [v0.6.1] — 2026-05-05 · `onda1-st6.1-login-redirects`

### Adicionado
- **`/login`**: email/senha + Google OAuth, `RootRedirect` com 3 branches
- `useAuth` (combina `getSession` + `onAuthStateChange`), `useActiveOrganization`
- `OrgSwitcher` com selo de iniciais, dropdown de avatar com logout

---

## [v0.5.0] — 2026-05-05 · `onda1-st5-self-signup-and-links`

### Adicionado
- EFs `start_self_signup`, `complete_self_signup`, `request_organization_link`, `approve_organization_link`, `reject_organization_link`
- UPDATE atômico para evitar race em approve/reject
- `_shared/onboarding_common.ts` para reuso entre EFs

---

## [v0.4.1] — 2026-05-05 · `onda1-st4-onboarding-direct-with-resend`

### Adicionado
- EFs `add_user_to_organization`, `validate_setup_token`, `complete_setup`, `resend_setup_token`, `request_setup_resend`
- Schemas Zod, helpers compartilhados, configuração de `verify_jwt` por EF

---

## [v0.3.0] — 2026-05-05 · `onda1-st3-send-email-with-secrets`

### Adicionado
- Edge Function `send_email`: SMTP primário + Resend fallback, 6 templates, tabela `email_send_log`
- Integração com Vault via `set_setting`/`get_setting` com cifragem real (substituto de pgsodium)

---

## [v0.2.0] — 2026-05-05 · `onda1-st2-settings-policies`

### Adicionado
- 7 tabelas: `platform_settings`, `organization_settings`, `user_preferences`, `policies`, `user_consent`, `invitations`, `pending_organization_links`
- Auditoria com redação condicional para secrets
- Função `current_policy(type)`, `custom_access_token_hook` (não-ativável em Lovable Cloud — TODO operacional)

---

## [v0.1.0] — 2026-05-05 · `onda1-st1-schema-base`

### Adicionado
- Schema base PostgreSQL com RLS multi-tenant: funções `is_member_of`, `has_role_in`, `current_user_is_superadmin`
- Máquina de estado de `user_organization` com guard trigger (7 estados)
- `audit_log` + trigger genérico reutilizável
- Hardening: `search_path` fixo, `REVOKE EXECUTE` nas funções sensíveis

---

*Última atualização: 2026-05-21 · estabilização mobile pós-BK-199 (v0.19.1) — 6 ajustes mobile (cards de listas, formulários, filtros de Reembolsos, footer, overflow, atualização do PWA).*
