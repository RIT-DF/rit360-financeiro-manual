---
title: "Instalar como aplicativo"
nav_order: 4
permalink: /instalar-como-app/
---

# Instalar a Bússola como aplicativo

A Bússola Financeira pode ser instalada como **aplicativo de verdade** no celular e no computador. Não precisa baixar nada de loja — a instalação acontece direto pelo navegador, com um clique. O app instalado tem ícone próprio na tela inicial / desktop, abre em janela cheia (sem barra de endereços do navegador) e carrega mais rápido em redes lentas.

Essa tecnologia se chama **PWA (Progressive Web App)** — um padrão moderno suportado por todos os navegadores atualizados.

---

## Por que instalar

- **Ícone próprio** na tela inicial do celular ou na barra de tarefas do computador.
- **Janela limpa**: o app abre em tela cheia, sem barra de endereços nem aba do navegador.
- **Mais rápido**: parte dos arquivos do app fica salva no aparelho — telas abrem em segundos.
- **Acesso direto**: tesoureiro que precisa registrar despesa no campo abre o app com 1 toque, sem digitar URL.
- **Atualização sob seu controle**: quando uma nova versão é publicada, o próprio app mostra uma notificação "Nova versão disponível" e pergunta se quer atualizar.

A instalação **não exige cadastro novo**, **não copia seus dados pro celular** e **não permite uso offline** — lançamentos, relatórios e tudo que vem do servidor continuam exigindo conexão com a internet.

---

## Android (Google Chrome)

1. Abra `bf.rit.org.br` no Chrome do celular Android.
2. Faça login normalmente.
3. Toque no menu de **3 pontinhos** no canto superior direito do Chrome.
4. Toque em **Instalar aplicativo**.
5. Confirme tocando em **Instalar** no diálogo que aparece.

Pronto — o ícone da Bússola aparece na sua tela inicial. Tocar nele abre o app em tela cheia.

> 💡 **Dica:** depois de usar o app por alguns segundos, a Bússola também mostra um banner discreto na parte inferior sugerindo a instalação — você pode tocar em **Instalar** ali se preferir.

---

## iPhone / iPad (Safari)

> Importante: no iPhone e iPad, a instalação de PWAs **só funciona no Safari**, não no Chrome iOS.

1. Abra `bf.rit.org.br` no **Safari** do iPhone ou iPad.
2. Faça login normalmente.
3. Toque no botão **Compartilhar** (quadrado com seta para cima) na parte inferior da tela.
4. Role para baixo no menu de compartilhamento.
5. Toque em **Adicionar à Tela de Início**.
6. Confirme o nome (ou edite se quiser) e toque em **Adicionar**.

O ícone da Bússola aparece na tela inicial do iPhone como qualquer outro app.

---

## Computador (Chrome ou Edge)

1. Abra `bf.rit.org.br` no Google Chrome ou Microsoft Edge.
2. Faça login normalmente.
3. Olhe para o lado direito da **barra de endereços** — aparece um pequeno ícone de **instalação** (monitor com seta para baixo, ou um círculo com sinal de +).
4. Clique nesse ícone.
5. Clique em **Instalar** no diálogo que aparece.

A Bússola passa a ter uma janela própria (separada do navegador) e fica disponível no menu Iniciar (Windows), Launchpad (Mac) ou lançador (Linux), como qualquer outro programa.

---

## O que muda depois de instalar

- **Aparência:** o app abre sem barra de endereços, sem abas, sem botões de voltar do navegador. Só a interface da Bússola.
- **Navegação no celular:** a barra inferior do app (**Painel** / **Movim.** / **Pag./Reemb.** / **Relatórios** / **Mais**) substitui o que seria a navegação do navegador — cinco itens fixos, todos diretos. Tocar em **Mais** abre um painel deslizante com o **seletor de organização** (quando você tem acesso a mais de uma OSC), as rotas que não cabem na barra (**Projetos**, **Configurações da organização**, **Meu perfil**), os links auxiliares (**Manual do Usuário**, **Política de Privacidade**, **Termos de Uso** — todos abrem em nova aba) e o botão **Sair**:

[![Painel "Mais" no celular com seletor de OSC](/assets/screenshots/mobile-more-sheet-org-switcher.png)](/assets/screenshots/mobile-more-sheet-org-switcher.png)
*Painel "Mais" no celular — bloco da OSC ativa no topo (chevron expande a lista quando há múltiplas OSCs)*

- **Atualizações:** quando uma nova versão da Bússola for publicada, um aviso discreto aparece dentro do app com botões **Atualizar agora** ou **Depois**. Você decide quando aplicar.
- **Dados:** continuam vindo da internet em tempo real. Sem conexão, o app mostra uma tela "Sem conexão" com botão **Tentar novamente** — não é possível registrar lançamentos sem internet.

---

## Como desinstalar

### Android

Pressione e segure o ícone da Bússola na tela inicial → arraste para **Desinstalar** (ou toque em **Informações do app** → **Desinstalar**).

### iPhone / iPad

Pressione e segure o ícone da Bússola → toque em **Remover app** → **Excluir app** (ou apenas **Remover da Tela de Início** se quiser manter os dados de navegador).

### Computador

Dentro do app instalado, clique no menu **⋮** (3 pontinhos) no canto superior direito da janela → **Desinstalar Bússola Financeira**.

Você pode reinstalar a qualquer momento abrindo `bf.rit.org.br` no navegador e seguindo os passos acima.

---

## Problemas comuns

**"Não aparece a opção Instalar aplicativo no menu do Chrome."**
Aguarde uns 30 segundos navegando pelo app antes de procurar a opção — o Chrome só oferece a instalação após algum uso real. Se mesmo assim não aparecer, limpe os dados do site (Configurações do Chrome → Sites → `bf.rit.org.br` → **Limpar dados**) e tente de novo.

**"Instalei mas o app abre dentro do Chrome com barra de endereços."**
Isso significa que foi criado um atalho, não uma instalação completa. Desinstale, limpe os dados do site no Chrome, reabra `bf.rit.org.br`, navegue por ~30 segundos e tente instalar de novo.

**"O app instalado está com versão antiga."**
Procure pela notificação **Nova versão disponível** dentro do app e toque em **Atualizar**. Se não aparecer, force atualização puxando a tela para baixo (Android) ou feche e abra o app de novo.

---

## Notificações push

Desde a v0.19.0, o app instalado pode enviar **notificações push** para o seu celular avisando sobre eventos importantes (reembolso aprovado, pedido aguardando sua aprovação, etc.). Funciona como notificação de banco: você recebe o aviso na tela mesmo com a Bússola fechada, toca, e abre direto na tela relevante.

A ativação é **por dispositivo**, com um interruptor mestre **"Ativar push neste dispositivo"** em **[Meu Perfil → Notificações](/configuracoes/perfil/)**. Cada celular/computador é independente — pode ativar no celular pessoal e desativar no do trabalho.

**Requisitos por plataforma:**

- **Android (Chrome / Edge / outro navegador moderno):** funciona direto, sem precisar instalar como app. Apenas autorize quando o navegador perguntar.
- **iOS (Safari):** push só funciona se a Bússola estiver **instalada como app** na tela de início (veja a seção do iPhone/iPad acima). Sem instalar, o interruptor fica desabilitado com instrução. Esse é o motivo principal para instalar como app no iPhone.
- **Desktop (Chrome / Firefox / Edge):** funciona como no celular. Útil para receber avisos quando você está com outro aplicativo em primeiro plano.

Configuração granular por evento × canal em **Meu Perfil → Notificações** — a coluna Push é mais uma ao lado de E-mail, WhatsApp e Telegram. Default: tudo ligado; você silencia o que não quer receber.
