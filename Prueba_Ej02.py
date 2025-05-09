"""Prueba Python 09-05-2025"""

# #Desarrolle un programa en python que permita ingresar dos números enteros que indique un rango numérico. 
# El primer valor debe ser menor que el segundo. Luego, debe poder generar un número aleatorio (al azar) entre ese rango numérico. 

# Para hacer esto último, se sugiere hacer lo siguiente:

# 1. from random import randint
# 2. numero = randint(num1, num2)

# Con esto realizado, su programa debe permitir simular un juego que le permita adivinar el número generado aleatoriamente 

# El juego consta de 3 intentos. 
# Si no se adivina en el primer intento, el juego debe permitir dar el segundo intento, sin antes decir si el número a adivinar es mayor o menor. 
# Si aún no se adivina en el segundo intento, se debe decir lo mismo que en el primer intento, pero además dar una pista. 
# La pista consta de que, debe decir cuál número está más cerca del número que queremos adivinar: si el nUmero ingresado en el 
# primer intento o el numero ingresado en el segundo intento.
# Luego, si aun no adivina, se dará el tercer y último intento. 
# Si no adivina, deberá mostrar un mensaje diciendo: “Perdiste”. En caso de que se adivine el número, independiente del intento
# en que se logró, el programa deberá terminar y entregar el mensaje: “Felicitaciones, pudiste adivinar.”

def inicio_prog():
    print("Bienvenido al juego de adivinar el numero aleatorio.")
    desc=input("¿Quieres colocar los numeros tu mismo?\nSi\nNo\n")
    desc=desc.replace("í","i").lower()
    if desc== "si":
        juego_m()   
    elif desc== "no":
        juego_fa()
    else:
        print("Algo ha salido mal, intentalo de nuevo")
        inicio_prog()

def juego_fa():
    import random
    intentos=0
    num_alt= random.randint(1,10)

    print("El numero aleatorio estará entre 1 al 10.")
    while intentos < 3:
        res=int(input("Ingresa tu respuesta aquí: "))
        intentos += 1
        if res== num_alt:
            print(f"¡Muy bien! Acertaste el numero.")
            volver()
            if intentos== 1:
                print("¡Lo lograste al primer intento!")
                volver()

        elif res < num_alt:
            print(f"¡Oh no! El numero aleatorio es más alto, Este es tu {intentos} intento.")    
        elif res > num_alt:
            print(f"¡Oh no! El numero aleatorio es más bajo, Este es tu {intentos} intento.")    
        elif intentos== 3:
            print("GAME OVER.\n Perdiste")
            volver()
        elif res < 1 or res > 10:
            print("Oh no, parece que no te has mantenido en el rango. Intentalo de nuevo.")

    print(f"El numero aleatorio es: {num_alt} ")
    volver()

def juego_m():
    print("Recuerda que el primer numero debe ser más bajo que el segundo")
    a=int(input("Ingresa el primer numero: "))
    b=int(input("Ingresa el segundo numero: "))
    import random
    intentos=0
    num_alt= random.randint(a,b)

    while intentos < 3:
        res=int(input("Ingresa tu respuesta aquí: "))
        intentos += 1
        if res== num_alt:
            print(f"¡Muy bien! Acertaste el numero.")
            volver()
            if intentos== 1:
                print("¡Lo lograste al primer intento!")
                volver()

        elif res < num_alt:
            print(f"¡Oh no! El numero aleatorio es más alto, Este es tu {intentos} intento.")    
        elif res > num_alt:
            print(f"¡Oh no! El numero aleatorio es más bajo, Este es tu {intentos} intento.")    
        elif intentos== 3:
            print("GAME OVER.\n Perdiste")
            volver()
        elif res < 1 or res > 10:
            print("Oh no, parece que no te has mantenido en el rango. Intentalo de nuevo.")

    print(f"El numero aleatorio es: {num_alt} ")
    volver()

def volver():
    vol=input("¿Quieres volver a jugar?\nSi\nNo\n")
    vol=vol.replace("í","i").lower()
    if vol== "si":
        juego_fa()
    else:
        print("¡Adios! Nos vemos pronto.")

inicio_prog()