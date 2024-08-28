class Persona:
    def __init__(self, matricula, dni, nombreApellido, direccion):
        self.matricula = matricula
        self.dni = dni
        self.nombreApellido = nombreApellido
        self.direccion = direccion

    def __str__(self):
        return f"Matricula: {self.matricula}, DNI: {self.dni}, Nombre: {self.nombreApellido}, Direccion: {self.direccion}"


class Estudiante(Persona):
    def __init__(self, matricula, dni, nombreApellido, direccion, anioCurso, materias):
        super().__init__(matricula, dni, nombreApellido, direccion)
        self.anioCurso = anioCurso
        self.materias = materias

    def __str__(self):
        materias_str = ", ".join(self.materias)
        return (super().__str__() + f", Año de Curso: {self.anioCurso}, Materias: {materias_str}")


class Docente(Persona):
    def __init__(self, matricula, dni, nombreApellido, direccion, cursosAcargo):
        super().__init__(matricula, dni, nombreApellido, direccion)
        self.cursosAcargo = cursosAcargo

    def __str__(self):
        cursos_str = ", ".join(self.cursosAcargo)
        return (super().__str__() + f", Cursos a Cargo: {cursos_str}")

# Ejemplo de uso
def main():
    estudiante1 = Estudiante(
        matricula="03948",
        dni="49.767.743",
        nombreApellido="paula gomez",
        direccion="barrio la banda 431 ",
        anioCurso=2,
        materias=["Matemáticas", "Historia", "Ciencias"]
    )

    docente1 = Docente(
        matricula="65421",
        dni="37.614.821",
        nombreApellido="micaela velez",
        direccion="moreno y seanz peña 132",
        cursosAcargo=["Matemáticas", "Física"]
    )

    print(estudiante1)
    print(docente1)

if __name__ == "__main__":
    main()
