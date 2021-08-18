print("EJEMPLO NORMAL ")
mensaje = "Hola"
mensaje +=" "
mensaje += "Charly"
print(mensaje)
print()

print("Ejemplo CONCATENIACIÓN ")
mensaje1 = "Hola"
espacio = " "
nombre = "Charly"
print(mensaje1+espacio+nombre)
print()

print("EJEMPLO CONCATENACION CADENAS Y NUMEROS")
numero_uno = 4 
numero_dos = 2
resultado = numero_uno + numero_dos
resultado= str(resultado)
print("El resulrado de la suma es: " + resultado)
print()

print("EJEMPLO BUSCAR")
mensaje2 = "Hola Charly"
buscar_subcadena = mensaje2 .find("Charly")
print(buscar_subcadena)
print()

print("Ejemplo EXTRACCION")
mensaje3 = "Hola Charly"
extraer_subcadena = mensaje3[1:8]
print(extraer_subcadena)
print()

print("Ejemplo Comparacion")
mensaje4 = "Hola"
mensaje5 = "Hola"
print(mensaje4 == mensaje5)
print()