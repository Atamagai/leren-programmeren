croissantjes = 17
prijs_croissantje = 0.39
stokbroden = 2
prijs_stokbroden = 2.78 
totale_kortingsbonen = 3 
gebruikte_bonen = 0

totale_prijs = croissantjes * prijs_croissantje + stokbroden * prijs_stokbroden - gebruikte_bonen
float = totale_prijs
format_float = "{:.2f}".format(float)

print ("De feestlunch kost je bij de bakker " + format_float + " euro voor de " + str(croissantjes) + " croissantjes en de " + str(stokbroden) + " stokbroden als de " + str(totale_kortingsbonen) + " kortingsbonen nog geldig zijn!" )

#in de opdracht staat voor totale prijs 18.88 maar de brekeningen geven iets anders, ik heb in me code het juiste brekeningen gebruikt en niet die van de opdracht.