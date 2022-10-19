aluno = {}
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
aluno['nome'] = nome
aluno['media'] = media
if media < 7:
    sit = 'Reprovado'
else:
    sit = 'Aprovado'
aluno['situação'] = sit
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
