def numero_recebido():
    """Recebe um número inteiro do usuário"""
    numero = int(input("Digite um número inteiro: "))
    return numero

def procura_numero(lista, n):
    """Procura um número em uma lista"""
    for i in range(len(lista)):
        if n == lista[i]:
            return i + 1
    return -1
        
lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]
numero = numero_recebido()
index_of = procura_numero(lista, numero)
print(index_of)