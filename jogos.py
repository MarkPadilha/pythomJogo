import forca
import adivinhacao

print("********************************")
print("****** Escolha seu jogo! *******")
print("********************************")

print("(1) Jogo da Forca || (2) Jogo da Adivinhação")

jogo = int(input("Escolha o jogo: "))

if(jogo == 1) :
     print("Jogando Forca")
     forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    advinhacao.jogar()