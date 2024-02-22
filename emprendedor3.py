import math

print("Calculo de utilidades \n (Recuerda ingresar solo valores numericos, si ingresas letras o caracteres el programa dara error)\n\n ")

#Ingreso por teclado de variables
precio = int(input("Ingrese el Precio de Suscripcion = "))
cant_usuarios = int(input("Ingrese cantidad de Usuarios = "))
gastos = int(input("Ingrese los gastos totales = "))
utilidades_ant = int(input("Ingrese las utilidades del año anterior = "))

#Calculo de utilidades
utilidades_act = (precio*cant_usuarios)-gastos

print(f"La razon entre la utilidad actual y la utilidad anterior es = {(utilidades_act/utilidades_ant):.2f}")
