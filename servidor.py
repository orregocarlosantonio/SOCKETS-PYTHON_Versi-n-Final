#################################
#								#
#	MISE - UPM					#
#	LSE - PRACTICA 4			#
#	SOCKETS PYTHON				#
#								#
#	CARLOS ANTONIO ORREGO		#
#								#
#################################
#								#
#	        SERVIDOR	 		#
#								#
#################################
#--------------------------------------------------------------------------------------------------------------------#
# Protocolo de comunicacion:[Tipo de sensor, Identificador del sensor , Valor sensado] 
#	Descripcion de cada campo:
#		a)	|-------------------------------------------|
#			| Tipo de sensor 				|   Tipo	|
#			|-------------------------------|-----------|
#			| Temperatura					| 	  1		|
#			| Luminosidad					| 	  2		|
#			| Intensidad de sonido (dB)		| 	  3		|
#			| Sensor adicional				|	  n		|
#			|-------------------------------------------|
# 		b)	Identificador: Numero asignado apara su identificacion
#		c)	Valor sensado: Signo y Magnitud del sensor utilizado
#--------------------------------------------------------------------------------------------------------------------#

import socket,select,time
from os import curdir, sep

try:
	HOST_CLIENT = ''                
	PORT_CLIENT  = 1234              
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.bind((HOST_CLIENT, PORT_CLIENT))
	cliente.listen(1)

	HOST_SERVER = '127.0.0.1'
	PORT_SERVER  = 8080                
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind((HOST_SERVER, PORT_SERVER))
	serverSocket.listen(1);
	
	inputs =[cliente,serverSocket]
	
# Inicializacion de variables
	temperatura = 0
	decibeles = 0
	luminosidad = 0

	while True:
		(read, write, exc) =  select.select(inputs,[],[])
		for s in read:
			if s == cliente:
				conn, addr = s.accept()
				Rx_client = conn.recv(1024)
				Tipo = Rx_client [:1]
				Identificador = Rx_client [1:2]
				Valor = Rx_client [2:]
				if Tipo == '1' and Identificador == '1':
					temperatura = Valor
					print "Dato recibido del sensor de Temperatura = "+Valor+" [C]"
				conn.sendall(Rx_client)
				if Tipo == '2' and Identificador == '1':
					luminosidad = Valor
					print "Dato recibido del sensor de Luminosidad = "+Valor+" [C]"
				conn.sendall(Rx_client)
				if Tipo == '3' and Identificador == '1':
					decibeles = Valor
					print "Dato recibido del sensor de Intensidad Sonora = "+Valor+" [C]"
				conn.sendall(Rx_client)
#--------------------------------------------------------------------------------------------------------------------#
				#Para adicionar o agregar un nuevo de sensor,replicar las siguientes tres lineas					
				#if Tipo == 'n' and Identificador == 'z':	# Asigne valor a: n (Tipo de sensor) y z (Identificacion)
				#	Sensor = Valor							# Edite la palabra sensor, con el nombre correspondiente, Ejemplo: Humedad
				#	print "Dato recibido del sensor de __________ = "+Valor+" [C]"	# Complete la frase ___________
#--------------------------------------------------------------------------------------------------------------------#
			elif s == serverSocket:
					print 'Servidor en linea, Ctrl+C para salir'
					connectionSocket, addr = serverSocket.accept()
					try:	
						message = connectionSocket.recv(1024)
						filename = message.split()[1]
						path = "index.html"
						f = open(curdir + sep + path)
						outputdata = f.read()
						date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
						connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n')
						connectionSocket.send(outputdata.replace("temperatura","%s [&degC]"%(temperatura)).replace("decibeles","%s [dB]"%(decibeles)).replace("luminosidad","%s [lux]"%(luminosidad)).replace("fecha","%s"%(date)))
						connectionSocket.close()

					except IOError:
						connectionSocket.send('ERROR - 404 File not found\n') 
						connectionSocket.shutdown(1)						
						connectionSocket.close()
			else: 
				print "Servidor no detectado"
				continue

except (KeyboardInterrupt, SystemExit):
	print '  Ctrl+C recibido, apagando servidor'	
	serverSocket.shutdown(1)
	serverSocket.close()
