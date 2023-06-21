import random

palpite = 0
NumSec = random.randint(1,50)
while palpite != NumSec:
    
    palpite = int(input("Adivinhe o numero secreto entre 1 e 50: "))
    
    if palpite > NumSec:
        print("Seu palpite esta muito alto!")
        print()
        
    elif palpite < NumSec:
        print("Seu palpite esta muito baixo!") 
        print()
        
    elif palpite == NumSec:
        print("Parabens, Você acertou!!!")
        print(f"Numero Secreto {NumSec}, Seu Palpite {palpite}")
    