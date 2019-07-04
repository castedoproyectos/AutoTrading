import threading, queue

from telegramhandler import TelegramHandler
from handler import Handler

def func1(num, q):

    thd = TelegramHandler()
    thd.main_loop(num, q)

def func2(q):
    hd = Handler()
    

num = 20
q = queue.Queue()
thread1 = threading.Thread(target=func1,args=(num,q))
thread2 = threading.Thread(target=func2,args=(q))


thread1.start()
thread2.start()