# programa que determine la cantidad de ocurrencias repetidas en el archivo "metamorfosis.txt"

def contar_palabras_repetidas(nombre_archivo, archivo_resultado):
    try:
        with open(nombre_archivo, 'r') as archivo_entrada:
            contenido = archivo_entrada.read()
            contenido = contenido.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
        
            palabras = contenido.split()
            
            conteo_palabras = {}
            for palabra in palabras:
                if palabra in conteo_palabras:
                    conteo_palabras[palabra] += 1
                else:
                    conteo_palabras[palabra] = 1
            
            print("Palabras repetidas y sus conteos:")
            with open(archivo_resultado, 'w') as archivo_salida:
                archivo_salida.write("Palabras repetidas y sus conteos:\n")
                for palabra, conteo in conteo_palabras.items():
                    if conteo > 1:
                        resultado = f"Palabra: '{palabra}' - Repeticiones: {conteo}\n"
                        print(resultado)
                        archivo_salida.write(resultado)
    
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' esta mal identado.")
rutaArchivo = r'C:\Users\\Downloads\metamorfosis.txt' 

archivoResultado = "resultado.txt"

contar_palabras_repetidas(rutaArchivo, archivoResultado)
