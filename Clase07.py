# Clase 23-04-2024

"""Repaso de Definicion + ejercicio de prueba en linea 67"""

#def saludo():
    #nombre= str(input("¿Cuál es tu nombre?"))

    #print(f"Bienvenido {nombre}")

#saludo()

""" Nueva materia de DEF"""

def suma(a,b): #Lo que enseño el profe
    return a + b

resultado = suma(5,3)
print ("El resultado es: ", resultado)

#def Suma(): #version del Diego
  
    #a = int(input("Dime el primer numero"))
    #b = int(input("Dime tu segundo numero"))

    #print(f"Tu primer numero es {a}")
    #print(f"Tu primer numero es {b}")
    #c= a+b
    #return c
#resultado = Suma()
#print(f"El resultado es : {resultado}")

#def suma(): #Version 2 del Diego
    #a = int(input("Dime un numero"))
    #b = int(input("Dime un segundo numero"))
    #c = a+b
    #return c
#print(suma())

# def suma(): # Versión 3 del Diego
#     global a
#     global b
#     a = int(input("Dime el primer numero"))
#     b = int(input("Dime tu segundo numero"))
#     c= a+b
#     return c
# print(suma())


"""Dato"""

#dato = input("Ingresa un numero")
#print("Tipo de dato recibido ", type (dato))

#numero = int(dato)
#resultado = dato + 10

""" Lo que entra en la prueba"""

# promedio= float(input("Ingrese una nota:"))
# quint11 = int(input("Ingresa el quintil, 1, 2, 3, etc"))
# DescuentoA = 0
# DescuentoB = 0
# DescuentoC = 0

# if ifel else

"""Ejercicio de la Prueba"""

#Almacenamiento de puntos de tarjeta
#La tienda Falabella necesita desarrollar un programa para saber cuantos puntos tiene acumulado cada usuario por cada 1000 pesos que realice en una compra un usuario recibe 10 pts
#Cuando un usuario alcance al nivel premium que son 1000 pts tiene un descuento de 25% 
#Cuando un usuario alcande el nivel oro que son 500 pts tiene un desceunto de 10%
#Cuando un usuario alcande el nivel bronze que son 250 pts tiene una recompensa de uno de estos objetos: Audifonos, manos libres, relojes, etc.
# 1ra tarjeta= Marcos= 1500 pts a canjear. ¿Qué niveles le corresponden?
# 2da tarjeta= Jose Luis 2500 pts a canjear.
# 3ra tarjeta= Sebastian 300 pts a canjear.
#¿Qué niveles le corresponden a cada uno? Puede ser más de un nivel por usuario.
# Mostrar en pantalla la información que corresponda al usuario con sus niveles y al final un mensaje que motive a que siga comprando.