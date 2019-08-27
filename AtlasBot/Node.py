from random import randint


class No:

    def __init__(self, dados):
        self.__pai = None
        self.__pergunta = dados[0]
        self.__resposta = dados[1:]
        self.__proximoNo = None

    def getPai(self):
        return self.__pai

    def setPai(self, pai):
        self.__pai = pai

    def getPergunta(self):
        return self.__pergunta

    def setPergunta(self, pergunta):
        self.__pergunta = pergunta

    def getResposta(self):
        return self.__resposta[randint(0, len(self.__resposta) - 1)]

    def setResposta(self, resposta):
        self.__resposta = resposta

    def getProximoNo(self):
        return self.__proximoNo

    def setProximoNo(self, proximoNo):
        self.__proximoNo = proximoNo