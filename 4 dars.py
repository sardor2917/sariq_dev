# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:52:37 2024

@author: user
"""
matn="Men 😀"
print(matn)
ism = 'Sardor '
print("Mening ismim "+ism)
familiya="Ravshanov"
print(f"{ism}\n{familiya}")
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{viloyat} viloyati, {tuman} tumani, {mahalla} mahallasi, {kocha} ko\'chasi")
kocha=input("Ko'cha nomini kiriting:\n>>>")
mahalla=input("Mahalla nomini kiriting:\n>>>")
tuman=input("Tuman nomini kiriting:\n>>>")
viloyat=input("Viloyat nomini kiriting:\n>>>")
manzil=f"{viloyat.title()} viloyati,\n{tuman.upper()} tumani,\n{mahalla.lower()} mahallasi,\n{kocha} ko\'chasi"
print(manzil)
