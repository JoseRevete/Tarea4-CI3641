import sys
from io import StringIO
from ManejadorTablas import ManejadorClases

def simulate_input(inputs):
    """Simula la entrada estándar para probar ClassManager."""
    original_stdin = sys.stdin
    try:
        sys.stdin = StringIO(inputs)
        manager = ManejadorClases()
        manager.ejecutar()
    finally:
        sys.stdin = original_stdin

if __name__ == "__main__":
    # Entradas de prueba
    inputs = """\
CLASS
CLASS A f g
CLASS A
CLASS F : C
CLASS B : A f h
DESCRIBIR B
DESCRIBIR A
CLASS C : B h i
DESCRIBIR C
CLASS D : C h i
DESCRIBIR D
CLASS E : D j
SALIR
"""
    print("Simulación de entrada:")
    simulate_input(inputs)
