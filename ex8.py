def soma_listas(lista1, lista2):
    """Soma os elementos de duas listas"""
    nova_lista = []
    for i in range(len(lista1)):
        nova_lista.append(lista1[i] + lista2[i])
    return nova_lista

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]
nova_lista = soma_listas(lista1, lista2)
print(nova_lista)