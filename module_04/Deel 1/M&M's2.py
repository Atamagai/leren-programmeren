import random

kleur = ["rood", "blauw", "groen", "geel", "bruin"]
rood = 0
blauw = 0
groen = 0 
geel = 0
bruin = 0

zakje = {}
repeat = True

while repeat == True:

    aantal = int(input("Hoeveel M&M's wil je toevoegen ?"))

    if aantal < 1:
        print("Je moet minimaal 1 toevoegen!")
        repeat = True
    else:
        repeat = False
        for i in range (aantal):
            RandomMM = random.choice(kleur)
            if RandomMM == "rood":
                rood = rood + 1 
                zakje["rood"] = rood
            if RandomMM == "blauw":
                blauw = blauw + 1 
                zakje["blauw"] = blauw
            if RandomMM == "groen":
                groen = groen + 1 
                zakje["groen"] = groen
            if RandomMM == "geel":
                geel = geel + 1 
                zakje["geel"] = geel
            if RandomMM == "bruin":
                bruin = bruin + 1 
                zakje["bruin"] = bruin

            # if kleur in zakje:
            #     zakje[kleur] = zakje[kleur] + aantal
            # else:
            #     zakje[kleur] = aantal


print(zakje)
