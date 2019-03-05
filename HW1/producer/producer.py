import pika
from time import sleep
from random import randint


params = pika.ConnectionParameters(host="rabbit",
                                   port=5672
                                  )
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="random numbers")

while True:
	try:
        sleep(randint(1, 10))
        number = str(random.randint(-10000, 10000))
        print('send: ', number)
        channel.basic_publish(exchange='',
                              routing_key="random numbers",
		                      body=str(number)
                             )
	except pika.exceptions.ConnectionClosed:
	    print("Lost connection. Message not delivered.")

connection.close()
