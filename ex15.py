def entrada_dados():
    """Recebe o nome e notas do aluno"""
    nome = input("Digite seu nome: ")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    return [nome, n1, n2]

def calcula_media_aluno(n1, n2):
    """Calcula a média das notas de um aluno"""
    return (n1 + n2) / 2

def calcula_media_turma(lista):
    """Calcula a média da turma"""
