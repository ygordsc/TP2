def recebe_numeros():
    """Recebe dois números inteiros do usuário"""
    n1 = int(input("Digite o primeiro número do intervalo: "))
    n2 = int(input("Digite o último número do intervalo: "))
    return n1, n2

def calcula_intervalo(n1, n2):
    """Gera uma lista com os números do intervalo"""
    lista = []
    for i in range(n1, n2 + 1):
        lista.append(i)
    return lista

def verifica_primo(n):
    """Verifica se um número é primo"""
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return False
    return True
        
def testa_primos(lista):
    """Testa se os números de uma lista são primos"""
    primos = []
    for item in lista:
        if(verifica_primo(item)):
            primos.append(item)
    return primos    
    
n1, n2 = recebe_numeros()
lista = calcula_intervalo(n1, n2)
primos = testa_primos(lista)
print(f"Lista de números primos no intervalo: {primos} \nQuantidade de números primos: {len(primos)}")