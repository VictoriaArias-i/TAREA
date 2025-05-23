"""EJ 1"""

# El programa debe comenzar permitiendo ingresar un numero que seria el n° de personas que se van a registrar. 
# Este n° deberia ser entero  y se debe resgutrar a cada paciente con:
#   - Nombre
#   - ID
#   - Edad
#   - Si tienes vacunas
#   - Si tiene alguna enfermedad 
#   - Si tiene alguna alergia.

# En el caso de responder alguna pregunta , debe mostrar esquema completo.
#Una vez ingresa la informacion, el programa tiene que mostrar la info recopilada. 
#Cada Ingreso debe mostrarse con una excepción si es que no se cumple lo que estás solicitando. Debe preguntar  la información correcta.
#Por ultimo tiene que solicitar un numero para salir y al salir mostrar un mensaje de despedida.


personas=int(input("Buenos dias, ¿Cuántas personas se vas a registrar hoy?"))

with open("pers_regis.txt","w") as archivo:
     archivo.write("Nombre del paciente: Victoria Arias\n Edad: 25\n ¿Tienes alguna vacuna?: Si\n ¿Tienes algua enfermedad?: No\n ¿Tienes alguna enfermedad?: No")

with open("pers_regis.txt","a") as archivo:
    cantidad= int(input("Indica cuantos pacientes: "))

    for i in range(cantidad): 
        print(f"Ingresa datos del estudiante {i+1}:")
        nombre= input("Nombre: ")
        edad= int(input("Edad: "))
        vacuna= input(" ¿Tienes alguna vacuna?: ")
        enfermedad= str(input("Promedio: "))

        archivo.write(f"Estudiante {i+1}:\n ")
        archivo.write(f"Nombre {nombre}:\n ")
        archivo.write(f"Edad {edad}:\n ")
        archivo.write(f"¿Tienes alguna vacuna?: {vacuna}:\n ")
        archivo.write(f"Promedio {promedio}:\n ")

print("\n Archivo creado con exito")