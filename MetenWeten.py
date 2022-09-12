#1 input en if-statement 
print("Voer een getal in als {a}: ")
a = input()
print("Voer een getal in als {b}: ")
b = input()


if a > b :
    max = a
    min = b
    print("a is het grootste getal: " + max )
# 2.elif-statement
elif a < b :
    min = a
    max = b
    print("a is het kleinste getal: " + min)
# 3 else-statement 
else :
    print("a en b zijn even groot")

# 4 Min en Max
print("Het maximum is : " + str(max))
print("Het minimun is : " + str(min))
