trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
idade = 2020 - nasc
trabalhador['idade'] = idade
ctps = int(input('Carteira de Trabalho [0 não tem]: '))
if ctps != 0:
    trabalhador['ctps'] = ctps
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    apos = (trabalhador['contratação'] + 30) - nasc
    trabalhador['aposentadoria'] = apos
else:
    trabalhador['ctps'] = ctps
print('-' * 30)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
