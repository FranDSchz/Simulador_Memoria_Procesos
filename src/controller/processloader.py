from src.models.proceso import Proceso
from abc import ABC, abstractmethod
from src.utils.constantes import TAM_MAX

class Loader(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def cargarProcesos(self, simu):
        pass

class ConsoleLoader(Loader):

    def cargarProcesos(self, simu):
        n = self.validarEntero("Ingrese la cantidad de procesos que desea cargar (máx 10)\n>> ", 1, 10)

        for i in range(1, n+1):
            print(f"Proceso N°: {i}")
            ti = self.validarEntero('Ingrese el tiempo de irrupción válido (> 0): ', 1, float('inf'))
            taMemoria = self.validarEntero('Ingrese el tiempo de arribo a memoria válido (>= 0): ', 0, float('inf'))
            tam = self.validarEntero(f"Ingrese el tamaño entre > 0 y <= {TAM_MAX} sin la unidad (KB): ", 1, TAM_MAX)
            
            simu.nuevos.append(Proceso(i, ti, taMemoria, tam))

    def validarEntero(self, mensaje, min_val, max_val):
        while True:
            try:
                valor = int(input(mensaje))
                if min_val <= valor <= max_val:
                    return valor
                print(f"Valor inválido. Debe estar entre {min_val} y {max_val}")
            except ValueError:
                print("El valor ingresado no es un número válido. Intente de nuevo.")

class InterfazLoader(Loader):
    def cargarProcesos(self, simu):
        pass  # Implementar cuando sea necesario
