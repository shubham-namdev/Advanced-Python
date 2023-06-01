"""
-> QUEUE
~ Type 1: FIFO - First in First Out
"""

import queue

q = queue.Queue()

for x in range(10):
    q.put(x) 


for x in range(10):
    print(q.get())

"""
? put() -> insert element
? get() -> get element
"""
"""
! Queuing Resources
"""

import threading
import queue
import time

q = queue.Queue()
threads = []

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processed : {item}")
        time.sleep(2)
        q.task_done()

for x in range(3):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

nums = [145, 154, 78, 454, 10, 78, 11 ,21 ,10 ,33 ,51]

for item in nums:
    q.put(item)

q.join()

for i in range(5):
    q.put(None)


"""
~ Type 2: LIFO -Last in first out (sort of stack)
"""
import queue

q = queue.LifoQueue()

nums = [1, 2, 3, 4, 5]

for x in nums:
    q.put(x)

while not q.empty():
    print(q.get())


"""
~ Type 3: Priority Queue
"""
import queue

q = queue.PriorityQueue()

q.put((7, "Hello"))
q.put((5, "Bye"))
q.put((75, True))
q.put((1, "First"))

while not q.empty():
    print(q.get())
"""
(1, 'First')
(5, 'Bye')
(7, 'Hello')
(75, True)
"""
"""
? Wanna get only values -
"""
while not q.empty():
    print(q.get()[1])
"""
First
Bye
Hello
True
"""