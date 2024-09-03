# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:37:00 2024

@author: nguyentransonglam
"""
nam_sinh = int(input("Nhập năm sinh của bạn là: "))
nam_hien_tai = int(input("Nhập năm hiện tại là: "))
so_tuoi = nam_hien_tai - nam_sinh
print(f"Bạn sinh năm {nam_hien_tai} vay ban {so_tuoi} tuổi.")
