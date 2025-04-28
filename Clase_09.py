#Clase 09, 28-04-25

"""Ejercicio de prueba"""

#   Necesitamos generar un programa en python que nos deje crear numeros aleatorios dentro de un rango definido por el usuario y juntarlos dividiendolos por 4
# El usuairo luego tiene que dar otro numero para dividirlo por un maximo de 3 itentos.
#Condiciones del juego: 
#1-. Ingreso de datos 
#   a) dos numeros enteros que representan el rango numerico aleatorio
#   b) El primer numero tiene que se rmenor que el segundo.
#2-. Generacion de numeros aleatorios:
#   a) si es es que se elige un numero aleatorio dentro del rango ingresado el numero se ajusta diviviendolo entre 4, y redondeandolo en el multiplo de 4 más cercano
#3-. Usuario:
#   a) primer intento, si el usuario acierta se muestra "Felicitaciones, adivinaste al primer intento"
#   b) segundo intento, si el usuairo no acierta se indicará si el numero es mayor o menor.
#   c) tercer intento, si no acierta se vuelve a dar una pista
#   d) resultado final, si no acierta los tres intentos el prograa muestra el mensaje "Game over, perdiste, el numero es incorrecto"

def inicio():
    name=input("Bienvenid@, ingrese su nombre. ")
    print(f"Hola, {name}, te explicaré las reglas del juego.")
    print("-----------------------------------------")
    print("Primero tienes que ingresar dos numeros enteros, el primero tiene que ser menor que el segundo.\nPor ejemplo: el primer numero puede ser 1, y el segundo 100.")
    print("-----------------------------------------")
    azar(name)

def salida(name):
    print("-----------------------------------------")
    print("Gracias por haber jugado, vuelve pronto.")
    print("-----------------------------------------")

def azar(name):
    a=int(input("Ingrese el primer numero: "))
    b= int(input("Ingrese el segundo numero: "))

    if a<b:
        print(f"¡Muy bien, {name}! \nTus numeros son {a} y {b}")
        import random
        def alt(a,b):
            return random.randint(a,b)
        num_alt= alt(a,b)
        print(f"Tu numero aleatorio es: {num_alt}")
        mult_1(num_alt, name)
    else:
        print("Algo ha salido mal, tenemos que volver a colocar los numeros. \n **Recuerda que el primer numero es menor al segundo.**")
        azar(name)

def mult_1(num_alt, name):
    print("Ahora vamos a dividirlo en 4 y redondearlo en multiplos de 4.")
    res= (num_alt//4)-((num_alt//4)%4)
    print("-----------------------------------------")
    print(f" {name}, ahora tienes que adivinar el redondeo de {num_alt} entre 4.")

    intentos= 0
    while intentos < 3:
        red= int(input("Ingresa aquí la respuesta: "))
        intentos += 1

        if red==res and intentos==1:
            print("¡Felicitaciones, adivinaste al primer intento!\n¿Quieres volver a jugar?")
            op= input(" a)Sí \nb) No")
            if op == "a":
                azar(name)
            else:
                salida(name)
        elif red == res:
            print("¡Felicitaciones, adivinaste!\n¿Quieres volver a jugar?")
        elif red<res:
            print("¡Oh no! Te has equivocado, pero te daré una pista, el numero es mayor.")
        elif red>res:
            print("¡Oh no! Te has equivocado, pero te daré una pista, el numero es menor.")
        else:
            print(f"GAME OVER\nEl resultado es {res}.")
            op2= input(" ¿Quieres volver a jugar? \na)Sí \nb)No")
            if op2 == "a":
                azar(name)
            else:
                salida(name)
inicio()