from celery import Celery

#setup broker
broker_url = 'amqp://guest:guest@localhost:5672/'

#create app
app = Celery('tasks', broker=broker_url)