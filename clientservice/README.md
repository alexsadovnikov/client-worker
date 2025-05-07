![build](https://github.com/alexsadovnikov/client-worker/actions/workflows/worker-ci.yml/badge.svg)
![coverage](https://codecov.io/gh/alexsadovnikov/client-worker/branch/main/graph/badge.svg)
![lint](https://github.com/alexsadovnikov/client-worker/actions/workflows/lint.yml/badge.svg)
![docs](https://img.shields.io/badge/docs-wiki-blue?logo=github)
![docker](https://img.shields.io/docker/image-size/alexsadovnikov/client-worker/latest?logo=docker)

# 📦 ClientService — Микросервисная архитектура
---

## 🔐 Auth-сервис

Реализован отдельный микросервис `auth` с поддержкой JWT авторизации.

### Поддерживаемые маршруты:

| Метод | Путь            | Описание                       |
|-------|------------------|--------------------------------|
| POST  | `/auth/login`    | Аутентификация и получение JWT |
| GET   | `/auth/protected`| Проверка защищённого ресурса   |
| GET   | `/auth/verify`   | Верификация токена             |

### 🧩 Стек:

- `Flask`
- `flask-jwt-extended`
- `flask-smorest`
- `Pydantic`
- `Swagger UI` (OpenAPI 3.0)

### 📄 Swagger доступен по адресу:
[http://localhost:5001/apidocs](http://localhost:5001/apidocs)

## 🧩 Микросервисы проекта

| Сервис        | Назначение                                                   | Swagger UI                                      |
|---------------|--------------------------------------------------------------|-------------------------------------------------|
| `auth`        | JWT-аутентификация и проверка токена                         | [`/auth/apidocs`](http://localhost:5001/apidocs) |
| `chat`        | WebSocket-сервис обмена сообщениями в реальном времени       | [`/chat/apidocs`](http://localhost:5002/apidocs) |
| `crm`         | Mock CRM для обмена данными с внешними системами            | [`/crm/apidocs`](http://localhost:5053/apidocs)  |
| `worker`      | Основная бизнес-логика, API, Kafka consumer                  | [`/worker/apidocs`](http://localhost:5050/apidocs) |
| `dashboard`   | Streamlit-дэшборд аналитики, управления и визуализации       | [`/dashboard`](http://localhost:8501)           |
| `api_gateway` | Единая точка входа, агрегация OpenAPI, проверка авторизации  | [`/gateway/apidocs`](http://localhost:8080/apidocs) |

> ✅ Все сервисы (кроме dashboard) используют `Flask + flask-smorest` и поддерживают OpenAPI 3.0.