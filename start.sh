
#!/usr/bin/env bash
echo "Iniciando Jul.IA WhatsApp Backend em http://127.0.0.1:8011 ..."
uvicorn main:app --reload --host 127.0.0.1 --port 8011
