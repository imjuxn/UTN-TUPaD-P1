import math

# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return suma, resta, multiplicacion, division

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# Programa principal
if __name__ == "__main__":
    # Punto 1
    imprimir_hola_mundo()

    # Punto 2
    nombre = input("\nIngresá tu nombre: ")
    print(saludar_usuario(nombre))

    # Punto 3
    nombre = input("\nNombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # Punto 4
    radio = float(input("\nIngresá el radio de un círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    # Punto 5
    segundos = int(input("\nIngresá cantidad de segundos: "))
    print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")

    # Punto 6
    numero = int(input("\nIngresá un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # Punto 7
    a = float(input("\nPrimer número: "))
    b = float(input("Segundo número: "))
    suma, resta, multi, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multi}")
    print(f"División: {div}")

    # Punto 8
    peso = float(input("\nIngresá tu peso en kg: "))
    altura = float(input("Ingresá tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")

    # Punto 9
    celsius = float(input("\nTemperatura en °C: "))
    print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f} °F")

    # Punto 10
    n1 = float(input("\nNúmero 1: "))
    n2 = float(input("Número 2: "))
    n3 = float(input("Número 3: "))
    print(f"El promedio es: {calcular_promedio(n1, n2, n3):.2f}")
