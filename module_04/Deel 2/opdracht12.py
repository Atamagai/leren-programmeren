from fruitmand import fruitmand


name = []

for fruit in fruitmand:
    name.append(fruit["name"])
    name.sort(key=len)

fruitnaam = (name[-1])

kleurs ={
    "red" : "rood",
    "orange" : "oranje",
    "yellow" : "geel",
    "brown" : "bruin"
}

for fruit in fruitmand:
    if fruitnaam == fruit["name"] :
        fruitkleur = (fruit["color"])
        fruitgewicht = (fruit["weight"])
        fruitgewicht = fruitgewicht / 1000

print("De "+ (fruitnaam) + "(" +str(len(fruitnaam))+ ") heeft een "+kleurs[fruitkleur]+ " kleur en een gewicht van "+ str(fruitgewicht) +" kg")