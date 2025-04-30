#Clase 10 30-04-25

"""Ejericio prueba"""

#Desarrolla un programa en python que permite calcular el subcidio de gas según el quintil de ingreso al que pertenece la familia del solicitante y sus condiciones laborales.

#Condiciones socioeconomicas:
#   1-. Quintil de ingreso. (1= -or ingreso, 5= +or ingreso)
#   2-. Condiciones laboral: Se considera si la persona está empleada o desempleada.
#   3-. Condiciones del subicidio de gas: 

#    QUINTIL       ESTADO               SUBCIDIO
 #      1       CUALQUIERA                10000
 #      2       CUALQUIERA                8000
 #      3       DESEMPLEADO               6000
 #      4       EMPLEADO                  4000
 #      5       CUALQUIERA                1500

 #BONO ADICIONAL= si el participante se encuentra en el quintil uno o dos recibe un bono adicional de 2000$ y si además tiene 65 años de 3000$

def inicio():
    name= input("Bienvenido, para poder revisar su quintil de subicidio ingrese su nombre: ")
    edad= input("También necesitamos saber tu edad. \nIngresalo aquí: ")
    print(f"¡Hola, {name}, un gusto!\n En este momento tienes {edad} años.")
    quint()        

def ed(edad):
    if edad >= 65:
        print("¡Enhorabuena! Tienes en el beneficio de jubilación, se te agregará un bono de $3.000 pesos.")
    else:
        edad <= 64
        print("Desafortunadamente no entras en el rango de edad para el bono de jubilación.")
def priqui():
    print("¡Felicitaciones! Por encontrarte en el primer y segundo quitil se te ha entregado un bono adicional de $2.000 pesos.")

def quint():
    print(" Ahora necesitamos saber en qué Quintil te encuentras.\nRecuerda que sabemos que el \"primer quintil es el más bajo\" entonces el \"quinto es el más alto\".")
    quin= input("Ingresa tu QUINTIL: \n a) 1\n b) 2\n c) 3\n d) 4\n 3) 5 \n ")

    if quin == "a":
        print("En este momento te encuentras en el primer quintil.")
        est(quin)
    elif quin == "b":
        print("En este momento te encuentras en el segundo quintil.")
        est(quin) 
    elif quin == "c":
        print("En este momento te encuentras en el tercero quintil.")
        est(quin) 
    elif quin == "d":
        print("En este momento te encuentras en el cuarto quintil.")
        est(quin)         
    elif quin == "e":
        print("En este momento te encuentras en el quinto quintil.")
        est(quin) 
    else:
        print("¡Oh no! Algo ha salido mal, vuelve a ingresar tu quintil.")
        quint()

def est(quint):
    print("El siguiente paso es saber tu estado de empleo.")
    esta= input("Ingrese su estado: \na) Empleado.\nb) Desempleado.\n")

    if esta== "a":
        print("En este momento te encuentras empleado.")
        sub(quint, esta) 
    elif esta == "b":
       print("En este momento te encuentras empleado.")
       sub(quint, esta)
    else:
        print("Perdón, no se ha procesado bien tu respuesta, por favor vuelve a ingresarla.")
        est(quint)

def sub(quint, esta):
    print("Estamos por terminar, ahora vamos a calcular tu subcidio del gas.")

    if quint == "a" and esta == "a" or "b":
        print("Su subcidio este año es de 10.000$")
        priqui()
        perfil()
    elif quint == "b" and esta == "a" or "b":
        print("Su subcidio este año es de 8.000$")
        priqui()
        perfil()
    elif quint == "c" and esta == "b":
        print("Su subcidio este año es de 6.000$")
        perfil()
    elif quint == "d" and esta == "a":
        print("Su subcidio este año es de 4.000$")
        perfil()
    elif quint == "e"  and esta == "a" or "b":
        print("Su subcidio este año es de 8.000$")
        perfil()
    else:
        print("Perdón, en este momento no tenemos ningún subcicdio de gas para tu perfil.")
        perfil()

def perfil(name, ed, esta, quin):
    print("Como el ultimo antes de dejarte ir vamos a hacer una recopilación de datos.")
    print(f"    Tu perfil en esto momento es:   \nNombre: {name}.       Edad: {ed}.\nQuintil: {quin}        Estado: {esta}")
    salida()


def salida(name):
    vol= input(f"{name}, ¿Quieres volver a consultar sobre el subcidio del gas?\n a) Sí.\n b) No.")
    if vol == "a":
        print("Muy bien, tendrás que reingresar todos tus datos.")
        inicio()
    elif vol == "b":
        print(f"¡Un gusto {name}! Esperamos volver a verte.")
    else:
        print("Perdón, esa opción no está disponible.")
        salida()

inicio()