# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:11:01 2024

@author: user
"""

# """JUFT SON KIRITING"""
# =============================================================================
n=int(input("Son kiriting>>> "))
if n%2==0:
    print("Raxmat!")
else:
    print("Bu son juft emas")

# """Yosh haqida"""
# yosh=int(input("Yoshingizni kiriting:>>>"))

# if yosh<4 or yosh>60:
#     print("Kirish bepul")
# elif yosh<18:
#     print("Kirish 10000 so'm")
# else:
#     print("Kirish 20000 so'm")

# """ Taqqoslash"""
# n=int(input('1-sonni kiriting:>>>'))
# m=int(input('2-sonni kiriting:>>>'))
# if n==m :
#     print('Sonlar teng!')
# elif n>m:
#     print(f"{n} soni katta")
# else:
#     print(f"{m} soni katta")
    
# mahsulotlar = ['olma', 'banan', 'anor', 'suv', 'go\'sht', 'kartoshka', 'sabzi', 'olxo\'ri', 'shaftoli', 'piyoz']
# savat=[]
# for i in range(5):
#     savat.append(input('Mahsulot kiriting:'))
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print("Mahsulot do'konimizda bor")
#         else:
#             print("Mahsulot do'konimizda yo'q")
        
# mahsulotlar = ['olma', 'banan', 'anor', 'suv', 'go\'sht', 'kartoshka', 'sabzi', 'olxo\'ri', 'shaftoli', 'piyoz']
# borlar=[]
# yoqlar=[]
# for i in range(5):
#     mahsulot = input("Mahsulot kiriting: ")
#     if mahsulot in mahsulotlar:
#         borlar.append(mahsulot)
#     else:
#         yoqlar.append(mahsulot)
# if len(yoqlar)==0:
#     print("Siz so'ragan barcha mahsulot bor")
# else:
#     print(f"Quyidagi mahsuylotlar yo'q: {yoqlar}")
    
# foydalanuvchilar=['admin', 'Sardor', 'Sarvar', 'Sanjar', 'Kalit']
# login=input("login: ")
# if login in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login}")

son=int(input("Son kiriting: "))
for i in range(2, 11):
    if son%i==0:
        print(i)

        
    


        

    
    
    