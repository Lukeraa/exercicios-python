from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 Valores... ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(.3)
    print()


def somapar():
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    if soma == 0:
        print('Não encontrei nenhum valor par.')
    else:
        print(f'A soma dos valore pares é: {soma}')


num = []
sorteia(num)
somapar()
