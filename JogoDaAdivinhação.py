import random

def jogo_da_adivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    
    # Inicializa o número de tentativas
    tentativas = 0
    
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Eu estou pensando em um número entre 1 e 100.")
    
    while True:
        # Pede ao usuário para adivinhar o número
        chute = input("Qual é o seu chute? ")
        
        # Verifica se o chute é um número válido
        try:
            chute = int(chute)
        except ValueError:
            print("Ops! Isso não é um número válido. Tente novamente.")
            continue
        
        # Incrementa o número de tentativas
        tentativas += 1
        
        # Verifica se o chute é correto
        if chute == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif chute < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        else:
            print("O número secreto é menor. Tente novamente.")

# Executa o jogo
jogo_da_adivinhacao()