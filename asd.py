
import time
import os
lijstje = {}
loop = True
while loop == True:
        os.system("cls")
        wat = input("Wat wilt u toevoegen?: ")
        hoeveel = int(input("Hoeveel stuks?: "))
        if wat.lower() in lijstje:
            wat = wat.lower()
            lijstje[wat] = lijstje[wat] + hoeveel
            loop = True
        else:
            lijstje[wat] = hoeveel

        meer = input("Wilt u nog meer toevoegen? Y/N: ")
        if meer.lower() == "y":
            loop = True
        elif meer.lower() == "n":
            os.system("cls")
            print("BOODSCHAPPENLIJSTJE:")
            for key,value in lijstje.items():
                print(key,":",value)
            loop = False