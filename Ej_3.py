bienvenida = "PROGRAMA PARA CALCULAR EL IMC\n"
ingreso = "Ingrese el peso(kg)"
ingreso2 = "Ingrese la estatura(m)"

print(bienvenida)
print(ingreso)

peso = int(input())
print(ingreso2)
estatura = float(input())

IMC = peso/pow(estatura, 2)

print("Tu índice de masa corporal es:"  + format(IMC, ".2f"))

