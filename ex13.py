def verifica_paridade(numero):
    """Verifica se um número é par ou ímpar"""
    if numero % 2 == 0:
        return True
    else:
        return False

def divide_lista(lista):
    """Divide uma lista em duas, uma de números pares 
    e outra de números ímpares"""
    lista_pares = []
    lista_impares = []
    for item in lista:
        if (verifica_paridade(item)):
            lista_pares.append(item)
        else:
            lista_impares.append(item)
    return lista_pares, lista_impares

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
pares, impares = divide_lista(lista)
print(f"Pares: {pares} \nÍmpares: {impares}")