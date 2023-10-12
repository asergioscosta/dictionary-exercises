def cmedia(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

numeroavaliacoes = int(input("Digite o número de avaliações do aluno: "))
numeroalunos = int(input("Digite o número de alunos: "))

turma = {}

for i in range(numeroalunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for j in range(numeroavaliacoes):
        nota = float(input(f"Digite a nota da avaliação {j + 1}: "))
        notas.append(nota)
    media = cmedia(notas)
    turma[nome] = media

for nome, media in turma.items():
    print(f" O aluno {nome} possui a média {media:.2f}")

mediaturma = sum(turma.values()) / len(turma)
print(" A média da turma é: ", mediaturma)