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
