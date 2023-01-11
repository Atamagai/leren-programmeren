import random
repeat = True
namen = []

while repeat == True:

    naam = input ("Voer een naam in: \n").lower()
    
    if naam in namen:
        print ("deze naam bestaat al!")
    
    else: 
        namen.append(naam)
        meernamen = input ("wil je meer namen toevoegen?").lower()


        if meernamen == "ja":
            repeat = True
        
        elif meernamen == "nee":
            lengtelijst = len(namen)
            repeat = False

            if int(lengtelijst) >= 3:
                repeat = False

            else:
                print ("je moet minimaal 3 namen invoeren\nvoer a.u.b meer namen in")
                repeat = True


random.shuffle(namen)
x = 0

print("Hier is je lijst met lootjes:\n")

for i in range (len(namen)-1):
    print("'" + namen[x] + "'" + " heeft " + "'" + namen[x + 1] + "'")
    x = x + 1
print("'" + namen[-1] + "'" + " heeft " + "'" + namen[0] + "'")
