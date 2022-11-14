# name of student: Emad Hajiabadi
# number of student: 99071577
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #


aantalvijfe = 0
aantaldriee = 0
aantaltweee = 0
aantalvijftig = 0
aantaltwintig = 0
aantaltien = 0
aantalvijf = 0  
aantaltwee = 0

vijfe = 5
driee = 3
tweee = 2
vijftijg = 50
twintig = 20
tien = 10
vijfc = 5
tweec = 2





vijf = 500 
drie = 300
twee = 200

if change > 0: #
  coinValue = vijf #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 

    if coinValue == vijf:
      a = 5
      aantalvijfe = nrCoinsReturned 
      coinValue = drie
    elif coinValue == drie:
      b = 3
      aantaldriee = nrCoinsReturned 
      coinValue = twee
    elif coinValue == twee:
      c = 2
      aantaltweee = nrCoinsReturned 
      coinValue = 50
    elif coinValue == 50:
      d = 50
      aantalvijftig = nrCoinsReturned 
      coinValue = 20
    elif coinValue == 20:
      e = 20
      aantaltwintig = nrCoinsReturned 
      coinValue = 10
    elif coinValue == 10:
      f = 10
      aantaltien = nrCoinsReturned 
      coinValue = 5
    elif coinValue == 5:
      g = 5
      aantalvijf = nrCoinsReturned 
      coinValue = 2
    elif coinValue == 2:
      h = 2
      aantaltwee = nrCoinsReturned 
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print("""This is your change : \n""" + str(aantalvijfe) + " van " +str(vijfe) + " euro muntstukken \n"
  +str(aantaldriee) + " van " +str(driee) + " euro muntstukken\n""" 
  +str(aantaltweee) + " van " +str(tweee) + " euro muntstukken\n"""
  +str(aantalvijftig) + " van " +str(vijftijg) + " muntstukken\n""" 
  +str(aantaltwintig) + " van " +str(twintig) + " muntstukken\n""" 
  +str(aantaltien) + " van " +str(tien) + " muntstukken\n""" 
  +str(aantalvijf) + " van " +str(vijfc) + " muntstukken\n""" 
  +str(aantaltwee) + " van " +str(tweec) + " muntstukken\n""" 
 )

  print('done')