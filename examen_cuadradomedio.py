
print("METODO DEL CUADRADO MEDIO")
print("")

def cuadrado_medio(seed,n_numeros):
    cuadrado = str(seed ** 2).zfill(2 * n_numeros)  
   
    inicio = (len(cuadrado) - n_numeros) // 2 
    
    nuevo = int(cuadrado[inicio:inicio + n_numeros])  
   
    return nuevo


semilla = int(input("Ingrese se semilla inicial:"))
n_numeros = int(input("Ingrese la cantidad de digitos a utilizar:"))
resultado = cuadrado_medio(semilla, 4) 
print("Nueva semilla:", resultado)  
