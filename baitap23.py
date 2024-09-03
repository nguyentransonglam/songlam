# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:41:00 2024

@author: nguyentransonglam
"""

import math
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))
delta = b*b-4*a*c
if delta ==0:
    x = -b/2*a
    print("Phương trình có nghiệm kép x1=x2= ",x)
elif delta >0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("x1= ",x1)
    print("x2= ",x2)
else:
    print("Phương trình vô nghiệm.")
    