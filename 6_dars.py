# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:52:40 2024

@author: user
"""

mevalar=['olma', 'anjir', 'shaftoli', "o'rik"]
narxlar=[12000, 18000, 10800, 22000]
ism=['Anvar', 'Begzod', 'Malik' ]
print('Salom '+ism[0]+', bugun choyxona bormi?')
print(ism[1]+', choyxonaga boramizmi?')
sonlar=[12, 6.3, 45, -23.5,-89]
print(sonlar[0]+sonlar[2])
sonlar[1]=7
sonlar[3]=sonlar[3]+25.5
print(sonlar)
t_shaxslar=['Amir Temur', 'Bobur Mirzo', "Alisher Navoiy"]
z_shaxslar=['Ilon Mask', 'Bill Gates']
print('Men tarixiy shaxslardan '+t_shaxslar[0]+' bilan, zamonaviy shaxslardan esa '+z_shaxslar[0]+' bilan suhbat qilishni istar edim' )
friends=[]
friends.append('Anvar')
friends.append('Begzod')
friends.append('Rustam')
print(friends)
friends.remove('Begzod')
print(friends)
friends.insert(0, 'Asilbek')
print(friends)
friends.insert(2, 'Asilbek')
friends
dost1=friends.pop(0)
dost2=friends.pop(2)
mehmonlar=[]
mehmonlar.append(dost1)
mehmonlar.append(dost2)
print(mehmonlar)