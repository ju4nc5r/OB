print('PROGRAMA PARA SABER SI UN AÑO ES BISIESTO')
bienvenida = 'Ingrese el año que quiere consultar'
print(bienvenida)
año = int(input())

if año % 4 == 0:
    print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')

