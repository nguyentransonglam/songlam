# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:44:50 2024

@author: nguyentransonglam
"""
import math
a = float(input("Nhập giá trị a:"))
b = float(input("Nhập giá trị b:"))
A = (math.sqrt(a)-math.sqrt(b)) / ((math.pow(a, 1/4))-(math.pow(b, 1/4)))
B = (math.sqrt(a)+(math.pow(a+b, 1/4))) / (math.pow(a, 1/4))+(math.pow(b, 1/4))
print("Kết quả là ", A-B)