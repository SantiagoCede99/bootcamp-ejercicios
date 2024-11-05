"""
Crear una funcion que pida al usuario 2 notas y devuelva la mayor de ellas.
"""

def nota_Mayor():
   a=float(input("Ingrese nota 1: "))
   b=float(input("Ingrese nota 2: "))
   if a>b:
      return(a)
   else:
      return(b)

print("La nota mayor es: ", nota_Mayor())
