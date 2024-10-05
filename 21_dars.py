# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         for ism in ismlar:
#         # ism = ismlar.pop()
#             baho = input(f"talaba {ism.title()}ning bahosini kiriting: ")
#             baholar[ism]=baho
#     return baholar
# talabalar = ['ali', 'vali', 'hasan']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)
# AMALIYOT
# def katta(matn):
#     natija = []
#     while matn:
#         soz = matn.pop()
#         natija.append(soz.title())
#     return natija
# talabalar = ['ali', 'vali', 'hasan']
# natija = katta(talabalar[:])
# print(natija)
# print(talabalar)


def bahola(ismlar):
    baholar = {}

    for ism in ismlar:
    # ism = ismlar.pop()
        baho = input(f"talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
talabalar = ['ali', 'vali', 'hasan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)
