def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso
for num in range(20):
    if es_primo(num):
        print(num)
