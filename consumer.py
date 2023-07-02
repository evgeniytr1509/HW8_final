import pika

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создание очереди
channel.queue_declare(queue='email_queue')

# Функция для обработки сообщений из очереди
def process_email(body):
    print("Sending email to:", body)


    print("Email sent!")

# Callback-функция для получения сообщений
def callback(ch, method, properties, body):
    process_email(body)

# Подписка на очередь и ожидание сообщений
channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()
