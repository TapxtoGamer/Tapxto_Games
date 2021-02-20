import game_utils

ESTADO_PERSONAGEM = {}
ESTADO_JOGO = {}

def criar_jogador():
    nome = input("Que nome queres dar ao teu personagem? ")
    genero = game_utils.escolhe_opcao("Qual é o género do teu personagem? [M]asculino ou [F]eminino " , ["m", "f"])
    ESTADO_PERSONAGEM['nome'] = nome
    ESTADO_PERSONAGEM['genero'] = genero
    ESTADO_PERSONAGEM['idade'] = 20
    ESTADO_PERSONAGEM['inteligencia'] = 1
    ESTADO_PERSONAGEM['dinheiro_carteira'] = 500
    ESTADO_PERSONAGEM['dinheiro_banco'] = 0
    ESTADO_PERSONAGEM['forca'] = 0
    ESTADO_PERSONAGEM['sociabilidade'] = 0
    ESTADO_PERSONAGEM['profissao'] = "desempregado"
    ESTADO_PERSONAGEM['fome'] = 0
    ESTADO_PERSONAGEM['vida'] = 100
    ESTADO_PERSONAGEM['sono'] = 0
    ESTADO_PERSONAGEM['dividas'] = 0
    imprimir_estado_jogador()






def imprimir_estado_jogador():
    print(f"""
    Nome: {ESTADO_PERSONAGEM['nome']}
    Género: {ESTADO_PERSONAGEM['genero']}
    Idade: {ESTADO_PERSONAGEM['idade']}
    Características:
        Força: {ESTADO_PERSONAGEM['forca']}
        Sociabilidade: {ESTADO_PERSONAGEM['sociabilidade']}
        Inteligência: {ESTADO_PERSONAGEM['inteligencia']}
        Fome: {ESTADO_PERSONAGEM['fome']}
        Vida: {ESTADO_PERSONAGEM['vida']}
        Sono: {ESTADO_PERSONAGEM['sono']}
    Finanças:
        Carteira: {ESTADO_PERSONAGEM['dinheiro_carteira']}
        Banco: {ESTADO_PERSONAGEM['dinheiro_banco']}
        Dívidas: {ESTADO_PERSONAGEM['dividas']}
    Profissão: {ESTADO_PERSONAGEM['profissao']}
    """)

def imprimir_estado_do_jogo():
    pass

def executar_accao():
    accao = game_utils.escolhe_opcao("O que queres fazer agora? [C]omer; [D]ormir; [E]studar", ["c", "d", "e"])
    if accao == "c":
        opcao_comida = game_utils.escolhe_opcao("""
        Tipos de comida:
            [B]arra de cereais - 1€ = -5 de fome
            [P]ão - 2€ = -7 de fome
            [M]açã - 3€ = -10 de fome
            [E]sparguete - 10€ = -30""" , ["b", "p", "m", "e"])
        if opcao_comida == "b":
            ESTADO_PERSONAGEM['dinheiro_carteira'] -= 1
            ESTADO_PERSONAGEM['fome'] -= 5
        elif opcao_comida == "p":
            ESTADO_PERSONAGEM['dinheiro_carteira'] -= 2
            ESTADO_PERSONAGEM['fome'] -= 7
        elif opcao_comida == "m":
            ESTADO_PERSONAGEM['dinheiro_carteira'] -= 3
            ESTADO_PERSONAGEM['fome'] -= 10
        elif opcao_comida == "e":
            ESTADO_PERSONAGEM['dinheiro_carteira'] -= 10
            ESTADO_PERSONAGEM['fome'] -= 20
        if ESTADO_PERSONAGEM['fome'] < 0:
            ESTADO_PERSONAGEM['fome'] = 0
        imprimir_estado_jogador()
    elif accao == "d":
        ESTADO_PERSONAGEM['sono'] -= 20
        imprimir_estado_jogador()
    elif accao == "e":
        ESTADO_PERSONAGEM['inteligencia'] += 1
        ESTADO_PERSONAGEM['fome'] += 5
        ESTADO_PERSONAGEM['sono'] += 5
        imprimir_estado_jogador()

def terminar_dia():
    ESTADO_JOGO['dia'] += 1
    ESTADO_PERSONAGEM['sono'] += 20
    ESTADO_PERSONAGEM['fome'] += 20

def executar_jogo():
    while ESTADO_PERSONAGEM['vida'] > 0:
        imprimir_estado_do_jogo()
        while ESTADO_JOGO['accoes_disponiveis'] > 0:
            executar_accao()
            ESTADO_JOGO['accoes_disponiveis'] -= 1
        terminar_dia()




def jogar():
    print("""
                                                             
      | |                          | |        \ \    / /(_)    | |       
      | |  ___    __ _   ___     __| |  __ _   \ \  / /  _   __| |  __ _ 
  _   | | / _ \  / _` | / _ \   / _` | / _` |   \ \/ /  | | / _` | / _` |
 | |__| || (_) || (_| || (_) | | (_| || (_| |    \  /   | || (_| || (_| |
  \____/  \___/  \__, | \___/   \__,_| \__,_|     \/    |_| \__,_| \__,_|
                  __/ |                                                  
                 |___/                                                   """)
    print("""Bem vindo ao Jogo da Vida!

    Opções:
    Novo jogo [n]
    Como jogar [c]
    Sair [s]""")
    opcao = game_utils.escolhe_opcao("O que desejas fazer?", ["n", "c", "s"])
    if opcao == "n":
        global ESTADO_PERSONAGEM 
        global ESTADO_JOGO
        ESTADO_PERSONAGEM = {}
        ESTADO_JOGO = {
            'dia': 0,
            'local': 'casa_dos_pais',
            'accoes_disponiveis': 4
        }
        criar_jogador()
        executar_jogo()