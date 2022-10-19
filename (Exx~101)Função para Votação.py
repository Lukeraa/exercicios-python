def votar(i):
    from datetime import date
    atual = date.today().year
    id = atual - i
    if id == 16 or id == 17 or id >= 65:
        global voto
        return f'Com {id} anos: VOTO OPICIONAL'
    elif id < 16:
        return f'Com {id} anos: NÃO VOTA'
    else:
        return f'Com {id} anos: VOTO OBRIGATÓRIO'


idade = int(input('Digite seu ano de nascimento: '))
print(votar(idade))
