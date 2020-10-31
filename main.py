import time
import random

inventario = {
    'chave_porta_do_corredor': False,
    'queijo': False,
    'livro_de_bruxaria': False
}

def mostra_banner():
    print("""_______                                                            _______                     _______                                       
(_______)                   _                                      (_______)                   (_______)           _                          
 _______ _   _ _____ ____ _| |_ _   _  ____ _____    ____  _____    _       _____  ___ _____    _____ _____ ____ _| |_ _____  ___ ____  _____ 
|  ___  | | | | ___ |  _ (_   _) | | |/ ___|____ |  |  _ \(____ |  | |     (____ |/___|____ |  |  ___|____ |  _ (_   _|____ |/___)    \(____ |
| |   | |\ V /| ____| | | || |_| |_| | |   / ___ |  | | | / ___ |  | |_____/ ___ |___ / ___ |  | |   / ___ | | | || |_/ ___ |___ | | | / ___ |
|_|   |_| \_/ |_____)_| |_| \__)____/|_|   \_____|  |_| |_\_____|   \______)_____(___/\_____|  |_|   \_____|_| |_| \__)_____(___/|_|_|_\_____|                                                                                                                                             
    """)
    print("=" * 50 + " V1.1 " + "=" * 50)

def masmorras_frank():
    print("Estás acorrentado numa parede fria.")
    time.sleep(1)
    print("O Frankenstein está a chegar às masmorras...")
    time.sleep(1)
    print('Frankenstein: "Tu és muito fraco rapaz! Não resistes nem a um murro meu, quanto mais a dias acorrentado!"')
    time.sleep(1)
    print('Tu: "Cala-te! Eu vou escapar daqui! Tu vais ver!"')
    time.sleep(1)
    print('Frankenstein: Hahahahaha! Tchau fracote!')
    time.sleep(1)
    print("Passado algum tempo um rato aparece à tua frente com um ar esfomeado...")
    if inventario["queijo"]:
        print("Decides dar o teu pedaço de queijo ao rato...")
        print("E como recompensa o rato rói as correntes e tu consegues escapar.")
        print("Parabéns!")
        exit(0)
    else:
        print("O rato começa a cheirar os teus pés...")
        time.sleep(2)
        print("E começa a comer-te membro a membro...")

def nivel_sotao():
    print("Subiste as escadas e encontraste um sótão com três baús.")
    opcao = escolhe_opcao(
        "Queres abrir o baú de ouro[o], o baú de ferro[f], ou o baú de madeira[m] ou descer as escadas[d]?", ["o", "f", "m", "d"])
    if opcao == "o":
        print("Abriste o baú de ouro e de dentro dele saltaram cem aranhas venenosas!")
    elif opcao == "f":
        print("Abriste o baú de ferro, encontraste uma chave e decidiste descer as escadas")
        inventario['chave_porta_do_corredor'] = True
        nivel_corredor()
    elif opcao == "d":
        nivel_corredor()
    elif opcao == "m":
        print("Encontraste uma vassoura.")
        if inventario["livro_de_bruxaria"]:
            print("Com o teu livro de bruxaria transformaste a vassoura numa vassoura voadora e saíste dali para fora!")
            print("Parabéns!")
            exit(0)
        else:
            print("Se eu fosse bruxa, fazia alguma coisa com esta vassoura...")
            nivel_sotao()

def escolhe_opcao(pergunta, opcoes_validas):
    opcao = None
    while opcao not in opcoes_validas:
        print(pergunta)
        opcao = input()
    return opcao

def nivel_cave():
    print("Estás numa cave escura e fria...")
    print("Reparas que há dois buracos na parede.")
    opcao = escolhe_opcao("Metes a mão no buraco do lado esquerdo[e], o do lado direito[d] ou subir as escadas[s]?", ["e", "d", "s"])
    if opcao == "e":                
        print("...encontras uma jiboia que te engole vivo de uma só vez!!!")
    elif opcao == "s":
                nivel_corredor()
    elif opcao == "d":
        if inventario["queijo"] or inventario["livro_de_bruxaria"]:
            print("Este buraco encontra-se vazio. Já tiraste tudo o que havia para tirar")
            nivel_cave()
        else:
            queijo_ou_livro = random.randint(0, 1)
            if queijo_ou_livro == 0:
                inventario["queijo"] = True
                print("Hmm... Um pedaço de queijo... Delicioso...")
                print("Um pedaço de queijo adicionado ao inventário.")
            else:
                inventario["livro_de_bruxaria"] = True
                print('Hmm... Um livro? Deixa-me ler o título (está escrito "Os feitiços do demónio").')
                print("Hmm... Se calhar vai me dar jeito...")
                print("Um livro de feitiçaria adicionado ao inventário.")
            nivel_cave()
        

def mostra_introducao():
    print("""Foste transportado para um quarto escuro.
Estás desorientado, cheio de frio e de fome...
Será que consegues sair daqui com vida?
""")

def nivel_corredor():
    print("Estás num corredor com umas escadas e uma porta")
    opcao = escolhe_opcao(
        "Queres subir[s], descer[d], voltar para o quarto[q] ou abrir a porta[p]?", 
        ["s", "d", "q", "p"])
    if opcao == "s":
        nivel_sotao()
    elif opcao == "q":
        nivel_quarto()
    elif opcao == "p":
        if inventario['chave_porta_do_corredor']:
            print("Infelizmente, atrás da porta estava o Frankenstein!")
            time.sleep(2)
            bom_ou_mau = random.randint(0, 3)
            if bom_ou_mau == 0:
                print("Dá-te uma marretada na cabeça e desfaz-te aos pedaços!")
            else:                
                print("Agarra em ti e leva-te para o seu castelo e prende-te nas masmorras...")
                masmorras_frank()
        else:
            print("Lamento. A porta está trancada. Talvez devesses procurar uma chave...")
            nivel_corredor()
    elif opcao == "d":
        nivel_cave()        

def nivel_quarto():
    print("Olhas à tua volta e consegues ver um interruptor e uma porta.")
    opcao = escolhe_opcao("Queres abrir a porta[p] ou ligar o interruptor[i]", ["p", "i"])
    if opcao == "p":
        nivel_corredor()   
    else:
        print("Sentes um leve cheiro a gás, mas decides ligá-lo na mesma...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        bom_ou_mau = random.randint(0, 5)
        if bom_ou_mau != 0:
            print("Uma enorme explosão!!!!!")
            print("Infelizmente, esta não foi a decisão mais correta... :(")
        else:
            print("Tiveste sorte. A luz acendeu-se e consegues ver um túnel que te permite escapar.")
            print("Conseguiste!!!")
            exit(0)

opcao_sair_ou_continuar = None

while opcao_sair_ou_continuar != "s":
    for key in inventario.keys():
        inventario[key] = False
    mostra_banner()
    mostra_introducao()
    nivel_quarto()
    print("Infelizmente morreste!")
    opcao_sair_ou_continuar = escolhe_opcao("Queres recomeçar[r] ou sair[s]?", ["r", "s"])