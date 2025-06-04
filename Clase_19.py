""" Clase 19  04-06-2025"""

"""     Paso de materia     """

#   Coleccion de datos= Recopilación, una lista de datos o un diccionario (Se necesita la info más la forma de traerlo al codigo, diccionario ocupa llaves.)
#   Variable almacena información.
#   CRUD= Create, Read, Update, Delete. 
#   Existen las listas estaticas y las dinamicas, las estaticas no te permiten agregar información en comparación a la otra. 

""" DICCIONARIO"""

# diccionario = {"nombre": "Cesar Huispe",
# "fonos": [
#     988778882,
#     988877776,
#     877666333],
# "activo": True}

"EJ 1"

Persona = {
    "Nombre": "Jose",
    "Edad": 20,
    "Cuidad": "CS"
    }
print(Persona["Nombre"])  #Solo trae la "variable" a la que llamas, si quieres que lleve todo tienes que borrar la variable


""" LISTA"""
"EJ 1"
# milista = [1,2,3,4,5]
# milista.insert(3,"Juan")

# for elemento in milista:
#     print(elemento)

"EJ 2"

Nombre= ["Camila", "Juan"]
Nombre.insert(0, "Maria")   #El cero al principio es la posicion donde queda.
Nombre.append("Pepa")
Nombre.remove("Camila")
print(Nombre)