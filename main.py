from caixa import Caixa

caixa = Caixa()

while True:
    print("Digite 1 para depositar")
    print("Digite 2 para sacar")
    print("Digite outro valor para sair")
    x = int(input())
    if x == 1:
        while True:
            print("Digite a cédula desejada e a quantidade")
            print("Digite 0 0 para sair")
            x,y = input().split()
            x = int(x)
            y = int(y)
            if (x):
                caixa.abastecerCaixa(x,y)
            else:
                break
    elif x == 2:
        while True:
            print("Digite o valor desejado")
            print("Digite 0 para sair")
            x = int(input())
            if (x):
                caixa.sacarQuantia(x)
            else:
                break
    else:
        break