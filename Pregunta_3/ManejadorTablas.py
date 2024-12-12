# Clase que maneja las tablas de clases y métodos
class ManejadorClases:
    def __init__(self):
        self.clases = {}

    # Método para agregar una clase al manejador
    def agregar_clase(self, definicion_clase):
        partes = definicion_clase.split()
        if len(partes) < 2:
            print("Error: Definición de clase inválida")
            return

        nombre_clase = partes[1]
        if nombre_clase in self.clases:
            print("Error: La clase ya existe")
            return

        if ':' in definicion_clase:
            nombre_clase, super_clase = partes[1], partes[3]
            if super_clase not in self.clases:
                print("Error: La superclase no existe")
                return
            metodos = partes[4:]
        else:
            metodos = partes[2:]

        if len(metodos) != len(set(metodos)):
            print("Error: Métodos duplicados")
            return

        self.clases[nombre_clase] = {
            'metodos': {metodo: nombre_clase for metodo in metodos},
            'super': super_clase if ':' in definicion_clase else None
        }

        if self.detectar_ciclo(nombre_clase):
            del self.clases[nombre_clase]
            print("Error: Ciclo en la jerarquía de clases")
            return

    # Método para describir una clase
    def describir_clase(self, nombre_clase):
        if nombre_clase not in self.clases:
            print("Error: La clase no existe")
            return

        metodos = self.obtener_metodos(nombre_clase)
        for metodo, origen in metodos.items():
            print(f"{metodo} -> {origen} :: {metodo}")

    # Método para obtener los métodos de una clase
    def obtener_metodos(self, nombre_clase):
        metodos = {}
        clase_actual = nombre_clase
        while clase_actual:
            metodos.update(self.clases[clase_actual]['metodos'])
            clase_actual = self.clases[clase_actual]['super']
        return metodos

    # Método para detectar ciclos en la jerarquía de clases
    def detectar_ciclo(self, nombre_clase):
        visitados = set()
        clase_actual = nombre_clase
        while clase_actual:
            if clase_actual in visitados:
                return True
            visitados.add(clase_actual)
            clase_actual = self.clases[clase_actual]['super']
        return False

    # Método para ejecutar el manejador
    def ejecutar(self):
        while True:
            accion = input("$> ")
            if accion.startswith("CLASS"):
                self.agregar_clase(accion)
            elif accion.startswith("DESCRIBIR"):
                _, nombre_clase = accion.split()
                self.describir_clase(nombre_clase)
            elif accion == "SALIR":
                break
            else:
                print("Error: Acción inválida")

# Método principal
if __name__ == "__main__":
    manejador = ManejadorClases()
    manejador.ejecutar()