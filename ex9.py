def recebe_numeros():
    """Recebe uma lista de números inteiros do usuário"""
    lista = []
    while True:
        numero = int(input("Digite um número inteiro: "))
        if numero == 0:
            break
        else:
            lista.append(numero)
    return lista

def inverte_lista(lista):
    """Inverte a ordem dos elementos de uma lista"""
    return lista[::-1]

numeros = recebe_numeros()
numeros_invertidos = inverte_lista(numeros)
print(f"Lista invertida: {numeros_invertidos}")