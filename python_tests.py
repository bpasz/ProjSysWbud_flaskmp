# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:52:10 2019

@author: bartl
"""

a=5
b=5
def func():
    global a
    a,b=10,10
    print(a)
    print(b)
