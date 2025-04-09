print("👾")

 #Clase dos, tarea dos de Python 09-04 👾

    #variable= 10
    #variablefloat= 3.4
    #VariableStr = "Holo"
    #VariableBool= True

nombre= input("¿Cuál es tu nombre?")
print("Bienvenido, ", nombre)

edad= float(input("¿Qué edad tienes?"))
if  edad >= 18:
    print("Para verificar ingrese numeros para un par de ejercicios")

    V01= int(input("Dime un numero entero por favor: "))
    V02= float(input("Dime tu numedo decimal por favor: "))

    print("Primero una suma:")
    print(V01, " + ", V02, " =  ??" )

    R01= V01 + V02

    print("El resultado es: ", R01)

    # O print("El resultado es: {R01}")

    print("Ahora has una resta")

    V03 = int(input("Dime un numero entero por favor: "))
    V04= float(input("Dime tu numedo decimal por favor: "))

    print(V03, " - ", V04, " =  ??" )
    
    R02= V03 - V04

    print("El resultado es: ", R02)

    print("Ahora una multiplicación: ")

    print(V02, " x ", V04, " =  ??" )

    R03= V02 * V04

    print("El resultado es: ", R03)

    print("Ahora una división: ")

    print(V01, " : ", V03, " =  ??" )

    R04= V01 * V03

    print("El resultado es: ", R04)
else:
    print("Perdón, no tienes la edad par hacer este ejercicio")