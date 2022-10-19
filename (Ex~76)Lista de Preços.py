itens = ('Lápis', 1.75,
         'Borracha', 2,
         'caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('-' * 39)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    else:
        print(f'R${itens[pos]:>7.2f}')
print('-' * 39)
