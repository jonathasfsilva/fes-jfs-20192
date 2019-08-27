from AtlasBot.dataStructure import Estrutura

dados = Estrutura()
dados.carrega()


while True:
    pergunta = input("you: ")
    resposta = dados.pesquisa(pergunta)
    if resposta is not None:
        print("bot:", resposta)
    else:
        dado = [pergunta]
        while True:
            resposta = input(pergunta + " ")
            if resposta == '':
                break
            dado.append(resposta)
            print('aprendido!')
        dados.inserir(dado)