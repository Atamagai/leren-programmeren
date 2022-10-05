repeat = True
index = 0

while repeat == True:
    vraag = input("? ").lower()
    index +=1

    if vraag == "quit":
        repeat = False
        print(index)
        quit()

    else :
        repeat = True