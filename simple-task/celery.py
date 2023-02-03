from celery import Celery
import time


#create instance from celery .. message broker is RabbitMQ
app = Celery('first' , broker = 'amqp://guest:guest@localhost:5672')




#simple task using celery
@app.task(name = 'celery.sum')
def sum():
    time.sleep(10) #simulation of heavy task with 10 seconds time
    return 2+3