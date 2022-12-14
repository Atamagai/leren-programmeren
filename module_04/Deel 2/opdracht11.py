from fruitmand import fruitmand
Klijst = ['yellow', 'green', 'orange', 'brown', 'red']
repeat = True
rounde = 0
Nrounde = 0

while repeat == True:
    kleur = input("Kies een kleur: ['yellow', 'green', 'orange', 'brown', 'red']\n").lower()

    if kleur in Klijst:
        repeat = False
        for fruit in fruitmand:
            if kleur == fruit["color"]:
                print(fruit["name"])
                if fruit["round"] == True and kleur == fruit["color"]:
                    rounde = rounde + 1 
                elif fruit["round"] == False and kleur == fruit["color"]:
                    Nrounde = Nrounde + 1             
    else:
        print("Gekozen kleur bestaat niet, kies a.u.b een andere kleur:")
        repeat = True


print(rounde)
print(Nrounde)
meerronde = rounde - Nrounde
minderronde = Nrounde - rounde

if rounde > Nrounde :
    print(" Er zijn "+ str(meerronde) +" meer ronde vruchten dan niet ronde vruchten in de kleur " + kleur  )

elif Nrounde > rounde :
    print(" Er zijn " + str(minderronde) + " minder ronde vruchten dan niet ronde vruchten in de kleur " + kleur )

elif Nrounde == rounde:
    print ("Er zijn "+ str(rounde)+" ronde vruchten en "+str(Nrounde) + " niet ronde vruchten in de kleur " + kleur)

