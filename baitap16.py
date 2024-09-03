# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:19:48 2024

@author: nguyentransonglam
"""
thoi_gian = input("Nhập số (giờ phút giây: ")
gio, phut, giay = map(int, thoi_gian.split(" "))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là: ", tong_giay)
