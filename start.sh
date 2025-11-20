#!/bin/sh
echo "Instalando dependências..."
pip install -r requirements.txt

echo "Iniciando Jul.IA Secretária Virtual – WhatsApp Backend..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8013}
