import game_utils

tamanho_do_tabuleiro = 61

escolhas_do_jogador = set()
escolhas_do_computador = set()
tabuleiro = list(range(1, tamanho_do_tabuleiro + 1))

def mostra_introducao():
    print("""Como jogar:
    Podes retirar qualquer número, desde que exista nos números disponíveis pelo menos um divisor desse número.
    O número que retirares vai ser adicionado aos teus pontos.
    O computador vai ficar com todos os divisores do número que escolheste.
    Quando não houver mais números que possas retirar, o jogo termina sendo que os números restantes vão ser dados ao computador.""")



def mostra_banner():
    print("""
    
  ______     _                     ______           _       __              
 /_  __/____(_)___  _________ _   / ____/________  (_)___  / /_  ____ ______
  / / / ___/ / __ \/ ___/ __ `/  / __/ / ___/ __ \/ / __ \/ __ \/ __ `/ ___/
 / / / /  / / / / / /__/ /_/ /  / /___(__  ) /_/ / / / / / / / / /_/ (__  ) 
/_/ /_/  /_/_/ /_/\___/\__,_/  /_____/____/ .___/_/_/ /_/_/ /_/\__,_/____/  
                                         /_/                                
                                         
    """)
    print("=" * 50 + " V1.0 " + "=" * 50)


def esta_disponivel(numero):
    if numero in escolhas_do_jogador:
        return False
    elif numero in escolhas_do_computador:
        return False
    elif numero <= 0:
        return False
    elif numero > tamanho_do_tabuleiro:
        return False
    else:
        return True


def divisores_disponiveis(numero):
    div_disp = []
    for num_do_tabuleiro in tabuleiro:
        if esta_disponivel(num_do_tabuleiro) and num_do_tabuleiro != numero and numero % num_do_tabuleiro == 0:
            div_disp.append(num_do_tabuleiro)
    return div_disp

def o_jogo_terminou():
    for numero in tabuleiro:
        div_disp = divisores_disponiveis(numero)
        if div_disp:
            return False
    return True
    
        


def imprime_tabuleiro():
    lista_a_imprimir = []
    for numero in tabuleiro:
        if numero in escolhas_do_jogador or numero in escolhas_do_computador:
            lista_a_imprimir.append("X")
        else:
            lista_a_imprimir.append(str(numero))
    print('Números disponíveis:')
    print(' '.join(lista_a_imprimir))




def jogar():
    opcao = None
    mostra_banner()
    mostra_introducao()
    while opcao != "s":      
        while not o_jogo_terminou():  
            imprime_tabuleiro()
            print("Escolhe um número.")
            numero_escolhido = int(input())
            div_disp = divisores_disponiveis(numero_escolhido)
            if not esta_disponivel(numero_escolhido):
                print(f"O número {numero_escolhido} não está disponível. Escolhe outro.")
            elif not div_disp:
                print(f"O número {numero_escolhido} não pode ser escolhido porque não tem divisores disponíveis")
            else:
                escolhas_do_jogador.add(numero_escolhido)
                for num in div_disp:
                    escolhas_do_computador.add(num)       

        for numero in tabuleiro:
            if numero not in escolhas_do_jogador and numero not in escolhas_do_computador:
                escolhas_do_computador.add(numero)

        print("O jogo terminou!")
        print(f"Pontos do jogador: {sum(escolhas_do_jogador)}")
        print(f"Pontos do computador: {sum (escolhas_do_computador)}")

        if sum(escolhas_do_computador) > sum(escolhas_do_jogador):
            print("O computador venceu esta partida!")
        elif sum(escolhas_do_computador) < sum(escolhas_do_jogador):
            print("O jogador venceu a partida!")
        else:
            print("A partida ficou empatada!")

        opcao = game_utils.escolhe_opcao("Queres recomeçar[r] ou sair[s]?", ["r", "s"])

