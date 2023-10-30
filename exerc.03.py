 # numero =(input('Digite um numero inteiro:'))
 # if numero.isdigit():
 #     entrada_int =int(numero)
 #     par_impar = entrada_int % 2 == 0
   
 #     if par_impar:
 #        print('O numero digitado é {} numero digitado é par'.format(numero))
 #     else:
 #         print('O numero digitado é {} numero digitado é Impar'.format(numero))
 # else:
 #     print('Voçê não digitou um numero inteiro') 


 
     

# try:
#    hora = int(entrada)
#    if hora >= 0 and hora <= 11:
#        print('Bom Dia!')
#    elif hora >= 12 and hora <= 17: 
#         print('Boa tarde!')
#    elif hora >= 18 and hora <= 23:
#       print('Boa noite!')
#    else:
#     print('Não conheço essa hora!'.format(hora))
    
# except:
#     print('Por favoentrada = input('Digite a hora em números inteiros:')
# r digite apenas numeros inteiros')
    
nome = input('Qual seu nome?:')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
        
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome e normal!')
    else:
        print('Seu nome e muito grande')
else: 
    print('Digite mais de uma letra')

