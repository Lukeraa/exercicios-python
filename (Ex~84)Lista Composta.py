galera = []
pessoas = []
map = mep = 0
while True:
    n = str(input('Nome: '))
    p = float(input('Peso: '))
    pessoas.append(n)
    pessoas.append(p)
    if len(galera) == 0:
        map = mep = pessoas[1]
    else:
        if pessoas[1] > map:
            map = pessoas[1]
        else:
            if pessoas[1] < mep:
                mep = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    qc = str(input('Quer continuar? [S/N]')).upper()
    if qc == 'N':
        break
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi de {map}Kg. Peso de ', end='')
for p in galera:
    if p[1] == map:
        print(f'\033[1;31m-{p[0]}- \033[m', end='')
print(f'\nO menor peso foi de {mep}Kg. Peso de ', end='')
for p in galera:
    if p[1] == mep:
        print(f'\033[1;32m-{p[0]}- \033[m', end='')
