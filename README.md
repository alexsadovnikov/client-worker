from pathlib import Path

# Обновим содержимое README.md после сброса окружения
readme_path = Path("README.md")

new_content = """\
# Client Worker

[![CI/CD](https://github.com/alexsadovnikov/client-worker/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/ci-cd.yml)
[![Tests](https://github.com/alexsadovnikov/client-worker/actions/workflows/tests.yml/badge.svg)](https://github.com/alexsadovnikov/client-worker/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/alexsadovnikov/client-worker/branch/main/graph/badge.svg)](https://codecov.io/gh/alexsadovnikov/client-worker)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/github/license/alexsadovnikov/client-worker)

**Python worker + Kafka + CRM integration**

---

## 🧪 Тестирование, покрытие и OpenAPI

### 📁 Структура проекта

...

### ✅ Установка зависимостей

- Продакшен:

```bash
pip install -r requirements.txt
