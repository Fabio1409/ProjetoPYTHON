numero =(input('Digite um numero inteiro:'))
if numero.isdigit():
    entrada_int =int(numero)
    par_impar=entrada_int % 2 ==0
    
    if par_impar:
        par_impar_texto =''
   
    
    print('O numero é par{}'.format(numero))
else:
    print('Voçê não digitou um numero inteiro') 
#      print('Seu e par')
#  if numero == /% 1:
#       print('seu numero e impar')
     
     
# hora = input('Que horas são?')
# if hora <= '11:00': 
#     print('Bom dia.{}'.format(hora))