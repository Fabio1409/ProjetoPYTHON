# Calculadora com while

while True:
  numero_1 = input('Digite um número \n>> :')  
  numero_2 = input('Digite outro número \n>> :')
  operador = input('Digite o operador(+-*/)\n>> :')
  
  numeros_validos = None
  
   
  try:
    num_1_float = float(numero_1) 
    num_2_float = float(numero_2)
    numeros_validos = True
    
  except:
    numeros_validos = None
    num_1_float = 0 
    num_2_float = 0
    
  if numeros_validos is None:
    print('Um ou ambos os números digitados são inválidos')
    continue
    
  operadores_permitidos = '+*/-'
    
  if operador not in operadores_permitidos:
    print('Operador inválido')
    continue
    
  if len(operador) < 1:
    print('Digite apenas um operador de cada vez')
    continue
  
  ###
  print('Realizando suas operaçoes.')
  if operador == '+':
    print(f'{num_1_float} + {num_2_float} =',num_1_float + num_2_float)
    
    
  elif operador == '-':
    print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)
    
  elif operador == '*':
    print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
    
  elif operador == '/':
    print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)
  
  else:
    print('Miguel e lindo')
  
  sair = input('Quer sair? [s]im: \n>>> ').lower().startswith('s') 
  
  if sair is True:
    break

