import random


def jogo_adivinhacao() -> None:
    """Jogo simples de adivinhação de números."""
    numero_secreto = random.randint(1, 20)
    tentativas_maximas = 5

    print("🎮 Bem-vindo ao jogo de adivinhação!")
    print("Tente descobrir o número secreto entre 1 e 20.")
    print(f"Você tem {tentativas_maximas} tentativas.\n")

    for tentativa in range(1, tentativas_maximas + 1):
        while True:
            entrada = input(f"Tentativa {tentativa}: digite um número: ")
            if entrada.isdigit():
                chute = int(entrada)
                if 1 <= chute <= 20:
                    break
            print("Entrada inválida. Digite um número inteiro entre 1 e 20.")

        if chute == numero_secreto:
            print(f"\n✅ Parabéns! Você acertou na tentativa {tentativa}!")
            return

        if chute < numero_secreto:
            print("🔼 O número secreto é maior.\n")
        else:
            print("🔽 O número secreto é menor.\n")

    print(f"❌ Fim de jogo! O número secreto era {numero_secreto}.")


if __name__ == "__main__":
    jogo_adivinhacao()
