def área(l, c):
    a = l * c
    print(f'A área de um terreno retangular de {l}x{c} é {a}m²')


#Programa Principal
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
área(larg, comp)
