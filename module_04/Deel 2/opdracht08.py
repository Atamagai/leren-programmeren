from fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 1890,
    'color' : 'green',
    'round' : True
})

totaal = 0  

for gewicht in fruitmand:
    gewicht = gewicht["weight"]
    totaal += gewicht

print(totaal)