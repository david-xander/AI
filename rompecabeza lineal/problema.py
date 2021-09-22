from acciones import AccionesRompecabezaLineal

class ProblemaRompecabezaLineal:
    def __init__(self, inicial) -> None:
        self.estadoInicial = inicial
        self.estadoObjetivo = [1,2,3,4]
        
        self.acciones = AccionesRompecabezaLineal()
        
        self.operadores = []
        self.operadores.append(self.acciones.intercambiarIzquierda)
        self.operadores.append(self.acciones.intercambiarCentro)
        self.operadores.append(self.acciones.intercambiarDerecha)

    def funcion_objetivo(self, estado):
        return estado == self.estadoObjetivo
    
    def funcion_info_adicional(self, estado):
        return []