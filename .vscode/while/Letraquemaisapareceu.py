frase = 'O python e uma linguagem de programação '\
    'Multiparadigma.' \
    'python foi criado por guido van rossun.'
    
i = 0
qtd_atual = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtas_letra_apareceu = frase.count(letra_atual)
    
    if letra_atual == ' ':
         i += 1
         continue
    
    if qtd_atual < qtas_letra_apareceu:
        qtd_atual = qtas_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual
    i += 1  
   
print(
    'A letra que apareceu mais vezes foi: '
    f'"{qtd_atual}" que apareceu '
    f'{letra_apareceu_mais_vezes} x')
