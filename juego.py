#Importar librerías y declarar variables

#import random
from collections import deque
#import os

#librería deque que nos permite crear y utilizar una cola en Python. Una cola es una lista de datos a la que le podemos aplicar el método rotate, 
#para rotar los elementos a la izquierda o a la derecha. Ésto nos servirá para cambiar (rotar) el turno del jugador.
 
turno = deque(["0", "X"])
tablero = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "],
]

#Funcion para el tablero y para rotar el turno

#Crearemos una función para mostrar el tablero. Ésta imprimirá la multilista que contiene el tablero.

def mostrar_tablero():
	print("")
	for fila in tablero:		
		print (fila)
 
def actualizar_tablero(posicion, jugador):
	tablero[posicion[0]][posicion[1]] = jugador
 
def rotar_turno():
	turno.rotate()
	return turno[0]

#Funcion para procesar y verificar la posición

#Tenemos una función para procesar la posición, ésta convierte una cadena dada como “1,1” en una lista que contendrá los valores [0,0].
#La función posicion_correcta determina si la posición dada contiene un valor correcto. Por ejemplo, la posición dada “4,4” no sería correcta

def procesar_posicion(posicion):
	fila, columna = posicion.split(",")
	return [int(fila)-1, int(columna)-1]

def posicion_correcta(posicion):
	if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
		if tablero[posicion[0]][posicion[1]] == " ":
			return True
	return False

def procesar_posicion(posicion):
	fila, columna = posicion.split(",")
	return [int(fila)-1, int(columna)-1]
 
def posicion_correcta(posicion):
	if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
		if tablero[posicion[0]][posicion[1]] == " ":
			return True
	return False

#Función para verificar si se ha ganado el juego de tres en raya en Python

# compara las filas, luego las columnas y por último las diagonales. No compara si existe empate entre los jugadores

def ha_ganado(j):
	#compara las filas del tablero
	if tablero[0] == [j,j,j] or tablero[1] == [j,j,j] or tablero[2] == [j,j,j]:
		return True
	#compara las columnas
	elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
		return True
	elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
		return True
	elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
		return True
	#compara las diagonales
	elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
		return True
	elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
		return True
	return False

#Funcion de ver si ganaste el juego

#La función principal, a la que llamamos juego, utiliza un ciclo While
#infinito para preguntar al usuario la posición (fila, columna) en el tablero en la que desea dejar la marca del jugador en turno

def juego():
	mostrar_tablero()
	jugador = rotar_turno()
	while True:
		posicion = input("Juega {}, elige una posicion (fila, columna) de 1 a 3. 'salir' para salir".format(jugador))
		if posicion == 'salir':
			print ("Adios!!!")
			break
		try:
			posicion_l = procesar_posicion (posicion)			
		except:
			print ("Error, posicion {} no es válida. ".format(posicion))
			continue
		if posicion_correcta(posicion_l):
			actualizar_tablero(posicion_l, jugador)
			mostrar_tablero()
			if ha_ganado(jugador):
				print ("Jugador de {} ha ganado!!!".format(jugador))
				break
			jugador = rotar_turno()
		else:
			print ("Posicion {} no válida".format(posicion))
	
#Funcion principal del juego.
def juego():
	mostrar_tablero()
	jugador = rotar_turno()
	while True:
		posicion = input("Juega {}, elige una posicion (fila, columna) de 1 a 3. 'salir' para salir".format(jugador))
		if posicion == 'salir':
			print ("Adios!!!")
			break
		try:
			posicion_l = procesar_posicion (posicion)			
		except:
			print ("Error, posicion {} no es válida. ".format(posicion))
			continue
		if posicion_correcta(posicion_l):
			actualizar_tablero(posicion_l, jugador)
			mostrar_tablero()
			if ha_ganado(jugador):
				print ("Jugador de {} ha ganado!!!".format(jugador))
				break
			jugador = rotar_turno()
		else:
			print ("Posicion {} no válida".format(posicion))
	
juego()