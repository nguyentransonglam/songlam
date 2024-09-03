# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:00:01 2024

@author: nguyentransonglam
"""
chu_thuong = input("Nhập ký tự chữ thường: ")
chu_hoa = chu_thuong.upper()
if chu_thuong.islower():
    print("Ký tự chữ hoa tương ứng là: ", chu_hoa)
else:
    print("Nhập lại ký tự thường.")
