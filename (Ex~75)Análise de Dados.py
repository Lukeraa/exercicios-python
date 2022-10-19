num = (int(input('Digite um número: ')), int(input('Digite mais número: ')),
      int(input('Digite outro número: ')), int(input('Digite o último número: ')))
print('Você digitou os valores: ', end='')

for n in num:
    print(f'{n} ', end='')

print(f'\nO valor 9 apareceu {num.count(9)} vez(es)')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('O(s) valor(es) par(es) digitado(os) foram: ', end='')
for n in num:
    if n % 2 == 0:
         print(n, end=' ')
