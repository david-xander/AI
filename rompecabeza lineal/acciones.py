class AccionesRompecabezaLineal:

    @staticmethod
    def intercambiarIzquierda(estado):
        input = estado
        return [input[1], input[0], input[2], input[3]]

    @staticmethod
    def intercambiarCentro(estado):
        input = estado
        return [input[0], input[2], input[1], input[3]]

    @staticmethod
    def intercambiarDerecha(estado):
        input = estado
        return [input[0], input[1], input[3], input[2]]

