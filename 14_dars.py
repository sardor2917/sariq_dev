# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:06:07 2024

@author: user
# """
# ukam={'ismi':'sanjar', 'tugilgan_yili':2003, 'shahri':'navoiy', 'manzili':'navbahor tumani halovattepa mahallasi'}
# print(f"Ukamning ismi {ukam['ismi'].title()}, {ukam['tugilgan_yili']}-yilda, {ukam['shahri'].title()} shahrida tug'ilgan")

# sevimli_taomlar={'dadam':'osh', 'onam':'somsa', 'men':'qovurdoq','ukam': 'baliq', 'xotinim':'manti'}
# print(f"Dadamning sevimli taomi {sevimli_taomlar['dadam']}")
# print(f"Onamning sevimli taomi {sevimli_taomlar['onam']}")
# print(f"Ukamning sevimli taomi {sevimli_taomlar['ukam']}")

i_l={'integer':'butun son', 'float':'kasr son', 'if': 'agar','else':'aks holda', 'string':'satr'}
soz=input("So'z kiriting:>>> ")
# print(i_l.get(soz,'Bunday soz mavjud emas'))
if i_l.get(soz)!=None:
    print(i_l[soz])
else:
    print('Bunday qiymat mavjud emas')

    