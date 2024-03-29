# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:46:49 2024

@author: user
"""

# shaxs1={
#         'ism':'bil',
#         'familiya':'geyts',
#         'kasbi':'dasturchi',
#         'millati':'ingliz',
#         'asarlari':['odamlar','boy bo\'lish sirlari','ikki odam']
#         }

# shaxs2={
#         'ism':'stiv',
#         'familiya':'jobs',
#         'kasbi':'muhandis',
#         'millati':'britan',
#         'asarlari':['kompyuter','tadqiqot', 'olimlar']
#         }

# shaxs3={
#         'ism':'ronaldo',
#         'familiya':'krishtiano',
#         'kasbi':'futbolchi',
#         'millati':'portugal',
#         'asarlari':['real madrid', 'yunayted', 'al_nasr']
#         }

# shaxs4={
#         'ism':'ilon',
#         'familiya':'mask',
#         'kasbi':'injener',
#         'millati':'fransuz',
#         'asarlari':['kimsa','dunyo','shahar']
#         }

# shaxs=[shaxs1,shaxs2,shaxs3,shaxs4]

# for i in shaxs:
#     print(f"\n{i['ism'].title()} {i['familiya'].title()}, "
#           f"Millati {i['millati'].title()}. "
#           f"Kasbi {i['kasbi']} "
#           "Quyidagi asarlari mavjud:")
#     for k in i['asarlari']:
#         print(f"{k.title()}", end=', ')
    
# kinolar={
#     'ali':['terminator','rux','jazo'],
#     'hakim':['muhabbat','yurak','sevginator'],
#     'bilol':['bespredel','panda', 'o\'rdak']
#     }

# for ism, kino in kinolar.items():
#     print(f"{ism.title()} quyidagi kinolarni yoqtiradi:")
#     for i in kino:
#         print(f"{i.title()}")
        
davlatlar={
    'tojikiston':{'poytaxti':'dushanbe',
                  'm':1992,
                  'v':12
                  },
    'qirg\'iziston':{'poytaxti':'bishkek',
                     'm':1991,
                     'v':10
                     },
    'afg\'oniston':{'poytaxti':'kobul',
                    'm':1989,
                    'v':23
                    }
    }
d=input('Davlatni kiriting:')

if d.lower() in davlatlar:
    info=davlatlar[d.lower()]
    print(f"{d.title()} Respublikasi",
          f"Poytaxti {info['poytaxti'].title()} shahri",
          f"{info['m']}-yil mustaqil bo'lgan",
          f"{info['v']} ta viloyatga ega"
          )
else:
    print("Bizda bu davlat mavjud emas")
        


