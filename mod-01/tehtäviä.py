# print("Hei, Onnipekka Sorjonen")

# nimi = input("Anna nimesi: ")
# print(f"Terve {nimi}")

# pi = 3.14
# ymp = int(input("Anna ympyrän säde, niin lasken sen pinta-alan: "))
# pintaala = ymp**2 * pi
# print(pintaala)

# print("Suorakulmion piirin ja pinta-alan laskuri")
# korkeus = int(input("Syötä suorakulmion korkeus: "))
# kanta = int(input("Syötä suorakulmion kanta: "))
# piiri = 2 * korkeus + 2 * kanta
# pintaala = korkeus * kanta
# print(f"Suorakulmion piiri on {piiri}, ja pinta-ala on {pintaala}.")

# print("Summa-, tulo- ja keskiarvolaskuri")
# summa1 = int(input("Anna ensimmäinen luku: "))
# summa3 = int(input("Anna kolmas luku: "))
# summa = summa1 + summa2 + summa3
# keskiarvo = summa / 3
# tulo = summa1 * summa2 * summa3
# print(f"Summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo}.")

# print("Keskiaikaisten mittojen muuntaja nykyaikaisiin mittoihin")
# leiviska = int(input("Leiviskät: "))
# naula = int(input("Naulat: "))
# luoti = int(input("Luodit: "))
# lei = leiviska * 20 * 32 * 13.3
# nau = naula * 32 * 13.3
# luo = luoti * 13.3
# summa = int((lei + nau + luo) / 1000)
# gr = (lei + nau + luo)%1000
# print(f"{summa} kiloa ja{gr: .0f} grammaa.")

import random
from stringprep import b1_set

a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
print(f"Kolminumeroinen koodi: {a}{b}{c}")

a1 = random.randint(1,6)
b1 = random.randint(1,6)
c1 = random.randint(1,6)
d = random.randint(1,6)
print(f"Nelinumeroinen koodi: {a1}{b1}{c1}{d}")



