# CÓDIGO QUE NOS DICE EL PROMEDIO DE UN GRUPO DE ALUMNOS, POR MEDIO DE UN ARCHIVO DE TEXTO
def leer_alumnos(archivo):
    alumnos = []
    try:
        with open(archivo, 'r') as file:
            for linea in file:
                linea = linea.strip()
                if linea:  # Verifica que la línea no esté vacía
                    if ',' in linea:  # Verifica que haya un separador ','
                        nombre, calificacion = linea.split(',')
                        try:
                            alumnos.append((nombre, int(calificacion)))
                        except ValueError:
                            print(f"Error de formato en la calificación: {calificacion}")
                    else:
                        print(f"Línea inválida (sin separador ','): {linea}")
                else:
                    print("Línea vacía encontrada, omitiendo...")
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no fue encontrado.")
    return alumnos

def calcular_promedio(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos para calcular el promedio.")
        return 0
    total_calificaciones = sum(calificacion for nombre, calificacion in alumnos)
    promedio = total_calificaciones / len(alumnos)
    return promedio

def alumnos_sin_derecho(alumnos):
    sin_derecho = [nombre for nombre, calificacion in alumnos if calificacion <= 6]
    return sin_derecho

# Ordenar alumnos por calificación en orden ascendente usando sorted
def ordenar_alumnos(alumnos):
    return sorted(alumnos, key=lambda x: x[1])

# Archivo de texto
archivo = 'alumnos.txt'

# Leer alumnos y calificaciones
alumnos = leer_alumnos(archivo)

# Ordenar alumnos por calificación en orden ascendente
alumnos = ordenar_alumnos(alumnos)

# Mostrar los alumnos sin derecho a calificación
sin_derecho = alumnos_sin_derecho(alumnos)
print("Alumnos sin derecho a calificación:", sin_derecho)

# Calcular el promedio del grupo
promedio = calcular_promedio(alumnos)
print(f"Promedio del grupo: {promedio:.2f}")

# Mostrar los nombres y calificaciones en orden ascendente
print("Lista de alumnos y calificaciones en orden ascendente:")
for nombre, calificacion in alumnos:
    print(f"{nombre}: {calificacion}")
