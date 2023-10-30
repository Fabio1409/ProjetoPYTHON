numero =(input('Digite um numero inteiro:'))
if numero.isdigit():
    entrada_int =int(numero)
    par_impar = entrada_int % 2 == 0
   
    if par_impar:
       print('o numero digitado é {} numero digitado é par'.format(numero))
    else:
        print('O numero digitado é {} numero digitado é Impar'.format(numero))
else:
    print('Voçê não digitou um numero inteiro') 
     
     
# hora = input('Que horas são?')
# if hora <= '11:00': 
#     print('Bom dia.{}'.format(hora))