#ping_redis.py
import time

from rq import Queue
import background_task
import redis


def task(n):
    time.sleep(5)
    return n


r = redis.Redis()
q = Queue(connection=r)

setter = r.set('foo', 'bar')
getter = r.get('foo')

from ping_redis import task
job = q.enqueue(task, 5)

print(setter, getter)
