#Faça um programa que peça para 𝑛 pessoas a sua idade, ao final o programa deverá
#verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então,
#dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

numero = int( input("Digite o número de pessoas que vão ser contabilizadas: "))
idade_total = 0

for n in range(1 , numero + 1):
    idade_entrada = int( input("Digite a idade de uma das pessoas a serem medidas: "))
    idade_total += idade_entrada
media = idade_total / numero
if (0 < media < 26):
    print (f"A turma é considerada jovem, com média {media}.")
elif (26 <= media < 61):
    print (f"A turma é considerada adulta, com média {media}.")
else:
    print (f"A turma é considerada idosa, com média {media}.")