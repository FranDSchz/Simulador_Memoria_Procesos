#ver que cosas tengo que importar para que esta vaina funcione
class CTRLProcesador:
    """
    Se encarga de gestionar los algoritmos de planificacion
    """
    def __init__(self,quantum = None):
        self.quantum = quantum
        self.cont = 0
    
    
    def roundRobin(self,cpu,simu, consola):
        if cpu.estaOcupada():
            proceso = cpu.getProcesoActual()
            if proceso.finalizo():
                proceso.tr = simu.getTiempo() 
                consola.procesoFinalizado(proceso) #Implementar en views para mostrar por pantalla que el proceso termino
                cpu.agregarATerminados(proceso)
                cpu.liberarCPU()
                self.cont = 0
                simu.contarMultiPro(-1)
            elif self.quantum == self.cont:
                consola.AbandonoCPU(proceso) #Ver como implemento
                simu.agregarAListos(proceso)
                cpu.liberarCPU()
                self.cont = 0
                simu.contarMultiPro(-1)
            else:
                proceso.ejecutar()
                cpu.setProcesoActual(proceso)
                self.cont += 1
                simu.avanzarUnTiempo()
        else:
            if simu.hayProcesos():
                consola.ingresaCPU() #falta implementar
                proceso = simu.primeroEnLista()
                cpu.setProcesoActual(proceso)
                self.cont = 0
                simu.contarMultiPro()
            else:
                simu.avanzarUnTiempo()
