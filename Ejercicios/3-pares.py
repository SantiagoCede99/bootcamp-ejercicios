"""
Imprimir los primeros 100 numeros pares
"""
n=int(input("Escriba un número: "))
n=(n+1)*2

i=0

for i in range (2,n,2):
    print(i)
