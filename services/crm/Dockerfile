# services/crm/Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY services/crm/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/crm/app ./app

CMD ["python", "app/crm_mock.py"]
