import random

Kleuren = ("oranje", "blauw", "groen", "bruin")

zakje = []
repeat = True

while repeat == True:
    try:
        aantalMs = int(input("Voer een getal in: "))
        if aantalMs >= 1:
            repeat = False
            for i in range(aantalMs):
                MMs = random.choice(Kleuren)
                zakje.append(MMs)
        
        else:
            repeat = True
            print("Het getal moet hoger dan 1 zijn!")
                
    except Exception as error:
        print("Dat is geen getal!")

print(zakje)
