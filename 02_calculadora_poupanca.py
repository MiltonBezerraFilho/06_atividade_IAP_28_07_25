#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
#Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros
#no período

depo_inicial = float( input("Digite o valor do depósito inicial: "))
taxa = float( input("Digite a taxa de juros em porcentagem: "))
taxa = taxa / 100
ganho_juros = 0
rendimento = depo_inicial
juro_final = 0

for n in range(1, 25):
    ganho_juros = rendimento * taxa
    juro_final += ganho_juros
    rendimento += ganho_juros
    print(f'No mês {n} o valor era de R${rendimento}.')
print(f'O ganho total de juros foi de R${juro_final}.')