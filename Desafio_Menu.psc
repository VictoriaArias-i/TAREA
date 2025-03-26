Proceso Desafio_Menu
	// Preguntar preferencia de comida (3 opciones) y validar su edad, requisitos = nombres y edad del usuario, mayor o menor de edad, "
	// Bienvenido" si es que es mayor, para los que son menores los invitamos a comer todos los vegetales con un mensaje,
	// y les presentaran el menu de opciones o alimentos, 1- Pasta, 2- Pizza, 3- Ensalada, 4- Otros. 
	
	Definir USUARIO Como Caracter;
	Definir EDAD Como Entero;
	Definir OPCIONES Como entero;
	
	Escribir "Bienvenido al programa, ¿Cuál es tu nombre?";
	Leer USUARIO;
	
	Escribir "Hola ", USUARIO, " ¿Qué edad tienes?";
	Leer EDAD;
	Si EDAD > 17 Entonces
		Escribir USUARIO, " gracias por responder. Las opciones de almuerzo del casino son:";
		
		Escribir "- Pasta";
		Escribir "- Pizza";
		Escribir "- Ensalada";
		Escribir "- Otro";
		Leer OPCIONES;
		
		Segun OPCIONES Hacer
			1:
				Escribir "1- Pasta";
			2:
				Escribir "2- Pizza";
			3:
				Escribir "3- Ensalada";
			De Otro Modo:
				Escribir "No tenemos más opciones, por favor encuentra otro lugar para comer.";
		FinSegun
		
	SiNo 
		Escribir USUARIO, ", te invitamos a comer todos los vegetales";
	FinSi
	
FinProceso
