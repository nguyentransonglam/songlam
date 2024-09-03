# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:37:47 2024

@author: nguyentransonglam
"""
thoi_gian = input("Nhập vào đây giờ phút giây hh:mm:ss là: ")
gio, phut, giay = map(int, thoi_gian.split(":"))
if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
    print("Giờ, phút, giây hợp lệ.")
else:
    print("Giờ, phút, giây không hợp lệ.")
     