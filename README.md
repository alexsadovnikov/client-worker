from pathlib import Path

readme_content = """\
# Client Worker

[![CI/CD](https://github.com/alexsadovnikov/client-worker/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/ci-cd.yml)
[![Tests](https://github.com/alexsadovnikov/client-worker/actions/workflows/tests.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/alexsadovnikov/client-worker/branch/main/graph/badge.svg)](https://codecov.io/gh/alexsadovnikov/client-worker)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/github/license/alexsadovnikov/client-worker)

**ClientServiceDocs: микросервисная архитектура на Python с поддержкой JWT, Kafka, CRM, Streamlit-дэшбордом и автотестами.**

---

## 📁 Структура

- `worker/` — Flask + JWT, Kafka producer, OpenAPI, автотесты
- `crm/` — мок-сервис CRM для тестов
- `producer/` — Kafka producer утилита
- `dashboard/` — Streamlit дэшборд
- `schemas/` — Pydantic-схемы
- `.github/workflows/` — CI/CD и тесты

---

## ✅ Установка зависимостей

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
