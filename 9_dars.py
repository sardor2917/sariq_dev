# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:32:24 2024

@author: user
"""

ismlar=['Anvar', 'Siroj', 'Sharof', 'Begzod', 'Erkin']
for ism in ismlar:
    print(f"Qalinroq kiyin {ism}")
print(f"Kod {len(ismlar)} marta takrorlandi")
sonlar=list(range(11,100,2))
kinolar=[]
for k in range(5):
    kinolar.append(input(f"{k+1}-kinoni kiriting: "))
print(kinolar)