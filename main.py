from caixa import Caixa

caixa = Caixa()

print("###########################")
print("# Digite 1 para depositar #")
print("# Digite 2 para sacar     #")
print("# Digite 9 para sair      #")
print("###########################")

while True:
    print("Operação: ",end='')
    x = int(input())
    if x == 1:
        while True:
            print("Digite a cédula desejada e a quantidade (0 0 para sair): ",end='')
            x,y = input().split()
            x = int(x)
            y = int(y)
            if (x):
                print()
                print(caixa.abastecerCaixa(x,y))
                print()
            else:
                break
    elif x == 2:
        while True:
            print("Digite o valor desejado (0 para sair): ", end='')
            x = int(input())
            if (x):
                print()
                print(caixa.sacarQuantia(x))
            else:
                break
    else:
        break