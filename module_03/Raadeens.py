import random


print("Welkom!")
print("Raad het getal tussen 1-1000 en score punten.")

score = 0
ronde = 0
repeat = True
repeat1 = True

while repeat1 == True:
    getal = random.randint(1,1000)
    x = 0
    ronde = ronde + 1
    repeat = True

    while repeat == True:
        print(getal)
         
    
        try:
            geraden_getal = int(input("Raad het nummer: "))
            x = x + 1
            geraden_getal
            repeat = False
            roundtwintig = geraden_getal - getal

            if int(geraden_getal) > 1000 :
                repeat = True
                print("Het getal moet tussen 1 en 1000 zijn!")

            # ingevoerde getal is lager
            elif geraden_getal > getal:
                print("Lager!")
                repeat = True
                if abs(int(roundtwintig)) <= 20:
                    print("Je bent heel warm!")
                    repeat = True
                
                elif abs(int(roundtwintig)) <= 50:
                    print("Je bent warm!")
                    repeat = True
                
            elif geraden_getal < getal:
                print("Hoger!")
                repeat = True
                if abs(int(roundtwintig)) <= 20:
                    print("Je bent heel warm!")
                    repeat = True
                elif abs(int(roundtwintig)) <= 50:
                    print("Je bent warm!")
                    repeat = True
            
            elif geraden_getal == getal:
                score = score + 1 
                print("Dat is juist!\n" +"Jouw score : "+ str(score))
                opnieuw = input("Nog een getal raden? [Ja/Nee]\n").lower()
                
                if opnieuw == "ja":
                    repeat1 = True
                    if int(ronde) == 3:
                        print("Helaas zijn je ronde's voorbij\nGame Over!\n" + "Jouw score: " + str(score))
                        quit()
                    
                elif opnieuw == "nee":
                    print("Bedankt voor spelen!\nTot ziens")
                    quit()
            
            if int(x) == 10:
                repeat = False
                print("Helaas zijn je pogingen voorbij\n" + "Jouw score : " + str(score))
            
                opnieuw = input("Nog een getal raden? [Ja/Nee]\n").lower()
                if opnieuw == "ja":
                    repeat1 = True
                    if int(ronde) == 20:
                        print("Helaas zijn je ronde's voorbij\nGame Over!\n" + "Jouw score: " + str(score))
                        quit()
    
                elif opnieuw == "nee":
                    print("Bedankt voor spelen!\nTot ziens")
                    quit()

            

        except Exception as error:
            print("Dat is geen getal! ")       

 