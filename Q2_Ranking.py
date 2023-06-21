List = []

qtd = int(input("Quantos livros vai informar ao ranking?: "))

for i in range(qtd):
    nome = str(input("Informe o nome do livro: "))
    rank = int(input("Informe o rank do livro: "))
    tupla = (rank, nome)
    List.append(tupla)
    
NewList = sorted(List)

print("__Ranking from Books__")

for rank, nome in NewList:
    print(f"{rank} - {nome}")
    
    
