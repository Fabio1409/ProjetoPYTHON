'''
Intrudução ao try/except
try -> tentar executar o codigo 
'''
# print(1234)
# print(567)
# int('a')

numero_str = input(
    'Vou dobrar o numero que vc digitar:')
try:
    print('STR:',numero_str)
    #numero_str.isdigit():
    numero_float = float(numero_str)
    print('FLOAT:',numero_float)
    print(f'O dobro do nùmero {numero_float} é {numero_float * 2:.2f}')
   
except:
    print('Isso não é um número!')
    
# print(numero_str.isdigit)
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro do nùmero {numero_float} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número!')