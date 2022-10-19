times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atléico-MG', 'Fluminense', 'Botafogo',
         'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('-=' * 15)
print('Tabela de Classificação do Brasileirão \n')
for t in times:
    print(t)
print('-=' * 15)

print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 15)

print(f'Os últimos quatro são: {times[-4:]}')
print('-=' * 15)

print(f'Times em oredem alfabética: {sorted(times)}')
print('-='* 15)

print(f'O Palmeiras está na {times.index("Palmeiras") + 1}ª posição')
