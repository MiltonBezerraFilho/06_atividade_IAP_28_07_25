'''
Escreva um programa que leia um número e verifique se ele é primo. Para fazer essa
verificação, calcule o resto da divisão do número informado por todos os número menores
que ele a partir de 2. Se o resto de uma dessas divisões for igual a 0, o número não é
primo. Note que 0 e 1 não são primos e que 2 é o único primo que é par.
'''
entrada = int ( input("Digite o número para ser verificado se é primo: "))

if (entrada <= 1):
    print("Não é primo.")
elif(entrada == 2):
    print ("É primo.")
else:
    e_primo = True
    for n in range (2, entrada):
        if entrada % 2 == 0:
            e_primo = False
            break
    if (e_primo):
        print ("É primo.")
    else:
        print ("Não é primo.")