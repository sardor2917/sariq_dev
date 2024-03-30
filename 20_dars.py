# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:50:57 2024

@author: user
"""

# def shaxs_info(ism, familiya, t_yil, email=None, t_raqam=None):
#     shaxs={
#         'ism':ism,
#         'familiya':familiya,
#         't_yil':t_yil,
#         'yoshi':2024-t_yil,
#         'email':email,
#         't_raqam':t_raqam
#         }
#     return shaxs
# # print(shaxs_info('sardor', 'ravshanov', 2000, 24, 'sardorravshanov23@gmail.com'))

# print("Mijoz haqida ma'lumotlarni kiriting!")
# shaxslar=[]
# while True:
#     ism = input('Ismingizni kiriting:')
#     familiya=input('Familiyangizni kiriting: ')
#     t_yil=int(input("Tug'ilgana yilingizni kiriting:"))
#     email=input("Email:")
#     t_raqam=input('Telefon raqamingizni kiriting:')
#     natija=shaxs_info(ism, familiya, t_yil,email,t_raqam)
#     shaxslar.append(natija)
#     savol=input('Yana foydalanuvchi qo\'shasizmi(ha/yo\'q):')
#     if savol=="yo'q":
#         break
# for i in shaxslar:
#     print(f"{i['ism'].title()} {i['familiya'].title()} {i['t_yil']}-yilda tug\'ilgan. {i['yoshi']} yoshda. "
#           f"Tel raqami {i['t_raqami']}")
    
# def taqqosla(s1,s2,s3,s4,s5):
#     sonlar=[s1,s2,s3,s4,s5]
#     max=s1
#     for son in sonlar:
#         if max<son:
#             max=son
#     return max
# print(taqqosla(25,45,198,25,200))                   
                    
# def aylana(r, pi=3.14):
#     info={
#         'radius':r,
#         'diametr':2*r,
#         'perimetr':2*pi*r,
#         'yuza':pi*r**2
#         }   
#     return info
# print(aylana(2))         

# def tub_son(min, max):
#     s=list(range(min, max+1))
#     if min==1:
#         s.remove(min)
#     for i in range(min,max+1):
#         for j in range(1,int(i*(0.5))+1):
#             if i%j==0 and j!=1:
#                 s.remove(i)
#                 break
#     return s

# print(tub_son(1, 11))

# def finobacci(son):
#     s=[1]
#     i=1
#     while i<=son:
#         s.append(i)
#         i=s[-1]+s[-2]
#     return s
# print(finobacci(56))
        
        