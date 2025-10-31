import random

numero = random.randint(1, 100)

print("--- Jogo de Adivinhar o Número ---")
print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

while True:
    try:
        escolha = int(input("Digite seu palpite (de 1 a 100): "))
        if escolha < 1 or escolha > 100:
            print("Valor inválido. Digite um número entre 1 e 100.")
        elif escolha > numero:
            print("Errado! O número que eu escolhi é MENOR. Tente de novo.") 
        elif escolha < numero:
            print("Errado! O número que eu escolhi é MAIOR. Tente de novo.")
        else:
            print(f"Parabéns! Você acertou o número! Era {numero}!")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas um número.")
