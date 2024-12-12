from abc import ABC, abstractmethod

# Clase abstracta Secuencia
class Secuencia(ABC):
    def __init__(self):
        self.secuencia = []

    # Método abstracto para agregar un elemento a la secuencia
    @abstractmethod
    def agregar(self, elemento):
        pass

    # Método abstracto para remover un elemento de la secuencia
    @abstractmethod
    def remover(self):
        pass

    # Método para verificar si la secuencia está vacía
    def vacio(self):
        return len(self.secuencia) == 0
    
# Clase Cola para representar una cola
class Cola(Secuencia):
    def agregar(self, elemento):
        self.secuencia.append(elemento)
    
    def remover(self):
        if self.vacio():
            raise IndexError("La cola está vacía")
        return self.secuencia.pop(0)


# Clase Pila para representar una pila
class Pila(Secuencia):
    def agregar(self, elemento):
        self.secuencia.append(elemento)
    
    def remover(self):
        if self.vacio():
            raise IndexError("La pila está vacía")
        return self.secuencia.pop()



# Pruebas de las clases
def main():
    cola = Cola()
    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)
    print(cola.remover())
    print(cola.remover())
    print(cola.vacio())
    print(cola.remover())
    print(cola.vacio())
    
    pila = Pila()
    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)
    print(pila.remover())
    print(pila.remover())
    print(pila.vacio())
    print(pila.remover())
    print(pila.vacio())


if __name__ == "__main__":
    main()