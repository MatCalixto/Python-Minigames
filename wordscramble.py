import random
playagain = 1
while playagain == 1:
  number = random.randint(1, 5) #random number from 1 to 5
  print("")
  print("Unscramble Word by Matheus Calixto")
  print("")
  print("THEME: Animals")
  print("")
  sol1 = ""
  sol2 = ""
  sol3 = ""
  scrambledword = ""
  context = ""
  if number == 1: #sorted number
     context = "Good at carrying weights, looks like a horse"
     scrambledword = "okdnye"
     sol1 = "Donkey"
     sol2 = "donkey" #solutions
     sol3 = "DONKEY"
  elif number == 2:
     context = "Good at flight, a bird"
     scrambledword = "lcfona"
     sol1 = "Falcon"
     sol2 = "falcon"
     sol3 = "FALCON"
  elif number == 3:
     context = "Good at repeating things humans say"
     scrambledword = "rpoart"
     sol1 = "Parrot"
     sol2 = "parrot"
     sol3 = "PARROT"
  elif number == 4:
     context = "Doens't get to live after christmas, also a country"
     scrambledword = "ekrtuy"
     sol1 = "Turkeu"
     sol2 = "turkey"
     sol3 = "TURKEY"
  elif number == 5:
     context = "Well known orange sea fruit"
     scrambledword = "isrhpm"
     sol1 = "Shrimp"
     sol2 = "shrimp"
     sol3 = "SHRIMP"
  print(context)
  guess = ""
  guess = (str(input("Find a word which unscrambles the word: " + 
  scrambledword + " "))) #the guess from player
  print("")
  if guess in [sol1, sol2, sol3]:
      print("You correctly unscrumbled the word, congrats!")
  else:
      print("You guessed it wrong, the word was " + sol1)
  playagain = 0
  playagain = int(input("Type 1 if you want to play again: "))
  print("")
else:
  print("Game ended")