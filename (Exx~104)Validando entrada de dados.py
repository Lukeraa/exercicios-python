def leiaInt(text):
    nu = str(input(f'{text}'))
    if nu.isnumeric() == False:
        while nu.isnumeric() == False:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            nu = str(input(f'{text}'))
    if nu.isnumeric():
        print(f'Você digitou o número \033[1;32m{nu}\033[m')
        print('\033[1;97m✂---' * 9)
        print('\033[1;34m<<<\033[m \033[1;34mVolte Sempre\033[m \033[1;34m>>>\033[m')
        exit()


#Programa Principal
n = leiaInt('Digite um número: ')
