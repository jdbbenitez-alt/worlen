palabra_secreta = "python"
intentos = 5
letras_adivinadas = ["_"] * len(palabra_secreta)

print("Juego de adivinar la palabra")

while intentos > 0:
    print("\nEstado actual:", letras_adivinadas)
    
    letra = input("Ingresa UNA letra: ").lower()

    if letra in palabra_secreta:
        print("La letra está en la palabra")

        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                letras_adivinadas[i] = letra
                print(f"→ Letra '{letra}' en posición {i}")

    else:
        print("La letra NO está en la palabra")
        intentos -= 1

    print("Resultado ahora:", letras_adivinadas)

    if "_" not in letras_adivinadas:
        print("\n¡Ganaste!")
        break

print("La palabra era:", palabra_secreta)
