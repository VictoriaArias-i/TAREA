"""Prueba Python 09-05-2025"""

#Ejercicio 1 

# Desarrolle un programa en Python que permita calcular los beneficios a los estudiantes de
# primer año según sus condiciones académicas y socioeconómicas. 
# Las condiciones académicas están basadas en el promedio final con el que salieron del colegio o liceo. 
# Las condiciones socioeconómicas están basadas según el quintil al que pertenece su grupo familiar (5 quintiles en total). 
# 
# La tabla siguiente muestra el beneficio según las condiciones recién mencionadas:

# Condición Académica Condición                       Socioeconómica Beneficio
# Promedio mayor a 6.0 Quintil 1 o Quintil 2             20% descuento arancel
# Promedio mayor a 6.0 Quintil 3 o Quintil 4            15% descuento arancel
# 5.0 < Promedio <= 6.0 Quintil 1 o Quintil 2           13% descuento arancel
# 5.0 < Promedio <= 6.0 Quintil 3 o quintil 4           10% descuento arancel

# Además, por el solo hecho de pertenecer al Quintil 1, 2 o 3 tiene un descuento del 10% en la
# matrícula y si perteneciendo a esos quintiles su promedio es mayor o igual a 5.5 se obtiene  un 5% adicional.

# El programa debe entregar el valor final del arancel y matrícula suponiendo que se le entrega
# el promedio y el quintil del estudiante. Suponga que el valor del arancel es de $1.800.000 y la matrícula es de $90.000.

def inicio_prog():
    print("Bienvenido al programa de beneficio estudiantil.")
    promedio=float(input("Para comenzar necesitamos su promedio final: "))
    socio_eco=input("Y tu nivel socioeconomico:\n Recuerda que hay 5 quintiles siendo el primero el más bajo.\na)Primero\nb)Segundo\nc)Tercero\nd)Cuarto\ne)Quinto\nResponde con las letras indicadas: ")
    socio_eco=socio_eco.lower()
    beneficios(promedio,socio_eco)

def beneficios(promedio,socio_eco):
    desc2=0
    desc1=0
    
    if socio_eco in ["a", "b","c"]:
        print("Por ser parte de los primeros quintiles, tienes un descuento de 10% para tu matricula.")
        desc1=0.10
        if promedio >= 5.5:
            print("Además tienes extra de 5% de descuento en tu matricula logrando un 15% ")
            desc1=0.15
        elif promedio < 5.5:
            print("Solo tienes el 10% de descuento. ")
            desc1=0.10
    else:
        print("Desafortunadamente no tienes descuento en tu matricula.")
        desc1=0

    if promedio > 6.0 and socio_eco in ["a","b"]:
        print("Muy bien, tienes un descuento de 20% para tu arancel.")
        desc2=0.20
    elif promedio > 6.0 and socio_eco in ["c","d"]:
        print("Muy bien, tienes un descuento de 15% para tu arancel.")
        desc2=0.15
    elif 5.0 < promedio <= 6.0 and socio_eco in ["a","d"]:
        print("Muy bien, tienes un descuento de 13% para tu arancel.") 
        desc2=0.13       
    elif 5.0 < promedio <= 6.0 and socio_eco in ["c","d"]:
        print("Muy bien, tienes un descuento de 10% para tu arancel.")
        desc2=0.10    
    elif socio_eco == "e":
        print("Desafortunadamente no tienes descuento en tu arancel.")
    
    print("Ahora vamos a calcular tu arancel y matricula.")
    calculo(promedio,socio_eco,desc1,desc2)

def calculo(promedio,socio_eco,desc1,desc2):
    aran=1800000
    matr=90000
    total1=0
    total2=0

    print("El valor del arancel es de $1.800.000 y la matrícula es de $90.000")
    if promedio > 6.0 and socio_eco in ["a","b"]:
        total1= aran * desc2
        total2= matr * desc1

        t_final1= aran - total1
        t_final2= matr - total2
        print(f"EL total del descuento de su arancel es {total1} y el de su matricula es de {total2}")
        print(f"Y el resultado final de su arancel es {t_final1} y el de su matricula es de {t_final2}")
    elif promedio > 6.0 and socio_eco in ["c","d"]:
        total1= aran *  desc2
        total2= matr * desc1

        t_final1= aran - total1
        t_final2= matr - total2
        print(f"EL total del descuento de su arancel es {total1} y el de su matricula es de {total2}")
        print(f"Y el resultado final de su arancel es {t_final1} y el de su matricula es de {t_final2}")
    elif 5.0 < promedio <= 6.0 and socio_eco in ["a","d"]:
        total1= aran * desc2
        total2= matr * desc1 

        t_final1= aran - total1
        t_final2= matr - total2
        print(f"EL total del descuento de su arancel es {total1} y el de su matricula es de {total2}")
        print(f"Y el resultado final de su arancel es {t_final1} y el de su matricula es de {t_final2}")
    elif 5.0 < promedio <= 6.0 and socio_eco in ["c","d"]:
        total1= aran *  desc2
        total2= matr * desc1

        t_final1= aran - total1
        t_final2= matr - total2
        print(f"EL total del descuento de su arancel es {total1} y el de su matricula es de {total2}")
        print(f"Y el resultado final de su arancel es {t_final1} y el de su matricula es de {t_final2}")
    elif 5.5 <= promedio and socio_eco in ["a","b", "c"] :
        total1= aran * desc2
        total2= matr * desc1 

        t_final1= aran - total1
        t_final2= matr - total2
        print(f"EL total del descuento de su arancel es {total1} y el de su matricula es de {total2}")
        print(f"Y el resultado final de su arancel es {t_final1} y el de su matricula es de {t_final2}")

        print("Adios, nos vemos pronto.")

inicio_prog()