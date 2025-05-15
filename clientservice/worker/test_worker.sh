---
# 📦 .github/workflows/ci-cd.yml — CI/CD pipeline для инфраструктуры и контейнеров
name: CI/CD для ClientService

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: 🏠 Checkout репозитория
        uses: actions/checkout@v4

      - name: ⚖️ Сборка и запуск контейнеров
        run: docker compose -f docker-compose.yml up -d --build

      - name: 🔍 Проверка запущенных сервисов
        run: docker compose -f docker-compose.yml ps

      - name: 👀 Проверка доступности Swagger UI
        run: |
          curl --fail http://localhost:5050/apidocs
          curl --fail http://localhost:5001/apidocs
          curl --fail http://localhost:8080/apidocs

      - name: ❌ Остановка сервисов
        run: docker compose -f docker-compose.yml down

---

# 🔮 .github/workflows/tests.yml — Unit-тесты worker и Codecov
name: 🧪 Тесты для worker

on:
  push:
    paths:
      - "clientservice/worker/**"
      - ".github/workflows/tests.yml"
  pull_request:
    paths:
      - "clientservice/worker/**"
      - ".github/workflows/tests.yml"

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: 📄 Клонирование репозитория
        uses: actions/checkout@v4

      - name: 🐍 Установка Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: 📦 Установка зависимостей
        run: |
          pip install -r clientservice/worker/requirements.txt
          pip install pytest pytest-cov

      - name: 🔮 Запуск unit-тестов
        run: |
          PYTHONPATH=clientservice/worker pytest \
            --cov=clientservice/worker/app \
            --cov-report=term \
            --cov-report=xml \
            clientservice/worker/tests

      - name: 📈 Отправка покрытия в Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage.xml
          flags: worker-tests
          name: codecov-client-worker