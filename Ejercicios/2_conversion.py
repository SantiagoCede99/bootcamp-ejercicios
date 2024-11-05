print("[1] Fareheit a Celcius")
print("[2] Celcius a Farenheit")

escala = int(input("Ingrese escala deseada [1] o [2]: "))


if escala==1:
    val= float(input("Ingrese valor a convertir: "))
    conv=(val-32)*(5/9)
    print(round(conv,2), "°C")
elif escala==2:
    val= float(input("Ingrese valor a convertir: "))
    conv=((val*(9/5))+32)
    print(round(conv,2), "°F")
else:
    print("Comando desconocido")
