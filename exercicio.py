print("********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("********************************")

numero_secreto = 20
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Você está na rodada {} de {}.".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: {}".format(chute_str))
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você ACERTOU!")
    else:
        if(maior):
            print("Você errou e seu chute foi MAIOR que o número secreto.")
        elif(menor):
            print("Você errou e seu chute foi MENOR que o número secreto.")

    rodada = rodada + 1

print("Fim do Jogo (:")