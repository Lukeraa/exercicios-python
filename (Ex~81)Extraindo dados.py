num = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    qc = str(input('Quer continuar? [S/N]')).upper()
    if qc == 'S':
        print('Continuando...')
    else:
        break
r = sorted(num, key=int, reverse=True)
print(f'Foram digitados {len(num)} valores')
print(f'Sua lista em forma decrescente ficou assim: {r}')
if num.count(5) >=1:
    print(f'O valor 5 foi digitado {num.count(5)} vez(es)')
else:
    print(f'O valor 5 não foi digitado')
print('-'*80)
