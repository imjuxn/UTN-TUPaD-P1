#Ejercicio 1

edad = int(input("Por favor, inregese su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de 18 años")

    # Ejercicio 2

nota = int(input("Ingresa tu nota: "))

if nota >= 6:
    print("Estás aprobado!")
else:
    print("Desaprobaste =(")

# ejercicio 3

numero = int(input("ingrese un número par: "))

if numero % 2 == 0:
    print("Ingresaste un número par")
else:
    print("Debes ingresar un número par")


# Ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres un niño")
elif edad >= 12 and edad < 18:
    print("Eres adolecente")
elif edad >= 18 and edad < 30:
    print("Eres adulto/joven")
elif edad > 30:
    print("Eres adulto")
 
 
#finalgoritmo

    # ejercicio 5

def ingresar_contra():
    contra = input("Ingrese una contraseña (entre 8 a 14 caracteres): ")
    longitud = len(contra)
    if 8 <= longitud <= 14:
        print("contraseña valida")
    else:
        print("conttraseña invalida")
ingresar_contra()

#ejercicio 7

def procesar_string ():

    string_usuario = input("Ingrese una palabra o frase: ")

    vocales = "aeiouAEIOU"

    if string_usuario[-1] in vocales:
        string_resultante = string_usuario + "!"
        print(string_resultante)
    else:
        string_resultante = string_usuario

        print(string_resultante)

procesar_string()

#Ejercicio 8

def main():

    nombre = input("Ingrese su nombre: ")


    print("Ingrese 1 si quieres tu nombre en mayúsucula")
    print("Ingrese 2 si quieres tu nombre en minuscula")
    print("Ingrese 3 si quieres tu nombre con la primera letra en mayúscula")

    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
     print(f"Tu nombre en mayúscula es: {nombre.upper()}")
    elif opcion == "2":
     print(f"Tu nombre en minúscula es: {nombre.lower()}")
    elif opcion == "3":
     print(f"Tu nombre en primer letra es: {nombre.title()}")
main()


#Ejercicio 9

def main():

 magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))

 if magnitud < 3:
    print("Muy leve (imperceptible)")
 elif 3 <= magnitud < 4:
    print("Leve")
 elif 4 <= magnitud < 5:
    print("Moderado")
 elif 5 <= magnitud < 6:
    print("Fuerte")
 elif 6 <= magnitud < 7:
    print("Muy fuerte")
 elif 7 <= magnitud < 8:
    print("Extremo")
main()

#Ejercicio 10

def determinar_estacion(hemisferio, mes, dia):
    # Determinar la estación según el mes y el día
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        if hemisferio == 'N':
            return 'Invierno'
        else:
            return 'Verano'
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        if hemisferio == 'N':
            return 'Primavera'
        else:
            return 'Otoño'
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        if hemisferio == 'N':
            return 'Verano'
        else:
            return 'Invierno'
    else:
        if hemisferio == 'N':
            return 'Otoño'
        else:
            return 'Primavera'

def main():
    hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
    while hemisferio not in ['N', 'S']:
        hemisferio = input("Por favor, ingresa N para hemisferio norte o S para hemisferio sur: ").upper()

    mes = int(input("¿Qué mes es? (1-12): "))
    while mes < 1 or mes > 12:
        mes = int(input("Por favor, ingresa un mes válido (1-12): "))

    dia = int(input("¿Qué día es? (1-31): "))
    while dia < 1 or dia > 31:
        dia = int(input("Por favor, ingresa un día válido (1-31): "))

    # Validación básica para meses con menos de 31 días
    while (mes in [4, 6, 9, 11] and dia > 30) or (mes == 2 and dia > 28):
        dia = int(input("El mes ingresado no tiene tantos días. Por favor, ingresa un día válido: "))

    estacion = determinar_estacion(hemisferio, mes, dia)
    print(f"Te encuentras en {estacion}.")

if __name__ == "__main__":
    main()
