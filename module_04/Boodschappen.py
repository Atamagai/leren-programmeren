print("Welkom")
lijst = {}
repeat = True

while repeat == True:
    item = input("Wat wil je aan je boodschappen lijst toevoegen? ").lower()
    aantal = int(input("Hoeveel wil je daarvan? "))

    # print(list(lijst.keys()))
    
    if item in lijst:
        lijst[item] = lijst[item] + aantal
    else:
        lijst[item] = aantal

    herhaal = input("Will je nog iets toevoegen? ").lower()

    if herhaal == "ja":
        repeat = True

    elif herhaal == "nee":
        repeat = False
    
print("\nHier is jou lijst:")
print("---------------------------")
for key, value in lijst.items():
    print(value,"x ",key)
print("---------------------------")




