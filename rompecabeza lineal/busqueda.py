import uuid

class Nodo:
    def __init__(self, estado, padre=None, accion=None) -> None:
        self.identificador = uuid.uuid4()
        self.estado = estado
        self.padre = padre
        if accion == None:
            self.accion = {"nombre": None, "accion": None}

class Queue:
    def __init__(self) -> None:
        self.nodes = []
    
    def enqueue(self, item) -> None:
        self.nodes.insert(0, item)

    def dequeue(self) -> list:
        return self.nodes.pop()
    

class AlgoritmoBusquedaBFS:
    def __init__(self, problema) -> None:
        self.problema = problema
        self.nodos = Queue() # porque es LIFO
        self.nodos.enqueue( Nodo(self.problema.estadoInicial) )

    def buscar(self):
        # se supone que el estado inicial no debería ser el estado objetivo

        estado = self.nodos.dequeue()
        if estado == []:
            return None
        
        for accion in self.problema.acciones:
            estado_nuevo = accion.funcion(estado)
            padre = estado
            accion = accion
            nodo = Nodo(estado_nuevo, padre, accion)

            if self.problema.funcion_objetivo( estado_nuevo ):
                return nodo
            else:
                self.nodos.enqueue( nodo )

        return self.buscar()