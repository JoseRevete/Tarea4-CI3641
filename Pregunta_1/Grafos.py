from abc import ABC, abstractmethod
from collections import deque

# Clase Grafo para representar un grafo
class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.lista_adyacencia = [[] for _ in range(num_nodos)]

    # Método para agregar una arista entre dos nodos
    def agregar_arista(self, nodo1, nodo2):
        self.lista_adyacencia[nodo1].append(nodo2)
        self.lista_adyacencia[nodo2].append(nodo1)
    

# Clase abstracta Busqueda
class Busqueda(ABC):
    def __init__(self, grafo):
        self.grafo = grafo

    # Método abstracto para buscar un camino entre dos nodos
    @abstractmethod
    def buscar(self, D, H):
        pass

# Clase DFS para realizar una búsqueda en profundidad
class DFS(Busqueda):
    def buscar(self, D, H):
        visitados = set()
        stack = [D]
        while stack:
            nodo = stack.pop()
            if nodo not in visitados:
                visitados.add(nodo)
                if nodo == H:
                    return len(visitados) -1
                for vecino in reversed(self.grafo.lista_adyacencia[nodo]):
                    if vecino not in visitados:
                        stack.append(vecino)
        return -1
    

# Clase BFS para realizar una búsqueda en amplitud
class BFS(Busqueda):
    def buscar(self, D, H):
        visitados = set()
        queue = deque([D])
        while queue:
            nodo = queue.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                if nodo == H:
                    return len(visitados) -1
                vecinos = self.grafo.lista_adyacencia[nodo]
                for vecino in vecinos:
                    if vecino not in visitados:
                        queue.append(vecino)
        return -1
    
# Pruebas de las clases
def main():
    grafo = Grafo(6)
    grafo.agregar_arista(0, 1)
    grafo.agregar_arista(0, 2)
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(1, 4)
    grafo.agregar_arista(2, 5)
    
    dfs = DFS(grafo)
    print(dfs.buscar(0, 5))
    
    bfs = BFS(grafo)
    print(bfs.buscar(0, 5))

if __name__ == "__main__":
    main()