
"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string  = 'jose Fabio'
outra_variavel = {f'{string[:3]}ABC{string[4:]}'}
print(string)
print(outra_variavel) # strings sao imutaveis
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.zfill(100))# vai aparecer  zeros a esquerda do sua string