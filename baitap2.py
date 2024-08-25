# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:29:05 2024

@author: NguyenTranSongLam
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
chia_lay_du = a % b
chia_lay_nguyen = a // b


print("Tổng của 2 số:", tong)
print("Hiệu của 2 số:", hieu)
print("Tích của 2 số:", tich)
print("Thương của 2 số (làm tròn 2 chữ số):", round(thuong, 2))
print("Thương của 2 số (làm tròn 3 chữ số):", round(thuong, 3))
print("Chia lấy dư của 2 số:", chia_lay_du)
print("Chia lấy nguyên của 2 số:", chia_lay_nguyen)