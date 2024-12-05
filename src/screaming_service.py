from rabbitmq import RabbitMQ

rabbitmq_queue_in = 'filtered_messages'
rabbitmq_queue_out = 'screaming_messages'

def callback(ch, method, properties, body):
  global rabbitmq_queue_out
  message = body.decode().split("=>")
  message[1] = message[1].upper()
  rabbitmq = RabbitMQ()
  rabbitmq.connect()
  print(message)
  rabbitmq.publish(rabbitmq_queue_out, '=>'.join(message))

rabbitmq = RabbitMQ()
rabbitmq.consume(rabbitmq_queue_in, callback)
