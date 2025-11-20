from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")

@app.get("/")
async def root():
    return {"status": "ok", "message": "Jul.IA WhatsApp Backend rodando localmente."}

@app.get("/webhook")
async def verify(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge or "")
    else:
        return PlainTextResponse(content="Token inválido.", status_code=403)

@app.post("/webhook")
async def webhook_received(request: Request):
    data = await request.json()
    print("📩 RECEBIDO DO META:", data)
    return JSONResponse(content={"status": "ok"})
