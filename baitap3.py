# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:52:57 2024

@author: nguyentransonglam
"""
N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if N <= 10 or N > 99:
    print("Nhập số nguyên dương có 2 chữ số")
else:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    a = hang_chuc + hang_don_vi
    print(f"Tổng các chữ số:{a}")
    
    
