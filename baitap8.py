# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:50:30 2024

@author: nguyentransonglam
"""
can_nang = float(input("Nhập vào số cân nặng là(kg): "))
chieu_cao = float(input("Nhập vào chiều cao là(m): "))
BMI = can_nang/(chieu_cao*chieu_cao)
print("Số đo kiểm tra sức khỏe BMI là:", BMI)
