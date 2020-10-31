import game_utils
import casa_fantasma
import adivinha_numero


opcao = None
print('Jogos disponívels:')
print('   - 1: Adivinha o número')
print('   - 2: Aventura na Casa Fantasma')
opcao = game_utils.escolhe_opcao("Que jogo queres jogar?", ["1", "2"])

if opcao == "1":
    adivinha_numero.jogar()
elif opcao == "2":
    casa_fantasma.jogar()