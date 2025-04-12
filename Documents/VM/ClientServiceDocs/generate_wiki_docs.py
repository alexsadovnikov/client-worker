from pathlib import Path

wiki_path = Path("client-worker.wiki")
wiki_path.mkdir(exist_ok=True)

# Home.md
(wiki_path / "Home.md").write_text("""# Home

Добро пожаловать в документацию проекта `client-worker`.

## Навигация
- [[Architecture|Architecture]]
- [[API|API]]
- [[Testing|Testing]]
- [[CI-CD|CI-CD]]
""", encoding="utf-8")

# Architecture.md
(wiki_path / "Architecture.md").write_text("""# 🏗 Архитектура проекта

Проект построен по микросервисной архитектуре:

- `worker` — основной Flask-сервис
- `crm` — моковая CRM (Flask)
- `producer` — Kafka-продюсер
- `dashboard` — Streamlit-интерфейс

Коммуникация осуществляется через:
- Kafka (события)
- REST API (между сервисами)
""", encoding="utf-8")

# API.md
(wiki_path / "API.md").write_text("""# 🔌 API и OpenAPI

Flask-сервис `worker` предоставляет REST API со Swagger UI:

- Сущности: Contact, Case, Agent, Call, Interaction
- Поддерживаются: GET, POST, PUT, DELETE

Документация доступна по адресу:
http://localhost:8000/apidocs
""", encoding="utf-8")

# Testing.md
(wiki_path / "Testing.md").write_text("""# 🧪 Тестирование

В проекте настроены автотесты через `pytest` + `pytest-cov`:

```bash
pytest worker/tests --cov=worker
