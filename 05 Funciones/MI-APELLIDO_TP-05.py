1. Crear una lista con los números del 1 al 100 que sean múltiplos de 4
Python
multiplos_de_4 = [i for i in range(1, 101) if i % 4 == 0]
print(multiplos_de_4)
2. Crear una lista y mostrar el penúltimo elemento
Python
mi_lista = ["manzana", "banana", "naranja", "kiwi", "mango"]
penultimo = mi_lista[-2]
print(penultimo)
3. Crear una lista vacía y agregar palabras
Python
lista_vacia = []
lista_vacia.append("casa")
lista_vacia.append("perro")
lista_vacia.append("gato")
print(lista_vacia)
4. Reemplazar valores en la lista "animales"
Python
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)
6. Crear una lista con números del 10 al 30 con saltos de 5
Python
numeros = list(range(10, 31, 5))
print(numeros[:2])
7. Reemplazar valores centrales en la lista "autos"
Python
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "deportivo"]
print(autos)
8. Crear una lista "dobles" y agregar valores
Python
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
9. Modificar la lista "compras"
Python
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
10. Crear una lista anidada
Python
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
