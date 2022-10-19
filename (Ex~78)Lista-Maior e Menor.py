num = []
n = 0
while n < 5:
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
    n += 1
print(f'Os números digitados foram: {num}')
print(f'O maior valor lido foi: {max(num)}, na(s) posição(ões) ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}...', end='')
print(f'\nO menor valor lido foi: {min(num)}, na(s) posição(ões)', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}...', end='')
