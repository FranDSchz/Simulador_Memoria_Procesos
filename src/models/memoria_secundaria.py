#Ver si borramos esta clase... Se implementa esta logica en simulador.py
class MemoriaSecundaria:
    def __init__(self):
        self.Suspendidos = []
    
    def haySuspendidos(self):
        return self.Suspendidos != []
    
    def getSuspendidos(self):
        return self.Suspendidos
    
    def devolverPrimero(self):
        try:
            return self.Suspendidos[0]
        except:
            print('error')
            return False
    
    def eliminarProceso(self,x):
        try:
            del self.Suspendidos[x]
        except:
            try:
                self.Suspendidos.remove(x)
            except: 
                print('Error')
    
    def agregarProceso(self,x):
        self.Suspendidos.append(x)
