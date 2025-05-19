"""Clase 16: Ejercicio tipo examen + Repaso """

"""19-05-25"""

# Ejercicios mandandos en el ava

print("Papá, revisa 3 numeros.")

#   Lista

numero= [5, 4, 6]

#   Contador

num_primo= 0
num_no_primo= 0

def es_primo(n):
    if n <= 1:
        return False # Retrun sirve para volver sin tener que llamarlo o re hacerlo
    for i in range(2, int(n//2)+1):
        if n % i == 0:
            return False
    return True

for i, numero in enumerate(numero):
    print(f"{i+1} numero: {numero}", end= "->")
    if es_primo(numero):
        print("¡Es primo!")
        num_primo += 1
    else:
        print("No es primo")
        num_no_primo += 1
    print("\nResultado")
    print(f"Se ingresa {num_primo} numero primo.")
    print(f"Se ingresa {num_no_primo} numero {"s" if num_no_primo > 1 else ""} No primo")

#EJERCICIO DE PRUEBA