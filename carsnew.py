# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:02:07 2024

@author: HOME
"""

# cars = ['toyota', 'mazda', 'hyudai', 'gm', 'kia']
# for car in cars:
#     if car.lower() != 'gm' and car.lower() !='kia':
#         print(car.title())
#     else:
#         print(car.upper())
        
# foydalanuvchi_ismi=input("Login ismigizni kiriting:")
# if foydalanuvchi_ismi.lower()=='admin':
#     print("Xush kelibsiz Admin. \nFoydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {foydalanuvchi_ismi.title()}")
    
# x,y = float(input("Birinchi sonni kiriting:")), float(input("Ikkinchi sonni kiriting:"))
# if x==y:
#     print(f"{x} va {y} o'zaro teng")
# else: print("Sonlar teng emas!")
# son=float(input("Istalgan son kiriting:"))
# if son>0:
#     print("Musbat son")
# elif son<0:
#     print("Son manfiy")
# else: print("Son o ga teng")

# son=float(input("Istalgan son kiriting:"))
# if son>0:
#     print(f"Sonning ildiz, {son**0.5} ga teng")
# else: print("Musbat son kiriting")

# mahsulot = ['non','choy', 'un','yog', 'tuxum', 'uzum', 'banan','shakar', 'novvot', 'uzum']
# savat = []
# for n in range(1,6):
#     savat.append(input(f"{n} -mahsulotni kiriting:"))
    
# for max in savat:
#     if max in mahsulot:
#         print(f"Do'konimizda {max} bor")
#     else:
#         print(f"Do'konimizda {max} yo'q")
        
mahsulot = ['non','choy', 'un','yog', 'tuxum', 'uzum', 'banan','shakar', 'novvot', 'uzum']
savat = []
for n in range(1,6):
    savat.append(input(f"{n} -mahsulotni kiriting:"))
    
bor_mahsulotlar = []
mavjud_emas = []
    
for max in savat:
    if max in mahsulot:
        bor_mahsulotlar.append(max)
    else:
        mavjud_emas.append(max)
        
if len(mavjud_emas)==0:
    print("Do'konimizda siz so'ragan barcha mahsulotlar bor")
else:
    print(f"quyidagi mahsuklotlar dokonimizda yo'q: {mavjud_emas}")
    

    