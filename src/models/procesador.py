class Procesador:
    def __init__(self):
        self.terminados = []
        self.procesoActual = None

    def estaOcupada(self):
        return self.procesoActual != None

    def getTerminados(self):
        return self.procesados

    def agregarATerminados(self, proceso):
        self.terminados.append(proceso)

    def getProcesoActual(self):
        return self.procesoActual

    def setProcesoActual(self,proceso):
        self.procesoActual = proceso

    def liberarCPU(self):
        self.procesoActual = None

    def ejecutarProceso(self):
        self.procesoActual.ejecutar()
