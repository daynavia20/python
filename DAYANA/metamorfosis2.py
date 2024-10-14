def analizar_texto(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
        
    palabras = texto.split()
    total_palabras = len(palabras)
    
    longitudes_palabras = [len(palabra) for palabra in palabras]
    longitud_media_palabras = sum(longitudes_palabras) / total_palabras if total_palabras > 0 else 0

    oraciones = texto.split('.')
    total_oraciones = len([oracion for oracion in oraciones if oracion.strip()])

    palabra_mas_larga = max(palabras, key=len) if palabras else ''
    
    return total_palabras, longitud_media_palabras, total_oraciones, palabra_mas_larga

ruta_archivo = 'C:\\Users\\\\Downloads\\metamorfosis.txt'
total_palabras, longitud_media_palabras, total_oraciones, palabra_mas_larga = analizar_texto(ruta_archivo)

print(f'Número total de palabras: {total_palabras}')
print(f'Longitud media de las palabras: {longitud_media_palabras:.2f}')
print(f'Número de oraciones: {total_oraciones}')
print(f'La palabra más larga: {palabra_mas_larga}')
