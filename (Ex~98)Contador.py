import time


def contador(i, f, p):
    print(f'Contando: de {i} até {f} de {p} em {p}')
    time.sleep(.3)
    for c in range(i, f, p):
        print(f' {c} ', end='')
        time.sleep(0.5)
    if c != f and f - c == p or c - f == p:
        print(f'-> {f}')
    else:
        print()
    print('=' * 50)


contador(1, 10, 1)
contador(10, 0, -2)
print('Sua vez...')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if p == 0:
    f = 1
if i < f:
    if p < 0:
        p *= -1
if i > f:
    if p < 0:
        p *= -1
    p *= -1
contador(i, f, p)
print('<<< Volte sempre! >>>')
