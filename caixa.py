from collections import Counter

class Caixa():
    
    def __init__(self) -> None:
        self.__quantiaTotal = 0
        self.__notas = {"10": 0, "20": 0, "50": 0, "100": 0}
    
    
    def abastecerCaixa(self, nota, quantia):
        self.__notas[str(nota)] += quantia
        self.__quantiaTotal += nota * quantia
        print("Caixa abastecido com "+str(quantia)+" nota(s) de "+str(nota))

    def sacarQuantia(self, quantia):
        retorno = self.__avaliarSaque(quantia)
        if (retorno):
            self.__informarNotasSaque(retorno)
        else:
            print("Saque Rejeitado")
    
    def __avaliarSaque(self, quantia):
        if quantia > self.__quantiaTotal:
            return False
        else:
            return self.__algoritmoSaque(quantia)        

    def __dicionarioParaLista(self, dicionario):
        listaNotas = []
        for nota, quantidade in dicionario.items():
            for i in range(0, quantidade):
                listaNotas.append(int(nota))
        return listaNotas
    
    def __listaParaDicionario(self, lista):
        dicionarioNotas = {"10": 0, "20": 0, "50": 0, "100": 0}
        for i in range(len(lista)):
            if lista[i] == 10:
                dicionarioNotas["10"] += 1
            elif lista[i] == 20:
                dicionarioNotas["20"] += 1
            elif lista[i] == 50:
                dicionarioNotas["50"] += 1
            else:
                dicionarioNotas["100"] += 1
        return dicionarioNotas

    def __algoritmoSaque(self, quantia):
        resposta = []
        temporario = []
        lista = self.__dicionarioParaLista(self.__notas)
        lista = sorted(list(set(lista)))
        self.__backtracking(resposta, lista, temporario, quantia, 0)
        lista = self.__dicionarioParaLista(self.__notas)
        for subLista in resposta:
            if self.__sublista(lista, subLista):
                saque = self.__listaParaDicionario(subLista)
                self.__notas = {chave: self.__notas[chave] - saque.get(chave, 0) for chave in self.__notas.keys()}
                return saque
        return False
 
    def __backtracking(self, resposta, lista, temporario, quantia, indice):
        if(quantia == 0):
            resposta.append(list(temporario))
            return
        for i in range(indice, len(lista)):
            if(quantia - lista[i]) >= 0:
                temporario.append(lista[i])
                self.__backtracking(resposta, lista, temporario, quantia-lista[i], i)
                temporario.remove(lista[i])
    
    def __sublista(self, lista1, lista2):
        sobra = Counter(lista2)
        for valor in lista1:
            if sobra[valor]:
                sobra[valor] -= 1
        return False if +sobra else True

    def __informarNotasSaque(self, saque):
        print("Notas liberadas no saque:")
        for nota, quantidade in saque.items():
            if quantidade:
                print(str(quantidade)+" de "+nota+" reais")