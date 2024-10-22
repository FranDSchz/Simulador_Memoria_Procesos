class Particion:
    """
    Representa a una particion de la Memoria Principal
    Parametros Obligatorios (id,tam)
    """
    tamUltPart = 0
    def __init__(self,id,tam, proAsig = None):
        self.id = id
        self.tam = tam
        self.proAsig = proAsig
        self.dir_inicio = self.tamUltPart
        self.dir_fin = self.tamUltPart + tam
        Particion.tamUltPart = self.dir_fin
    
    def __str__(self):
        return f'ID: {self.id}\nTAM: {self.tam} KB\nPROCESO ASIGNADO: {self.proAsig}\nDIRECCION DE INICIO: {self.dir_inicio} KB\nDIRECCION DE FIN: {self.dir_fin} KB\n'
    
    def fragInterna(self):
        try:
            return self.tam - self.proAsig.getTam()
        except:
            return 0
    
    def estaLibre(self):
        return self.proAsig == None
    
    def liberarParticion(self):
        self.proAsig = None

    def asignar(self, proceso):
        self.proAsig = proceso
    
    def getId(self):
        return self.id
    
    def getTam(self):
        return self.tam
    
    def getProAsig(self):
        return self.proAsig
    
    def getDirInicio(self):
        return self.dir_inicio
    
    def getDirFin(self):
        return self.dir_fin
    
    