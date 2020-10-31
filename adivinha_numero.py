import random

def jogar():
    tentativas = 0
    minimo = 1
    maximo = 1000
    tentativa_do_jogador = None
    numero_aleatorio = random.randint(minimo, maximo)

    print("Olá")
    nome_do_jogador = input("Qual é o teu nome? ")
    print(f"Ok {nome_do_jogador}! Vou pensar num número de {minimo} a {maximo}")


    while tentativa_do_jogador != numero_aleatorio:
        tentativa_do_jogador = int(input("Em que número eu estou a pensar? "))
        tentativas += 1
        if tentativa_do_jogador < numero_aleatorio:
            print(f"Não acertaste. O número é maior do que {tentativa_do_jogador}! ")
        else:
            print(f"Não acertaste. O número é menor do que {tentativa_do_jogador}!")

    print(f"Boa {nome_do_jogador}! Acertaste em {tentativas} tentativas!")
    exit(0)