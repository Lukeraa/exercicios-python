num = []
a = 0
while a < 5:
    n = int(input('Digite um valor: '))
    if a == 0 or n > num[-1]:
        num.append(n)
        print(f'Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
    a += 1
print(f'sua lista ficou assim: {num}')