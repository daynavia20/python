#El programa recibe los siguientes parámetros:
#Tipo del Pokémon atacante.
#Tipo del Pokémon defensor.
#Ataque: Entre 1 y 100.
#Defensa: Entre 1 y 100.

def calcular_dano(tipo_atacante, tipo_defensor, ataque, defensa):
    efectividades = {
        ('agua', 'fuego'): 2.0,
        ('agua', 'planta'): 0.5,
        ('agua', 'electrico'): 1.0,
        ('fuego', 'planta'): 2.0,
        ('fuego', 'agua'): 0.5,
        ('fuego', 'electrico'): 1.0,
        ('planta', 'agua'): 2.0,
        ('planta', 'fuego'): 0.5,
        ('planta', 'electrico'): 1.0,
        ('electrico', 'agua'): 2.0,
        ('electrico', 'fuego'): 1.0,
        ('electrico', 'planta'): 1.0,
    }
    efectividad = efectividades.get((tipo_atacante, tipo_defensor), 1.0)
    dano_original = 50 * (ataque / defensa) * efectividad
    dano = max(1, min(dano_original, 100))  
    return dano_original, dano, efectividad 

pokemones = ["agua", "fuego", "planta", "electrico"]
tipo_atacante = input("Ingrese el Pokémon atacante: ").lower()
tipo_defensor = input("Ingrese el Pokémon defensor: ").lower()

if tipo_atacante not in pokemones or tipo_defensor not in pokemones:
    print("El Pokémon no está dentro de los 4 disponibles.")
else:
    ataque = int(input("Ingresa el valor del ataque (1-100): "))
    defensa = int(input("Ingresa el valor de defensa (1-100): "))
    
    if 1 <= ataque <= 100 and 1 <= defensa <= 100:
        dano_original, dano, efectividad = calcular_dano(tipo_atacante, tipo_defensor, ataque, defensa)
        efectividad_msg = "neutro"
        if efectividad == 2.0:
            efectividad_msg = "súper efectivo"
        elif efectividad == 0.5:
            efectividad_msg = "no es efectivo"
        
        print(f'El daño del ataque es: {dano_original} ({efectividad_msg})')
    else:
        print("El valor de ataque y  la sdefensa debe estar entre 1 y 100.")
