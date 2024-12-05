from rabbitmq import RabbitMQ
import smtplib
import os

rabbitmq_queue = 'screaming_messages'



def send_email(message):
    receiver_emails = os.getenv("RECEIVER_EMAILS", "Jhon,Munir").split(',') # Make it a list
    try:
        with smtplib.SMTP('127.0.0.1', 1025) as server:
            for r in receiver_emails:
                server.ehlo()
                server.sendmail(message[0], r, message[1])
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def callback(ch, method, properties, body):
    message = body.decode().split("=>")
    send_email(message)  # Send the email

rabbimq = RabbitMQ()
print('started')
rabbimq.consume(rabbitmq_queue, callback)
