import random
import itertools

Kleuren = ("harten", "klaveren", "schoppen",)
nummer = ("2", "3", "4","5","6","7","8","9","10","Boer", "Vrouw", "Heer", "Aas",)
MyDeck = []

for i in range (len(Kleuren)):
    for y in range (13): 
        MyDeck.append((Kleuren[i])+ " " + (nummer[y]))

for x in range (2):
    MyDeck.append("Joker")

random.shuffle(MyDeck)

for d in range (7):
    print(MyDeck[d])
    MyDeck.pop()

# print(MyDeck[7:54]) 
print(MyDeck)
print(len(MyDeck))