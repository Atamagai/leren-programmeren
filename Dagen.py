from timeit import repeat


dagen = ["maandag","dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
vraag = input("Welke dag van de week is vandaag? ").lower()
index = 0


repeat = True

if vraag in dagen:

    while repeat == True :
        print(dagen[index])
        
        if vraag == dagen[index] :
            repeat = False

        index = index + 1
else :
    print("Dit is geen bestaande dag!")    
