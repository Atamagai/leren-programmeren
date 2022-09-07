# Emad Hajiabadi
# opdracht: Pizza calculator

naam_resturant = "Piazza della vita"

print("welkom bij ", naam_resturant)
print("Op welke naam wilt u een bestelling plaatsen? ")
naam = input()
mymenu= ["Large {€12}", "Medium {€10}", "Small {€7}"]
# menu en prijzen zodat de klant weet welke grote hoeveel kost.
repeat = True 

while repeat == True:
    print("Hallo "+ naam +  " welke grote pizza wilt u? "+ str(mymenu))
    vraag = x =input(" Maak nu a.u.b een keuze:  ")

    if vraag == "Large":
        repeat = False 
        print("Voer nu het aantal in: ")
        s = 12

    elif vraag == "Medium":
        repeat = False
        print("Voer nu het aantal in: ")
        s = 10

    elif vraag == "Small":
        repeat = False
        print("Voer nu het aantal in: ")
        s = 7

    else :
        print("U moet een keuze maken tussen \"Large\"Medium\"Small\". ")

# while loop voor grote kiezen, als de gebruiker iets anders dan de menu in typt herhaalt de code zich weer.


y = input()

total = int(y) * s


if  int(y) == 1 :
    print("-------------------------")
    print("      " + naam_resturant )
    print("  ")
    print("Bestelling geplaatsd door : " + naam)
    print("  ")
    print("U heeft " + y + " " + x + " pizza besteld." )
else :
     print("-------------------------")
     print("      " + naam_resturant )
     print("  ")
     print("Bestelling geplaatsd door : " + naam)
     print("  ")
     print("U heeft " + y + " " + x + " pizza's besteld." )

print("Uw totaal bedrag is: €" + str(total) )
print("  ")
print("""Eet smakellijk :)
Tot de volgende keer.""")
print("-------------------------")

# De bon 


