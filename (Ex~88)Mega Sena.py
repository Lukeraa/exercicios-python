from random import randint
from time import sleep
nj = int(input('Número de jogos a serem sorteados: '))
jogos = []
jogo = []
c = count = 0
while count < nj:
    while c < 6:
        chute = randint(1, 60)
        if chute not in jogo:
            jogo.append(chute)
            c += 1
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    c -= 6
    count += 1
print('-' * 40)
str = 'Mega Sena Automática'
print(f'{str:^40}')
print('-' * 40)
print(f'-=-=-=-=-= Sorteando {nj} Jogos -=-=-=-=-=-')
print('\n')
cnt = 1
for j in jogos:
    print(f'Jogo {cnt}: {j}')
    cnt += 1
    sleep(1)
print('\n')
print('-' * 40)
str = 'Boa Sorte!'
print(f'{str:^40}')
print('-' * 40)
