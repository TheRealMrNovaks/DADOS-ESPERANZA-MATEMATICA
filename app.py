import random
import time

datos = []
repeticion = int(input("- "))

print("Generando números...")
inicio = time.perf_counter()
for i in range(repeticion):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    suma = num1+num2
    datos.append(suma)
    if i == repeticion/2:
        print("Mitad de los números generados...")
fin = time.perf_counter()

print("Resultados: ")
numero = 2
while True:
    if numero == 13:
        break
    contador = datos.count(numero)
    print(f" {numero}: {contador} ({(contador/repeticion)*100}%)")
    numero += 1
tiempo = fin-inicio
print(f"Tiempo transcurrido en la generación de los datos: {tiempo:.6f} segundos")