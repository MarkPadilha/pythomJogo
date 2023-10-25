import random

print("********************************")
print("Bem vindo ao jogo de advinhação!")
print("********************************")
print("********************************")
print("********************************")
print("Escolha a diculdade")
print("(1) Fácil - 10 tentativas ")
print("********************************")
print("(2) médio - 5 tentativas " )
print("********************************")
print("(3) Difícil - 3 tentativas ")
print("********************************")
dificuldade = int(input("Digite o número da dificuldade: "))
numero_secreto = random.randrange(1, 101)
total_tentativas = 0
rodada = 1
pontos = 1000

if (dificuldade == 1):
    total_tentativas = 20
elif (dificuldade == 2):
    total_tentativas = 10
else:
    total_tentativas = 5




for rodada in range(1, total_tentativas +1):
    print("Tentativa {} de {}.".format(rodada, total_tentativas), )
    chute_string = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_string)
    chute = int(chute_string)


    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto
    acertou = chute == numero_secreto

    if(chute < 1 or chute > 100):
        print("Número precisa ser entre 1 e 100!")
        continue

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(chute_maior):
            print("Você errou, seu chute foi maior que o número secreto!!")
        elif(chute_menor):
            print("Você errou, seu chute foi menor que o número secreto!")
        chute_errado = abs(numero_secreto - chute)
        pontos = pontos - chute_errado


print("o Número secreto era {}".format(numero_secreto))
print("Você ficou com {} pontos" .format(pontos))
print("Fim de jogo!")