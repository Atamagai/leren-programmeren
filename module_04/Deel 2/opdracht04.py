import random
from fruitmand import fruitmand

getal = int(input("Voer een getal in: "))

i = random.choice(fruitmand)
for x in range (getal):
    print(i["name"])