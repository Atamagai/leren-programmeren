num = input("Vul een nummer in: ")

for i in range (1,11,1):
    x = int(num) * i 
    print(str(i) + " x " + str(num) + " = " + str(x))