import time
import threading
import queue


class Queue:
    def __init__(self, max_processes):
        self.max_processes = max_processes
        self.q = queue.Queue()
        self.available_processes = max_processes

    def run(self, thread_num):
        while True:
            task, task_args = self.q.get()
            task(task_args)
            self.q.task_done()
            print(f'Thread #{thread_num} is doing task #{task} in the queue.')

    def start_thread(self):
        if self.available_processes > 0:
            self.available_processes -= 1
            worker = threading.Thread(target=self.run, args=(self.available_processes,), daemon=True)
            worker.start()
        else:
            print("All threads are being used")

    def add_to_q(self, task, task_args):
        self.q.put((task, task_args))


def square(x):
    time.sleep(2)
    print(x * x)


def cube(x):
    time.sleep(1)
    print(x * x * x)


if __name__ == '__main__':
    Q = Queue(max_processes=4)
    for i in range(4):
        Q.start_thread()
    for j in range(3):
        Q.add_to_q(square, 3)
    for j in range(3):
        Q.add_to_q(cube, 2)

    Q.q.join()
