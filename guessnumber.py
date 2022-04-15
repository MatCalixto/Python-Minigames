import random
language = int(input("1 para português, 2 for english: "))
if language == 2:
  playagain = 1
  while playagain == 1:
    print("")
    print("Guess a number from starting number to ending number with x amount of lives")
    print("")
    startnum = int(input("Choose a starting number: "))
    print("")
    endnum = int(input("Choose an ending number: "))
    print("")
    lifesleft = int(input("Choose how many lives: "))
    print("")
    number = random.randint(startnum, endnum)
    while lifesleft > 0:
      guess = (int(input("Guess a number from " + str(startnum) + " to " +
                         str(endnum) + ", you have " + str(lifesleft) + " chances: ")))
      print("")
      if guess == number:
        print("You guessed it right, the number was ", number)
        lifesleft = -19
      elif guess < number:
        print("You got it wrong, the number was higher than your guess")
      else:
        print("You got it wrong, the number was lower than your guess")
      print("")
      lifesleft = lifesleft - 1
    else:
      if lifesleft == -20:
        print("End of game")
      else:
        print("You are out of lifes and lost the game, the number was ", number)
        print("")
      playagain = 0
      playagain = int(input("Type 1 if you want to play again: "))
  else:
      print("Game ended")
else:
  playagain = 1
  while playagain == 1:
    print("")
    print("Chute um número que está entre o número de início e o número limite")
    print("")
    startnum = int(input("Escolha número de início: "))
    print("")
    endnum = int(input("Escolha número limite: "))
    print("")
    lifesleft = int(input("Escolha quantas chances: "))
    print("")
    lifesleftstr = str(lifesleft)
    startnumstr = str(startnum)
    endnumstr = str(endnum)
    number = random.randint(startnum, endnum)
    while lifesleft > 0:
      guess = (int(input("Chute um número de " + startnumstr + " até " +
                         endnumstr + ", você tem " + lifesleftstr +
                         " chances: ")))
      print("")
      if guess == number:
        print("Você acertou, o número era ", number)
        lifesleft = -19
      elif guess < number:
        print("Você errou, o número é maior do que o seu chute")
      else:
        print("Você errou, o número é menor do que o seu chute")
      print("")
      lifesleft = lifesleft - 1
    else:
      if lifesleft == -20:
        print("Fim de jogo")
      else:
        print("Você gastou todas as chances e perdeu o jogo, o número era", number)
        print("")
      playagain = 0
      playagain = int(input("Digite 1 se quiser jogar novamente: "))
  else:
      print("Fim de jogo")
