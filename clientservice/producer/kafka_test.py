from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send('client-topic', {'test': 'message'})
producer.flush()
print("📤 Сообщение отправлено в Kafka!")
