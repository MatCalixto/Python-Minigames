playagain = 1
while playagain == 1:
    print("Digite 1 para português e 2 para inglês")
    print("Type 1 for portuguese and 2 for english")
    language = int(
        input("\nFirst or second language - Língua 1 ou 2: "))  # language
    if language == 2:
        print("\nTIC-TAC-TOE PvP - Player vs Player")
        print("Made by Matheus Calixto")
    else:
        print("\nJogo da Velha PvP - Jogador vs Jogador")
        print("Feito por Matheus Calixto")
    print()
    print("       1    2    3 ")
    print("   a  a1 | a2 | a3 ")
    print("      ---|----|--- ")
    print("   b  b1 | b2 | b3 ")
    print("      ---|----|--- ")
    print("   c  c1 | c2 | c3 ")
    print("")
    if language == 2:
        print("RULES:")
        print("-Positions are described as letter (a, b or c) + number (1, 2 or 3).")
        print("-Examples of this are a1, b2, b3, c2.")
        print("-All normal Tic-Tac-Toe rules and winning positions apply, have fun!")
    else:
        print("REGRAS:")
        print("-Posições são descritas como letra (a, b or c) + número (1, 2 or 3).")
        print("-Exemplos disso são a1, b2, b3, c2.")
        print("-Todas as regras usuais de Jogo da Velha se aplicam, divirtam-se!")
    if language == 2:
        firstplayername = str(input("\nFirst player's name is: "))
    else:
        firstplayername = str(
            input("\nO nome do primeiro jogador é: "))  # ask user name
    if language == 2:
        secondplayername = str(input("\nSecond player's name is: "))
    else:
        secondplayername = str(input("\nO nome do segundo jogador é: "))
    print()
    a1 = "  "  # define all positions
    a2 = "  "
    a3 = "  "
    b1 = "  "
    b2 = "  "
    b3 = "  "
    c1 = "  "
    c2 = "  "
    c3 = "  "
    numberofgames = 0
    player = 0
    while numberofgames < 9:  # while less than 9 games have been played
        if player == 0:
            if language == 2:
                # where will he put a cross
                move = str(input(firstplayername + " (X)'s turn: "))
                print()
            else:
                move = str(input("É a vez de " + firstplayername + " (X): "))
                print()
        else:
            if language == 2:
                # where will he put a ball
                move = str(input(secondplayername + " (O)'s turn: "))
                print()
            else:
                move = str(input("É a vez de " + secondplayername + " (O): "))
                print()
        if move == "a1":  # find the square
            if a1 == " X" or a1 == " O":
                if language == 2:
                    # player chose
                    print("Invalid position, that square is already taken, try again")
                else:  # used square
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    a1 = " X"
                else:
                    a1 = " O"
        elif move == "a2":
            if a2 == " X" or a2 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    a2 = " X"
                else:
                    a2 = " O"
        elif move == "a3":
            if a3 == " X" or a3 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    a3 = " X"
                else:
                    a3 = " O"
        elif move == "b1":
            if b1 == " X" or b1 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    b1 = " X"
                else:
                    b1 = " O"
        elif move == "b2":
            if b2 == " X" or b2 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    b2 = " X"
                else:
                    b2 = " O"
        elif move == "b3":
            if b3 == " X" or b3 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    b3 = " X"
                else:
                    b3 = " O"
        elif move == "c1":
            if c1 == " X" or c1 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    c1 = " X"
                else:
                    c1 = " O"
        elif move == "c2":
            if c2 == " X" or c2 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    c2 = " X"
                else:
                    c2 = " O"
        elif move == "c3":
            if c3 == " X" or c3 == " O":
                if language == 2:
                    print("Invalid position, that square is already taken, try again")
                else:
                    print("Posição já foi tomada, tente novamente")
                numberofgames = numberofgames - 1
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                if player == 0:
                    c3 = " X"
                else:
                    c3 = " O"
        else:
            if language == 2:
                print("Invalid position, try again")
            else:
                print("Posição inválida, tente novamente")
            numberofgames = numberofgames - 1
            if player == 0:
                player = 1
            else:
                player = 0
        if (a1 == " X" and a2 == " X" and a3 == " X" or  # did player 1 win the game?
                b1 == " X" and b2 == " X" and b3 == " X" or
                c1 == " X" and c2 == " X" and c3 == " X" or
                a1 == " X" and b1 == " X" and c1 == " X" or
                a2 == " X" and b2 == " X" and c2 == " X" or
                a3 == " X" and b3 == " X" and c3 == " X" or
                a1 == " X" and b2 == " X" and c3 == " X" or
                a3 == " X" and b2 == " X" and c1 == " X"):
            if language == 2:
                print(firstplayername + " \nwon the game, congrats!")
                print("")
            else:
                print(firstplayername + " \nganhou o jogo, parabéns!")
                print("")
            numberofgames = 15
        if (a1 == " O" and a2 == " O" and a3 == " O" or  # did player 2 win the game?
                b1 == " O" and b2 == " O" and b3 == " O" or
                c1 == " O" and c2 == " O" and c3 == " O" or
                a1 == " O" and b1 == " O" and c1 == " O" or
                a2 == " O" and b2 == " O" and c2 == " O" or
                a3 == " O" and b3 == " O" and c3 == " O" or
                a1 == " O" and b2 == " O" and c3 == " O" or
                a3 == " O" and b2 == " O" and c1 == " O"):
            if language == 2:
                print(secondplayername + " \nwon the game, congrats!")
                print()
            else:
                print(secondplayername + " \nganhou o jogo, parabéns!")
                print()
            numberofgames = 15
        print("       1    2    3 ")
        print("   a ", a1, "|", a2, "|", a3, "")  # print game
        print("      ---|----|--- ")
        print("   b ", b1, "|", b2, "|", b3, "")
        print("      ---|----|--- ")
        print("   c ", c1, "|", c2, "|", c3, "")
        print("")
        if player == 0:
            player = 1
        else:
            player = 0
        numberofgames = numberofgames + 1
    else:
        if numberofgames == 16:  # end of loop, either it is a draw or a player won
            if language == 2:
                print("Game ended")
            else:
                print("O jogo acabou")
        else:
            if language == 2:
                print("Game ended, it's a tie!")
            else:
                print("O jogo acabou, foi empate!")
        print()
        playagain = 0
        if language == 2:
            playagain = int(input("Type 1 if you want to play again: "))
            print()
        else:
            playagain = int(input("Digite 1 se quiser jogar novamente: "))
            print()
else:
    if language == 2:
        print("Program has come to an end")
    else:
        print("Programa finalizado")
