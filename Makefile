# ✅ Makefile для управления проектом ClientService

# Запуск docker-compose
up:
	docker compose up -d --build

# Остановка контейнеров
down:
	docker compose down

# Просмотр логов
logs:
	docker compose logs -f

# Тесты с покрытием
test:
	PYTHONPATH=client-worker/worker pytest --cov=app --cov-report=term client-worker/worker/tests

# Отчёт о покрытии в файл
coverage:
	PYTHONPATH=client-worker/worker pytest --cov=app --cov-report=xml client-worker/worker/tests

# Линтинг
lint:
	flake8 client-worker/worker

# Очистка
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".DS_Store" -delete
