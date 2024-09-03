# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:05:32 2024

@author: nguyentransonglam
"""
import math
loai_hinh = input("Nhập hình (v:hình vuông, n:hình chữ nhật, t:hình tròn):  ")
if loai_hinh == 'v':
    print("Tính S và P của hình vuông")
    a = float(input("Độ dài cạnh: "))
    S = a ** 2
    P = a * 4
    print(f"Kết quả: Diện tích = {S}, Chu vi = {P}")
elif loai_hinh == 'n':
    print("Tính S và P của hình chữ nhật")
    a = float(input("Nhập chiều rộng: "))
    b = float(input("Nhập chiều dài: "))
    S = a * b
    P = (a + b) * 2
    print(f"Kết quả: Diện tích = {S}, Chu vi = {P}")
elif loai_hinh == 't':
    print("Tính S và P của hình tròn")
    r = float(input("Bán kính hình tròn: "))
    S = pow(r, 2) * math.pi
    P = 2 * math.pi * r
    print(f"Kết quả: Diện tích = {S}, Chu vi = {P}")
else:
    print("Vui lòng nhập lại loại hình.")
