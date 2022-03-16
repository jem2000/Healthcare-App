import time
import multiprocessing as mp
from multiprocessing import Pool
import _thread
import threading
import queue


class Queue:
    def __init__(self, max_processes):
        self.max_processes = max_processes
        self.q = queue.Queue()

    def run(self, thread_no):
        while True:
            task = self.q.get()
            square(3)
            self.q.task_done()
            print(f'Thread #{thread_no} is doing task #{task} in the queue.')

    def start_threads(self):
        for i in range(self.max_processes):
            worker = threading.Thread(target=self.run, args=(i,), daemon=True)
            worker.start()


def square(x):
    time.sleep(2)
    print(x * x)


def cube(x):
    time.sleep(1)
    print(x * x * x)


if __name__ == '__main__':
    Q = Queue(3)
    Q.start_threads()
    for j in range(10):
        Q.q.put(j)

    Q.q.join()
