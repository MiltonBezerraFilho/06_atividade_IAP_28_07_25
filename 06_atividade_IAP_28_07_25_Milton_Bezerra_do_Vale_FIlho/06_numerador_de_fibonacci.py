'''
No século XIII, o matemático Leonardo Pisa, conhecido como Fibonacci, propôs a seguinte
sequência: (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...). Essa sequência tem uma lei de formação
simples; cada elemento, a partir do terceiro, é obtido somando-se os dois anteriores. Veja:
1+1=2, 2+1=3, 3+2=5 e assim por diante. Faça um programa que leia um número inteiro n
e exiba na tela a sequência de Fibonacci com n elementos.
'''

entrada = int ( input("Digite um número inteiro: "))
anterior = 0
proximo = 1

if (entrada < 1):
    print("Erro matemático.")
else:
    for n in range(0, entrada):
        soma = anterior + proximo
        anterior = proximo
        proximo = soma
        print(anterior)