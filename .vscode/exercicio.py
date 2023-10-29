nome = input('Digite sem nome:')
idade = input('Qual sua idade?:')
if nome and idade:
    print('Seu nome è {} e sua idade è :{} anos'.format(nome,idade))
    print(f'Seu nome invertido è {nome[::-1]}')
    print(f'Seu nome contém: {len(nome)} Letras ')
    print(f'A primeira letra do seu nome é:{nome[0]}')
    print(f'A ultima letra do seu nome é:{nome[-1]}')
    
    if ' 'in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome nao contém espaço')
else:
    print('Desculpe, voçê deixou os campos vazios.')