@echo off
set PORT=8011
set META_VERIFY_TOKEN=julIA2025_verify
set META_ACCESS_TOKEN=SEU_TOKEN_AQUI
uvicorn main:app --host 0.0.0.0 --port 8011
