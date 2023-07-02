import pika

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создание очереди
channel.queue_declare(queue='email_queue')

# Список контактов
contacts = ['contact1@example.com', 'contact2@example.com', 'contact3@example.com']

# Отправка сообщений в очередь
for contact in contacts:
    channel.basic_publish(exchange='', routing_key='email_queue', body=contact)
    print("Sent email to:", contact)

connection.close()
