import threading, queue, time
from telegramhandler import TelegramHandler
from handler import Handler
from senial import Senial
from mt4handler import Mt4Handler
from aux_function import tprint

def main_telegram(num, qt):
    thd = TelegramHandler()
    tprint("Inicializado el lector de telegram")

    while True:
        msn = thd.get_msn_demo(5)
        #msn = thd.get_msn(5)
        new_msn = thd.is_new_msn(msn)

        for item in new_msn:
            qt.put(item)

        time.sleep(5)


def func2(qt, qm):
    hd = Handler()
    tprint("Inicializado el manejador de mensajes")

    while True:

        if qt.qsize() > 0:
            msn = qt.get()
            tprint("Handler - Nuevo mensaje")
                
            senial_convert = hd.convert_msn_to_senial(msn)
            if senial_convert is not None:
                tprint("Handler - El mensaje es una senial")
                pos = hd.is_new_senial(senial_convert)
                if pos is None:
                    tprint("Handler - La senial es nueva")
                    hd._total_senials.append(senial_convert)
                    qm.put(senial_convert)
                else:
                    tprint("Handler - La senial es antigua")
                    hd._total_senials[pos].set_new_text(senial_convert._text)

        else:
            tprint("Handler - Ningún mensaje")
            time.sleep(2)

def func3(qm):
    hmt4 = Mt4Handler()
    tprint("inicializado el mt4")

    while not qm.empty():
        sen = qm.get()
        _trade = hmt4.convert_senial_to_trade(sen)
        hmt4.new_operation(_trade)


num = 20
q_telegram = queue.Queue()
q_mt4 = queue.Queue()

thread_telegram = threading.Thread(target=main_telegram,args=(num,q_telegram))
thread_handler = threading.Thread(target=func2,args=(q_telegram, q_mt4))
thread_mt4= threading.Thread(target=func3,args=(q_mt4))

thread_telegram.start()
thread_handler.start()