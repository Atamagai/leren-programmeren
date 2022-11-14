num = 50
som = str(num)
totaal = num
aantal = 0
while totaal <=1000:
    num = num + 1
    totaal = totaal + num
    som = som + "+" + str(num)
    print(som + "=" + str(totaal))
    aantal = aantal + 1

print("",aantal,"sommen")