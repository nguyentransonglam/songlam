# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:59:44 2024

@author: nguyentransonglam
"""

print("============ MENU ============ ")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("============================== ")
chon_mon = input("Moi nhap lua chon: " )
print("============================== ")
if chon_mon == '1':
    print("Ban chon hu tieu.")
elif chon_mon == '2':
    print("Ban chon chao long.")
elif chon_mon == '3':
    print("Ban chon banh canh.")
elif chon_mon == '4':
    print("Ban chon bun rieu.")
elif chon_mon == '5':
    print("Ban chon pho bo.")
else:
    print("Chon mon co trong menu.")