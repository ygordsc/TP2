def exibir_menor(lista):
    """Exibe o menor número de uma lista"""
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor   

def exibir_maior(lista):
    """Exibe o maior número de uma lista"""
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior 

def exibir_media(lista):
    """Exibe a média dos números de uma lista"""
    soma = 0
    for item in lista:
        soma += item
    media = soma / len(lista)
    return media

def exibir_soma(lista):
    """Exibe a soma dos números de uma lista"""
    soma = 0
    for item in lista:
        soma += item
    return soma

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
menor = exibir_menor(lista)
maior = exibir_maior(lista)
media = exibir_media(lista)
soma = exibir_soma(lista)
print(f"Menor: {menor} \nMaior: {maior} \nMédia: {media} \nSoma: {soma}")