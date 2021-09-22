class AccionesRompecabezaLineal:
    def __init__(self, estado) -> None:
        self.estado = estado

    def intercambiarIzquierda(self):
        input = self.estado
        return [input[1], input[0], input[2], input[3]]

    def intercambiarCentro(self):
        input = self.estado
        return [input[0], input[2], input[1], input[3]]

    def intercambiarDerecha(self):
        input = self.estado
        return [input[0], input[1], input[3], input[2]]

