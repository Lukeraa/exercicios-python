from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
c = 1
print('-'*40)
str = 'Jogo de Dados'
print(f'{str:^40}')
print('-'*40)
while c < 5:
    j = randint(1, 6)
    jogadores[c] = j
    print(f'Jogador {c} tirou {j}')
    sleep(1)
    c += 1
print('-'*40)
str = 'RANKING'
print(f'{str:^40}')
print('-'*40)
sleep(.5)
count = 1
ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in ranking:
    print(f'{count}° Lugar: Jogador {k} que tirou {v}')
    count += 1
    sleep(1)
