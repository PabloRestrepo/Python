import math
def primo(n):
	valor = True
	for i in range(2, math.floor(n ** 1/2) + 1):
		if((n % i) == 0):
			valor = False
	return valor

an = 2

while(an < 1000):
	an = (2 ** an) - 1
	print(an, " ", primo(an))
