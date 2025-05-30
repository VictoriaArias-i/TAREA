"""Clase 18     26-05-25"""

# Ejercicio tipo examen


"""Ejercicio 1"""

# Se solicita desarrollar, un programa en python que permita calcular el area de varios triangulos, para esto se le solicuta al usuario cuantos triangulos desea procesar
# Luego, por cada triangulo, se debe ingresar la base y la altura, ambos valores positivos y reales (Decimales).
# El area de un triangulo se calcula con la siguiente  formula: a= b*a/2. SI su usuario ingresa un valor invalido se debe mostrar un mensaje de error.

def ejercicio_1():
    with open("triangulos.txt", "a") as archivo:
        while True:
            try:
                cantidad= int(input("¿Cuántos triangulos quiere sacar el area de?: "))
            except ValueError:
                print("Intentalo con un numero entero")
                continue
            break

        for i in range(cantidad):
            print(f"Ingresa datos del triangulo {i+1}:")
            base=float(input("Ingrese el numero postivo y decimal de la base:"))
            altu=float(input("Ingrese el numero postivo y decimal de la altura:"))

            archivo.write(f"Triangulo {i+1}:\n ")
            archivo.write(f"Base {base}:\n ")
            archivo.write(f"altura {altu}:\n ")

            area= (base * altu)/2
            print("El area de tu triangulo es", area)
        print("\n Archivo creado con exito")
ejercicio_1()
""""Ejercicio 2"""

# Construya un progama simple de venta, de entradas para el cine por medio de un menú de opciones que permita al usuario recibir la bienvenida al cine, 
# ver cuantas entradas quedan, comprar una cantidad de entradas de acuerdo a la cantidad de usuarios solicitada, permitir consultar disponibilidad de la sala
# y, por ultimo, consultar salida con mensaje de despedida. 

print("Bienvenido al menu del cine.")
entradas_disp=20
while True:
    try:
        opc=int(input("¿Qué desea hacer hoy?\n1-. Ver las entradas disponibles\n2-. Comprar la entradas\n3-. Consultar disponibilidad de sala.\n4-. Salir\n"))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    
    if opc== 1:
        print(f"En este momento tenemos {entradas_disp} entradas disponibles para la pelicula.")
    elif opc==2:
        comp_entra=int(input("¿Cuantas entradas desea comprar?"))
        res_entra= entradas_disp -comp_entra
        print(f"Ahora solo quedan {res_entra} entradas.")
    elif opc==3:
        if entradas_disp > 0:
            print("Aún quedan asientos que rellenar.")
        else: 
            print("No quedan asientos que comprar.")
    elif opc==4: 
        print("Adios, nos vemos pronto.")
        break
    else:
        print("Oh no, ha habido un error, intentalo de nuevo.")
