# croissantjes = 17  
from lib2to3.pytree import convert


prijs_croissantje = 0.39
prijs_stokbroden = 2.78 


print('Voer het aantal croissantjes in: ')
x = input()
str(x)

print('Voer het aantal stokbroden in: ')
y = input()
str(y)

print('Voer het aantal gebruikte kortingsbonen in: ')
q = input()
str(q)

totale_prijs = float(x) * float(prijs_croissantje) + float(y) * float(prijs_stokbroden) - float(q)
float = totale_prijs
format_float = "{:.2f}".format(float)

print('------------------------')
print('De feestlunch kost je bij de bakker ' + format_float + ' euro voor de ' + x + ' croissantjes en de ' + y + ' stokbroden als ' + q + ' kortingsbonen zijn gebruikt.' )
print('------------------------')


# de feestlunch kost je bij de bakker 12.19 euro voor
# de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonen nog geldig zijn!




