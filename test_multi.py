#!/usr/bin/python3
import _thread
import time

from test_class_multi import run_Cliente
from test_class_multi import run_Servidor

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s -- Count: %s" % ( threadName, time.ctime(time.time()), str(count) ))

# Create two threads as follows
try:
   _thread.start_new_thread( run_Test, ("Thread-1", ) )
   #_thread.start_new_thread( run_Servidor, ("Thread-2", ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass