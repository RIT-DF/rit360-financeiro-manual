---
layout: section
title: "Configurações — Usuários"
permalink: /configuracoes/usuarios/
---

> Disponível para **Presidente (admin)**.

A página **Usuários** é onde você gerencia quem tem acesso à sua OSC dentro do Bússola — convidar novos membros, alterar papéis, suspender acessos.

[![Configurações — Usuários](../assets/screenshots/manual-09b-config-usuarios.png)](../assets/screenshots/manual-09b-config-usuarios.png)
*Configurações — Gerenciamento de usuários*

> 💡 **Por que isso importa**
> A pessoa errada com permissão errada é o caminho mais curto para um problema sério em OSC. Acesso administrativo dado para alguém que não devia, papel de aprovador para quem não tem mandato, voluntário recém-saído que ainda tem acesso meses depois — todos os casos derivam de gestão de usuários frouxa. Esta página é o ponto onde você mantém **quem entra, quem sai e quem pode o quê**.

Listagem traz todos os membros da OSC com nome, e-mail, papel, status (ativo/pendente/inativo) e foto de perfil.

## Adicionar usuário

Clique em **+ Adicionar usuário**. Informe o **e-mail** e o **papel** desejado. A Bússola dispara automaticamente um e-mail de convite com o link de primeiro acesso. O status do usuário fica como "Pendente" até ele aceitar.

> 📖 **Conceito · Convite vs acesso direto**
> A Bússola usa **convite por e-mail** como mecanismo de entrada, não cadastro aberto. Isso protege a OSC de spam, garante que a pessoa convidada confirma o acesso pelo próprio e-mail, e permite mensagem personalizada no convite. O convite tem prazo de validade — se expirar, o admin pode reenviar pelo mesmo fluxo.

## Ações por membro

Cada linha tem menu de ações que muda conforme o status:

- **Alterar papel** — muda o papel do usuário (Presidente, Tesoureiro, Coordenador, Voluntário)
- **Desativar acesso** — bloqueia entrada sem excluir histórico
- **Reativar acesso** — restaura entrada de quem estava desativado
- **Cancelar convite pendente** — remove convite que ainda não foi aceito
- **Reenviar convite** — re-dispara o e-mail de convite (útil quando o destinatário não recebeu ou o link expirou)

> ⚠️ **Atenção · Mudança de papel deve ser deliberada**
> Promover alguém para Tesoureiro dá acesso à aprovação de despesas. Conversão entre papéis com poder financeiro deve passar pela diretoria, não ser ação unilateral do presidente. Em OSC com estatuto formal, pode até exigir ata de assembleia ou eleição. O sistema não bloqueia a mudança, mas registra tudo no audit log com data, autor e papéis anterior/novo.

> ⚠️ **Atenção · Desativar ≠ excluir**
> Desativar bloqueia entrada mas **preserva todo o histórico** (lançamentos criados, aprovações dadas, comentários escritos). Para auditoria e prestação de contas, isso é essencial — você consegue mostrar quem fez o quê mesmo depois que a pessoa saiu. A Bússola não tem opção de "excluir usuário"; só "desativar" + histórico preservado. Quem deixou a OSC: desative.

## Solicitações pendentes

Em OSCs com **acesso público ao link de vínculo** ativado (em Configurações → Organização), pessoas externas podem pedir entrada espontaneamente. As solicitações pendentes aparecem em uma seção separada, com botão **Aprovar** ou **Rejeitar**. Aprovar gera o convite formal; rejeitar nega o acesso sem criar conta.

## Foto de perfil dos membros

A lista mostra a foto de cada membro (configurada por cada um no Meu Perfil). Caso a pessoa não tenha foto, aparece um avatar com as iniciais do nome.

## Por onde seguir

- **Papéis e Permissões** — para entender o que cada papel pode fazer antes de atribuir.
- **Configurações → Fluxo de Aprovações** — para definir quais papéis aprovam e quem é aprovador individual.
- **Configurações → Organização** — para controlar o acesso público de vínculo.
