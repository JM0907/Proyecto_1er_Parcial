#Murillo Santos Joseph
#Quizhpi Aviles Aaron
#Cmpoverde Yong Esthela
#Olvera Herrera Shirley
class Material:
    contador_libro = 0
    contador_revista = 0

    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible):
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        self._anio = value

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, value):
        self._editorial = value

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        self._disponible = value

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, value):
        self._cantidad_disponible = value


class Libro(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo_pasta):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id = Material.contador_libro + 1
        self._tipo_pasta = tipo_pasta
        Material.contador_libro += 1

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, value):
        self._tipo_pasta = value

    def get_titulo(self):
        return self._titulo


























class Revista(Material):
    def __init__(self, codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible, tipo):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self.id = Material.contador_revista + 1
        self._tipo = tipo
        Material.contador_revista += 1

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value


class Persona:
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, value):
        self._numero_libros = value

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = value

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, value):
        self._carrera = value

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True

    def __str__(self):
        return f'Persona: [Nombre: {self._nombre} {self._apellido}, Cedula: {self._cedula}]'


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


class Pedido:
    contador_pedido = 0

    def __init__(self, solicitante, lista_material, materia, fecha_prestamo, fecha_devolucion):
        self.id = Pedido.contador_pedido + 1
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._materia = materia
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        Pedido.contador_pedido += 1

    @property
    def solicitante(self):
        return self._solicitante

    @solicitante.setter
    def solicitante(self, value):
        self._solicitante = value

    @property
    def lista_material(self):
        return self._lista_material

    @lista_material.setter
    def lista_material(self, value):
        self._lista_material = value

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, value):
        self._materia = value

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, value):
        self._fecha_prestamo = value

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, value):
        self._fecha_devolucion = value

    def pedir_material(self, list_materia, solicitante, materia):
        self._lista_material = list_materia
        self._solicitante = solicitante
        self._materia = materia

    def devolver_material(self, solicitante):
        self._solicitante = solicitante


# Ejemplo de uso
libro = Libro("123", "Autor", "Título Libro", 2021, "Editorial", True, 5, "Tapa dura")
revista = Revista("456", "Autor", "Título Revista", 2021, "Editorial", False, 3, "Digital")

estudiante = Estudiante("1234567890", "Juan", "Pérez", "juan@example.com", "123456789", "Dirección", 2, True, "Informática", "3er Nivel")
docente = Docente("0987654321", "María", "Gómez", "maria@example.com", "987654321", "Dirección", 3, True, "Matemáticas", "Ph.D.", "M.Sc.")

pedido = Pedido(estudiante, libro, "Programación", "2023-06-11", "2023-06-18")
