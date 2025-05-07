    # Clase 13 07-05-25

"""Ejercicio de prueba"""

#Desarrolla un programa en Python que permita ingresar dos números enteros que indiquen un rango numérico. El primer valor debe ser menor que el segundo. 
# El programa generará un número aleatorio dentro de ese rango. Luego, el usuario intentará adivinar el número generado en tres intentos.

#Si el usuario adivina en el primer intento, el programa mostrará el mensaje: "Felicitaciones, adivinaste en el primer intento."
#Si no acierta en el primer intento, el programa indicará si el número es mayor o menor que el intento del usuario.
#En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
#Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: "Perdiste, el número era [número]."

import random

def inicio_prog():
    print("Bienvenid@, en este programa vamos a hacer ejercicios numericos.\n El programa generará un número aleatorio dentro de ese rango. Luego, el usuario intentará adivinar el número generado en tres intentos.")
    azar()

def azar():
    a= int(input("Ingresa el primer numero: "))
    b= int(input("Ingresa el segundo numero: "))

    if a < b:
        print(f"Tu primer numero es {a} y tu segundo numero es {b}.")
        def alt(a,b):
            return random.randint(a,b)
        num= alt(a,b)
        print("Tenemos el numero, ahora tienes que adivinarlo.")
        adivinar(num)
    elif b < a:
        print("Perdón, parece que no me he explicado bien, el primer numero tiene que ser menor al segundo, intentalo de nuevo.")
        azar()
    else: 
        print("Oh no, algo ha salido mal, intentalo de nuevo.")
        azar()

def adivinar(num):
    print("Tienes 3 intentos para poder descubrir el numero.")
    intentos=0
    while intentos < 3:
        res=int(input("Aquí: "))
        intentos += 1

        if  res == num and intentos== 1:
            print("Felicitaciones, adivinaste en el primer intento")
        elif res < num and intentos == 1: 
            print(f"Oh, el numero que ingresaste es más bajo que el seleccionado. Este es tu {intentos} intento.")
        elif res < num and intentos == 2: 
            print(f"Oh, el numero que ingresaste es más bajo que el seleccionado. Este es tu {intentos} intento.")
        elif res < num and intentos == 3: 
            print(f"Oh, el numero que ingresaste es más bajo que el seleccionado. Este es tu {intentos} intento.")
            salida(num)
        elif res > num and intentos == 1: 
            print(f"Oh, el numero que ingresaste es más alto que el seleccionado. Este es tu {intentos} intento.")
        elif res > num and intentos == 2: 
            print(f"Oh, el numero que ingresaste es más alto que el seleccionado. Este es tu {intentos} intento.")
        elif res > num and intentos == 3: 
            print(f"Oh, el numero que ingresaste es más alto que el seleccionado. Este es tu {intentos} intento.")
            salida(num)
        elif res!= num and intentos == 3: 
            print(f"El juego ha terminado, el numero era {num}.") 
        elif res == num:
            print(f"Enhorabuena, lo has logrado en el {intentos}, el numero era {num}.")   
        else:
            print("Oh no, algo ha salido mal, intentalo de nuevo.")
            azar()

def salida(num):
    print("El numero indicado es el ", num)
    volv=input("¿Quieres volver a jugar?\na) Si\nb) No\n ")
    if volv == "a":
        azar()
    elif volv == "b":
        print("Un gusto, nos vemos pronto.")     

inicio_prog()
