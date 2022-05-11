'''
2. A pirâmide etária é uma forma gráfica que permite demonstrar como encontra-se
distribuída uma população de acordo com suas faixas etárias. Para tal são consideradas
as seguintes faixas etárias:
a) Criança: até 11 anos;
b) Adolescente: dos 12 aos 17 anos;
c) Adultos: dos 18 aos 59 anos;
d) Idoso: 60 anos ou mais;
Considerando as informações acima, faça um programa em Python que receba a idade
para um determinado cidadão brasileiro e especifique em qual faixa etária da pirâmide o
mesmo se encontra. Veja os exemplos:
'''

idade = int(input("Insira sua idade: "))
if (idade >= 0) and (idade <= 11):
    print("Criança")
elif (idade >= 12) and (idade <=17):
    print("Adolescente")
elif (idade >= 18) and (idade <=59):
    print("Adultos")
elif idade >=60:
    print("Idoso")
else:
    print("Idade invalida")