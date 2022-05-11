'''
1. Faça um programa em Python que solicite ao usuário um valor inteiro. Após armazenar
este valor verifique se o mesmo se trata de um valor par ou ímpar, exibindo como
consequência uma mensagem ao usuário. Veja os exemplos:
'''

valor = int(input("Insira um valor inteiro: "))

if (valor % 2 == 0) and (valor != 0):
    print(valor, "é par.")
elif valor == 0:
    print("O valor zero é nulo.")
else:
    print(valor, "é impar.")
