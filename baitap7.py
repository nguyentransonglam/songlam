# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:42:03 2024

@author: nguyentransonglam
"""
import math
ban_kinh = float(input("Nhập vào bán kính hình tròn là: "))
chu_vi = 2*math.pi*ban_kinh
dien_tich = math.pi * ban_kinh**2
print("Chu vi hình tròn là:", chu_vi)
print("Diện tích hình tròn là:", dien_tich)