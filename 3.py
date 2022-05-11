'''
3. Faça um programa em Python que indique a ordem de classificação para três atletas
olímpicos e acordo com o seu tempo de chegada na prova dos 100m de natação.
Considerando que a ordem de classificação dos nadadores é feita na ordem crescente
dos seus tempos, ou seja, o primeiro é quem possui o menor tempo, solicite ao usuário
os três tempos (double) e apresente a classificação final baseada nos mesmos. Veja o
exemplo:
- Digite os três tempos: 2.35 2.20 3.05
- Classificação Final:
- 1º lugar – “2.20”
- 2º lugar – “2.35”
- 3º lugar – “3.05”
'''
tempo = float(input("Insira o tempo do primeiro nadador? "))
tempo2 = float(input("Insira o tempo do segundo nadador? "))
tempo3 = float(input("Insira o tempo do terceiro nadador? "))
#1º lugar
if (tempo < tempo2) and (tempo < tempo3):
    print("1º lugar -",tempo)
elif (tempo2 < tempo) and (tempo2 < tempo3):
    print("1º lugar -",tempo2)
elif (tempo3 < tempo) and (tempo3 < tempo2):
    print("1º lugar -",tempo3)
#2º lugar
if (tempo > tempo3) and (tempo < tempo2):
    print("2º lugar -",tempo)
elif(tempo > tempo2) and (tempo < tempo3):
    print("2º lugar -",tempo)
elif (tempo2 > tempo3) and (tempo2 < tempo):
    print("2º lugar -",tempo2)
elif (tempo2 > tempo) and (tempo2 < tempo3):
    print("2º lugar -",tempo2)
elif (tempo3 > tempo) and (tempo3 < tempo2):
    print("2º lugar -",tempo3)
elif (tempo3 > tempo2) and (tempo3 < tempo):
    print("2º lugar -",tempo3)

#3º Lugar
if (tempo > tempo2) and (tempo > tempo3):
    print("3º lugar -",tempo)
elif (tempo2 > tempo) and (tempo2 > tempo3):
    print("3º lugar -",tempo2)
elif (tempo3 > tempo) and (tempo3 > tempo2):
    print("3º lugar -",tempo3)
else:
    print("EMPATE")

