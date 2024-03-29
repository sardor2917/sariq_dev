# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:33:00 2024

@author: user
"""

# i_l={'integer':'butun son', 'float':'kasr son', 'if': 'agar','else':'aks holda', 'string':'satr'}
# for key, value in i_l.items():
#     print(f"{key} - {value}")

# poytaxtlar={'turkiya':'anqara','rossiya':'moskva','germaniya':'berlin', 'avstraliya':'kanberra','avstriya':'vena'}
# for key in sorted(poytaxtlar):
#     print(key.title())
    
# for value in sorted(poytaxtlar.values()):
#     print(value.title())

# davlat=input('Davlatni kiriting:')
# print(poytaxtlar.get(davlat.lower(), 'Bunday davlat mavjud emas').title())

menu={'osh':25000, 'shorva': 30000, 'manti': 8000, 'shashlik': 17000, 'jiz':80000}
taom=[]
for i in range(3):
    taom.append(input(f"{i+1}-taomni kiriting: "))
for j in taom:
    if j in menu:
        print(f"{j}ning narxi {menu[j]} so'm")
    else:
        print("Bizda bunday taom yo'q")
       