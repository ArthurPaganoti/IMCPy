valor_massa = float(input('Digite aqui o seu peso:'))
valor_altura = float(input('Digite aqui a sua altura:'))
calculo_imc = valor_massa / (valor_altura*valor_altura)

if calculo_imc < 18.5:
    print('Magreza')

elif calculo_imc == 18.5 and calculo_imc <= 24.9:
    print('Normal')

elif calculo_imc == 25 and calculo_imc <= 29.9:
    print('Sobrepeso')

elif calculo_imc > 30:
    print('Obesidade')