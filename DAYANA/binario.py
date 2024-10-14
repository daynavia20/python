def entero_a_binario(numero):
    if numero == 0:
        return '0'
    
    resultado = ''
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero = numero // 2
    
    return resultado

numero_entero = int(input("Ingresa un numero para trasnformar a binario"))
numero_binario = entero_a_binario(numero_entero)

print(f"El número entero {numero_entero} en binario es: {numero_binario}")
