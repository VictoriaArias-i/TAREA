#   Clase 25-04-25

"""Repaso y ejercicios de la prueba en linea 49"""

#   Una función se inicia con def.

#def saludo():
#    print("Hola, buenos días") # El espacio se llama ideltación.

#saludo()

"""Repaso función con input"""

#name=input(" Dime tu nombre por favor.")

#def Inicion(name):
#    print(f"Buenos días, {name}")

#Inicio(name)

"""Repaso de función con suma"""

#def Suma(a,b):
#    return a + b
#resultado = Suma(4,9)

#print(f"El resultado es {resultado}") #Se puede hacer así o como el de abajo
#print("Resultado: ", resultado)

"""Otro ejercicio"""

# def calc(a,b,c):
#     return a * b /c
# result= calc(12,9,3)

# print(f"El resultdo es {result}")

"""Ejercicio propio según repaso"""

# a = int(input("Dime el primer numero"))
# b= int(input("Dime el segundo numero"))
# c= int(input("Dime el tercer numero"))

# def mul(a,b,c):
#     return b *c/a *b
# res= mul(a,b,c)
# print(f" El resultado es {res}")

"""Ejercicio de prueba"""

#Realizar un programa que les solicite dos numeros a un usuario, "A" y "B", y, en base a esos dos numeros hay que sacar un numero aleatorio.
        # Limite inferior es A, por ejemplo A = "1", y el limite superior es B = "100"
        #Hay que importar un "random". Un numero al azar es un numero aleatorio.
# De ese num aleatorio tienes que pedirle al user que te de un numero entero para que te de el porcentaje, o sea, si el user te dice num 10 es un 10% que se le saca al num aleatorio.
# Depués hay que hacer una suma o resta, es una opción para el usuario, y se va a restar o sumar con el num que queda del porcentaje.
# Finalmente se muestra el resultado de la suma o resta.

# print("Bienvenid@ usuario. \nEl día de hoy vamos a trabajar las matematicas. \nPrimero tienes que darnos dos numeros, en base a estos dos numeros hay que sacar un numero al azar")

# a= int(input("Agrega el primer numero: "))
# b= int(input("Agrega el segundo numero: "))

# import random

# def azar(a,b):
#     return random.randint(a,b)

# num_aleatorio= azar(a,b)
# print(f"El numero aleatorio es {num_aleatorio}")

# print("Ahora vamos a pedirte un tercer numero para sacar un porcentaje del numero aleatorio")
# c= int(input("Agrega el tercer numero:"))

# res= num_aleatorio * c / 100
# print(f"El resultado del porcentaje es {res}")

# print("Ahora vamos a hacer una suma o resta, tu escoges, con el numero aleatorio y el porcentaje recien sacado.")
# op= input("¿Qué quieres hacer? \n 1-. Sumar \n 2-. Restar")

# if op == "1":
#     print(f"Has elegido sumar: \n {num_aleatorio} + {res}= ?")
#     rest= num_aleatorio + res
#     print(f"El resultado final es {rest}")
# else:
#     print(f"Has elegido restar.\n {num_aleatorio} - {res} = ?")
#     rest= num_aleatorio + res
#     print(f"El resultado final es {rest}")
       
# print("¡Muchas gracias por participar! Nos vemos en el siguiente ejericicio")

"""Ejercicio de prueba 2"""

# La academia school of talent requiere realizar una app en python que les permita establecer el rango socioeconomico
# de cada uno de sus estudiantes para poder proporcionar distintos beneficios economicos.
# Sabiendo que cada uno de los deciles establecidos cuenta con una diferencia de 10%
# El decil 1= Beneficia al estrato economico más bajo(F) con notas de 7, con descuento 100%
# El decil 2= Beneficia al estrato economico bajo(D) con notas de 7, con descuento de 100%
# El decil 3= Beneficia al estrato economico medio bajo(C) con notas de 7, con descuento de 40%
# El decil 4= Beneficia al estrato economico medio(D) con notas de 6, con descuento de 30%
# El decil 5= Beneficia al estrato economico medio alto(B) con notas de 6, con descuento de 25%
# El decil 6= Beneficia al estrato economico medio alto(B) con notas de 5, con descuento de 20%
# El decil 7-10= No requiere ningun descuento si es nivel econonmico A
# El precio de la academia es de 300.000$ y dura 6 meses.
# El programa debe solicitar el nombre del estudiante, el nivel socioeconomico y la nota obtenida.

ef prog():
    print("Bienvenido usuario, para revisar si tiene un beneficio dentro de la academia responda las siguientes preguntas")
    name= input("Primero que nada, ¿Cuál es su nombre? ")
    print("        __________________")
    print(f"Le recuerdo, {name}, que el precio de la academia es de 300.000$ y dura 6 meses.\n        __________________")
    print("Teniendo en cuenta que el nivel socioeconomico se basa en en una escala de la F a la A, donde la \"F\" es el nive más bajo, y la \"A\" es el más alto.")
    nivel_so(name)

def salida(name):
    print(f"Muchas gracias, {name}, por ocupar nuestra aplicación, nos vemos pronto.")

def nivel_so(name):
    opc= input(f"{name} Ingrese en qué nivel socioeconomico se encuentre entre las diferentes opciones:\n 1-. F\n 2-. D \n 3-. C \n 4-. B \n 5-. A \n")
    while True:
        if opc == "1":
            decil_1(name)
            break
        elif opc == "2":
            decil_2(name)
            break
        elif opc == "3":
            decil_3(name)
            break
        elif opc == "4":
            decil_4(name)
            break
        elif opc == "5":
            decil_5(name)
            break
        else:
             salida(name)
        break

def decil_1(name):
        print(f"{name}, se encuentra en el nivel F. Para poder recibir el descuento del 100%, debe tener un promedio de 7.")
        print("             __________________")
        op2= input("¿Tiene un promedio de 7? \na)Sí \nb)No")
        if op2 == "a":
            print("Felicitaciones, tiene un descuento del 100%\nEl precio de la academia ahora será de 0$")
        elif op2 == "b":
            print("No tiene el descuento del 100%")
            salida(name)
        else:
            print("No es valido lo que ingresaste, intenta ingresar tus datos de nuevo.")  
            nivel_so(name) 
def decil_2(name):
        print(f"{name}, encuentra en el nivel D. Para poder recibir el descuento del 100%, debe tener un promedio de 7.")
        print("             __________________")
        op2= input("¿Tiene un promedio tiene? \na)De 7 \nb)Sobre 6 \nc) Otro")
        if op2 == "a":
            print("Felicitaciones, tiene un descuento del 100%\n El precio de la academia ahora será de 0$")
            salida(name)           
        elif op2 == "c":
            print("No tiene el descuento del 100%")
            salida(name)
        elif op2 == "b":
            print("Si es que tiene un promedio de 6, tiene un descuento del 30%")
            res= 300000 * 0.3
            print(f"Felicitaciones, tiene un descuento del 30%, el precio de la academia ahora tendrá un descuento de {res}$")
            salida(name)
        else:
            print("No es valido lo que ingresaste, intenta ingresar tus datos de nuevo.")  
            nivel_so(name) 
def decil_3(name):
        print(f"{name}, se encuentra en el nivel C. Para poder recibir el descuento del 40%, debe tener un promedio de 7.")
        print("             __________________")
        op2= input("¿Tiene un promedio de 7? \na)Sí \nb)No")
        if op2 == "a":
            print("Felicitaciones, tiene un descuento del 100%\n El precio de la academia ahora será de 0$")
            salida(name)
        elif op2 == "b":
            print("No tiene el descuento del 100%")
            salida(name)
        else:
            print("No es valido lo que ingresaste, intenta ingresar tus datos de nuevo.")  
            nivel_so(name) 

def decil_4(name):
        print(f"{name}, se encuentra en el nivel B. Para poder recibir el descuento del 30%, debe tener un promedio de 6.")
        print("             __________________")
        op2= input("¿Qué promedio tiene? \na)Sobre 6 \nb)Sobre 5 \nc) Más bajo")
        if op2 == "a":
            res= 300000 * 0.3
            print(f"Felicitaciones, tiene un descuento del 30%, el precio de la academia ahora tendrá un descuento de  {res}$")
            salida(name)
        elif op2 == "b":
            res= 300000 * 0.2
            print(f"Felicitaciones, tiene un descuento del 20%, el precio de la academia ahora tendrá un descuento de {res}$")
            salida(name)
        elif op2 == "c":
            print("No tiene el descuento del 100%")
            salida(name)
        else:
            print("No es valido lo que ingresaste, intenta ingresar tus datos de nuevo.")  
            nivel_so(name)

def decil_5(name):
        print(f"{name}, se encuentra en el decil más alto. En este momento no tenemos ningun beneficio para usted.")
        re=input(f"¿{name}, desea volver a intentarlo? \na)si o \nb)no")
        if re == "a":
            prog()
        elif re == "b":
            salida(name)

prog()
