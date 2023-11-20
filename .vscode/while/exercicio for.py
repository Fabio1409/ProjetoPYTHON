"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_Secreta = 'calculadora'
letras_acertadas = ''
numero_tentativas = 0
 
while True:
    
    letra_Digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    
    if len(letra_Digitada)> 1:
        print('digite apenas uma letra:')
        continue
    
    
    if letra_Digitada in palavra_Secreta:
        letras_acertadas += letra_Digitada
    palavra_formada = ''
       
    for letra_secreta in palavra_Secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra Formada:',palavra_formada)
            
    if palavra_formada == palavra_Secreta:
        
        print('Voçê ganhou parabéns!')
        print('A palavra secreta era:{}'.format(palavra_formada))
        print('Vou tentou vezes {}'.format(numero_tentativas))
        break
        
        