#43. Com a estrutura de repetição while, faça um Jogo de Adivinhação, onde:
#O PC escolhe um número entre 0 e 10 (função random), sem o jogador saber qual é este
#número. Guarde numa variável. O jogador deve ir dando palpites (chutando), até acertar o
#número escolhido pelo PC. No final, apresente quantas tentativas foram necessárias até acertar.

#CHUTA ATÉ ACERTAR 
import random
def gera():
    return random.randint(-0,11)

def game():
    resposta = gera()
    tentativa = 0
    print("\nPalpite gerado!\n")

    chute=0
    while chute is not resposta:
        tentativa +=1
        chute = int(input("Qual seu chute: "))
        if chute > resposta:
            print("Errou! É um valor MENOR - que ", chute)
        elif chute < resposta:
            print("Errou! É um valor MAIOR + que ", chute)
        else:
            print("Parabéns! O número gerado foi ",resposta, \
                  " Acertou em  ",tentativa,"  tentativas! ")
    
while True:
    game()