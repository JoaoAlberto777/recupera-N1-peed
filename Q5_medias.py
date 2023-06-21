
Notas = []

for i in range (10):
    Nota = float(input(f"Informe a nota do {i+1}° aluno: "))
    Notas.append(Nota)
    
Media = (sum(Notas) / 10)

print(f"A media Geral da turma é: {Media}")
