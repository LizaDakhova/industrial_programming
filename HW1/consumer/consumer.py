import pika

params = pika.ConnectionParameters(host="rabbit",
                                   port=5672,
                                   socket_timeout=10
                                  )
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="random numbers")

print(' Waiting for massages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(' Received %r" % body')

channel.basic_consume(callback,
                      queue="random numbers",
                      no_ack=True
                     )

while True:
	try:
	    channel.start_consuming()
	except pika.exceptions.ConnectionClosed:
	    channel.stop_consuming()

connection.close()


