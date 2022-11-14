import threading
import sys
from threading import Timer

# def raiseError(msg):
#     raise NameError (msg)

# try:
#     timeout = 3
#     t = Timer(timeout, raiseError, ['Sorry, times up'])
#     t.start()
#     answer = input("You have "+str(timeout)+" seconds to choose the correct answer...")
#     t.cancel()
# except Exception as err:
#     print(err)
# else:
#     print(answer)

# toSlow = False

# def setCheck(msg):
#     global toSlow
#     toSlow = True
#     print(msg)

# timeout = 3
# toSlow = False
# t = Timer(timeout, setCheck, [ " Sorry, times up "])
# t.start()
# x = input('?')
# t.cancel()


# if toSlow == False and x == "a":
#     print("hallo")

# else :
#     print("asjdlaksjdlkasd")


# import msvcrt
# import time
# x=''

# print("Enter any text.")
# starttime = time.time()
# while time.time() - starttime < 5:
#     if msvcrt.kbhit():
#         x=input()
#         break
# if x:
#     print("The input is " + x)
# else:
#     print("No input")
import time
import itertools
import threading
import sys
from threading import Timer
import msvcrt
from time import sleep

Hp = 100
bewakerA = 100
bewakerAA = 40 
bewakerAAA = 70


# attack =''

# print("typ je command in : ")
# starttime = time.time()
# while time.time() - starttime < 3:
#     if msvcrt.kbhit():
#         attack = input().lower()
#         break
# if attack == "attack":
#     bewakerA = bewakerA - 100
#     for i in range(4):
#         print(" Vijand Hp = " + str(bewakerA) )
#     print("Jouw Hp = " + str(Hp)) 
#     print("Alle vijanden zijn vermoord, goed gedaan ")
        
# else:
#     Hp = Hp - 100
#     print("Je werd aangevallen!")
#     print("Jouw Hp = " + str(Hp)) 
#     print("Game over!")
#     exit()


start1 = ("""
Kies nu hoe je de kasteel wilt binnen gaan:
""")

for char in start1:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

time.sleep(1)

Hp = 100
bewakerA = 100
Koning = 200


binnenvallen = ("""
Main gate
Geheime tunnel
""")

for char in binnenvallen:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

binnenvallen = input().lower()

if binnenvallen == "main gate":
    gateT = ("""
Je bent heel dapper zo te zien!
Er staan 4 bewakers voor de gate.
Take them down!
je hebt paar seconden om je zelf te verdedigen!
    """)

    for char in gateT:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    attack =''

    command = ("typ je command in : ")
    for char in command:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    starttime = time.time()
    while time.time() - starttime < 3:
        if msvcrt.kbhit():
            attack = input().lower()
            break

        
    if attack == "attack":
        bewakerA = bewakerA - 100
        for i in range(3):
            print(" Vijand Hp = " + str(bewakerA) )
        command = """ Jouw Hp = """ + str(Hp) + """
        Alle vijanden zijn vermoord, goed gedaan."""
        for char in command:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
            
   

    time.sleep(3)

    attack =''
    bewakerA = 100

    command = """
Er komen meer bewakers!
typ je command in : """
    for char in command:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    starttime = time.time()
    while time.time() - starttime < 3:
        if msvcrt.kbhit():
            attack = input().lower()
            break
    if attack == "attack":
        bewakerA = bewakerA - 100
        for i in range(4):
            print(" Vijand Hp = " + str(bewakerA) )
        command = """Jouw Hp = """ + str(Hp) + """
    Goed gedaan ga nu door naar de koning. """
        for char in command:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        
    else:
        Hp = Hp - 100
        command = """Je werd aangevallen!
        Jouw Hp = """ + str(Hp)+ """ 
        Game over!"""
        for char in command:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        exit()

    attack =''
    bewakerA = 100

    time.sleep(3)

    command = """
    daar is de koning, KILL HIM!
    typ je command in : """
    for char in command:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    starttime = time.time()
    while time.time() - starttime < 3:
        if msvcrt.kbhit():
            attack = input().lower()
            break
    if attack == "attack":
        Koning = Koning - 100
        print(" Koning Hp = " + str(Koning) )
        print("Jouw Hp = " + str(Hp)) 
        print("Hij is heel sterk, val hem nog een keer aan!")
        command = """
    typ je command in : """
        for char in command:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        starttime = time.time()
        while time.time() - starttime < 9:
            if msvcrt.kbhit():
                attack = input().lower()
                break
        if attack == "attack":
            Koning = Koning - 100
            print(" Koning Hp = " + str(Koning) )
            print("Jouw Hp = " + str(Hp)) 
            command = """YOU WIN
Nu is de land vrij en iedereen is blij"""
            for char in command:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()


    else:
        Hp = Hp - 100
        command = """Je werd aangevallen!
        Jouw Hp = """ + str(Hp)+ """ 
        Game over!"""
        for char in command:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        exit()
