from problema import ProblemaRompecabezaLineal
from busqueda import AlgoritmoBusquedaBFS

class Agente:
    def __init__(self) -> None:
        pass

    def solucion_problema_rompecabeza_lineal(self):
        estado_inicial = [2,4,1,3]
        busqueda = AlgoritmoBusquedaBFS( ProblemaRompecabezaLineal(estado_inicial) )


if __name__ == '__main__':
    pass
    
