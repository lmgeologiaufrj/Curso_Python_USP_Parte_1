def computador_escolhe_jogada(n, m):
    i = m
    if n <= m:
        jogada = n
    else:
        jogada = m
        while i > 0:
            if (n - i) % (m + 1) == 0:
                jogada = i
            i -= 1
    if jogada == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", jogada, "peças.")
    n = n - jogada
    if n == 0:
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Agora restam", n, "peças no tabuleiro.")
    print("")
    return jogada


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    print("")
    while jogada > m or jogada <= 0 or jogada > n:
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        jogada = int(input("Quantas peças você vai tirar? "))
        print("")
    if jogada == 1:
        print("Você tirou uma peça.")
    else:
        print("Voce tirou", jogada, "peças.")
    n = n - jogada
    if n == 1:
        print("Agora resta uma peça no tabuleiro.")
    else:
        print("Agora restam", n, "peças no tabuleiro.")
    print("")
    return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("")

    if n % (m + 1) == 0:
        print("Você começa!")
        print("")
        vez = 1
    else:
        print("Computador começa!")
        print("")
        vez = 0

    while n > 0:
        if vez == 0:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            vez = 1
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            vez = 0


def campeonato():
    print("Você escolheu um campeonato!")
    print("")
    rodada = 1
    while rodada <= 3:
        print("**** Rodada", rodada, "****")
        print("")
        partida()
        rodada += 1
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 X 3 Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
opcao = int(input("2 - para jogar um campeonato "))
print("")

if opcao == 1:
    partida()
else:
    campeonato()
