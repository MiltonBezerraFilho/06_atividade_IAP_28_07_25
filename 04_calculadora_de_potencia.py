#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. "Não utilize a função de potência da linguagem".

base = int( input("Digite a base: "))
expoente = int ( input("Digite o expoente: "))
potencia = 1

if (expoente == 0):
    potencia = 1
else:
    for n in range(1, expoente + 1):
        potencia *= base
print (f"O resultado da base {base} e do expoente {expoente} é a potência {potencia}.")