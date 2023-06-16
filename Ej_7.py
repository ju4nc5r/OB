class Alumno:

     def ingresoNombre(self):
         nombre = input('Ingrese su nombre:\n')
         print(nombre)

     def ingresoNota(self):
        self.nota = int(input('Ingrese su nota:\n'))
        print(self.nota)

     def resultado(self):
         if self.nota > 7:
            print('Aprobado')
         else:
             print('Desaprobado')

Alumno = Alumno()

Alumno.ingresoNombre()
Alumno.ingresoNota()
Alumno.resultado()

