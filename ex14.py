def valida_numero():
    """Valida se um número inteiro é maior ou igual a zero"""
    while True:
        numero = int(input("Digite um número inteiro: "))
        if (numero < 0):
            print("Número inválido. Digite um número inteiro maior ou igual a zero.")
        else:
            break

valida_numero()