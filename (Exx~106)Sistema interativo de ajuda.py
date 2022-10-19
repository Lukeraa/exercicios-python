def ajuda():
    while True:
        perg = str(input('Digite um comando ou uma biblioteca -> ')).lower()
        if perg != 'fim':
            print('\033[7;30m', end='')
            print(f'{help(perg)}')
            print('\033[m')
        if perg == 'fim':
            break


ajuda()
print('\033[1;30;41m<<< Volte sempre! >>>')
