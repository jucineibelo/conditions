pelagem = str(input("- Possui pelagem curta (c) ou médio (m) ou longo (l)? ")).lower()
peso = str(input("- Possui peso superior a 25kg (s) ou (n)? ")).lower()
altura = str(input("- Possui altura superior a 50 cm (s) ou (n)? ")).lower()
expectativa = str(input("- Possui expectativa de vida inferior a 10 anos (s) ou (n)? ")).lower()

if (pelagem == "c") and (peso == "i") and ( altura == "s") and (expectativa == "n"):
    print("Dalmata")
elif (pelagem == "m") and (peso == "s") and ( altura == "s") and (expectativa == "n"):
    print("Pastor Alemão")
elif (pelagem == "c") and (peso == "s") and ( altura == "n") and (expectativa == "s"):
    print("Bull Dog Inglês")
elif (pelagem == "c") and (peso == "i") and ( altura == "n") and (expectativa == "n"):
    print("Bull Terrier")
elif (pelagem == "m") and (peso == "s") and ( altura == "i") and (expectativa == "n"):
    print("Labrador")
elif (pelagem == "l") and (peso == "s") and ( altura == "s") and (expectativa == "n"):
    print("São Bernardo")
elif (pelagem == "l") and (peso == "s") and ( altura == "i") and (expectativa == "s"):
    print("Chow Chow")
elif (pelagem == "l") and (peso == "n") and ( altura == "n") and (expectativa == "s"):
    print("Pequenês")
elif (pelagem == "m") and (peso == "i") and ( altura == "i") and (expectativa == "n"):
    print("Cocker Inglês")
else:
    print("Opção Invalida")
