import math

print("Calculo de utilidades \n (Recuerda ingresar solo valores numericos, si ingresas letras o caracteres el programa dara error)\n\n ")

#Ingreso por teclado de variables
precio= int(input("Ingrese el Precio de Suscripcion = "))
cant_usuarios = int(input("Ingrese cantidad de Usuarios = "))
gastos= int(input("Ingrese los gastos totales = "))

#Calculo de utilidades
utilidades = (precio*cant_usuarios)-gastos

print(f"Las utilidades son = {math.ceil(utilidades)}")