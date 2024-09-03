# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:22:06 2024

@author: nguyentransonglam
"""
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
a = f"{ngay}/{thang}/{nam}"
b = f"{ngay}/{thang}/{str(nam) [2:]}"
c = f"{nam}/{thang}/{ngay}"

print("a)", a)
print("b)", b)
print("c)", c)

#ngược lại
cau_a= input("Nhập theo định dạng Ngày/Tháng/Năm: ")
cau_b= input("Nhập theo định dạng Ngày/Tháng/2 số cuối của Năm: ")
cau_c= input("Nhập theo định dạng Năm/Tháng/Ngày: ")

dda, mma, yyyya = map(int, cau_a.split("/"))
ddb, mmb, yyyyb = map(int, cau_b.split("/"))
ddc, mmc, yyyyc = map(int, cau_c.split("/"))
print("Kết quả định dạng a: ", dda, mma, yyyya)
print("Kết quả định dạng b: ", ddb, mmb, yyyyb)
print("Kết quả định dạng c: ", ddc, mmc, yyyyc)