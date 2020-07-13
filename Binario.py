import math

operacion = int(input("0. Pasar de binario a texto\n1. Pasar de texto a binario\n"))
m = str(input("\n"))
m = m.split()

def binarioDecimal(n):

    numero = 0

    for j in range(len(n)):
        for i in range(len(n[j])):
            numero = numero + int(n[j][len(n[j]) - i - 1]) * 2 ** i

        print(chr(numero),end="")
        numero = 0

def decimalBinario(n):
    
    for j in range(len(n)):
        for k in range(len(n[j])):
            nuevo = ""
            var = ord(n[j][k])

            for i in range(7, -1, -1):
                nuevo = nuevo + str(math.floor(var / 2**i))
                var = var % 2**i

            print(nuevo, end = " ")
        print("00100000")    

        
if(operacion == 0):
    binarioDecimal(m)
elif(operacion == 1):
    decimalBinario(m)
     
