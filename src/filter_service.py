from rabbitmq import RabbitMQ

rabbitmq_queue_in = 'messages'
rabbitmq_queue_out = 'filtered_messages'
stop_words = ["bird-watching", "ailurophobia", "mango"]

def callback(ch, method, properties, body):
    global rabbitmq_queue_out
    message = body.decode()
    if not any(word in message.split("=>")[1] for word in stop_words):
        rabbitmq = RabbitMQ()
        rabbitmq.connect()
        rabbitmq.publish(rabbitmq_queue_out, message)
        rabbitmq.close()
    else:
        print('There is the block word')





rabbitmq = RabbitMQ()
rabbitmq.consume(rabbitmq_queue_in, callback)
