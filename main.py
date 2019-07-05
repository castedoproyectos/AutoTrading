import threading, queue, time
from telegramhandler import TelegramHandler
from handler import Handler
from senial import Senial

def main_telegram(num, qt):
    thd = TelegramHandler()

    while True:
        msn = thd.get_msn(5)
        new_msn = thd.is_new_msn(msn)

        for item in new_msn:
            qt.put(item)

        time.sleep(5)


def func2(qt, qm):
    hd = Handler()

    while not qt.empty():
        msn = qt.get()       
        senial_convert = hd.convert_msn_to_senial(msn)
        if senial_convert is not None:
            pos = hd.is_new_senial(senial_convert)
            if pos is None:
                hd._total_senials.append(senial_convert)
                qm.put(senial_convert)
            else:
                hd._total_senials[pos].set_new_text(senial_convert._text)

    
    

num = 20
q_telegram = queue.Queue()
q_mt4 = queue.Queue()

thread_telegram = threading.Thread(target=main_telegram,args=(num,q_telegram))
thread_handler = threading.Thread(target=func2,args=(q_telegram, q_mt4))
thread_mt4= threading.Thread(target=func2,args=(q_mt4))

thread_telegram.start()
thread_handler.start()