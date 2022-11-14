repeat = True

while repeat == True:
    print("Is de kaas geel?")
    vraag = input().lower()

    if vraag == "ja":
        repeat = False 
        print("Zitten er gaten in? ")
        vraag = input().lower()
        
        if vraag == "ja":
            repeat = False
            print("Is de kaas belagelijk duur? ")
            vraag = input().lower()
            if vraag == "ja":
                repeat = False
                print("De kaas is een Emmenthaler.")
            elif vraag == "nee":
                repeat = False
                print("De kaas is een Leerdammer.")

        elif vraag == "nee":
            repeat = False
            print("Is de kaas hard als steen?")
            vraag = input().lower()
            if vraag == "ja":
                repeat = False
                print("De kaas is een Parmigiano Reggiano.")
            if vraag == "nee":
                repeat = False
                print("De kaas is een Goudse kaas.")


    elif vraag == "nee":
        repeat = False
        print("Heeft de kaas blauwe schimmel? ")
        vraag = input().lower()

        if vraag == "ja":
            repeat = False
            print("Heeft de kaas een korst? ")
            vraag = input().lower()
            if vraag == "ja":
                repeat = False
                print("De kaas is een Blue de Rochbaron.")
            elif vraag == "nee":
                repeat = False
                print("De kaas is een Foume d'Ambert.")
        
        elif vraag == "nee":
            repeat = False
            print("Heeft de kaas een korst? ")
            vraag = input().lower()
            if vraag == "ja":
                repeat = False
                print("De kaas is een Blue de Camembert.")
            elif vraag == "nee":
                repeat = False
                print("De kaas is een Mozzarella.")