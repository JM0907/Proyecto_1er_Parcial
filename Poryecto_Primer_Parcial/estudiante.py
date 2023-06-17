#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley
from persona import Persona
class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id = Estudiante.contador_estudiante + 1
        self._nivel = nivel
        Estudiante.contador_estudiante += 1

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value):
        self._nivel = value