# # '''formatação de strings
# # s - string
# # d - int
# # f - float
# # . - número de degitos>f
# # x ou X - Hexadecimal
# # (Caractere)(><^)quantidade
# # > - esquerda 
# # < - Direita
# # ^ - Centro
# # Sinal - + ou -
# # = - Força o número a aparecer antes dos zeros 
# # Ex.: 0>-100,.1f
# # Conversion flags - !r !s !a
# # '''
# # variavel = 'ABC'
# # print(f'{variavel}')
# # print(f'{variavel: >10}')
# # print(f'{variavel: <10}')
# # print(f'{variavel: ^10}')
# # print(f'{1000.458754125478:.1f}')
# # print(f'O hexadecimal de 1500 é {1500:08X}')
# # print(f'{variavel!r}')

# '''Fatiamento de string
# 0123456789
# Olá mundo
# -987654321
# fatiamento[i:f:p][::]
# Obs .:a função len retorna a quantidade de caracteres da str.
# '''
# variavel = 'Olá Mundo'
# # print(variavel[2])#mostra o caractere 2
# print(variavel[0:9:2])# vai do indice 4 ate o final 
# print(len(variavel[4]))
# print(variavel[0:len(variavel):1])