from time import sleep
jogadores = []
jogador = {}
gols = []
ct = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    c = 0
    total = 0
    while c < partidas:
        gol = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gol)
        total += gol
        c += 1
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogador['partidas'] = partidas
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()
    qc = str(input('Quer continuar? [S/N]')).upper()
    if qc not in 'SN':
        while qc not in 'SN':
            qc = str(input('Digite apenas "S" ou "N"? [S/N]')).upper()
    if qc == 'N':
        break
print('-' * 37)
print(f'cod   | Nome     | Gols       | Total')
c = 0
for k, v in enumerate(jogadores):
    print(f'{c}...... {jogadores[c]["nome"]}..... {jogadores[c]["gols"]}........ {jogadores[c]["total"]}')
    c += 1
while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    while escolha not in range(0, len(jogadores)) and escolha != 999:
        print('ERRO! Não existe jogador com este código.')
        print('-' * 50)
        escolha = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if escolha == 999:
        break
    print(f'-- Levantamento do jogador {jogadores[escolha]["nome"]}')
    c = 0
    for g in enumerate(jogadores[escolha]['gols']):
        print(f'No jogo {c + 1} fez {g[1]} gols.')
        c += 1
print('Encerrando...')
sleep(1)
print('<<< Volte Sempre! >>>')
