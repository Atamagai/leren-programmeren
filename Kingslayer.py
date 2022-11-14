from threading import Timer
import time
import itertools
import threading
import sys
import msvcrt



naam = input("Voer een gebruikersnaam in: ")

story = """
Ver weg van de zee is er een arme land met een onwaardige koning die alleen aan zichzelf denkt.
Mensen waren klaar met zijn actie's dus ze probeerden om een staatsgreep te plegen maar In deze staatsgreep ging de familie van 
""" + naam + """ dood.
""" + naam + """ wilt wraak nemen en in deze game speel je van zijn POV.
Lees de verhaal goed door en let op de details ;)
SUCCES!
"""

repeat = True

while repeat == True :
    print("Hallo " + naam + " welkom bij Kingslayer druk op [Enter] om door te gaan. ")
    var = input()

    if var == "":
        repeat = False
        import sys
        from time import sleep


        for char in story:
            sleep(0.01)
            sys.stdout.write(char)
            sys.stdout.flush()

    else:
        repeat = True

time.sleep(1)

def animation():
    done = False
    # here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading... ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write("""
    Done.
    """)

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(2)
    done = True

animation()

time.sleep(2)


start = ("""
Je hebt je wapen gepakt en je bent klaar om aan de mission te beginnen.
Goed om te weten :
bewakerA heeft een hp van 100
Jouw damage = 100
om aan te vallen typ [attack] in.
als je niks invult wordt je aangevallen en je FAALT.
""")

for char in start:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
    



repeat = True

while repeat == True :
    print("Hallo " + naam + " welkom bij Kingslayer druk op [Enter] om door te gaan. ")
    var = input()

    if var == "":
        repeat = False
    else:
        repeat = True

Hp = 100
bewakerA = 100
Koning = 200

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
