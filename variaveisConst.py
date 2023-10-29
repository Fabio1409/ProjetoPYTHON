'''Constante = 'variaveis que vão 
mudar muitas condiçoes no mesmo if(ruim)'
        <-Contagem de complexidade(ruim)'''

velocidade = 60 # Velocidade do carro
local_carro = 101 # Velocidade em que o carro está  na estrada.


Radar_1 = 60 # velocidade máxima do radar 1
local_1 = 100 # local onde o radar 1 está.
Radar_range = 1 # A distância onde o radar pega

if velocidade > Radar_1:
    print('Carro Passou acima da velicidade')   
    
    if local_carro >= (local_1 - Radar_range) and\
        local_carro <=(local_carro + Radar_range) and velocidade > Radar_1:
        print('Seu carro foi multado em radar_1!')
else:
    print('Carro passou abaixo da velocidade.')  
