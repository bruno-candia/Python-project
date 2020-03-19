import random

def jogar():

    print("*********************************")
    print("Bem Vindo ao Jogo da Adivinhação!")
    print("*********************************",end="\n\n")

    numero_secreto= random.randrange(1,101)
    total_de_tentativas=5
    pontos = 1000

    print("DIFICULDADE:")
    print("(1) Fácil (2) Médio (3) Difícil",end=("\n"))
    print("*******************************",end="\n")
    nivel = int(input("Escolha um dificuldade: "))
    print("*************************",end="\n\n")

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número 1 e 100: "))
        print("***********************",end="\n\n")

        if(chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100!",end="\n\n")
            # Oposto do break, não sai mas da continuidade
            continue

        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):    
            print("-> Você ACERTOU!")
            print("Sua pontuação foi de: {}".format(pontos),end="\n\n")
            break
        else:
            if(chute_maior): 
                print("-> Seu chute foi MAIOR que o numero secreto",end="\n\n")
            elif(chute_menor):
                print("-> Seu chute foi MENOR que o numero secreto",end="\n\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!!",end="\n\n")

if(__name__ == "__main__"):
    jogar()
