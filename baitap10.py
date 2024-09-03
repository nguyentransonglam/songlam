# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:11:40 2024

@author: nguyentransonglam
"""
bien_so = int(input("Nhập biển số xe (4 chữ số): "))
a = bien_so // 1000
b = (bien_so % 1000)//100
c = ((bien_so % 1000)%100)//10
d = bien_so % 10
tong_cac_chu_so = a+b+c+d
so_nut = tong_cac_chu_so % 10
print("Số nút của biển số xe là:", so_nut)