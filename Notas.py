soma_impares = 0
soma_pares = 0
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
for i in range(1,51):
    if i % 2 != 0:
        nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
        soma_impares = soma_impares + nota
media_impares = soma_impares / 25
print("MÉDIA DAS NOTAS DOS ALUNOS ÍMPARES = {:.2f}".format(media_impares))
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
for i in range(1,51):
    if i % 2 == 0:
        nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
        soma_pares = soma_pares + nota
media_pares = soma_pares / 25
print("MÉDIA DAS NOTAS DOS ALUNOS PARES = {:.2f}".format(media_pares))
if media_impares > media_pares:
    print("A MÉDIA DAS NOTAS DOS ALUNOS ÍMPARES FOI A MAIOR!")
else:
    print("A MÉDIA DAS NOTAS DOS ALUNOS PARES FOI A MAIOR!")