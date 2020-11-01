import game_utils
import casa_fantasma
import adivinha_numero
import trinca_espinhas

def mostra_banner():
    print("""
  ______                 __           ______                         
 /_  __/___ _____  _  __/ /_____     / ____/___ _____ ___  ___  _____
  / / / __ `/ __ \| |/_/ __/ __ \   / / __/ __ `/ __ `__ \/ _ \/ ___/
 / / / /_/ / /_/ />  </ /_/ /_/ /  / /_/ / /_/ / / / / / /  __(__  ) 
/_/  \__,_/ .___/_/|_|\__/\____/   \____/\__,_/_/ /_/ /_/\___/____/  
         /_/                                                         

    """)

mostra_banner()
opcao = None
print('Jogos disponívels:')
print('   - 1: Adivinha o número')
print('   - 2: Aventura na Casa Fantasma')
print('   - 3: Trinca-espinhas')
opcao = game_utils.escolhe_opcao("Que jogo queres jogar?", ["1", "2", "3"])

if opcao == "1":
    adivinha_numero.jogar()
elif opcao == "2":
    casa_fantasma.jogar()
elif opcao == "3":
    trinca_espinhas.jogar()