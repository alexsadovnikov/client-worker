from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time

def connect_kafka(max_retries=10, delay=3):
    for attempt in range(1, max_retries + 1):
        try:
            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            print(f"[Kafka] Подключение успешно на попытке {attempt}")
            return producer
        except NoBrokersAvailable as e:
            print(f"[Kafka] Попытка {attempt}: брокер недоступен, жду {delay}с...")
            time.sleep(delay)
    raise Exception(f"[Kafka] Не удалось подключиться после {max_retries} попыток")

if __name__ == "__main__":
    producer = connect_kafka()
    # Здесь можно продолжить логику отправки сообщений
    print("[Kafka] Producer готов к работе")

