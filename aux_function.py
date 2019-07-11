
import datetime


def tprint(text):
    
    dt = datetime.datetime.now()
    first = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second) + "." + str(round(dt.microsecond,4))
    second = str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)

    all = first + " " + second
    print(all + "\t" + text)


def get_time():
    dt = datetime.datetime.now()
    first = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second) + "." + str(round(dt.microsecond,4))
    second = str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)

    all = first + " " + second
    return all