---
title: "Organização"
nav_order: 1
parent: "Configurações da Organização"
permalink: /configuracoes/organizacao/
---

> Disponível para **Presidente (admin)**.

A página **Organização** centraliza os dados da sua OSC e as **integrações** com sistemas externos. Acessada pelo **ícone de engrenagem** no canto superior direito (a engrenagem só aparece para admin e tesoureiro) → Configurações → seção Organização.

[![Configurações — Organização](/assets/screenshots/config-organizacao.png)](/assets/screenshots/config-organizacao.png)
*Configurações — Dados da organização*

> 💡 **Por que isso importa**
>
> Os dados da OSC aqui aparecem em **todos os documentos gerados pelo Bússola** (recibos, declarações, relatórios para financiadores, exportações em PDF). Manter atualizado é o que faz a marca da sua OSC aparecer profissional na prestação de contas. As **integrações** abrem porta para automação: WooCommerce sincroniza vendas, WhatsApp Business envia notificações, Google Drive armazena documentos.

## Identidade da OSC

- **Nome** — como a OSC se identifica oficialmente
- **CNPJ** — formatado automaticamente conforme você digita. Aceita tanto o CNPJ numérico tradicional quanto o novo **CNPJ alfanumérico** (que passa a valer a partir de julho/2026)
- **E-mail institucional**
- **Telefone**
- **Site** — endereço completo (`https://...`)
- **Identificador único** — slug não editável usado em URLs e identificações internas (gerado a partir do nome no cadastro)

## Endereço e redes sociais

Endereço completo (CEP, logradouro, número, complemento, bairro, cidade, UF) e perfis em redes sociais (Instagram, Facebook, LinkedIn, YouTube).

> ✓ **Dica · Preencha endereço completo para documentos formais**
>
> Recibos e declarações geradas pelo Bússola usam o endereço daqui. OSC com endereço incompleto no sistema pode acabar com documentos que não passam em conferência de financiador ou contador.

## Logo da organização

Upload da logo da OSC (JPG, PNG ou WebP, até 2 MB). A imagem é redimensionada para 512×512. Aparece em documentos gerados, e em versões futuras vai aparecer na barra superior em vez do nome em texto.

## Configurações operacionais

- **Moeda** — padrão Real (BRL); pode ser alterada se a OSC opera em outra moeda
- **Fuso horário** — todas as datas/horas no sistema seguem esse fuso
- **Início do ano fiscal** — define os recortes de "Ano YTD" e "Ano anterior" nos filtros (default Janeiro)

## Acesso público

- **Aceitar solicitações públicas de vínculo** — quando ativado, qualquer pessoa com o link público da OSC pode pedir vínculo (a OSC ainda precisa aprovar). Desligado por default.

> ⚠️ **Atenção · Acesso público é compartilhamento controlado**
>
> "Aceitar solicitações públicas de vínculo" não dá acesso automático — ainda passa pelo admin. Mas com o link público, qualquer pessoa pode pedir entrada na sua OSC. Use quando você quiser receber inscrições espontâneas (ex: novos voluntários, novos associados); desligue quando preferir só convidar manualmente.

## Regras padrão para projetos

Valores iniciais que o módulo de [Projetos](/modulos/projetos/) usa ao planejar — em especial na **calculadora de taxa de eventos**. São apenas o **ponto de partida**: cada projeto pode ajustar conforme o caso.

- **Fundo de reserva padrão (%)** — uma folga de segurança sobre os custos previstos ao planejar o orçamento de um evento (default 10%). Entra como reserva no cálculo da taxa de inscrição.
- **Regra padrão de pagamento de voluntários** — como os voluntários entram na conta da taxa: **rateados** (não pagam; o custo deles é dividido entre os pagantes), **pagam taxa cheia**, **OSC paga** pelos voluntários, ou **com desconto** (quando aplicável, com o percentual de desconto).
- **Permitir que cada projeto sobrescreva esta regra** — se ligado, um projeto específico pode escolher uma regra de pagamento de voluntários diferente da padrão da OSC.

> 💡 **Por que isso importa**
>
> Definir essas regras uma vez, no nível da OSC, evita reconfigurar a calculadora de taxa a cada evento — e mantém coerência entre os projetos (todos partem do mesmo fundo de reserva e da mesma política de voluntários). Quando um evento for exceção, o projeto sobrescreve pontualmente, sem mudar o padrão da organização.

## Integrações

Integração permite que sistemas externos conversem com o Bússola — economizando trabalho manual de transferir dados de um sistema para outro.

### WooCommerce

[Saiba mais no manual de Movimentações → seção Importar lançamentos](/modulos/movimentacoes/#importar-lançamentos)

Sincroniza pedidos pagos da sua loja online (WooCommerce) como receitas no Bússola. Cron diário automático + botão para importar sob demanda. Refunds no WooCommerce viram estornos automáticos no Bússola. Cada pedido importado tem badge "WooCommerce" clicável na lista de movimentações que abre o pedido original no admin do WC.

Configure URL da loja, Consumer Key e Consumer Secret (com instruções passo a passo de como gerar no admin do WooCommerce), frequência da sincronização, modo de mapeamento de categorias (automático com categoria-mãe ou manual explícito), conta financeira destino, data de corte para backfill.

### Google Drive *(em implantação)*

Armazenamento de documentos da OSC no Google Drive da organização. Anexos de movimentações, reembolsos e pedidos serão sincronizados automaticamente.

### WhatsApp Business *(em implantação)*

Envio de notificações via número oficial WhatsApp Business da OSC. Habilita o canal "WhatsApp" da matriz de notificações dos usuários.

### Telegram *(em implantação)*

Envio de notificações via bot oficial Telegram da OSC para grupos/canais. Complementa o envio individual para usuários que vincularam Telegram no perfil pessoal.

## Exportar dados da organização (LGPD)

No fim da página, a seção **Exportação de dados da organização (LGPD)** permite ao admin **baixar todos os dados da OSC** em um único pacote — útil para guardar um backup, levar para outro sistema ou atender a uma solicitação de transparência.

[![Exportação e encerramento da organização](/assets/screenshots/config-organizacao-lgpd.png)](/assets/screenshots/config-organizacao-lgpd.png)
*Exportação de dados (LGPD) e zona de perigo para encerramento da organização*

- Clique em **Exportar dados da organização**. O pacote é um **ZIP** com uma planilha **Excel** (movimentações, reembolsos, pedidos de pagamento, membros, categorias, centros de custo e configurações) mais **todos os anexos e comprovantes**.
- A geração roda **em segundo plano**. Você recebe um **e-mail com o link de download** (válido por **7 dias**) assim que o pacote fica pronto. O link só pode ser baixado por administradores da OSC.
- O último pacote gerado fica listado na própria seção, com a data e um botão para baixar enquanto o link estiver válido.

> 💡 **Por que isso importa**
>
> Poder exportar a base inteira a qualquer momento é uma garantia de **autonomia e transparência**: os dados são da sua OSC, não ficam reféns da plataforma. Serve de backup, ajuda numa eventual migração e responde de imediato a um pedido de prestação de contas ou auditoria.

## Encerrar organização

Ainda no fim da página, a **Zona de perigo · Encerrar organização** inicia o encerramento definitivo da OSC no Bússola. É uma ação séria e foi desenhada com calma para que ninguém perca dados por engano.

- O encerramento **bloqueia novas escritas imediatamente** — a partir dali ninguém lança, edita ou aprova nada na OSC.
- Você tem uma **janela de 30 dias** para exportar tudo o que precisar antes da eliminação (use a exportação acima).
- Após o prazo, **identificadores e anexos são apagados** e os **dados pessoais dos membros são anonimizados**. Por **obrigação legal**, os **registros financeiros e a trilha de auditoria são mantidos sem identificação pessoal**, e o **CNPJ é retido**.

> ⚠️ **Atenção · Encerrar é irreversível pelo autosserviço**
>
> Não há botão para "desfazer" um encerramento pela própria interface. Só recorra a essa opção quando a OSC realmente vai deixar de operar no Bússola. Em dúvida, **exporte os dados primeiro** e procure o suporte/DPO antes de confirmar.

## Por onde seguir

- **Configurações → Usuários** — para gerenciar membros da OSC.
- **Configurações → Contas Bancárias** — para cadastrar as contas que aparecem em Movimentações.
- **Movimentações → Importar Lançamentos** — onde a integração WooCommerce aparece como fonte ao lado do CSV.
