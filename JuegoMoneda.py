import random
#Librería que genera núeros aleatorios

opcion = int(input("Ingrese 1 para cara, 0 para sello: "))
moneda = random.randrange(0,1+1)

if moneda == opcion:
	print("Ganaste Felicitaciones")	
else:
	print("Perdiste, suerte para la próxima")
