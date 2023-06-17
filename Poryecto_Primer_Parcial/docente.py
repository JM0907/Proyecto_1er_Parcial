#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley

from persona import Persona
class Docente(Persona):
    contador_docente = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera,
                 titulo_3er_nivel, titulo_4to_nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id = Docente.contador_docente + 1
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        Docente.contador_docente += 1

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, value):
        self._titulo_3er_nivel = value

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, value):
        self._titulo_4to_nivel = value
