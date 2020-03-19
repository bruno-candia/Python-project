import os, random, forca, adivinhacao
os.system('cls' if os.name == 'nt' else 'clear')

def escolhe_jogo():
    print("***************************")
    print("********Jogos .py**********")
    print("***************************",end="\n\n")


    print(" (1) Forca (2) Adivinhação")
    print(" *************************")

    jogo= int(input("Qual jogo? "))

    if(jogo == 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()