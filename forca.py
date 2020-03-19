import random

def jogar():
    print("***************************")
    print("Bem Vindo ao Jogo da Forca!")
    print("***************************",end="\n\n")

    arquivo = open("palavras.txt","r", encoding="utf-8")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavra))
    palavra_secreta = palavra[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    erros = 0
    cont = 0

    enforcou = False
    acertou = False
    print(letras_acertadas)
    
    #enquanto nao enforcou (True) E nao acertou(True)
    while((not enforcou) and (not acertou)):
        

        chute = input("{}º letra: ".format(cont+1))
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        cont += 1

    if(acertou):
        print("Você Ganhou!",end="\n\n")
    else:
        print("Você Perdeu!",end="\n\n")

    print("Fim de jogo!!",end="\n\n")

if(__name__ == "__main__"):
    jogar()