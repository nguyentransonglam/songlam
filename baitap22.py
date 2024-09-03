# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:03:34 2024

@author: nguyentransonglam
"""
a = float(input("Nhập giá trị a là: "))
b = float(input("Nhập giá trị b là: "))
if a == b and b == 0:
    print("Phương trình vô số nghiệm")
elif a != 0 and b == 0:
    print("Phương trình vô nghiệm")
elif a == 0 and b == 0:
    print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Phương trình có nghiệm là:", x)
