from flask import Flask, request
import redis
from rq import Queue

import time

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)
q = Queue(connection=r)


def background_task(n):

    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)


@app.route("/task")
def index():

    if request.args.get("n"):

        from app import background_task
        job = q.enqueue(background_task, request.args.get("n"))

        return f"Task ({job.id}) added to queue"

    return "No value for count provided"


if __name__ == "__main__":
    app.run()
