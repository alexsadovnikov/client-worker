from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send('client-submitted', {
    "client_id": 123,
    "name": "Иван Иванов",
    "action": "запрос обратного звонка"
})

producer.flush()
print("✅ Сообщение отправлено в Kafka!")

