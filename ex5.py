def recebe_numeros():
    """Recebe dois números inteiros do usuário"""
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    return n1, n2

def calcula_pa(n1, n2):
    """Calcula a soma de uma progressão aritmética
    a partir dos dois primeiros numeros da sequência"""
    diferenca = n1 - n2
    return abs(diferenca)

def gera_sequencia(n1, razao):
    """Gera a sequência de números da PA"""
    print(n1)
    for i in range(9):
        n1 += razao
        print(n1)

n1, n2 = recebe_numeros()
razao = calcula_pa(n1, n2)
gera_sequencia(n1, razao)