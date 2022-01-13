# name of student: Rodney Vlot
# number of student: 99058248
# purpose of program: Goed en op een makkelijke manier kunnen weten hoeveel wisselgeld je van elke munt moet teruggeven


# Database en inputs

toPay = int(float(input('Amount to pay: '))* 100) 
paid = int(float(input('Paid amount: ')) * 100) 
change = paid - toPay 
fiveeur = 0
threeeur = 0
twoeur = 0
fifityc = 0
twentyc = 0
tenc = 0
fivec = 0
twoc = 0
onec = 0


if change > 0: 
  coinValue = 500
  
  while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue 

# Optelling wisselgeld en optelling lijst met munten die terug worden gegeven

    if nrCoins > 0: 
      print('return maximal', nrCoins, 'coins of', coinValue, 'cents!') 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? '))
      if coinValue == 500:
        fiveeur += nrCoinsReturned
      elif coinValue == 300:
        threeeur += nrCoinsReturned
      elif coinValue == 200:
        twoeur += nrCoinsReturned
      elif coinValue == 50:
        fifityc += nrCoinsReturned
      elif coinValue == 20:
        twentyc += nrCoinsReturned
      elif coinValue == 10:
        tenc += nrCoinsReturned
      elif coinValue == 5:
        fivec += nrCoinsReturned
      elif coinValue == 2:
        twoc += nrCoinsReturned
      else:
        onec + nrCoinsReturned
        
      change -= nrCoinsReturned * coinValue
      
# Geeft aan van welke coin je het aantal terug moet geven

    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

# Print de lijst met de aantal teruggeven coins

if change > 0:
  print('Change not returned: ', str(change) + ' cents')
  print('-COINS RETURNED-')
  print('€5: '+str(fiveeur))
  print('€3: '+str(threeeur))
  print('€2: '+str(twoeur))
  print('€0,50: '+str(fifityc))
  print('€0,20: '+str(twentyc))
  print('€0,10: '+str(tenc))
  print('€0,5: '+str(fivec))
  print('€0,2: '+str(twoc))
  print('€0,1: '+str(onec))
else:
  print('-COINS RETURNED-')
  print('€5: '+str(fiveeur))
  print('€3: '+str(threeeur))
  print('€2: '+str(twoeur))
  print('€0,50: '+str(fifityc))
  print('€0,20: '+str(twentyc))
  print('€0,10: '+str(tenc))
  print('€0,5: '+str(fivec))
  print('€0,2: '+str(twoc))
  print('€0,1: '+str(onec))