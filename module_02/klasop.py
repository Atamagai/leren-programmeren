from operator import truediv
from random import randint

x = 0
play = True
bomb = randint(1,10)
score = 0

while play == True:
    print( "Ronde " + str(x) +": Op welke getal denk je dat de bomb niet ligt? ")
    vraag = input()
    x = int(x) + 1 
    if int(vraag) == bomb:
        play = False
        print("Boem! Game over.")
        exit()
    else :
        play = False
        score = int(score) + 1 

play = True

while play == True:
    print("Wilt u naar ronde " + str(x) + "? [Y/N] ")
    Vraag1 = input().lower()
    if Vraag1 == "n":
        play = False

    elif Vraag1 == "y":
        play = False
        print("U bent nu in ronde " + str(x) )
        print("score = " + str(score))
    else:
        play = True

