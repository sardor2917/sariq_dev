# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:23:25 2024

@author: user
"""

# savol="Kitob kiriting (dasturni to'xtatish uchun'stop' so'zini kiriting): "
# kitob=''
# while kitob!='stop':
#     kitob=input(savol)
    
# print("Dastur tugadi")

# y=input("Yoshingizni kiriting:")
# while y!='exit' and y!='quit':

#     if int(y)<7:
#         print('2000 so\'m')
#     elif int(y)<18:
#         print('3000 so\'m')
#     elif int(y)<65:
#         print('10000 so\'m')
#     else:
#         print('Kirish bepul')
#     y=input("Yoshingizni kiriting:")
# print('Tugadi')

# y=input("Yoshingizni kiriting:")
# ishora=True
# while ishora:
#     y=input("Yoshingizni kiriting:")
#     if y=='exit' or y=='quit':
#         ishora=False
#     elif int(y)<7:
#         print('2000 so\'m')
#     elif int(y)<18:
#         print('3000 so\'m')
#     elif int(y)<65:
#         print('10000 so\'m')
#     else:
#         print('Kirish bepul')

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue    
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
print('Tugadi')