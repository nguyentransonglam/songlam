# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:05:01 2024

@author: nguyentransonglam
"""
import math
a = float(input("Nhập số vào a là: "))
b = float(input("Nhập số vào b là: "))
A = ((a+b)/(math.pow(a,1/3)+math.pow(b,1/3))) - (math.pow(a*b,1/3))
B = ((math.pow(a,1/3))-(math.pow(b,1/3)))**2
print("Kết quả là: ", A/B)