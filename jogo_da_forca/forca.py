import random


def jogar_forca():
    imprime_mensagem_de_abertura()
    upper_palavra_secreta = importacao_lista_de_palavras()

    vetor = inicializa_letras_das_palavras(upper_palavra_secreta)
    letras_utilizadas = []

    tentativas = 7
    while tentativas > 0:

        count = 0
        print(f"VOCE POSUI:  {tentativas}  TENTATIVAS")
        letra = input("Qual a letra? ")
        print("")

        letra_upper = letra.upper()
        acertou = False
        numero_de_letras_usadas = 0

        if letra_upper not in letras_utilizadas:
            for cabelo in upper_palavra_secreta:
                if letra_upper == cabelo:
                    local = upper_palavra_secreta.index(letra_upper)
                    vetor[count] = letra_upper
                    marcador = 1
                    print(f"A LETRA -> {letra_upper} ESTÁ NA PALAVRA NA POSICAO {count + 1}")
                    print("")
                    acertou = True
                count = count + 1

        if letra_upper in letras_utilizadas:
            marcador = 1
            print(f"A letra {letra_upper} já foi usada, favor escolha outra letra")
            print("")
            tentativas = tentativas + 1

        letras_utilizadas.insert(numero_de_letras_usadas, letra_upper)
        numero_de_letras_usadas += numero_de_letras_usadas

        if not acertou:
            tentativas = tentativas - 1
        transforma_lista_para_string = ' '.join([str(elem) for elem in vetor])

        acertou = "_" not in vetor

        if (acertou):
            imprime_mensagem_vencedor(upper_palavra_secreta)
            break
        desenha_forca(tentativas, transforma_lista_para_string)

    if tentativas == 0:
        imprime_mensagem_perdedor(upper_palavra_secreta)


def imprime_mensagem_de_abertura():
    print("*****************************")
    print("Bem Vindo ao Jogo de FORCA")
    print("*****************************")


def importacao_lista_de_palavras():
    palavras = []
    arquivo = open("Lista-de-Palavras.txt", "r")
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    upper_palavra_secreta = palavra_secreta.upper()
    return upper_palavra_secreta


def inicializa_letras_das_palavras(upper_palavra_secreta):
    return ["_" for palavra in upper_palavra_secreta]


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("//                   \/\  ")
    print("\|    XXX     XXX   | /   ")
    print(" |    XXX     XXX   |/     ")
    print(" |                  |      ")
    print(" \__       X      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   \_      U     _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor(upperPalavraSecreta):
    print(f"Parabéns, você ganhou! a palavra secreta era: {upperPalavraSecreta}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(tentativas, transformaListaParaString):
    print(f"  _______               {transformaListaParaString}")
    print(" |/      |    ")

    if (tentativas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar_forca()
