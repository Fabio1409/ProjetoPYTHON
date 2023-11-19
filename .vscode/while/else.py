string = 'valorqualquer'

i = 0 
while i < len(string):
    letra = string[i]
    if letra == ' ':    # se estiver espaço haverá break
      break # se nao estiver espaço o brek e ignorado
    print(letra)
    i += 1    # sempre mostrara a proxima letra.
else:
    print('Não encontrei uma espaço na string.')    # se houver o break esse else nao sera executado.
    
print('fora do while.')