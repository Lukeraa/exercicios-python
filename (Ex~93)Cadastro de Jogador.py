jogador = {}
gols = []
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
c = 0
total = 0
while c < partidas:
    gol = int(input(f'Quantos gols na partida {c}? '))
    gols.append(gol)
    total += gol
    c += 1
jogador['gols'] = gols
jogador['total'] = total
print('-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
i = 0
while i < partidas:
    print(f'Na partida {i}, {jogador["nome"]} fez {jogador["gols"][i]}')
    i += 1
