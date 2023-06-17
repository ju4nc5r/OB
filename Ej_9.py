import time

hora = time.time()
horaActual = time.strftime("%H:%M:%S", time.localtime(hora))
minutos = time.strftime('%M')
hora_format = time.localtime().tm_hour
#hora_format = 9
print('Actualmente son las: ' + str(horaActual))
if hora_format >= 19:
    print('Es hora de ir a casa')

else:
    restante = 19 - hora_format
    print('El tiempo de trabajo restante son:',str(restante),':',str(minutos))


