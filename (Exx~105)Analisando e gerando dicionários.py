def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = {}
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n) / len(n)
    if sit:
        if dic['media'] >= 7:
            dic['situacao'] = '\033[1;32mBOA\033[m'
        elif dic['media'] >= 5:
            dic['situacao'] = '\033[1;33mRAZOÁVEL\033[m'
        else:
            dic['situacao'] = '\033[1;31mRuim\033[m'
    print(f'Foram digitadas {dic["total"]} notas')
    print(f'A maior nota foi {dic["maior"]}')
    print(f'A menor nota foi {dic["menor"]}')
    print(f'A media das notas foi {dic["media"]}')
    if sit:
        print(f'A situação é {dic["situacao"]}')


resp = notas(0, 0, 7, 8.5, sit=True)
