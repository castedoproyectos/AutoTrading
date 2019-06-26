import time
from senial import Senial

senials = list()

fil = open("test_data.txt", 'r')
rows = fil.readlines()

while True:
    time.sleep(5)
    for row in rows:
        s = Senial(row)
        if s._real_senial is True:
            if len(senials) is 0:
                senials.append(s)
            else:
                for item in senials:
                    if s._raw_info is item._raw_info:
                        senials.append(s)
                        print('Add')


