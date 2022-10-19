num = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    qc = str(input('Quer continuar? [S/N] ')).upper()
    if qc == 'N':
        break
par = []
imp = []
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
print(f'Sua lista completa ficou assim: {num}')
print(f'Os números pares da sua lista foram: {par}')
print(f'Os números impares da sua lista foram: {imp}')

