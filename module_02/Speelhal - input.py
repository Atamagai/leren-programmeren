prijs_in_VR_per_vijf_min = 0.37
prijs_per_persoon_speelhal = 7.45


print('Voer het aantal mensen in: ') 
x = input()
str(x)

print('Voer het anntal minuten in het VR in: ')
y = input()
str(y)

totale_prijs = (float(y) / float(5)) * float(prijs_in_VR_per_vijf_min) * float(x) + float(prijs_per_persoon_speelhal) * float(x)
float = totale_prijs
format_float = "{:.2f}".format(float)

print('Dit geweldige dagje uit met ' + x + ' mensen in de speelhal met ' + y + ' minuten VR kost je maar ' + format_float + ' euro')
