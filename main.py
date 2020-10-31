import time
import random

inventario = {
    'chave_porta_do_corredor': False
}

def nivel_tres():
    print("Subiste as escadas e encontraste um sótão com três baús.")
    opcao = escolhe_opcao(
        "Queres abrir o baú de ouro[o], o baú de ferro[f], ou o baú de madeira[m]?", ["o", "f", "m"])
    if opcao == "o":
        print("Abriste o baú de ouro e de dentro dele saltaram cem aranhas venenosas!")
    elif opcao == "f":
        print("Abriste o baú de ferro, encontraste uma chave e decidiste descer as escadas")
        inventario['chave_porta_do_corredor'] = True
        nivel_dois()
    elif opcao == "m":
        print("Encontraste uma vassoura de bruxa que te permitiu voar dali para fora")
        exit(0)
def escolhe_opcao(pergunta, opcoes_validas):
    opcao = None
    while opcao not in opcoes_validas:
        print(pergunta)
        opcao = input()
    return opcao

def mostra_introducao():
    print("""Foste transportado para um quarto escuro.
Estás desorientado, cheio de frio e de fome...
Será que consegues sair daqui com vida?
""")

def nivel_dois():
    print("Estás num corredor com umas escadas e uma porta")
    opcao = escolhe_opcao(
        "Queres subir[s], descer[d], voltar para o quarto[q] ou abrir a porta[p]?", 
        ["s", "d", "q", "p"])
    if opcao == "s":
        nivel_tres()
    elif opcao == "q":
        nivel_um()
    elif opcao == "p":
        if inventario['chave_porta_do_corredor']:
            bom_ou_mau = random.randint(0, 3)
            if bom_ou_mau != 0:
                print("Infelizmente, atrás da porta estava o Frankenstein! :(")
            else:
                print("Abriste a porta e escapaste da casa!")
                print("Ganhaste!")
                exit(0)


            
        else:
            print("Lamento. A porta está trancada. Talvez devesses procurar uma chave...")
            nivel_dois()
    else:
        print("Desceste as escadas e entraste numa cave escura e fria...")
        print("Acendes as luzes e, quando te viras...")
        time.sleep(5)
        print("...encontras uma jiboia que te engole vivo de uma só vez!!!")

def nivel_um():
    print("Olhas à tua volta e consegues ver um interruptor e uma porta.")
    opcao = escolhe_opcao("Queres abrir a porta[p] ou ligar o interrupetor[i]", ["p", "i"])
    if opcao == "p":
        nivel_dois()   
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
    mostra_introducao()
    nivel_um()
    print("Infelizmente morreste!")
    opcao_sair_ou_continuar = escolhe_opcao("Queres recomeçar[r] ou sair[s]?", ["r", "s"])