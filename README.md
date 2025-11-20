
# 🤖 Jul.IA Secretária Virtual – WhatsApp Backend

Backend em FastAPI para integrar a Jul.IA com o **WhatsApp Business Cloud API**.

- Endpoint `/webhook` para **validação** do Meta (GET)
- Endpoint `/webhook` para **receber mensagens** do WhatsApp (POST)
- Preparado para rodar localmente com `uvicorn` e em produção no **Railway**

---

## ⚙️ Variáveis de ambiente principais

- `META_VERIFY_TOKEN` – token de verificação que você cadastra no painel do Meta
- `WHATSAPP_TOKEN` – token de acesso da API do WhatsApp (Cloud API)
- `WHATSAPP_PHONE_NUMBER_ID` – ID do número de telefone (opcional por enquanto)
- `OPENAI_API_KEY` – chave da OpenAI, caso use geração de respostas inteligente

Exemplo de `.env` para desenvolvimento local:

```env
META_VERIFY_TOKEN=julIA2025_verify
WHATSAPP_TOKEN=INSIRA_SEU_WHATSAPP_TOKEN_AQUI
WHATSAPP_PHONE_NUMBER_ID=SEU_PHONE_NUMBER_ID
OPENAI_API_KEY=SUA_CHAVE_OPENAI_SE_TIVER
```

---

## ▶️ Rodando localmente

1. Crie e ative seu ambiente virtual (opcional, mas recomendado).
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` baseado no `.env.example`.
4. Rode o servidor:

   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8011
   ```

5. (Opcional) Use `ngrok` para expor localmente e testar o webhook do Meta:

   ```bash
   ngrok http 8011
   ```

---

## 🚀 Deploy no Railway

1. Suba este repositório no GitHub.
2. No Railway, crie um novo projeto **a partir do GitHub**.
3. Configure as variáveis de ambiente no Railway:

   - `META_VERIFY_TOKEN`
   - `WHATSAPP_TOKEN`
   - `WHATSAPP_PHONE_NUMBER_ID`
   - `OPENAI_API_KEY` (se for usar)

4. O Railway vai usar o `Dockerfile` ou o `railway.json` para subir o serviço.

---

## ✅ URL de webhook no Meta

Depois de o Railway subir, você vai ter algo como:

```text
https://julia-whatsapp-backend-production.up.railway.app
```

No painel do **WhatsApp Business** (Meta Developers), use:

- **URL de callback:** `https://SEU-DOMINIO/webhook`
- **Token de verificação:** o mesmo valor de `META_VERIFY_TOKEN`

Pronto. Webhook validado e backend da Jul.IA ouvindo as mensagens do WhatsApp. 🎯
