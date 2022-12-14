from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit["name"] == "druif":
        fruitmand.pop()
colors = []

for i in range(len(fruitmand)):
    x = (fruitmand[i]['color'])
    if x not in colors: 
        colors.append(x)
    
print(colors)
