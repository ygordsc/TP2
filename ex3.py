def recebe_lista():
    """Recebe uma lista de números inteiros do usuário"""
    lista = []
    while True:
        numero = int(input("Entre com um número inteiro: "))
        if numero == 0:
            break
        else:
            lista.append(numero)
    return lista

def calcula_fatorial(n):
    """Calcula o fatorial de um número n"""
    fatorial = 1
    for i in range(n, 0, -1):
        fatorial = fatorial * i
    return fatorial

def calcula_fatoriais(lista):
    """Calcula os fatoriais de uma lista de números"""
    fatoriais = 0
    for item in lista:
        fatorial = calcula_fatorial(item)
        print(f"Fatorial de {item}: {fatorial}")

lista = recebe_lista()
calcula_fatoriais(lista)
