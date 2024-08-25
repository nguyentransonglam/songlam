# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:13:06 2024

@author: nguyentransonglam
"""
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))

tong_so_giay = gio * 3600 + phut * 60 + giay
if gio >24:
    print("Giờ không hợp lệ")
elif gio <24:
    print("Giờ hợp lệ.")
    
    print("Tổng số giây là:", tong_so_giay)