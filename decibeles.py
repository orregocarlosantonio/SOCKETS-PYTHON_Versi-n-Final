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
#   Intensidad de sonido (dB)	#
#								#
#################################
import socket
import random
import math
import numpy
import numpy as np

HOST = ''
PORT = 1234         
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
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
Tipo = 3
Identificador = 1
Valor = math.floor(200+(random.random()-0.5)*200)
s.sendall(repr(Tipo)+repr(Identificador)+repr(Valor))
data = s.recv(1024)
print "Dato Recibido: Decibeles = " + data [2:6] +" (dB)"
