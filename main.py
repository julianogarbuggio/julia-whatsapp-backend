import os
from typing import Any, Dict, Optional

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
import httpx
from dotenv import load_dotenv

load_dotenv()

WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN', '')
WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID', '')
META_VERIFY_TOKEN = os.getenv('META_VERIFY_TOKEN', '')
PORT = int(os.getenv('PORT', '8013'))

app = FastAPI(title='Jul.IA Secretária Virtual - WhatsApp Backend')

class JulIASecretariaBrain:
    @staticmethod
    def normalize(text: str) -> str:
        return text.strip().lower()

    @classmethod
    def handle(cls, text: str) -> str:
        t = cls.normalize(text)
        if any(k in t for k in ['oi','ola','olá','bom dia','boa tarde','boa noite']):
            return 'Olá! Eu sou a Jul.IA Secretária Virtual. Me diga se é sobre: 1) empréstimos, 2) procuração, 3) processo, 4) agendar, 5) dúvidas.'
        return 'Me diga se sua questão é 1, 2, 3, 4 ou 5, ou explique um pouco mais.'

async def send_whatsapp_text(to: str, message: str) -> None:
    if not WHATSAPP_TOKEN or not WHATSAPP_PHONE_NUMBER_ID:
        print('[ERRO] Configuração de WhatsApp faltando.')
        return
    url = f'https://graph.facebook.com/v20.0/{WHATSAPP_PHONE_NUMBER_ID}/messages'
    headers = {'Authorization': f'Bearer {WHATSAPP_TOKEN}', 'Content-Type': 'application/json'}
    payload: Dict[str, Any] = {
        'messaging_product': 'whatsapp',
        'to': to,
        'type': 'text',
        'text': {'preview_url': False, 'body': message},
    }
    async with httpx.AsyncClient(timeout=15.0) as client:
        await client.post(url, headers=headers, json=payload)

@app.get('/health')
async def health() -> Dict[str, str]:
    return {'status': 'ok'}

@app.get('/webhook')
async def verify_webhook(hub_mode: Optional[str] = None, hub_challenge: Optional[str] = None, hub_verify_token: Optional[str] = None):
    if hub_mode == 'subscribe' and hub_challenge and hub_verify_token == META_VERIFY_TOKEN:
        return PlainTextResponse(content=hub_challenge, status_code=200)
    raise HTTPException(status_code=403, detail='Token de verificacao invalido.')

@app.post('/webhook')
async def whatsapp_webhook(request: Request) -> JSONResponse:
    body = await request.json()
    try:
        entry = body.get('entry', [])[0]
        changes = entry.get('changes', [])[0]
        value = changes.get('value', {})
        messages = value.get('messages', [])
    except Exception:
        return JSONResponse(content={'status': 'ignored'}, status_code=200)
    if not messages:
        return JSONResponse(content={'status': 'no_messages'}, status_code=200)
    for msg in messages:
        from_number = msg.get('from')
        msg_type = msg.get('type')
        if msg_type == 'text':
            text = msg.get('text', {}).get('body', '')
            resposta = JulIASecretariaBrain.handle(text)
            if from_number and resposta:
                await send_whatsapp_text(from_number, resposta)
    return JSONResponse(content={'status': 'processed'}, status_code=200)

@app.post('/test/send')
async def test_send(payload: Dict[str, Any]) -> Dict[str, Any]:
    to = payload.get('to')
    message = payload.get('message', 'Teste Jul.IA Secretária Virtual.')
    if not to:
        raise HTTPException(status_code=400, detail="'to' é obrigatório.")
    await send_whatsapp_text(to, message)
    return {'status': 'sent'}
