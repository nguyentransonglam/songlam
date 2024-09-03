# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:57:53 2024

@author: nguyentransonglam
"""
a = int(input("Nhập giá trị a là: "))
b = int(input("Nhập giá trị b là: "))
c = int(input("Nhập giá trị c là: "))
gia_tri_lon_nhat = a
if b > gia_tri_lon_nhat:
    gia_tri_lon_nhat = b
if c > gia_tri_lon_nhat:
    gia_tri_lon_nhat = c
print(f"Giá trị lớn nhất là: {gia_tri_lon_nhat}")
