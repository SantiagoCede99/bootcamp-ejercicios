#Ejercicios
"""
1.Crear un ejercicio que me permita saber si una persona es mayor de edad.
"""

edad=int(input("Ingrese su edad: "))

print("Es mayor de edad." * (edad>=18) + "Es menor de edad." * (edad<18))
