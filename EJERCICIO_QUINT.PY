"""Ejericio prueba"""

#Desarrolla un programa en python que permite calcular el subsidio de gas según el quintil de ingreso al que pertenece la familia del solicitante y sus condiciones laborales.

#Condiciones socioeconomicas:
#   1-. Quintil de ingreso. (1= -or ingreso, 5= +or ingreso)
#   2-. Condiciones laboral: Se considera si la persona está empleada o desempleada.
#   3-. Condiciones del subicidio de gas: 

#    QUINTIL       ESTADO               SUBSIDIO
#      1       CUALQUIERA                10000
#      2       CUALQUIERA                8000
#      3       DESEMPLEADO               6000
#      4       EMPLEADO                  4000
#      5       CUALQUIERA                1500

#BONO ADICIONAL= si el participante se encuentra en el quintil uno o dos recibe un bono adicional de 2000$ y si además tiene 65 años de 3000$

def inicio_prog():
    name=input("Bienvenid@, para poder saber si tienes un subsidio de gas necesitamos un par de datos. \n Ingresa tu nombre: ")
    edad=int(input("Ahora tienes que ingresar tu edad: "))
    respue=input(F"Entonces, ¿Tu nombre es {name} y tienes {edad} años?")
    respue=respue.lower()
    if respue == "si":
        print("¡Muy bien! Podemos seguir.")
        quintil(name,edad)
    elif respue == "no":
        print("¡Oh no! Volvamos a entroducir tus datos")       
        inicio_prog()
    else:
        print("Opción invalida, reintroduzca sus datos.")       
        inicio_prog()

def quintil(name,edad):
    print("Empecemos con los Quintiles.\nSabemos que el primer Quintil es el más bajo, y el quinto Quintil es el más alto.")
    quin=int(input("¿Cuál es tu Quintil? "))
    if quin in [1,2,3,4,5]:
        print(f"Muy bien {name}, tu Quintil es el : {quin}")
        estado_empleo(name,edad,quin)
    else:
        print("Algo ha salido mal, vuelve a ingresar tu Quintil.")
        quintil(name,edad)

def estado_empleo(name,edad,quin):
    print("Nos quedan pocos pasos, ahora tenemos que ver tu estado de empleo.")
    est=input("¿Estas Empleado o Desempleado?")
    est= est.lower()
    if est == "empleado":
        print(f"Tu estado es: {est}")
        bono_ad(name,edad,quin,est)
    elif est == "desempleado":
        print(f"Tu estado es: {est}")
        bono_ad(name,edad,quin,est)
    else:
        print("Opción invalida, por favor vuelve a introducir tu estado de empleo.")
        estado_empleo(name,edad,quin)

def bono_ad(name,edad,quin,est):
    bono=0
    if quin in [1,2]:
        print(f"¡Enhorabuena, {name}! Tienes un bono adicional de 2.000$ por ser del {quin} Quintil.")
        bono=2000
        calculo(name,edad,quin,est)
    elif quin in [3,4,5]:
        print(f"Desafortunadamente {name}, no tienes un bono adicional de Quintil.")
        calculo(name,edad,quin,est)
    elif edad >= 65:
        print(f"¡{name}! Tienes un bono adicional de 3.000$ por tener {edad} años.")
        bono=3000
        calculo(name,edad,quin,est)
    elif edad <= 64:
        print(f"Desafortunadamente {name}, no tienes un bono adicional de edad.")
        calculo(name,edad,quin,est)
    else:
        salida(name,edad,quin,est)

def calculo(name,edad,quin,est):
    if quintil == 1:
        subsidio = 10000
    elif quintil == 2:
        subsidio = 8000
    elif quintil == 3:
        subsidio = 6000 if estado_empleo == "desempleado" else 0
    elif quintil == 4:
        subsidio = 4000 if estado_empleo == "empleado" else 0
    elif quintil == 5:
        subsidio = 1500
    else:
        subsidio = 0

    # Calcular bonos adicionales
    bono_adicional = 0
    if quintil in [1, 2]:
        bono_adicional += 2000  # Bono por estar en quintiles 1 o 2
    if edad >= 65:
        bono_adicional += 3000  # Bono adicional por edad >= 65

    # Sumar el subsidio base con los bonos adicionales
    subsidio += bono_adicional

    # Mostrar el resultado final
    print(f"\n{name}, tu subsidio de gas es: ${subsidio}")
    

def salida(name,edad,quin,est):
    volver=input(f" Hemos terminado {name}. ¿Quieres volver a sacar tu subsidio?\n Si.\nNo.")
    volver=volver.lower()
    if volver== "si":
        inicio_prog()   
    else:
        print("Adios.")

inicio_prog()