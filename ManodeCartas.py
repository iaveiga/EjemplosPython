import random

palo = [1,2,3,4,5,6,7,8,9,10,11,12,13]
mano = []

#carta 1
num = random.randrange(0,len(palo))
mano.append(palo.pop(num))

#carta 2
num = random.randrange(0,len(palo))
mano.append(palo.pop(num))

#carta 3
num = random.randrange(0,len(palo))
mano.append(palo.pop(num))

#carta 4
num = random.randrange(0,len(palo))
mano.append(palo.pop(num))

#carta 5
num = random.randrange(0,len(palo))
mano.append(palo.pop(num))

print("Tus cartas son: ", mano)
