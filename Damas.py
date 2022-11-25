playagain = True
while playagain:
    # VARIÁVEIS
    mapa = {
    "a1": "⬤ ", "a2": "  ", "a3": "⬤ ", "a4": "  ", "a5": "  ", "a6": "  ", "a7": "◯ ", "a8": "  ",
    "b1": "  ", "b2": "⬤ ", "b3": "  ", "b4": "  ", "b5": "  ", "b6": "◯ ", "b7": "  ", "b8": "◯ ",
    "c1": "⬤ ", "c2": "  ", "c3": "⬤ ", "c4": "  ", "c5": "  ", "c6": "  ", "c7": "◯ ", "c8": "  ",
    "d1": "  ", "d2": "⬤ ", "d3": "  ", "d4": "  ", "d5": "  ", "d6": "◯ ", "d7": "  ", "d8": "◯ ",
    "e1": "⬤ ", "e2": "  ", "e3": "⬤ ", "e4": "  ", "e5": "  ", "e6": "  ", "e7": "◯ ", "e8": "  ",
    "f1": "  ", "f2": "⬤ ", "f3": "  ", "f4": "  ", "f5": "  ", "f6": "◯ ", "f7": "  ", "f8": "◯ ", 
    "g1": "⬤ ", "g2": "  ", "g3": "⬤ ", "g4": "  ", "g5": "  ", "g6": "  ", "g7": "◯ ", "g8": "  ",
    "h1": "  ", "h2": "⬤ ", "h3": "  ", "h4": "  ", "h5": "  ", "h6": "◯ ", "h7": "  ", "h8": "◯ "}
    listaLet = ["a", "b", "c", "d", "e", "f", "g", "h"]
    listaNum = ["1", "2", "3", "4", "5", "6", "7", "8"]
    jogador = "branco"
    loop = True
    # JOGO
    print("\nJogo de Damas em Python\nFeito por Matheus  Calixto, Marcos Barbosa \n")
    print("-- REGRAS --")
    print("Digite casa ou posição da peça escolhida, espaço, e casa ou posição de destino, exemplos válidos: c3 d4; g3 h4; a3 b4.")
    print("Se a posição for válida e seguir as regras usuais de Damas, agora será a vez do outro jogador de mover uma peça, se não, você poderá tentar novamente.\n")
    def createMap():
        print("\n")
        print(f'   8  {mapa["a8"]} | {mapa["b8"]} | {mapa["c8"]} | {mapa["d8"]} | {mapa["e8"]} | {mapa["f8"]} | {mapa["g8"]} | {mapa["h8"]}')
        print(f'      ---|----|----|----|----|----|----|---')
        print(f'   7  {mapa["a7"]} | {mapa["b7"]} | {mapa["c7"]} | {mapa["d7"]} | {mapa["e7"]} | {mapa["f7"]} | {mapa["g7"]} | {mapa["h7"]}')
        print(f'      ---|----|----|----|----|----|----|---')
        print(f'   6  {mapa["a6"]} | {mapa["b6"]} | {mapa["c6"]} | {mapa["d6"]} | {mapa["e6"]} | {mapa["f6"]} | {mapa["g6"]} | {mapa["h6"]}')
        print(f'      ---|----|----|----|----|----|----|---')
        print(f'   5  {mapa["a5"]} | {mapa["b5"]} | {mapa["c5"]} | {mapa["d5"]} | {mapa["e5"]} | {mapa["f5"]} | {mapa["g5"]} | {mapa["h5"]}')
        print(f'      ---|----|----|----|----|----|----|---')
        print(f'   4  {mapa["a4"]} | {mapa["b4"]} | {mapa["c4"]} | {mapa["d4"]} | {mapa["e4"]} | {mapa["f4"]} | {mapa["g4"]} | {mapa["h4"]}')
        print(f'      ---|----|----|----|----|----|----|---')
        print(f'   3  {mapa["a3"]} | {mapa["b3"]} | {mapa["c3"]} | {mapa["d3"]} | {mapa["e3"]} | {mapa["f3"]} | {mapa["g3"]} | {mapa["h3"]}')
        print(f'      ---|----|----|----|----|----|----|---')
        print(f'   2  {mapa["a2"]} | {mapa["b2"]} | {mapa["c2"]} | {mapa["d2"]} | {mapa["e2"]} | {mapa["f2"]} | {mapa["g2"]} | {mapa["h2"]}')
        print(f'      ---|----|----|----|----|----|----|---')
        print(f'   1  {mapa["a1"]} | {mapa["b1"]} | {mapa["c1"]} | {mapa["d1"]} | {mapa["e1"]} | {mapa["f1"]} | {mapa["g1"]} | {mapa["h1"]}')
        print(f'       a    b    c    d    e    f   g    h')
    createMap()
    def invalido():
        print(f'\nMovimento inválido ({stringMove}), tente novamente.')
    while loop:
        if jogador == "branco":
            move = input("\nÉ a vez das peças Brancas: ").split()
        else:
            move = input("\nÉ a vez das peças Pretas: ").split()
        stringMove = ' '.join(move)
        charLet1 = move[0][0]
        charNum1 = move[0][1]
        charLet2 = move[1][0]
        charNum2 = move[1][1]
        # Se o movimento está dentro da lista de possíveis posições (de a té h e de 1 até 8)
        if charLet1 in listaLet and charLet2 in listaLet and charNum1 in listaNum and charNum2 in listaNum:
            indexLet1 = listaLet.index(charLet1)
            indexNum1 = listaNum.index(charNum1)
            indexLet2 = listaLet.index(charLet2)
            indexNum2 = listaNum.index(charNum2)
            # Se for Peça Branca
            if mapa[move[0]] == "⬤ " and mapa[move[1]] in ["  ", "◯ ", "♕ "] and jogador == "branco" and ((indexLet2 == indexLet1 + 1 and indexNum2 == indexNum1 + 1) or (indexLet2 == indexLet1 - 1 and indexNum2 == indexNum1 + 1)):
                posMove1 = mapa[move[0]]
                posMove2 = mapa[move[1]]
                if mapa[move[1]] == "◯ " or mapa[move[1]] == "♕ ":
                    if indexLet2 == indexLet1 + 1:
                        jumpLet = listaLet[indexLet2 + 1]
                    else:
                        jumpLet = listaLet[indexLet2 - 1]
                    jump = str(jumpLet) + str(listaNum[indexNum2 + 1])
                    # Se peça que está na frente do movimento é vazia ou está preenchida, permitindo ou não comer a peça
                    if mapa[jump] == "  ":
                        mapa[jump] = mapa[move[0]]
                        mapa[move[1]] = "  "
                        mapa[move[0]] = "  "
                        jogador = "preto"
                        createMap()  
                    else: 
                        invalido()
                else:
                    if charNum2 == "8":
                        mapa[move[1]] = "♛ "
                    else:
                        mapa[move[1]] = posMove1
                    mapa[move[0]] = posMove2
                    jogador = "preto"
                    createMap()
            # Se for Dama/Rainha Branca
            elif mapa[move[0]] == "♛ " and mapa[move[1]] in ["  ", "◯ ", "♕ "] and jogador == "branco":
                posMove1 = mapa[move[0]]
                posMove2 = mapa[move[1]]
                if mapa[move[1]] == "◯ " or mapa[move[1]] == "♕ ":
                    if indexLet2 > indexLet1 and indexNum2 > indexNum1:
                        jump = str(listaLet[indexLet2 + 1]) + str(listaNum[indexNum2 + 1])
                    elif indexLet2 > indexLet1 and indexNum2 < indexNum1:
                        jump = str(listaLet[indexLet2 + 1]) + str(listaNum[indexNum2 - 1])
                    elif indexLet2 < indexLet1 and indexNum2 > indexNum1:
                        jump = str(listaLet[indexLet2 - 1]) + str(listaNum[indexNum2 + 1])
                    elif indexLet2 < indexLet1 and indexNum2 < indexNum1:
                        jump = str(listaLet[indexLet2 - 1]) + str(listaNum[indexNum2 - 1])
                    if mapa[jump] == "  ":
                        mapa[jump] = mapa[move[0]]
                        mapa[move[1]] = "  "
                        mapa[move[0]] = "  "
                        jogador = "preto"
                        createMap()  
                    else: 
                        invalido()
                else:
                    mapa[move[1]] = posMove1
                    mapa[move[0]] = posMove2
                    jogador = "preto"
                    createMap()  
            # Se for Peça Preta
            elif mapa[move[0]] == "◯ " and mapa[move[1]] in ["  ", "⬤ ", "♛ "] and jogador == "preto" and ((indexLet2 == indexLet1 + 1 and indexNum2 == indexNum1 - 1) or (indexLet2 == indexLet1 - 1 and indexNum2 == indexNum1 - 1)):
                posMove1 = mapa[move[0]]
                posMove2 = mapa[move[1]]
                if mapa[move[1]] == "⬤ " or mapa[move[1]] == "♛ ":
                    if indexLet2 == indexLet1 + 1:
                        jumpLet = listaLet[indexLet2 + 1]
                    else:
                        jumpLet = listaLet[indexLet2 - 1]
                    jump = str(jumpLet) + str(listaNum[indexNum2 - 1])
                    if mapa[jump] == "  ":
                        mapa[jump] = mapa[move[0]]
                        mapa[move[1]] = "  "
                        mapa[move[0]] = "  "
                        jogador = "branco"
                        createMap()  
                    else: 
                        invalido()
                else:
                    if charNum2 == "1":
                        mapa[move[1]] = "♕ " 
                    else:
                        mapa[move[1]] = posMove1
                    mapa[move[0]] = posMove2
                    jogador = "branco"
                    createMap()
            # Se for Dama/Rainha Preta
            elif mapa[move[0]] == "♕ " and mapa[move[1]] in ["  ", "⬤ ", "♛ "] and jogador == "preto":
                posMove1 = mapa[move[0]]
                posMove2 = mapa[move[1]]
                if mapa[move[1]] == "⬤ " or mapa[move[1]] == "♛ ":
                    if indexLet2 > indexLet1 and indexNum2 > indexNum1:
                        jump = str(listaLet[indexLet2 + 1]) + str(listaNum[indexNum2 + 1])
                    elif indexLet2 > indexLet1 and indexNum2 < indexNum1:
                        jump = str(listaLet[indexLet2 + 1]) + str(listaNum[indexNum2 - 1])
                    elif indexLet2 < indexLet1 and indexNum2 > indexNum1:
                        jump = str(listaLet[indexLet2 - 1]) + str(listaNum[indexNum2 + 1])
                    elif indexLet2 < indexLet1 and indexNum2 < indexNum1:
                        jump = str(listaLet[indexLet2 - 1]) + str(listaNum[indexNum2 - 1])
                    if mapa[jump] == "  ":
                        mapa[jump] = mapa[move[0]]
                        mapa[move[1]] = "  "
                        mapa[move[0]] = "  "
                        jogador = "branco"
                        createMap()  
                    else: 
                        invalido()
                else:
                    mapa[move[1]] = posMove1
                    mapa[move[0]] = posMove2
                    jogador = "branco"
                    createMap()
            else:
                invalido()
        else:
            invalido()
    playagain = False
    playagainVar = input("Desejam jogar novamente? (S / N) ")
    if playagainVar in ["Sim", "sim", "S", "Yes", "yes", "Ok", "ok"]:
        playagain = True