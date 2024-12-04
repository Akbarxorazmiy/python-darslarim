# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:44:43 2024

@author: HOME
"""

# mahsulot = ['non','choy', 'un','yog', 'tuxum', 'uzum', 'banan','shakar', 'novvot', 'uzum']
# savat = []
# for n in range(1,6):
#     savat.append(input(f"{n} -mahsulotni kiriting:"))
    
# bor_mahsulotlar = []
# mavjud_emas = []
    
# for max in savat:
#     if max in mahsulot:
#         bor_mahsulotlar.append(max)
#     else:
#         mavjud_emas.append(max)
        
# if mavjud_emas:
#     print("quyidagi mahsulotlar do'konimizda yo'q: ")
#     print(mavjud_emas)
# else:
#     print("Do'konimizda siz so'ragan barcha mahsulotlar bor")


# foydalanuvchilar =['Aziz', 'Admin', 'Zafar', 'Akbar', 'Firdavs']
# login = input("Yangi login tanlang:")
# x=len(foydalanuvchilar)

# for log in foydalanuvchilar:
#     if login.lower() in log.lower():
#         print("Login band, yangi login tanlang!")
#     else:
#         print("Xush kelibsiz, foydalanuvchi!")
    
x = int(input("Istalgan butun son kiriting:"))

for m in range(2,11):
    if x%m==0:
        print(f"{x} soni {m} ga qoldiqsiz bo'linadi")
        
































