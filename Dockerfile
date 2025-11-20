FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia só o requirements primeiro (cache de deps)
COPY requirements.txt ./

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Variável padrão de porta (Railway geralmente seta PORT)
ENV PORT=8013

# Comando para rodar o servidor
# Usa a PORT do ambiente se existir, senão 8013
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8013}"]
