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

print("Bienvenido usuario, para revisar si tiene un beneficio dentro de la academia responda las siguientes preguntas")

op= input("Ingrese en qué nivel socioeconomico se encuentre entre las diferentes opciones:\n 1-. F\n 2-. D \n 3-. C \n 4-. B \n 5-. A \n")

if op == "1":
    print("Se en")