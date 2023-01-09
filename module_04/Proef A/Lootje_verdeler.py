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
                print("aantal namen kleiner dan 3")
                print ("je moet minimaal 3 namen invoeren\nvoer a.u.b meer namen in")
                repeat = True


lootjes = namen.copy() 
random.shuffle(lootjes)
repeat1 = True

uitslag = {} 

while repeat1 == True: 
    for x in namen:
        uitslag[x] = lootjes.pop(0)
        repeat1 = False

    for i in uitslag:
        if uitslag[i] == i: 
            repeat1 = True

print (uitslag)


    