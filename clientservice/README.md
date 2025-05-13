[![CI/CD для ClientService](https://github.com/alexsadovnikov/client-worker/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/ci-cd.yml)
[![Unit-тесты для Worker](https://github.com/alexsadovnikov/client-worker/actions/workflows/tests.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/tests.yml)
[![Smoke Test Worker](https://github.com/alexsadovnikov/client-worker/actions/workflows/test-worker.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/test-worker.yml)
[![Code coverage](https://codecov.io/gh/alexsadovnikov/client-worker/branch/main/graph/badge.svg)](https://codecov.io/gh/alexsadovnikov/client-worker)
[![Lint](https://github.com/alexsadovnikov/client-worker/actions/workflows/lint.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/lint.yml)
[![Docs](https://img.shields.io/badge/docs-wiki-blue?logo=github)](https://github.com/alexsadovnikov/client-worker/wiki)
[![Docker](https://img.shields.io/docker/image-size/alexsadovnikov/client-worker/latest?logo=docker)](https://hub.docker.com/r/alexsadovnikov/client-worker)
[![My Service Tests](https://github.com/alexsadovnikov/client-worker/actions/workflows/test-my-service.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/test-my-service.yml)

# 📦 ClientService — Микросервисная архитектура

## 🔧 Makefile команды (для локальной разработки)

| Команда           | Описание                                        |
|-------------------|-------------------------------------------------|
| `make up`         | 🚀 Сборка и запуск всех Docker-сервисов        |
| `make down`       | 🛑 Остановка всех контейнеров                  |
| `make logs`       | 📋 Просмотр логов всех микросервисов          |
| `make test`       | 🧪 Запуск unit-тестов с покрытием              |
| `make coverage`   | 📈 Генерация `coverage.xml` для Codecov        |
| `make lint`       | 🔍 Проверка стиля кода с помощью `flake8`     |
| `make clean`      | 🧹 Очистка кешей, `__pycache__`, `.pyc`, etc.  |

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

## 🚀 My Service

Добавлен микросервис `my_service` — простой API на Flask с поддержкой OpenAPI 3.0.

### Поддерживаемые маршруты:

| Метод | Путь     | Описание         |
|-------|----------|------------------|
| GET   | `/ping`  | Тестовый эндпоинт|

### 🧩 Стек:

- `Flask`
- `flask-smorest`
- `Swagger UI` (OpenAPI 3.0)

### 📄 Swagger доступен по адресу:
[http://localhost:5054/apidocs](http://localhost:5054/apidocs)

## 🧩 Микросервисы проекта

| Сервис        | Назначение                                                   | Swagger UI                                      |
|---------------|--------------------------------------------------------------|-------------------------------------------------|
| `auth`        | JWT-аутентификация и проверка токена                         | [`/auth/apidocs`](http://localhost:5001/apidocs) |
| `chat`        | WebSocket-сервис обмена сообщениями в реальном времени       | [`/chat/apidocs`](http://localhost:5002/apidocs) |
| `crm`         | Mock CRM для обмена данными с внешними системами            | [`/crm/apidocs`](http://localhost:5053/apidocs)  |
| `worker`      | Основная бизнес-логика, API, Kafka consumer                  | [`/worker/apidocs`](http://localhost:5050/apidocs) |
| `my_service`  | Пример сервиса с маршрутом `/ping` и Swagger UI              | [`/my_service/apidocs`](http://localhost:5054/apidocs) |
| `dashboard`   | Streamlit-дэшборд аналитики, управления и визуализации       | [`/dashboard`](http://localhost:8501)           |
| `api_gateway` | Единая точка входа, агрегация OpenAPI, проверка авторизации  | [`/gateway/apidocs`](http://localhost:8080/apidocs) |