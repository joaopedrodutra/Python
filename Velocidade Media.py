#Esse programa recebe a distância e o tempo e calcula a velocidade média
#Primeiro vamos pedir a distância e o tempo
print("Esse é o calculador de velociade média")
distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo gasto: ")
#Realizando o cálculo
velocidade_media = float(distancia) / float(tempo)
#Exibindo a mensagem
print("Velociade média = {0:.2f} km/h".format(velocidade_media))