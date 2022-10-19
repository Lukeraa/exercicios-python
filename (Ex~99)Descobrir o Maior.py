from time import sleep


def maior(* num):
    m = 0
    for n in num:
        if m == 0:
            m = n
        elif n > m:
            m = n
    print('-=' * 50)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
