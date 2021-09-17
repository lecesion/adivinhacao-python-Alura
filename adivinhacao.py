import random

def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de ADIVINHAÇÃO!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Easy (2) Medium (3) Hard")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Você está na rodada {} de {}.".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: {}".format(chute_str))
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você ACERTOU e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou e seu chute foi MAIOR que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}.".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou e seu chute foi MENOR que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}.".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo (:")

if(__name__ == "__main__"):
    jogar()