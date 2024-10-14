
def adivinar_palabra():
palabra = "python"
adivinar = ["_"] * len("palabra")
intentos = 7

while intentos > 0 and "_" in adivinar:
    print(" ".join(adivinar))
    print(f"Te quedan {intentos} intentos.")
    letra = input("Adivina una letra: ")

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                adivinar[i] = letra
    else:
        intentos -= 1

if "_" in adivinar:
    print(" perdiste, la palabra era 'python'.")
else:
    print(" adivinaste la palabra era 'python'.")

   

        