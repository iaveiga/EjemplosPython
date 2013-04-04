import random

vecesGanadas = 0
saldo = 10000
for i in range(1,11):
    print("Turno : ",i)
    opcion = int(input("\nIngrese 1 para cara, 0 para sello: "))
    moneda = random.randrange(0,2)
    if moneda == opcion:
        print("Ganaste !!!\n")
        vecesGanadas = vecesGanadas + 1
        saldo = saldo + 1000
    else:
        print("\t Perdiste !!!\n")
        saldo = saldo - 500
print ("\n \n Ud ha ganado ", vecesGanadas, " veces")
print ("\n Su saldo es: ", saldo)



