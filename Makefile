.PHONY: up down restart dev logs status test coverage lint clean test-myservice dashboard shell rebuild logs-service restart-service free-port clean-docker

# 🚀 Запуск всех контейнеров
up:
	docker compose up -d --build

# 💛 Остановка всех контейнеров
down:
	docker compose down

# 🔁 Перезапуск всех контейнеров
restart:
	docker compose down
	docker compose up -d --build

# 🧲 Локальная разработка с override
dev:
	lsof -ti:5050 -ti:5000 -ti:5051 -ti:8501 | xargs kill -9 || true
	docker compose -f docker-compose.yml -f docker-compose.override.yml up -d --build

# 📋 Логи всех сервисов
logs:
	docker compose logs -f

# 📊 Статус всех контейнеров
status:
	docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 🥪 Unit-тесты для worker
test:
	PYTHONPATH=clientservice/worker pytest --cov=app --cov-report=term clientservice/worker/tests

# 📈 Покрытие кода worker в файл
coverage:
	PYTHONPATH=clientservice/worker pytest --cov=app --cov-report=xml clientservice/worker/tests

# 🥪 Тесты для my_service
test-myservice:
	PYTHONPATH=clientservice/my_service pytest --cov=app --cov-report=term clientservice/my_service/tests

# 🔍 Линтинг worker-сервиса
lint:
	.venv/bin/flake8 clientservice/worker

# 🥵 Очистка временных и кэш-файлов
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".DS_Store" -delete
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.coverage" -delete

# 📊 Локальный запуск дэшборда
dashboard:
	streamlit run clientservice/dashboard/streamlit_app.py --server.port 8501 --server.address 0.0.0.0

# 👤 Вход в контейнер: make shell SERVICE=worker
shell:
	docker exec -it $(SERVICE) /bin/sh

# 🔄 Пересборка сервиса: make rebuild SERVICE=worker
rebuild:
	docker compose build --no-cache $(SERVICE)
	docker compose up -d $(SERVICE)

# 📋 Логи конкретного сервиса: make logs-service SERVICE=crm
logs-service:
	docker compose logs -f $(SERVICE)

# 🔁 Перезапуск сервиса: make restart-service SERVICE=auth
restart-service:
	docker compose restart $(SERVICE)

# 🔌 Очистка занятого порта (5050)
free-port:
	lsof -ti:5050 | xargs kill -9 || true

# 📤 Удаление остановленных контейнеров
clean-docker:
	docker container prune -f

# 🐳 Проверка статуса Docker Daemon
check-docker:
	@if ! docker info >/dev/null 2>&1; then \
		echo "❌ Docker daemon не запущен. Проверь Docker Desktop и перезапусти его."; \
		exit 1; \
	else \
		echo "✅ Docker daemon запущен и работает."; \
	fi