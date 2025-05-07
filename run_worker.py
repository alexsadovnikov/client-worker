import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent))

from clientservice.worker.app.main import create_app

app = create_app()
