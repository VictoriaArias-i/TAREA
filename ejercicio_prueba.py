#Almacenamiento de puntos de tarjeta
#La tienda Falabella necesita desarrollar un programa para saber cuantos puntos tiene acumulado cada usuario por cada 1000 pesos que realice en una compra un usuario recibe 10 pts
#Cuando un usuario alcance al nivel premium que son 1000 pts tiene un descuento de 25% 
#Cuando un usuario alcande el nivel oro que son 500 pts tiene un desceunto de 10%
#Cuando un usuario alcande el nivel bronze que son 250 pts tiene una recompensa de uno de estos objetos: Audifonos, manos libres, relojes, etc.
# 1ra tarjeta= Marcos= 1500 pts a canjear. ¿Qué niveles le corresponden?
# 2da tarjeta= Jose Luis 2500 pts a canjear.
# 3ra tarjeta= Sebastian 300 pts a canjear.
#¿Qué niveles le corresponden a cada uno? Puede ser más de un nivel por usuario.
# Mostrar en pantalla la información que corresponda al usuario con sus niveles y al final un mensaje que motive a que siga comprando.

"""Ejercicio"""

print("Bienvenido a la tienda Falabella")
print("Recuerde que por cada 1000 pesos gastados, acumula 10 puntos.")
print("Los niveles de puntos son los siguientes:\n- Bronce: 250 puntos (regalo de audífonos, manos libres o reloj)\n- Oro: 500 puntos (10% de descuento en su próxima compra)\n- Premium: 1000 puntos (25% de descuento en su próxima compra)")

user = input("¿Cuál es su nombre de usuario?")
pts = int(input("¿Cuántos puntos tiene acumulados?"))

nvl_prem = 1000
if pts >= 1000:
    nivel = "Premium"
elif pts >= 500:
    nivel = "Oro"
elif pts >= 250:
    nivel = "Bronce"
else:
    nivel = "Sin nivel"

if user == "Marcos":
    print(f"¡Bienvenido {user}!\n En este momento has acumulado {pts} puntos.")
    if pts <= 1000:
        print(f"¡Felicitaciones, {user}! Has alcanzado el nivel Premium con un descuento del 25% en tu próxima compra.")
    elif pts >= 1500:
        print(f"¡Increíble, {user}! Has acumulado más de {pts} puntos. Eso significa que puedes disfrutar de los beneficios de los niveles Premium y Oro.")
    elif pts <= 500:
         print(f"¡Genial, {user}! Has alcanzado el nivel Oro con un descuento del 10% en tu próxima compra.")
    elif pts <= 250:
        print(f"¡Felicidades, {user}! Has alcanzado el nivel Bronce y puedes canjear un regalo como audífonos, manos libres o relojes.")
    else:
        print(f"¡Sigue comprando, {user}! Te falta poco para alcanzar el nivel Bronce y obtener un regalo.")
      

elif user == "Jose Luis":
    print(f"¡Bienvenido {user}!\n En este momento has acumulado {pts} puntos.")
    if pts <= 500:
         print(f"¡Genial, {user}! Has alcanzado el nivel Oro con un descuento del 10% en tu próxima compra.")
    elif pts <= 250:
        print(f"¡Felicidades, {user}! Has alcanzado el nivel Bronce y puedes canjear un regalo como audífonos, manos libres o relojes.")
    elif pts <= 1500:
        print(f"¡Increíble, {user}! Has acumulado más de {pts} puntos. Eso significa que puedes disfrutar de los beneficios de los niveles Premium y Oro.")
    elif pts >= 2000:
        print("¡Enhorabuena, {user}! Has acumulado más de 2000 puntos. ¡Sigue así!\n Eso significa que puedes disfrutar de los beneficios del nivel Premium de forma doble y Oro.")
    else:
        print(f"¡Sigue comprando, {user}! Te falta poco para alcanzar el nivel Bronce y obtener un regalo.")

     
elif user == "Sebastian":
    print(f"¡Bienvenido {user}! \n En este momento has acumulado {pts} puntos.")
    if pts >= 1000:
        print(f"¡Felicitaciones, {user}! Has alcanzado el nivel Premium con un descuento del 25% en tu próxima compra.")
    elif pts <= 500:
        print(f"¡Genial, {user}! Has alcanzado el nivel Oro con un descuento del 10% en tu próxima compra.")
    elif pts <= 250:
        print(f"¡Felicidades, {user}! Has alcanzado el nivel Bronce y puedes canjear un regalo como audífonos, manos libres o relojes.")
    else:
        print(f"¡Sigue comprando, {user}! Te falta poco para alcanzar el nivel Bronce y obtener un regalo.")
    
else:
    print("Usuario no reconocido. Por favor, verifica tu nombre.")
    print("¡Sigue comprando para acumular más puntos y obtener grandes recompensas!")

print("************************")
print(f"Tu perfil de usuario consta con tu nombre: {user}\n Tus puntos acumulados: {pts} \n Tu nivel es: {nivel}")
print("Gracias por visitar la tienda Falabella.\n ¡Esperamos verte pronto!")
print("************************")