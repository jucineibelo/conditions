inteiro = int(input("Digite um valor inteiro: "))
if inteiro % 2 == 0:
    print("O número",inteiro," é divisível por 2, logo:")
else:
    print("O numero",inteiro, "não é divisivel por 2")
if (inteiro % 2 == 0) and (inteiro % 3 == 0):
    print("O número",inteiro,"é divisível por 6;")
else:
    print("O número",inteiro,"não é divisível por 6")
if (inteiro % 3 == 0) and (inteiro % 4 == 0):
    print(inteiro,"é divisível por 12")
else:
    print("O número",inteiro, "não é divisível por 12")
if (inteiro % 3 == 0) and (inteiro % 5 == 0):
    print("O número",inteiro,"é divisível por 15")
else:
    print("O número",inteiro, "não é divisível por 15")