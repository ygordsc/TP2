def conta_vogais():
    """Solicita ao usuário que digite caracteres até que ele 
    digite um ponto, e retorna uma lista com as vogais digitadas"""
    char = ""
    lista = []
    while(char != "."):
        char = input("Entre com um caractere: ")
        if(len(char) > 1):
            print("Digite apenas um caractere.")
        elif(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
            print("Vowel")
            lista.append(char)
    return lista

vogais = conta_vogais()
print(f"Número de vogais: {len(vogais)}")
    