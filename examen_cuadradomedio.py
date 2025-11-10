print(" MÉTODO DEL CUADRADO MEDIO ")

def cuadrado_medio(seed, n_digitos): 
    cuadrado = str(seed ** 2).zfill(2 * n_digitos)  
    inicio = (len(cuadrado) - n_digitos) // 2        
    nuevo = int(cuadrado[inicio:inicio + n_digitos]) 
    return nuevo


semilla = int(input("Ingrese la semilla inicial: "))
n_digitos = int(input("Ingrese la cantidad de dígitos de la semilla: "))
n = int(input("¿Cuántos números pseudoaleatorios desea generar?: "))

print("\nGenerando números...\n")

for i in range(n):
    nueva_semilla = cuadrado_medio(semilla, n_digitos)
    numero_pseudo = nueva_semilla / (10 ** n_digitos)  
    print(f"{i+1}. Semilla: {semilla} Pseudoaleatorio: {numero_pseudo}")
    semilla = nueva_semilla  
