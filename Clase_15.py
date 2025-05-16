"""Clase de texto 16-05-2025"""

# REPASO DE ARCHIVO DE DATOS

#Esto es una recopilción de datos.
# with open("datos.txt","w") as archivo:
#     archivo.write("Nombre: Victoria Arias.\n Edad: 25.\n Carrera: Programación.\nPromedio: 4.5")


# Verificar cuántos estudiantes ya están registrados (COPILOT)
try:
    with open("datos.txt", "r") as archivo:
        lineas = archivo.readlines()
        # Contar cuántas veces aparece "Estudiante" en el archivo
        contador = sum(1 for linea in lineas if "Estudiante" in linea)
except FileNotFoundError:
    # Si el archivo no existe, comenzamos desde 0
    contador = 0

# Esto es para agregar datos.
with open("datos.txt","a") as archivo:
    cantidad= int(input("Indica cuantos estudiantes: "))

    for i in range(cantidad): 
        print(f"Ingresa datos del estudiante {i+1}:")
        nombre= input("Nombre: ")
        edad= int(input("Edad: "))
        carrera= input("Carrera: ")
        promedio= float(input("Promedio: "))

        archivo.write(f"Estudiante {i+1}:\n ")
        archivo.write(f"Nombre {nombre}:\n ")
        archivo.write(f"Carrera {edad}:\n ")
        archivo.write(f"Carrera {carrera}:\n ")
        archivo.write(f"Promedio {promedio}:\n ")

print("\n Archivo creado con exito")

#Agregar información sin que se pierda la ya puesta