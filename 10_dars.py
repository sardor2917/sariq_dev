# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:57:44 2024

@author: user
"""

cars=['toyoto', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())


ism = input('Login: ')
if ism.lower()=='admin':
    print(f"Xush kelibsiz, Admin. Foydalanuvchi ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {ism.title()}")
    
son1=input('Birinchi sonni kiriting:')
son2=input('Ikkinchi sonni kiriting:')
if son1==son2:
    print('Sonlar teng!')