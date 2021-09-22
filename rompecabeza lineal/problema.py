from acciones import AccionesRompecabezaLineal

class ProblemaRompecabezaLineal:
    def __init__(self, inicial) -> None:
        self.estadoInicial = inicial
        self.estadoObjetivo = [1,2,3,4]
        
        # self.acciones = AccionesRompecabezaLineal()
        
        self.acciones = []
        self.acciones.append({"nombre": 'II', "funcion": AccionesRompecabezaLineal().intercambiarIzquierda})
        self.acciones.append({"nombre": 'IC', "funcion": AccionesRompecabezaLineal().intercambiarCentro})
        self.acciones.append({"nombre": 'ID', "funcion": AccionesRompecabezaLineal().intercambiarDerecha})

        # OPERADOR

    def funcion_objetivo(self, estado):
        return estado == self.estadoObjetivo
    
    def funcion_info_adicional(self, estado):
        return []