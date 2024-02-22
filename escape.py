import math 

print("Calculo de Velocidad \n (Recuerda ingresar solo valores numericos, si ingresas letras o caracteres el programa dara error)\n\n ")

radioKm= float(input("Ingrese el radio en Kilometros = "))
gravedad= float(input("Ingrese el valor de la constante g = "))

radiom = radioKm*1000 #Radio Kilometors a Metros

velocidadE = math.sqrt(2*gravedad*radiom)

print(f'La velocidad de Escape es = {velocidadE:.1f} m/s')

