#Numa eleição existem três candidatos. Faça um programa que peça o número total de
#eleitores, leia os votos consistindo nos números dos candidatos (você define tais números)
#e, ao final, exiba o número de votos de cada um recebeu.

eleitores = int ( input("Digite o número total de eleitores: "))
cand_1 = 0
cand_2 = 0
cand_3 = 0

for n in range (1, eleitores + 1):
    voto = int ( input("Digite o número do candidato em que quer votar (1, 2 ou 3): "))
    if (voto == 1):
        cand_1 += 1
    elif (voto == 2):
        cand_2 += 1
    elif (voto == 3):
        cand_3 += 1
    else:
        print("Número inválido.")
print(f'O candidato 01 recebeu ({cand_1}) votos, o candidato 02 recebeu ({cand_2}) votos e o candidato 03 recebeu ({cand_3}) votos.')