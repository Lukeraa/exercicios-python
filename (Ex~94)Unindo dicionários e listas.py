pessoa = {}
pessoas = []
mulheres = []
qtd = 1
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('sexo: [M/F]')).upper()
    pessoa['idade'] = int(input('Idade: '))
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    qc = str(input('Quer continuar? [S/N]')).upper()
    if qc == 'N':
        break
    qtd += 1
media = soma / qtd
str = 'Análise'
print('-' * 50)
print(f'{str:^50}')
print('-' * 50)
print(f'Foram cadastradas {qtd} pessoas')
print(f'A média de idade do grupo é: {media}')
print(f'As mulheres cadastradas foram: \n{mulheres}')
print('As pessoas com idade acima da média foram:')
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k}....{v} ||', end='')
        print()
        print()
print('<<< Volte sempre! >>>')
