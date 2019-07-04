
import threading, queue

def func1(num, q):
    while num < 100000000:
        num = num**2

        a = ['hola', 'carlos']
        q.put(a)

def func2(num, q):
    while num < 100000000:
        lista = q.get()
        print(num)

num = 2
q = queue.Queue()
thread1 = threading.Thread(target=func1,args=(num,q))
thread2 = threading.Thread(target=func2,args=(num,q))

print('setup')

thread1.start()
thread2.start()