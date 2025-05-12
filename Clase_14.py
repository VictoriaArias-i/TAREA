"""Clase Bucle 12-05-2025"""

# Inicio del bucle, nos permite repetir de forma infinita.

# Ciclo For: i es una variable que es necesaria declararla.
# EJ: for i in range(5):
#       print("No botar basura")

# Ciclo While:  Tiene un numero finito de repeticiones al ciclo, thile permite eecutar las fases mientras la condiciones se cumpla.
# EJ: a= 5
#     while(a>0):
#        print(f"el valor de a es: {a})
#        a = int(input("ingrese el valor-"))

# EXCEPCIONES
# Es normal que salga errores en los codigos, por esto hay TRY y EXCEPT, como un else, por si se sale dentro del rango para que no de el SYNTAX ERROR.

"""MATERIA TXT PARA LA PRUEBA 3"""

#Con el comando open todo lo que este en "w"(write) =archivo.write cae en la hoja "datos.txt".

# with open ("datos.txt", "w") as archivo:
#       archivo.write("Nombre: Maria \n Edad: 26 años.\n Carrera: Ing.")

#Para leerlo necestiamso agregar una variable, en este caso "r(read)" = archivo.read 

# try:
#     archivo = open("datos.txt", "r")
#     contenido= archivo.read
# except FileExistsError as error:
#         print("Existe un error, el arvicho no existe", error)
# else:
#      print("Archivo exitoso")

# """Ejercicio 01"""

#Los dueños del vivero San Joaquin necesitan realizar un programa en Python, y para ello cuentan con su talento como desarrolladores cuyo programa les va a colaborar en el inventrio
# y venta de las plantas. A continuacion los 10 productos más vendidos:
#1-. Rosas blancas "Excelente para esta primavera" = 2000$
#2-. "Traida de mexico", la mata de navidad = 5000$
#3-. Orquidea "Planta parasitaria muy bella que sobrevive de otra planta" = 3000$
#4-. Copihue "Planta  cerofila original de la region" = 10000$
#5-. Rosas rojas "Una excelente opción para el día de los enamorados" = 7000$
#6- 10.LAS AÑADIMOS NOSOTROS 

# Genera una archivo txt que guarde las primeras 5 plantas en tu inventario y que pueda quedar abierto para almacenar infinitamente.

def agregar_prod():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = input("Ingrese el precio del producto: ")

    with open("dtos.txt", "a") as archivo:
        # Escribimos la nueva información en el archivo
        archivo.write(f"{nombre}, \"{descripcion}\" = ${precio}\n")
    print("¡Producto agregado con éxito!")

# Llamamos a la función para permitir al usuario agregar productos
while True:
    agregar_producto()
    # Preguntamos al usuario si desea agregar otro producto
    continuar = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
    if continuar != 's':
        print("Proceso finalizado.")
        break

# with open("dtos.txt", "w") as archivo:
#     archivo.write("1-. Rosas blancas, \"Excelente para esta primavera\" = $2.000\n2-. Mara de navidad, \"Traida de mexico\" = $5.000\n")
#     archivo.write("3-. Orquidea, \"Planta parasitaria muy bella que sobrevive de otra planta\" = $3.000\n")
#     archivo.write("4-. Copihue \"Planta  cerofila original de la region\" = $10.000\n5-. Rosas rojas \"Una excelente opción para el día de los enamorados\" = $7.000")
