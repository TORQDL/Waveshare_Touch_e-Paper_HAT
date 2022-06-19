#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
    
from TP_lib import icnt86
from TP_lib import epd2in9_V2

import time 
import logging
import traceback
import threading

logging.basicConfig(level=logging.DEBUG)
flag_t = 1

def pthread_irq() :
    print("pthread irq running")
    while flag_t == 1 :
        if(tp.digital_read(tp.INT) == 0) :
            ICNT_Dev.Touch = 1
        else :
            ICNT_Dev.Touch = 0
        time.sleep(0.01)
    print("thread irq: exit")

try:
    logging.info("epd2in9_V2 Clear Screen")
    
    epd = epd2in9_V2.EPD_2IN9_V2()
    tp = icnt86.INCT86()
    
    ICNT_Dev = icnt86.ICNT_Development()
    ICNT_Old = icnt86.ICNT_Development()
    
    logging.info("init and Clear")
    epd.init()
    tp.ICNT_Init()
    epd.Clear(0xFF)

    t1 = threading.Thread(target = pthread_irq)
    t1.setDaemon(True)
    t1.start()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    flag_t = 0
    epd.sleep()
    time.sleep(2)
    t1.join()
    epd.Dev_exit()
    exit()
