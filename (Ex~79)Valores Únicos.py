num = []
a = True
while a == True:
    n = (int(input('Digite um Número: ')))
    if n not in num:
        num.append(n)
        print(f'Valor adicionado com sucesso!')
    else:
        print('Este valor já foi digitado, portanto, não será adicionado!')
    qc = str(input('Quer continuar? [S/N]')).upper()
    while qc.upper() not in'SN':
        qc = str(input('Quer continuar? [S/N]')).upper()
        if qc in'SN':
            break
    if qc == 'N':
        break
    else:
        print('continuando...')
print(f'Sua lista ficou assim: {num}')
