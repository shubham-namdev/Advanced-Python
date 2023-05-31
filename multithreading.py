"""
-> MULTITHREADING
Threads are lightweight processes that perform certain actions in a program
and they are part of a process themselves. These threads can work in parallel
with each other in the same way as two individual applications can.
"""

import threading

def function1():
    for i in range(10000):
        print(f"One : {i}")

def function2():
    for i in range(10000):
        print(f"Two : {i}")


t1 = threading.Thread(target= function1)
t2 = threading.Thread(target= function2)
#t1.start()
#t1.run()
t1.start()

""""""
""" 
? t1.run() VS t1.start() : 
When we use the run function to execute our threads, 
they run serially one after the other. They wait for each other to finish.
The start function puts all of them to work simultaneously.
"""

""" 
-> Join()
If we want to wait for our threads to finish before we move on with the
code, we can use the join function. We can pass maximum number of seconds we 
want to wait as a param.
"""

t1.join(3)

print("This is the end of program!")


"""
-> Locking :  
Basically, one thread is locking all of the other threads and 
they can only continue to work when the lock is removed. Synchronizing threads.
"""

import threading

x = 2000
lock = threading.Lock()

def divide():
    global x
    lock.acquire()

    while(x > 1) :
        x /= 2
        print(x)
    
    lock.release()
    print("Finished process 1")

def multiply():
    global x
    lock.acquire()

    while(x < 4000):
        x *= 2
        print(x)
    
    lock.release()
    print("Finished process 2")

th1 = threading.Thread(target=divide)
th2 = threading.Thread(target=multiply)

th1.start()
th2.start()


"""
-> Semaphores: 
Used when we don't want to completely lock a resource but just limit it to a
certain amount of threads or accesses."""

import threading
import time

semaphore = threading.BoundedSemaphore(value=2)

def access(thread_number: int) -> None:
    print(f"{thread_number} : Trying Access...\n")
    semaphore.acquire()

    print(f"{thread_number} : Access Granted!\n")

    print(f"{thread_number} : Waiting 2 seconds...\n")

    time.sleep(2)
    semaphore.release()

    print(f"{thread_number} : Releasing...\n")

for thread_number in range(10):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()

"""
? Advantage: 
This process makes a lot of sense when we have limited resources or
limited computational power in a system and we want to limit the access to it.
"""


"""
-> Events:
We can pause a thread and wait for a certain event to happen, in order to continue it.
Event is triggered using set() function
"""
import threading

event = threading.Event()

def doSomething():
    print("Waiting for event...")
    event.wait()  #paused
    print("Continuing!..")

thread = threading.Thread(target=doSomething)
thread.start()

x = input("Trigger event? ")
if(x == "yes"):
    event.set()  #triggered


"""
-> Daemon Threads
Special kind of thread that runs in the background.
This means that the program can be terminated even if this thread is still running.
? Usage
-background tasks like synchronizing, loading or cleaning up files that are not needed anymore.
"""

import threading
import time

path = "./test.txt"
text = ""

def readFile():
    global path, text

    while True:
        with open(path) as f:
            text = f.read()
        time.sleep(3)

def printLoop():
    global text
    for x in range(50):
        print(text)
        time.sleep(1)

thread1 = threading.Thread(target=readFile, daemon=True)  # set daemon = True for daemon thread
thread2 = threading.Thread(target=printLoop)

thread1.start()
thread2.start()



