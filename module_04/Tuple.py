Alle_dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

Ralle_dagen = reversed(Alle_dagen)
Ralle_dagen = tuple(Ralle_dagen)
werkdagen = reversed(Alle_dagen[0:5])
werkdagen = tuple(werkdagen)
weekend = reversed(Alle_dagen[5:7])
weekend = tuple(weekend)

print(Alle_dagen)
print(Alle_dagen[0:5])
print(Alle_dagen[5:7])
print(Ralle_dagen)
print(werkdagen)
print(weekend)