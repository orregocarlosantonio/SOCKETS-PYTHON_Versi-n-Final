#################################
#				#
#	MISE - UPM		#
#	LSE - PRACTICA 4	#
#	SOCKETS PYTHON		#
#				#
#	CARLOS ANTONIO ORREGO	#
#				#
#################################

#--------------------------------------------------------------------------------------------------------------------#

1) Ejecutar en un terminal el siguiente comando:
	python servidor.py      # Se inicializa el servidor

2) En el navegador colocar el siguiente vinculo
	http://localhost:8080   # Se refrescara automaticamente cada 5 segundos despues de cargar la pagina

3) Ejecutar en otro terminal los siguientes comandos:
 	python temperatura.py  	# Lee el sensor de Temperatura
	python decibeles.py  	# Lee el sensor de Intensidad Sonora
	python luminosidad.py  	# Lee el sensor de Luminosidad

#--------------------------------------------------------------------------------------------------------------------#

GENERALIDADES DEL CODIGO

#--------------------------------------------------------------------------------------------------------------------#

1. Se utiliza un solo puerto para recibir la informacion de todos los clientes.

2. Se establecio el siguiente Protocolo de comunicacion:[Tipo de sensor, Identificador del sensor , Valor sensado] 
	Descripcion de cada campo:
	a)	|------------------------------------------|
		| Tipo de sensor 		|   Tipo   |
		|-------------------------------|----------|
		| Temperatura			|      1   |
		| Luminosidad			|      2   |
		| Intensidad de sonido (dB)	|      3   |
		| Sensor adicional		|      n   |
		|------------------------------------------|
	b) Identificador: Numero asignado apara su identificacion
	c) Valor sensado: Signo y Magnitud del sensor utilizado
#--------------------------------------------------------------------------------------------------------------------#

3. Para adicionar o agregar un nuevo de sensor en el servidor,tan solo debe replicar las siguientes tres lineas
#--------------------------------------------------------------------------------------------------------------------#				
	#if Tipo == 'n' and Identificador == 'z':	# Asigne valor a: n (Tipo de sensor) y z (Identificacion)
	#	Sensor = Valor				# Edite la palabra sensor, con el nombre correspondiente, Ejemplo: Humedad
	#	print "Dato recibido del sensor de __________ = "+Valor+" [C]"	# Complete la frase ___________
#--------------------------------------------------------------------------------------------------------------------#

4. Para dicionar un nuevo cliente, duplique uno de los archivos y solo debe actualizar la información de:
	a) Tipo
	b) Identificador
	c) Mensaje a visualizar

5. El navegador se refresca automaticamente cada 5 segundos

6. El navegador muestra la fecha y hora de su ultima actualizacion
