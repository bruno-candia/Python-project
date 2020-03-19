import random

def jogar():
    
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

 
    enforcou = False
    acertou = False
    erros = 0
    cont = 0
    
    #enquanto nao enforcou (True) E nao acertou(True)
    while((not enforcou) and (not acertou)):
        

        chute = pede_chute(cont)

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        cont += 1

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def imprime_mensagem_vencedor():
    print("Você Ganhou!",end="\n\n")

def imprime_mensagem_perdedor():
    print("Você Perdeu!",end="\n\n")


def imprime_mensagem_abertura():
    print("***************************")
    print("Bem Vindo ao Jogo da Forca!")
    print("***************************",end="\n\n")

def pede_chute(cont):
    chute = input("{}º letra: ".format(cont+1))
    return chute.strip().upper()

def carrega_palavra_secreta():
    arquivo = open("palavras.txt","r", encoding="utf-8")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavra))
    return palavra[numero].upper()
    
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index=0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


if(__name__ == "__main__"):
    jogar()