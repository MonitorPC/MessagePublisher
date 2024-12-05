from flask import Flask, request, jsonify
from rabbitmq import RabbitMQ

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    if not data or 'message' not in data or 'user' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    message = data['message']
    user = data['user']

    try:
        rabbitmq_queue = 'messages'
        rabbitmq = RabbitMQ()
        rabbitmq.connect()
        rabbitmq.publish(rabbitmq_queue, '=>'.join([user, message]))
        rabbitmq.close()
        return jsonify({'status': 'Message sent'}), 200
    except pika.exceptions.AMQPConnectionError as e:
        return jsonify({'error': f'Failed to connect to RabbitMQ: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

