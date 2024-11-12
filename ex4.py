def calcula_tabuada():
    """Calcula a tabuada de um a dez"""
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

calcula_tabuada()