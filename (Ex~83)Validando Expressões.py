e = str(input('Digite uma Expressão: '))
pilha = []
for s in e:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão Válida')
else:
    print('Expressão inválida')
