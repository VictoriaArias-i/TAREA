# Contexto:

# La tienda EcoVida ha decidido mejorar su sistema de atención al cliente ofreciendo descuentos y recargos personalizados 
# dependiendo del tipo de cliente, el monto de compra, el método de pago y hasta... ¡las letras del nombre del cliente! 
# Además, aplican un "número de la suerte" para ofrecer beneficios adicionales.

# Crear un programa en Python que:
# 1. Solicite los siguientes datos al usuario:
#   1. Nombre del cliente
# II. Tipo de cliente (Normal, Frecuente, Premium, Empresarial, Adulto Mayor)
# III. Monto de la compra
# IV. Método de pago (Efectivo, Débito, Crédito)
#   2. Aplique descuentos según:
# 1. Tipo de cliente y monto de compra.
# II. Método de pago
# III. Contenido del nombre (si incluye letras "a", "e" u "D")
#   3. Aplique recargos si:
# 1. Paga con tarjeta de crédito y compra es menor a 20.000. T
#   4. Genere un "número de la suerte" al azar:
# 1. Si sale 709 descuento del 5%
# II. Si sale 102 recargo del 3%
# III. Si sale 5 gana un cupón (sin afectar el precio final)
#   5. Calcule el total a pagar y muestre resumen.

#Condición                                      # Descuento/Recargo

# Cliente Normal y compra ≥$100.000              # 5% de descuento
# Cliente Frecuente y compra ≥ $80.000          # 10% de descuento
# Cliente Premium y compra≥ $50.000              # 15% de descuento
# Cliente Empresarial y compra ≥$200.000         # 20% de descuento
# Cliente Adulto Mayor y compra ≥ $30.000       # 8% de descuento
# Método de pago: Efectivo y compra ≥ $50.000   # 3% de descuento
# Método de pago: Crédito y compra < $20.000    # 5% de recargo
# Nombre contiene "a", "e" "o" u "d"            # 2% de descuento
# Número de la suerte = 7o9                     # 5% de descuento
# Número de la suerte = 1o2                     # 3% de recargo
# Número de la suerte = 5                       # Gana un cupón

def inicio_prog():
    print("Bienvenido a la tienda EcoVida. \n Para agradecerle a nuestros clientes su preferencia hemos dado unos beneficios.")
    print("Averiguelos al final del programa.")
    name=input("¿Cuál es su nombre?\n")
    print(f"¡Hola, {name}.")
    tipo_cliente=int(input("¿Qué tipo de cliente es?\n1-Normal\n2-Frecuente\n3-Premium\n4-Empresarial\n5-Adulto Mayor\n"))
    tipo_compra= input("¿Y con qué vas a comprar hoy?\n Efectivo\n Debito\n Credito\n")
    tipo_compra=tipo_compra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").lower()
    compra=int(input("¿Cuanto es el total de su carrito?"))
    descuento(name,tipo_cliente,tipo_compra,compra)

def descuento(name,tipo_cliente,tipo_compra,compra):
    desc_total = 0
    recargo_total = 0

    if any(letra in name.lower() for letra in ["a", "e", "o", "d"]):
        print("Su nombre contiene una \"a-e-o-d\", por ende tiene un 2% de descuento ")
        desc_total += 0.02
    else:
        print("No tiene descuento de nombre.")

    if tipo_cliente == 1 and compra >= 100000:
        print(f"Al pagar con {tipo_compra} tiene un 5% de descuento.")
        desc_total += 0.05

    elif tipo_cliente== 2 and compra >= 80000:
        print(f"Al pagar con {tipo_compra} tiene un 10% de descuento.")
        desc_total += 0.10
    elif tipo_cliente== 3 and compra >= 50000:
        print(f"Al pagar con {tipo_compra} tiene un 15% de descuento.")
        desc_total += 0.15
    elif tipo_cliente== 4 and compra >= 200000:
        print(f"Al pagar con {tipo_compra} tiene un 20% de descuento.")
        desc_total += 0.20
    elif tipo_cliente== 5 and compra >= 30000:
        print(f"Al pagar con {tipo_compra} tiene un 8% de descuento.")
        desc_total += 0.08
    else:
        print("No tiene descuento de tipo de cliente.")

    if tipo_compra== "credito" and compra <= 20000:
        print(f"Al pagar con {tipo_compra} tiene un 5% de recargo.")
        recargo_total += 0.05
    elif tipo_compra== "efectivo" and compra >= 50000:
        print(f"Al pagar con {tipo_compra} tiene un 3% de descuento.")
        desc_total += 0.03
    else:
        print("No tiene descuento de tipo de compra.")
    
    print("¡Ultimo intento de descuento!\n Genere un numero al azar, usted escoge los numeros, recuerde que el primero es el numero más bajo.")
    import random
    a= int(input("Primer numero: "))
    b= int(input("Segundo numero: "))
    num_alt= random.randint(a,b)

    print(f"El numero al azar es {num_alt}")
    if num_alt in [7,9]:
        print("Bien, ha ganado un 5% de descuento.")
        desc_total += 0.05
    elif num_alt in [1,2]:
        print("Oh, ha ganado un 3% de recargo.")
        recargo_total += 0.03
    elif num_alt == 5:
        print("¡Que suerte! Ha ganado un cupón.")
    else:
        print("No tiene descuento de numero de la suerte.")

    total = compra * (1 - desc_total)
    total *= (1 + recargo_total)
    print(f"El total de descuento que tiene sobre su compra de {compra} es de {total}")
inicio_prog()