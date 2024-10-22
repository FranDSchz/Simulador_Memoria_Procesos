class Simulador:
    def __init__(self):
        self.listos = []
        self.suspendidos = []
        self.espera = []
        self.nuevos = []
        self.tiempo = 0
        self.multiPro = 0
    
    def getTiempo(self):
        return self.tiempo
    
    def avanzarUnTiempo(self):
        self.tiempo += 1

    def contarMultiPro(self, n = 1):
        self.multiPro += n
    
    def getMultiPro(self):
        return self.multiPro
    
    def agregarAListos(self,proceso):
        self.listos.append(proceso)

    
    def hayProcesos(self, memoria = False):
        if not memoria:
            return (self.listos != [])
        else:
            return (self.espera != []) or (self.suspendidos != [])
        
    def primeroEnLista(self):
        if self.suspendidos != []:
            result = self.suspendidos[0]
            del self.suspendidos[0]
        else:
            result = self.listos[0]
            del self.listos[0]
        return result
    
    def hayNuevosProcesos(self): #No me gusta el nombre de esta funcion :S
        return self.nuevos != []
    
    def actualizarListas(self):
        self.espera.extend([proceso for proceso in self.nuevos if proceso.taMemoria == self.tiempo])
        self.nuevos = [proceso for proceso in self.nuevos if proceso.taMemoria != self.tiempo]
    
    def getProcesos(self):
        return self.suspendidos + self.espera
    
    def quitarDeLista(self,proceso):
        if proceso in self.suspendidos:
            self.suspendidos.remove(proceso)
        else:
            self.espera.remove(proceso)
