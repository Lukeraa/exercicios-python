num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print(f'''({num[0][0]}) ({num[0][1]}) ({num[0][2]})
({num[1][0]}) ({num[1][1]}) ({num[1][2]})
({num[2][0]}) ({num[2][1]}) ({num[2][2]})''')
pares = []
for l in num:
    for n in l:
        if n % 2 == 0:
            pares.append(n)
soma = 0
for n in pares:
    if soma == 0:
        soma = n
    else:
        soma += n
print(f'A soma dos valores pares é: {soma}')
somatc = num[0][2] + num[1][2] + num[2][2]
print(f'A soma dos valores da terceira coluna é: {somatc}')
mv = 0
for n in num[1]:
    if mv == 0:
        mv = n
    elif n > mv:
        mv = n
print(f'O maior valor da segunda linha é: {mv}')
