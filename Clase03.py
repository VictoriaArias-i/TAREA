#Clase 03, Python. 11-04

"""Repaso"""
#v01= int(input("Dime un numero"))
#print(f"Tu numero es {v01}")

"""Ejercicio adelantado"""

#list=[ 1, 2, 3, 4] 
#Es una lista de variable. Si está entre corchetes entonces es una lista. Para empezar el listado se empieza con 0 y sigue de corrido, se mueve un numero.

#list.append(5)
#el numero puesto en esta linea va a colocarse al final de la lista. Append significa añadir en la lista al final.

#mi_Tupla= ("Banana", "Manzana", "Cereza") 
#Tupla es una lista constante, que no cambia.
#print (mi_Tupla[0])


#EJERCICIO 

"""1-. Mensaje de bienvenida a mi usuario"""
"""2-. Agregar los productos"""
"""3-. Mostrar un mensaje al usuario que añade los productos, y que modifique alguno de ellos"""
"""4-. Como eliminar uno de los productos"""
"""5-. Y una lista de resultados"""

user= input("¿Cuál es tu nombre?")

print(f"Bienvenido a tu lista {user}")

productos= ["1- Café", "2- Té", "3- Pan", "4- Muffin", "5- Otro"]
seleccionados= []
while True:
    print(f"\nProductos disponibles:\n{productos}")
    op = input("\n¿Qué quieres hacer?\na) Agregar\nb) Salir\n> ")
    
    if op == "a":
        seleccionados.append(input("Nombre del nuevo producto: "))
    elif op == "b":
      break
while True:
    print(f"\nProductos disponibles:\n{seleccionados}")
    op = input("\n¿Qué quieres hacer?\na) Quitar\nb) Salir\n> ")
    
    if op == "a":
        seleccionados.append(input("Nombre del producto a eliminar: "))
    elif op == "b":
      break
print(f"\n--- Menú Final ---\n{seleccionados}")


