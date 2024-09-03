# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:47:55 2024

@author: nguyentransonglam
"""
a = int(input("Nhập số nguyên a là: "))
b = int(input("Nhập số nguyên b là: "))
c = int(input("Nhập số nguyên c là: "))
d = int(input("Nhập số nguyên d là: "))
gia_tri_nho_nhat = a
if b < gia_tri_nho_nhat:
    gia_tri_nho_nhat = b
if c < gia_tri_nho_nhat:
    gia_tri_nho_nhat = c
if d < gia_tri_nho_nhat:
    gia_tri_nho_nhat = d
print(f"Giá trị nhỏ nhất là: {gia_tri_nho_nhat}")
        
