from time import sleep
pessoas = []
aluno = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    pessoas.append(aluno[:])
    aluno.clear()
    qc = str(input('Quer continuar? [S/N]')).upper()
    if qc not in 'SN':
        while qc not in 'SN':
            qc = str(input('Digite apenas "S" ou "N"? [S/N]')).upper()
    elif qc == 'N':
        break
traco = '-'
print(f'   {traco * 40}')
str = 'Boletim'
print(f'   {str:^40}')
print(f'   {traco * 40}')
print('\n           N° | Nome          | Média')
c = 0
for l in pessoas:
    print(f'           {c:^}__|{pessoas[c][0]:^} {pessoas[c][3]:_>15.2f}')
    c += 1
while True:
    opc = int(input('Você deseja saber as notas de qual aluno? (999 Para sair): '))
    if opc == 999:
        print('Terminando...')
        break
    if opc <= len(pessoas) - 1:
        print(f'\nAs notas de {pessoas[opc][0]} são {pessoas[opc][1]} e {pessoas[opc][2]}\n')
sleep(1)
print('\033[1;32m<<< Volte Sempre! >>>')
