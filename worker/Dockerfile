FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "worker.py"]
# Внести небольшое изменение, например, пробел или комментарий
echo "# dummy change" >> worker/Dockerfile
