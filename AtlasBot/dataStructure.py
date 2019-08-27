from AtlasBot.Node import No


class Estrutura:

    def __init__(self):
        self.__primeiroNo = None

    def getPrimeiroNo(self):
        return self.__primeiroNo

    def setPrimeiroNo(self, no):
        self.__primeiroNo = no

    def inserir(self, dados):
        novoNo = No(dados)
        if self.estaVazia():
            self.setPrimeiroNo(novoNo)
        else:
            no = self.getPrimeiroNo()
            while no.getProximoNo() is not None:
                no = no.getProximoNo()
            no.setProximoNo(novoNo)

    def pesquisa(self, pergunta):
        if not self.estaVazia():
            no = self.getPrimeiroNo()
            while no.getProximoNo() is not None:
                if no.getPergunta() == pergunta:
                    return no.getResposta()
                else:
                    no = no.getProximoNo()
            else:
                if no.getPergunta() == pergunta:
                    return no.getResposta()
        return None

    def show(self):
        no = self.getPrimeiroNo()
        while no.getProximoNo() is not None:
            print(no.getPergunta())
            print(no.getResposta())
            no = no.getProximoNo()
        print(no.getPergunta())

    def estaVazia(self):
        return self.getPrimeiroNo() is None

    def carrega(self):
        arquivo = open("data.db", 'r')
        for linha in arquivo.readlines():
            dados = linha.split(',')
            self.inserir(dados)