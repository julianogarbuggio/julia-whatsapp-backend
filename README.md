# Jul.IA Secretária Virtual – WhatsApp Backend

Backend em **FastAPI** que integra a **Jul.IA Secretária Virtual** com a **WhatsApp Cloud API**, servindo como cérebro-orquestrador para:

- Receber mensagens do webhook do WhatsApp
- Processar e classificar o atendimento (novos clientes, andamento de processos, dúvidas sobre empréstimos, etc.)
- Acionar outros serviços da Jul.IA (Petições, Procurações, Agenda & Intimações)
- Responder ao cliente de forma automatizada e personalizada

---

## 🧠 Visão Geral da Arquitetura

- **FastAPI** como framework web
- **Uvicorn** como servidor ASGI
- Integração via **HTTP** com a WhatsApp Cloud API (Meta)
- Configuração via variáveis de ambiente (`.env` / Railway)
- Deploy em plataforma PaaS (Railway)

Fluxo básico:

1. Cliente envia mensagem no WhatsApp  
2. Meta chama o endpoint `/webhook` deste backend  
3. O backend:
   - valida a assinatura / token
   - interpreta a mensagem
   - chama, se necessário, outros serviços da Jul.IA
   - envia resposta ao cliente via API do WhatsApp

---

## 📁 Estrutura básica do projeto

```text
.
├── main.py            # App FastAPI (webhook, saúde, teste, etc.)
├── requirements.txt   # Dependências Python
├── Dockerfile         # Build da imagem para deploy
├── Procfile           # Comando web padrão (Heroku-like)
├── railway.json       # Configurações padrão para Railway
├── .env.example       # Modelo de variáveis de ambiente
├── run_local.bat      # Script para rodar localmente no Windows
├── start.sh           # Script opcional de inicialização (Linux/containers)
└── README.md          # Este arquivo :)
