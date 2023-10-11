import pika


def callback(ch, method, properties, body):
    print(f"Received: {body}")


def receive_feedback_prompts():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the same queue for receiving feedback prompts
    channel.queue_declare(queue='feedback_prompts')

    # Set up a callback to process received messages
    channel.basic_consume(queue='feedback_prompts', on_message_callback=callback, auto_ack=True)

    print('Waiting for feedback prompts. To exit, press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    receive_feedback_prompts()
