import pika


def send_feedback_prompt(interviewer_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('http://localhost:15672/'))
    channel = connection.channel()

    # Declare a queue for sending feedback prompts
    channel.queue_declare(queue='feedback_prompts')

    message = f'Please provide feedback for interview ID: {interviewer_id}'

    # Send the message to the 'feedback_prompts' queue
    channel.basic_publish(exchange='', routing_key='feedback_prompts', body=message)

    print(f"Sent: {message}")
    connection.close()


if __name__ == '__main__':
    interviewer_id = 123  # Replace with the actual interviewer's ID
    send_feedback_prompt(interviewer_id)
