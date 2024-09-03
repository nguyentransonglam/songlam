# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:09:55 2024

@author: nguyentransonglam
"""
N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if N <= 10 and N > 99:
    print("Nhập số nguyên dương có 2 chữ số")
else:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    a = hang_chuc + hang_don_vi
    print(f"Tổng các chữ số:{a}")
    
    
