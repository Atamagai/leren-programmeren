print("Welkom")
lijst = {}

item = input("Wat wil je aan je boodschappen lijst toevoegen? ").lower()
aantal = int(input("Hoeveel wil je daarvan? "))
lijst[item] = aantal

repeat = True

while repeat == True:
    herhaal = input("Will je nog iets toevoegen? ").lower()

    if herhaal == "ja":
        item = input("Wat wil je nog aan je boodschappen lijst toevoegen? ").lower()
        
        aantal1 = int(input("Hoeveel wil je daarvan? "))
        if item in lijst:
            aantal = aantal1 + aantal
            lijst.update({item : aantal})
        else:
            lijst[item] = aantal
        repeat = True 

    elif herhaal == "nee":
        repeat = False
    
lijst[item] = aantal

print("\nHier is jou lijst:")
print("---------------------------")
for key, value in lijst.items():
    print(value,"x ",key)
print("---------------------------")