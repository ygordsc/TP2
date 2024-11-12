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

def filtra_numeros(numeros):
    """Filtra os números maiores ou iguais à media da lista"""
    numeros_filtrados = []
    media = sum(numeros) / len(numeros)
    for numero in numeros:
        if numero >= media:
            numeros_filtrados.append(numero)
    return numeros_filtrados

numeros = recebe_numeros()
numeros_filtrados = filtra_numeros(numeros)
print(f"Lista com números maiores ou iguais a media: {numeros_filtrados}")