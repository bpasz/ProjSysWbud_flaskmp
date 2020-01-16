# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 00:48:03 2020

@author: bartl
"""


import time
import os


def led(d):
    licznik=0
    while True:
#        if d["state"]=="go":
#            print("Stan go")
#        else:
#            print("nie go")
        print(d["state"])
        print("Lcznik %d ",licznik)
        print("Process pid ",os.getpid())
        licznik=licznik+1
        #print("akakaka")
        time.sleep(2)
        


    
   
