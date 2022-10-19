num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print(f'''({num[0][0]}) ({num[0][1]}) ({num[0][2]})
({num[1][0]}) ({num[1][1]}) ({num[1][2]})
({num[2][0]}) ({num[2][1]}) ({num[2][2]})''')