# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:41:31 2024

@author: nguyentransonglam
"""
print("Bài 26a:")
a = float(input("Nhập số nguyên a là : "))
b = float(input("Nhập số nguyên b là: "))
c = float(input("Nhập số nguyên c là: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(f"Các số theo thứ tự tăng dần là: {a}, {b}, {c}")

print("Bài 26b:")
N = input("Nhập số nguyên bất kì dưới dạng chuỗi: ")
so = sorted(N)
so_sap_xep = ''.join(so)
print(f"Số có các chữ số theo thứ tự tăng dần là: {so_sap_xep}")