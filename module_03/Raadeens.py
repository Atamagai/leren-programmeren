import random


print("Welkom!")
print("Raad het getal tussen 1-1000 en score punten.")

getal = random.randint(1,1000)
score = 0
scoren = score + 1 
x = 0
repeat = True

while repeat == True:
    geraden_getal = input("Raad het nummer: ")
    x = x + 1 

    try:
        int(geraden_getal)
        repeat = False
        roundtwintig = int(geraden_getal) - int(getal)

        if int(geraden_getal) > 1000 :
            repeat = True
            print("Het getal moet tussen 1 en 1000 zijn!")

        elif int(geraden_getal) > getal:
            print("Lager!")
            repeat = True
            if abs(int(roundtwintig)) < 20:
                print("Je bent heel warm!")
                repeat = True
            
            elif abs(int(roundtwintig)) < 50:
                print("Je bent warm!")
                repeat = True
            

        elif int(geraden_getal) < getal:
            print("Hoger!")
            repeat = True
            if abs(int(roundtwintig)) < 20:
                print("Je bent heel warm!")
                repeat = True
            elif abs(int(roundtwintig)) < 50:
                print("Je bent warm!")
                repeat = True
        
        elif int(geraden_getal) == getal:
            print("Dat is juist!\n" +"Jouw score : "+ str(scoren))
            opnieuw = input("Nog een getal raden? [Ja/Nee]\n").lower()
            if opnieuw == "ja":
                x = 0 
                repeat = True
            elif opnieuw == "nee":
                print("Bedankt voor spelen!\nTot ziens")
                quit()
        
        if int(x) == 10:
            repeat = False
            print("Helaas zijn je pogingen voorbij\n" + "Jouw score : " + str(score))
           
            opnieuw = input("Nog een getal raden? [Ja/Nee]\n").lower()
            if opnieuw == "ja":
                x = 0 
                repeat = True
            elif opnieuw == "nee":
                print("Bedankt voor spelen!\nTot ziens")
                quit()


    except Exception as error:
        print("Dat is geen getal! ")       
