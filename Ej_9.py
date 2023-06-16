import time

hora = time.time()
horaActual = time.strftime("%H:%M:%S", time.localtime(hora))
hora_format = time.localtime().tm_hour

print('Actualmente son las: ' + str(horaActual))
if hora_format >= 19:
    print('Es hora de ir a casa')

else:
    restante = 19 - hora_format
    print('El tiempo restante de trabajo son: ' + str(restante),' hs')


