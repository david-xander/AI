import uuid

class Nodo:
    def __init__(self, estado, padre=None, accion=None) -> None:
        self.identificador = uuid.uuid4()
        self.estado = estado
        self.padre = padre
        if accion == None:
            self.accion = {"nombre": None, "accion": None}
        else: self.accion = accion

class Queue:
    def __init__(self) -> None:
        self.nodes = []
    
    def enqueue(self, item) -> None:
        self.nodes.insert(0, item)

    def dequeue(self) -> list:
        return self.nodes.pop()
    
    def size(self) -> int:
        return len(self.nodes)
    

class AlgoritmoBusquedaBFS:
    def __init__(self, problema) -> None:
        self.problema = problema
        self.nodos = Queue() # porque es LIFO
        self.nodos.enqueue( Nodo(self.problema.estadoInicial) )

    def buscar(self):
        # se supone que el estado inicial no debería ser el estado objetivo

        nodo_padre = self.nodos.dequeue()
        if nodo_padre.estado == []:
            return []
        
        for accion in self.problema.acciones:
            estado_nuevo = accion["funcion"](nodo_padre.estado)
            nodo = Nodo(estado_nuevo, nodo_padre, accion)
            self.nodos.enqueue( nodo )

            if self.problema.funcion_objetivo( estado_nuevo ):
                return self.trace_nodo(nodo)

        return self.buscar()
    
    def trace_nodo(self, nodo) -> str:
        res = ""
        while not nodo.padre == None:
            res += nodo.accion["nombre"]+" "+str(nodo.estado)
        return res