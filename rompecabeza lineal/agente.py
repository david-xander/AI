from problema import ProblemaRompecabezaLineal
from busqueda import AlgoritmoBusquedaBFS

class Agente:
    def __init__(self) -> None:
        pass

    def solucion_problema_rompecabeza_lineal(self, estado_inicial):
        busqueda = AlgoritmoBusquedaBFS( ProblemaRompecabezaLineal(estado_inicial) ).buscar()
        return busqueda

if __name__ == '__main__':
    agente = Agente()
    res = agente.solucion_problema_rompecabeza_lineal([2,4,1,3])    
    print(res)
    
