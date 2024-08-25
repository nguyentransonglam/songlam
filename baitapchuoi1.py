# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:19:25 2024

@author: lam
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
#nhap = nhap.split(", ")
#print(nhap)
nhap = chuoi.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "")
sub_string=nhap.split(", ")
for sub in sub_string:
    print(sub)