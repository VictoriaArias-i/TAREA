"""Clase 16: Ejercicio tipo examen + Repaso """

"""19-05-25"""

# Ejercicios mandandos en el ava

print("Papá, revisa 3 numeros.")

#   Lista

numero= [5, 4, 6]

#   Contador

num_primo= 0
num_no_primo= 0

def es_primo(n):
    if n <= 1:
        return False # Retrun sirve para volver sin tener que llamarlo o re hacerlo
    for i in range(2, int(n//2)+1):
        if n % i == 0:
            return False
    return True

for i, numero in enumerate(numero):
    print(f"{i+1} numero: {numero}", end= "->")
    if es_primo(numero):
        print("¡Es primo!")
        num_primo += 1
    else:
        print("No es primo")
        num_no_primo += 1
    print("\nResultado")
    print(f"Se ingresa {num_primo} numero primo.")
    print(f"Se ingresa {num_no_primo} numero {"s" if num_no_primo > 1 else ""} No primo")

#EJERCICIO DE PRUEBA


#El usuario debe ingresar el registro de una temperatura en un rango de (-50 a 50 grados centrigados)° dado que el usuario puede ingresar cualquier dato (Incluso cadena de texto), 
# se puede usar manejo de excepción para evitar que el progrma se detenga.
#   1-. Si el dato ingresado no es num enter(int) debe decir: "ERROR: Debe ingresar un numero entero valido y repetir hasta que se valido" 
#   2-. Si el user ingresa un numero entero fuera del rango debe decir: "ERROR: Temperatura fuera del rango permitid mostrar el rango permitido" hasta que el user ingrese datos validos"
#   3-. Si el user ingresa los datos correctamente "Temperatura registrada exitosamente"
#   4-. Deber tener una opcion para salir del programa con un menajse que indique "Cierre del programa, hasta luego".

def inicio():
    print("Holiwis, vamos a agregar el registro de la temperatura")
