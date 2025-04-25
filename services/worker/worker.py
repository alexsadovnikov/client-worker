# services/worker/worker.py
from app.main import app

if __name__ == "__main__":
    # тот же порт, что и в docker-compose (5050 внутри контейнера)
    app.run(host="0.0.0.0", port=5050)
