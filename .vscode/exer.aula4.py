# # nome = 'Jose Fabio'
# # sobrenome = 'Miranda Da Silva'
# # idade = 37
# # ano_nascimento = 2023-idade
# # maior_de_idade = idade >=18
# # alturametros = 1.78
# # peso = 110
# # imc = peso/alturametros ** 2
# # linha1 = f'{nome}tem{alturametros:.2f}de altura'
# # linha2 = f'pesa {peso} quilos e seu imc è'
# # linha3 = f'{imc:.2f}'
# # print(linha1)
# # print(linha2)
# # print(linha3)
# # Operadores in e not in 
# #strings são ireráveis
# # 0,1,2,3,4,5
# # J O S E F A B I O
# # -6-6-4-3-2-1
# # nome = 'José Fabio'
# # print(nome[3])# mostra a letra que queremos mostrar.
# # print(nome[-4])# indice
# # print('é'in nome )#operador in 
# # print('z'in nome)
# # print(10*'>')
# # print('é'not in nome )#operador not in 
# # print('z'not in nome)
# nome = input('Digite seu nome:')
# encontrar = input('Digite o que deseja encontrar:')
# if encontrar in nome:
#     print(f'{encontrar}está em nome')
# else:
#     print(f'{encontrar}não está em nome')

# Interpolação básica de strigs
# s - String
# d e i - int
# f - float
# x e x - hexadecimal(ABCDEF0123456789)
nome = 'Fábio'
preco = 1000.95897643
variavel = '%s o preço e R$%.2f'%(nome,preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 1500))