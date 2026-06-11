---
layout: section
title: "Configurações — Usuários"
permalink: /configuracoes/usuarios/
---

> Disponível para **Presidente (admin)**.

A página **Usuários** é onde você gerencia quem tem acesso à sua OSC dentro do Bússola — convidar novos membros, alterar papéis, suspender acessos.

[![Configurações — Usuários](/assets/screenshots/manual-09b-config-usuarios.png)](/assets/screenshots/manual-09b-config-usuarios.png)
*Configurações — Gerenciamento de usuários*

> 💡 **Por que isso importa**
> A pessoa errada com permissão errada é o caminho mais curto para um problema sério em OSC. Acesso administrativo dado para alguém que não devia, papel de aprovador para quem não tem mandato, voluntário recém-saído que ainda tem acesso meses depois — todos os casos derivam de gestão de usuários frouxa. Esta página é o ponto onde você mantém **quem entra, quem sai e quem pode o quê**.

Listagem traz todos os membros da OSC com nome, e-mail, papel, status (ativo/pendente/inativo) e foto de perfil.

## Adicionar usuário

Clique em **+ Adicionar usuário**. Informe o **e-mail** e o **papel** desejado. A Bússola dispara automaticamente um e-mail de convite com o link de primeiro acesso. O status do usuário fica como "Pendente" até ele aceitar.

> 📖 **Conceito · Convite vs acesso direto**
> A Bússola usa **convite por e-mail** como mecanismo de entrada, não cadastro aberto. Isso protege a OSC de spam, garante que a pessoa convidada confirma o acesso pelo próprio e-mail, e permite mensagem personalizada no convite. O convite tem prazo de validade — se expirar, o admin pode reenviar pelo mesmo fluxo.

## Importar usuários em lote (planilha CSV)

[![Importar usuários — tela de upload](/assets/screenshots/manual-config-usuarios-importar.png)](/assets/screenshots/manual-config-usuarios-importar.png)
*Importar usuários — instruções, download do template e área de upload*

Para OSCs que estão migrando de outro sistema ou que precisam cadastrar muitos membros de uma vez, há a opção **Importar usuários** ao lado de "Adicionar usuário". O fluxo é o mesmo padrão do importador de movimentações.

1. Clique em **Importar usuários** → abre uma tela dedicada.
2. **Baixe o template** CSV. O arquivo já vem com o cabeçalho correto e algumas linhas de exemplo.
3. Preencha sua planilha. Campos **obrigatórios**: nome completo, e-mail e papel. **Opcionais**: telefone, WhatsApp, Telegram, data de nascimento, CPF, RG.
4. Faça **upload** do arquivo. A Bússola mostra uma **pré-visualização** com cada linha classificada por status:
   - **Novo** — vai receber convite por e-mail
   - **Já cadastrado** — usuário existente em outra OSC; cria vínculo direto sem convite
   - **Vínculo ativo na OSC** — usuário que já é membro; perfil pode ser atualizado (campos vazios apenas)
   - **Com erro** — linha que será pulada (motivo explícito ao lado)
5. Clique em **Importar**. A Bússola dispara os convites por e-mail para os novos cadastros e atualiza os perfis dos demais.

> 📖 **Conceito · Upsert seletivo**
> Quando o e-mail da planilha já existe na sua OSC, a Bússola **só preenche os campos que estão vazios** no perfil atual. Nenhum dado existente é substituído. Útil para migrações onde você importa dados de uma planilha mestre sem o risco de sobrescrever informações que o membro já cadastrou no próprio perfil.

> ⚠️ **Atenção · Multi-papel não entra via planilha**
> Cada linha do CSV atribui exatamente um papel. Se o membro precisar acumular papéis (ex: Coordenador de Projeto + Comissão Fiscal), use o botão **Editar papéis** no menu de ações depois da importação. Isso é decisão pra evitar erros de digitação em CSV grande.

> ⚠️ **Atenção · Dados de pagamento (PIX/conta) não vêm no CSV**
> Por segurança e simplicidade, a planilha não importa dados de PIX, banco ou conta. Cada membro preenche isso depois no próprio perfil, em **Configurações → Perfil** (acessível por qualquer usuário). Mantém esse dado fora da planilha que circula entre administradores.

> ⚠️ **Atenção · Senha não vem no CSV**
> O fluxo é igual ao convite individual: para cada e-mail novo, a Bússola envia link de setup por e-mail. O usuário define a própria senha ao clicar no link. Admin nunca digita nem vê a senha de outro membro.

## Ações por membro

Cada linha tem menu de ações que muda conforme o status:

- **Editar papéis** — abre painel lateral com checkboxes para os papéis disponíveis (Presidente, Tesoureiro, Diretor, Coordenador de Projeto, Comissão Fiscal e Voluntário). Um usuário pode ter mais de um papel ao mesmo tempo — ver [Papéis e Permissões](/papeis/) para a regra de combinações.

  [![Editar papéis — painel multi-select](/assets/screenshots/manual-config-usuarios-editar-papeis.png)](/assets/screenshots/manual-config-usuarios-editar-papeis.png)
  *Editor de papéis — marque os papéis desejados; combinações proibidas ficam visualmente desabilitadas*

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
