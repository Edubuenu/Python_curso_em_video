peso = float(input('Insira seu peso em kilos:'))
altura = float(input('Insira sua altura em metros:'))
imc = peso / (altura**2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você esté na faixa de peso normal')
elif 25 <= imc < 30:
    print('Você esta em sobrepeso')
elif 30 <= imc < 40:
    print('Você esta em obsedidae, cuidado')
elif imc>= 40:
    print('Você esta em obesidade morbida, cuidado!')
    
    


            
