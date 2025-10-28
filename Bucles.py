# Ejemplos de for

nombres = ["Maria", "Carlos", "Barbara", "Luis"]

cantidadNombres = len(nombres)
print(cantidadNombres)

""" for nombre in nombres:
    print("El nombres es", nombre) """

for numero in range(7):
    print(numero)

# Ejemplo while

count =  0

while(count < 10):
    count += 1
    if count == 5:
        # break
        continue
    print(count)