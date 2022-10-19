lista = []
imp = []
par = []
c = 1
while c <= 7 :
    v = int(input(f'Digite o {c}° valor: '))
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
    c += 1
lista.append(par)
lista.append(imp)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
