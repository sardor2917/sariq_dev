# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:39:50 2024

@author: user
"""

# mahsulot=[]
# while True:
#     buyurtma=input("Buyurtma bering: ")
#     mahsulot.append(buyurtma)
#     savol=input("Buyurtma qo'shasizmi(ha/yo'q): ")
#     if savol=='yo\'q':
#         break
bozor={}    
while True:
    mahsulot=input("Mahsulotni kiriing: ")
    narx=input(f"{mahsulot} narxini kiriting: ")
    bozor[mahsulot]=narx
    savol=input("Yana mahsulot kiritasizmi?(ha/yo'q): ")
    if savol=="yo'q":
        break
    

mahsulot=[]
while True:
    buyurtma=input("Buyurtma bering: ")
    mahsulot.append(buyurtma)
    savol=input("Buyurtma qo'shasizmi(ha/yo'q): ")
    if savol=='yo\'q':
        break

for i in mahsulot:
    if i in bozor:
        print(f"{i}ning narxi {bozor[i]} so'm")
    else:
        print(f"Bizda {i} yo'q")