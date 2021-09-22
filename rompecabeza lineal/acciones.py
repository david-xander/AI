class AccionesRompecabezaLineal:

    @staticmethod
    def intercambiarIzquierda(input) -> list:
        return [input[1], input[0], input[2], input[3]]

    @staticmethod
    def intercambiarCentro(input) -> list:
        return [input[0], input[2], input[1], input[3]]

    @staticmethod
    def intercambiarDerecha(input) -> list:
        return [input[0], input[1], input[3], input[2]]

