
import os
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from dotenv import load_dotenv

# Carrega variáveis do .env em ambiente de desenvolvimento local
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("julia-whatsapp-backend")

app = FastAPI(
    title="Jul.IA Secretária Virtual – WhatsApp Backend",
    version="1.0.0",
    description="Webhook do WhatsApp Business API + Jul.IA."
)

VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")

@app.get("/")
async def root():
    """Endpoint simples de healthcheck."""
    return {
        "status": "ok",
        "message": "Jul.IA WhatsApp Backend rodando.",
    }

@app.get("/webhook")
async def verify(request: Request):
    """Endpoint usado pelo Meta para validar o webhook."""
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    logger.info("GET /webhook | mode=%s token=%s challenge=%s", mode, token, challenge)

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge or "")
    raise HTTPException(status_code=403, detail="Invalid verify token")

@app.post("/webhook")
async def webhook(request: Request):
    """Endpoint que recebe mensagens e eventos do WhatsApp."""
    body = await request.json()
    logger.info("POST /webhook | payload=%s", body)
    # Aqui depois você trata as mensagens (chama OpenAI, responde, etc.).
    return JSONResponse({"status": "ok"})
