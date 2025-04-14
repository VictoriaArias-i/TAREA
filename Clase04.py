# Clase 04 , 14-04

#Ejercicio: Tienda de perfume "Gloria"

"""El representante de venta de la tienda de perfume necesita organizar el formulario de venta. Y el piensa que representando el siguiente formulario podría mejorar sus ventas."""
"""Tiene 10 items para poder atender a una persona, los campos que el gerente de venta quiere implementar: 
Nro de boleta, ID, nombre del cliente, y productos del pedido. De 10 pasa a 4"""
"""Inventario: 1-. Perfume Organza para damas, 2-. Katy Perry, 3-. Mañana Fresca, 4- La mejor noche, 5-. Sueño exclusivo. 
6-. Antonio Bandera 7-. Lacoste 8-. Hugo Boss 9-. A que te quito el sueño
50 ml = 10.000 $
100 ml= 18.000 $ 
Añadir el pedido, sacarle el subtotal, y después el iva."""

print("Bienvenid@ a la tienda de perfumes \"Gloria\"\n Para iniciar necesitamos un par de datos.")
user=input("¿Cuál es tu nombre?")
print(f"Hola, {user}")

ID=input("¿Cuál es tu RUT?")
print(f"Tu id es: {ID}")

factura=input("¿Cuál es tu número de boleta?")
print(f"El numero es: {factura}")
while True:
    prod = input(" ¿Qué tipo de perfumes está buscando? \n a) Varones \n b) Damas")

    if prod == "a": 
        perfumeVarones_Tupla = ["Antonio Bandera", "Lacoste", "Hugo Boss", "A que te quito el sueño"]
        print(f"\nProductos disponibles:\n{perfumeVarones_Tupla}")
        seleccion = input("Seleccione un perfume escribiendo su nombre: ")
        if seleccion in perfumeVarones_Tupla:
            print(f"Has seleccionado: {seleccion}")
            print("¿Cuántos ml desea? \n 50 ml = 10.000 $ \n 100 ml = 18.000 $")
            ml= input("Seleccione la cantidad de ml: ")
            if ml == "50":
                precio = 10000
            elif ml == "100":
                precio = 18000
            else:
                print("Opción inválida, por favor elija nuevamente.")
            break
        else:
            print("Opción inválida, por favor elija nuevamente.")
    elif prod == "b":
        perfumeMujeres_Tupla = ["Perfume Organza", "Katy Perry", "Mañana Fresca", "La mejor noche", "Sueño exclusivo"]
        print(f"\nProductos disponibles:\n{perfumeMujeres_Tupla}")
        seleccion = input("Seleccione un perfume escribiendo su nombre: ")
        if seleccion in perfumeMujeres_Tupla:
            print(f"Has seleccionado: {seleccion}")
            print("¿Cuantos ml desea? \n 50 ml = 10.000 $ \n 100 ml = 18.000 $")
            ml= input("Seleccione la cantidd de ml:")
            if ml == "50":
                precio = 10000
            elif ml == "100":
                precio = 18000
            else:
                print("Opción inválida, por favor elija nuevamente.") 
        break

