vidas=5
palabra_a_adivinar=str(input("ingrese la palabra \n"))
listaTemporal={}
tupla=[]

for i in range(len(palabra_a_adivinar)):
    tupla.append(i)

tupla=tuple(tupla)

for i in range(len(palabra_a_adivinar)):
    listaTemporal[tupla[i]]="_"
   
def verificaLetra(letra):
    if((letra in palabra_a_adivinar)==True):
        for i in range(len(palabra_a_adivinar)):
            if(letra==palabra_a_adivinar[i]):
                listaTemporal[tupla[i]]=letra            
        return True              

def verificaPalabra(palabra):
    if(palabra==palabra_a_adivinar):
        return True

print("bienvenido, tienes 5 vidas")
while(vidas>0):
    contador=0
    boolean=str(input("desea adivinar la palabra si/no \n"))
    if(boolean=="si"):
        palabra=str(input("palabra\n"))
        if(verificaPalabra(palabra)==True):
            print("ganaste")
            break
        else:
            vidas=vidas-1
            print(vidas)
    letra=str(input("ingrese una letra \n"))
    if(verificaLetra(letra)!=True):
        vidas=vidas-1
    for i in range(len(palabra_a_adivinar)):
        
        print(listaTemporal[tupla[i]]+" ",end="")
        if(listaTemporal[tupla[i]]!="_"):
            contador=contador+1
    if(contador==len(palabra_a_adivinar)):
        print("\n ganaste")
        break
    print(contador)
    print(vidas)
if(vidas==0):
    print("perdiste")
       