# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:14:51 2024

@author: nguyentransonglam
"""
thoi_gian = input("Nhập thời gian vào theo định dạng hh:mm:ss là:  ")
gio,phut,giay = map(int, thoi_gian.split(':'))
doi_ra_giay = gio*3600 + phut*60 +60
print(f"Tổng số giây là:", doi_ra_giay)
