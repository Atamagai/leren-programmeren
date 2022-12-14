from fruitmand import fruitmand

fruitmand.pop(4)
colors = []

for i in range(len(fruitmand)):
    x = (fruitmand[i]['color'])
    if x not in colors: 
        colors.append(x)
    
print(colors)
