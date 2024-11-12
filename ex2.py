def calcula_media():
    """Calcula a soma e a média dos números de 0 a 100"""
    soma = 0
    for i in range(101):
        soma += i
    media = soma / 100
    return soma, media

soma, media = calcula_media()
print(f"Soma: {soma} \nMédia: {media}")