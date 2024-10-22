class Proceso:
    """
    Representa a los procesos del simulador que se van a ejecutar para la simulacion
    """
    nroInstancias = 0
    def __init__(self, id, ti, taMemoria, tam):
        self.id = id
        self.ti = ti
        self.taMemoria = taMemoria
        self.tam = tam
        self.taListos = None
        self.tr = None
        self.tiempoEjecutado = 0 #Tiempo Ejecutado
        self.partAsig = None #Deberia poner en none cuando termina la ejecucion o da igual?
        Proceso.nroInstancias += 1
    def __str__(self):
        return f'ID: {self.id}\nTI: {self.ti}\nTA: {self.taMemoria}\nTAM: {self.tam}\n'
    def finalizo(self):
        return self.ti == self.tiempoEjecutado
    
    def setTiempoRetorno(self, tiempo):
        self.tr = tiempo
    
    def getTiempoRetorno(self):
        return self.tr
    
    def getTaListos(self):
        return self.taListos
    def setTaListos(self,tiempo):
        self.taListos = tiempo
    
    def getTaMemoria(self):
        return self.taMemoria

    def getTam(self):
        return self.tam
    
    def ejecutar(self):
        self.tiempoEjecutado += 1

    def getPartAsig(self):
        return self.partAsig
    
    def asignar(self,particion):
        self.partAsig = particion
    