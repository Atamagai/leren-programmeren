repeat = True

print("Welkom, vul uw naam a.u.b in: ")
naam = input()

try:
    if naam == "Justin":
        raise NameError ("Ewa kleintje!")
    
except Exception as Err :
    print(Err)
    exit()
    
    

while repeat == True:
    print("Heeft u praktijkervaring met dieren-dressuur OF ervaring met jongleren OF praktijkervaring met acrobatiek? [Ja, Nee] ")
    ervaring = input().lower()

    if ervaring == "ja" :
        repeat = False
        print("Hoeveel jaren? [Voer alleen een getal in]")
        jaren = str(input())

        try:
            if int(jaren) == 1:
                raise NameError ("Te weinig! Ga ergens anders")
        
        except Exception as Err :
            print(Err)
            exit()
        
    elif ervaring == "nee" :
        repeat = False

    else:
        repeat = True


repeat = True
repeat1 = True 
repeat2 = True
repeat3 = True
repeat4 = True


while repeat4 == True :
    print("Heeft u een MBO-4 diploma? [ja, nee]")
    diploma = input().lower()

    if diploma == "ja" or "nee":
        repeat4 = False

    else :
        repeat4 = True
    

while repeat1 == True:
    print("Welke typ rijbewijs heeft u in bezit? [A,B,C]")
    rijbewijs = input().upper()

    if rijbewijs == "A" or rijbewijs == "B" or rijbewijs == "C":
        repeat1 = False
        while repeat == True:
            print("Heeft u een hoge hoed in bezit? [Ja] [Nee] ")
            hoed = input().lower()
    
            if hoed == "ja" or hoed == "nee":
                repeat = False
                while repeat2 == True:
                    print("Wat is uw geslacht? ")
                    geslacht = input().lower()


                    if geslacht == "man" :
                        repeat2 = False
                        print("Hoe breed is uw snor? [in hele cm]")
                        snor = input()

                    elif geslacht == "vrouw" :
                        repeat2 = False
                        while repeat3 == True:
                            print("Welke soort haren heeft u? [krul] of [recht]")
                            haren = input().lower()

                            if haren == "krul" or haren == "recht":
                                repeat3 = False
                                print("Hoelang zijn uw haren? [in hele cm] ")
                                Lharen = input()

                            else:
                                repeat3 = True
                    else :
                        repeat2 = True 
            else :
                repeat = True
    else:
        repeat1 = True


print("Hoelang bent u ? [in hele cm] ")
Lengte = input()

print("Hoe zwaar bent u ? [in hele kg] ")
gewicht = input()

print("Heeft u Certificaat Overleven met gevaarlijk personeel? [Ja] [Nee]")
certificaat = input()

print("Heeft u een bril ? [Ja] [Nee]")
bril = input().lower()

try:
    if str(bril) == "ja" :
        raise NameError ("Nerd's zijn niet toegestaan hier! ")
        
except Exception as Err :
    print(Err)
    exit()

print("Wat is uw schoenen maat?")
schoenen = input()

print("Wat is uw favoriete kleur? ")
kleur = input()

print("Bent u getrouwd? [Ja] [Nee]")
getrouwd = input()

if ervaring == "ja":
    if jaren == "5" or jaren == "4" or jaren == "3":
        if diploma == "ja":
            if rijbewijs == "C":
                if hoed == "ja":
                    if geslacht == "man" :
                        if int(snor) >= 10 :
                            if int(gewicht) >= 90:
                                    if certificaat == "ja":
                                        print("""
    Beste """ + naam + " Gefeliciteerd! U komt in aanmerking voor een solicitatiegesprek, stuur snel uw CV door aan ons.""")
                                    else :
                                        print("Beste " + naam + ", U voldoet niet aan onze strenge eisen voor de functie van Ruimte-vuilnisman, het spijt ons.")
                    elif geslacht == "vrouw" :
                        if haren == "krul":
                            if int(Lharen) >= 150 :
                                if int(gewicht) >= 90:
                                    if certificaat == "ja":
                                        print("""
    Beste """ + naam + ", Gefeliciteerd! U komt in aanmerking voor een solicitatiegesprek, stuur snel uw CV door aan ons.""")
                                    else :
                                        print("Beste " + naam + ", U voldoet niet aan onze strenge eisen voor de functie van Ruimte-vuilnisman, het spijt ons.")

else :
    print("Beste " + naam + ", U voldoet niet aan onze strenge eisen voor de functie van Ruimte-vuilnisman, het spijt ons.")