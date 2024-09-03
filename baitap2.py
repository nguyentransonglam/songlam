# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:49:35 2024

@author: nguyentransonglam
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
tong = a+b
hieu = a-b
tich = a*b
thuong = a/b
print("Tổng của 2 số:", tong)
print("Hiệu của 2 số:", hieu)
print("Tích của 2 số:", tich)
print("Thương của 2 số (làm tròn 2 chữ số):", round(thuong, 2))
print("Thương của 2 số (làm tròn 3 chữ số):", round(thuong, 3))
