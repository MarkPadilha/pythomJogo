import random

def jogar():

    print("********************************")
    print("** Bem vindo ao jogo da forca **")
    print("********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        print("jogando...")
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if(letra.upper() == chute.upper()):
                print("Tem a letra {} na posição {}".format(letra, index))
            index = index + 1

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
