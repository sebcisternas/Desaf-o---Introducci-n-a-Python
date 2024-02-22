import math

print("Calculo de utilidades\n(Recuerda ingresar solo valores numericos, si ingresas letras o caracteres el programa dara error)\n\n ")

#Ingreso por teclado de variables
precio= int(input("Ingrese el Precio de Suscripcion = "))
cant_usuarios = int(input("Ingrese cantidad de Usuarios Normales = "))
cant_usuariosPrem = int(input("Ingrese cantidad de Usuarios Premium = "))
gastos= int(input("Ingrese los gastos totales = "))

#Calculo de utilidades con el precio de usuarios normales y usuarios premium
utilidades = (precio*cant_usuarios)+(1.5*precio*cant_usuariosPrem)-gastos

print(f"Las utilidades son = ${math.ceil(utilidades)}")