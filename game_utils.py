def escolhe_opcao(pergunta, opcoes_validas):
    opcao = None
    while opcao not in opcoes_validas:
        print(pergunta)
        opcao = input()
    return opcao

escolhe_opcao = escolhe_opcao