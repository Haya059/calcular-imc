def calcular_imc(peso, altura):
    calculo = peso / (altura ** 2)
    return calculo

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


altura = float(input('Digite sua altura, em metros: '))
peso = float(input('Digite o seu peso, em kg: '))

imc = calcular_imc(peso, altura)
print(f'Seu IMC é: {imc:.2f}. Sua classificação é: {classificacao_imc(imc)}')