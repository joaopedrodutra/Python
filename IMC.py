peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso/altura**2
if imc >= 40.00:
    print("Seu IMC é {:.2f} e você se encontra na categoria Obesidade Grau III".format(imc))
elif imc >= 35.00:
    print("Seu IMC é {:.2f} e você se encontra na categoria Obesidade Grau II".format(imc))
elif imc >= 30.00:
    print("Seu IMC é {:.2f} e você se encontra na categoria Obesidade Grau I".format(imc))
elif imc >= 25.00:
    print("Seu IMC é {:.2f} e você se encontra na categoria Sobrepeso".format(imc))
elif imc >= 18.50:
    print("Seu IMC é {:.2f} e você se encontra na categoria Peso Ideal".format(imc))
elif imc >= 17.00:
    print("Seu IMC é {:.2f} e você se encontra na categoria Baixo Peso Grau I".format(imc))
elif imc >= 16.00:
    print("Seu IMC é {:.2f} e você se encontra na categoria Baixo Peso Grau II".format(imc))
else:
    print("Seu IMC é {:.2f} e você se encontra na categoria Baixo Peso Grau III".format(imc))