'''
4. Considere que a situação de um aluno é definida de acordo com sua nota anual (NA), e
que esta é calculada de acordo com a média de suas 4 notas parciais bimestrais (NPB).
Sendo assim sua pode ser:
a) Reprovado por Nota: para NA menor que “5”;
b) Em Recuperação: para NA maior ou igual a “5” e menos que “7”;
c) Aprovado: para NA maior ou igual a 7;
Contudo a frequência também deve ser levada em consideração, com isso, caso ela seja
menor que 75% o aluno deve ter sua situação como “Reprovado por Frequência”.
A partir das informações apresentadas implemente um algoritmo em Python que receba
as 4 notas parciais bimestrais (NPB) e a frequência do aluno e indique se ele está
"Aprovado", "Em Recuperação" ou "Reprovado". . Caso a situação seja “Reprovado”,
indique por qual critério. Veja os exemplos a seguir:
- Digite as 4 notas bimestrais: 7.5 8.5 5.0 6.0
- Digite a frequência: 80
- Média Anual: 6.7
- Situação: Em Recuperação
- Digite as 4 notas bimestrais: 9.0 9.5 9.5 10.0
- Digite a frequência: 60
- Média Anual: 9.5
- Situação: Reprovado por Frequência
'''
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))
frequencia = float(input("Qual a frequência do aluno: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if (media < 5) and (frequencia >= 75):
    print("Média Anual",media,"Reprovado por nota.")
elif (media >= 5) and (media <7) and frequencia >= 75:
    print("Média Anual",media,"Em recuperação.")
elif (media >= 7) and frequencia >= 75:
    print("Média Anual",media,"Aprovado.")
elif (media < 5 ) and frequencia < 75:
    print("Média Anual", media, "Reprovado por falta e por nota.")

