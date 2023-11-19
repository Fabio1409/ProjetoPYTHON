# texto = 'python'

# i = 0

# Tm_string = len(texto) 
# while i < Tm_string:
   
#     print(texto[i],i)
#     i += 1

senha = '1234567'
senhaDigitada = ''
repeticoes = 0 

while senha != senhaDigitada:
    senhaDigitada = input(f'sua senha({repeticoes}):')
    repeticoes += 1
    
print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas.')



