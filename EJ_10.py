import fileinput

archivo = open('archivo1.txt', 'w')
archivo.write("Archivo de configuracion\n")
archivo.close()

archivo = open('archivo1.txt', 'r+')
archivo.readline()
archivo.write('Linea2')

archivo.close()