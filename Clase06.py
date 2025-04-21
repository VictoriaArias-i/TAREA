#Clase 21-04. Repaso, nueva manteria en la linea 44 y ejercicio de examen en linea 55

"""Repaso de introducción de datos"""

#Edad=int(input("¿Qué edad tienes?"))

#if Edad >= 18: 
#    print(f"Tu edad es {Edad} años.")
#else:
#    print(f"Tienes {Edad} años.\nNo tienes la edad para entrar.")

"""Repaso de promedio de notas"""

#nota1 = float(input("Dime tu primera nota."))
#nota2 = float(input("Dime tu segunda nota."))
#nota3 = float(input("Dime tu tercer nota."))

#prom= nota1 + nota2 + nota3/ 3

#if prom >= 6.0:
#    print(f" ¡Buenisima!, tu promedio es {prom}")
#elif prom >= 4.0:
#    print(f" Debes mejorar, tu promedio es {prom}")
#else:
#    print("Perdón, no has pasado.")

"""Repetición en un ejemplo de contador con WHile"""

#cont= 1

#while cont <= 10:
#    print(f"Repetición: {cont}")
#    cont += 1

""" El "For" """

#for i in range(1,10):
#    print(f"Valor: {i}") #Solo llega a 9 porque parte desde 0

#for i in range(1,10+1):
#    print(f"Valor: {i}") #Con el +1 esto se resuelve.


""" Funciones, materia nueva"""

#def saludo():
#    print("Hola, bienvenid@...")
#saludo() 
"""Para mostrar el mensaje tienes que llamar de vuelta como nombraste lo que definiste."""

#def salida():
#    print("Adios, que te vaya bien")
#salida()

"""Ejercicio tipo examen"""

#La empresa Certifika necesita nuestros servicios como desarrolladores y nos solicita realizar un programa que cumpla con las siguientes condiciones:
    # Alumnos con calificaciones mayor a 6.0 reciben un descuento de 20%
    # Alumnos con calicicaciones mayor a 5.0 reciben un descuento de 15%
    # Alumnos con calificaciones mayor a 4.0 reciben un descuento de 10%
    # Al resto le invitamos a seguir estudiante.

user=input("Bienvenido, ¿Cuál es tu nombre?")
prom = float(input(f"{user}, ¿Cuál es tu promedio?\n Ingresa las notas con decimales."))

if prom >= 6.0:
    print(f"¡Felicitaciones! Tu promedio es de {prom}, gracias a esto tienes un Descuento de 20%")
elif prom >= 5.0:
    print(f"¡Enhorabuena! Tu promedio es de {prom}, gracias a esto tienes un Descuento de 15%")
elif prom >= 4.0:
    print(f" Tu promedio es de {prom}, gracias a esto tienes un Descuento de 15%")
else:
    print("¡Oh no! No tienes el promedio suficiente para solicitar el programa.")