# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:58:48 2024

@author: nguyentransonglam
"""
chu_cai = input("Nhập 1 chữ cái bất kỳ: ")
if chu_cai.islower():
   chu_cai = chu_cai.upper()
   print("Chữ cái sau khi chuyển đổi là: ",chu_cai)
elif chu_cai.isupper():
    chu_cai = chu_cai.lower()
    print("Chữ cái sau khi chuyển đổi là:", chu_cai)
else:
    print("Chữ cái này không hợp lệ.")
