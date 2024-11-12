#ver que cosas tengo que importar para que esta vaina funcione
from src.utils.funcAux import pausar
from time import sleep

class CTRLProcesador:
    """
    Se encarga de gestionar los algoritmos de planificacion
    """
    def __init__(self,quantum = None):
        self.quantum = quantum
        self.cont = 0
    
    
    def roundRobin(self,cpu,simu, consola,mp, nroInstancias):
        #x = input(f'simu.tiempo INICIO:{simu.tiempo}')
        #x = input(f'cpu.estaOcupada: {cpu.estaOcupada()}')
        
        if cpu.estaOcupada():
            proceso = cpu.getProcesoActual()
            #x = input(f'proceso: {cpu.getProcesoActual()}')
            #x = input(f'proceso.finalizo(): {proceso.finalizo()}')
            #x = input(f'self.quantum == self.cont {self.quantum == self.cont}')
            if proceso.finalizo():
                #x = input(f'simu.getTiempo():{simu.getTiempo()}')
                proceso.tr = simu.getTiempo() 
                
                #x = input(f'cpu.terminados antes de add:{cpu.terminados}')
                cpu.agregarATerminados(proceso)
                proceso.partAsig.proAsig = None #Ver como implemento mejor esto---------------------------------------------------
                #x = input(f'cpu.terminados [post] add:{cpu.terminados}')
                #x = input(f'cpu.procesoActual antes liberar:{cpu.procesoActual}')
                cpu.liberarCPU()
                #x = input(f'cpu.procesoActual post liberar:{cpu.procesoActual}')
                self.cont = 0
                #x = input(f'multiprogramacion antes desc:{simu.multiPro}')
                simu.contarMultiPro(-1)
                #x = input(f'multiprogramacion post desc:{simu.multiPro}')
                if consola != None:
                    consola.procesoFinalizado(proceso) #Implementar en views para mostrar por pantalla que el proceso termino
                    sleep(1)
                if len(cpu.terminados) == (nroInstancias) and consola != None:
                    consola.show_status(cpu.getProcesoActual(), self.getQuantum_rest(), simu.getTiempo(), mp.particiones, simu.listos)
                    pausar()
            elif self.quantum == self.cont:
                #x = input(f'simu.listos antes de add:{simu.listos}')
                simu.agregarAListos(proceso)
                #x = input(f'simu.listos post  add:{simu.listos}')
                #x = input(f'cpu.procesoActual antes liberar:{cpu.procesoActual}')
                cpu.liberarCPU()
                #x = input(f'cpu.procesoActual post liberar:{cpu.procesoActual}')
                self.cont = 0
                simu.contarMultiPro(-1)
                if consola != None:
                    consola.proceso_abandona_cpu(proceso) #Ver como implemento
                    sleep(1)
                    consola.proceso_ingresa_cola_listos(proceso)
                    sleep(1)
                #pausar()
            else:
                #x = input(f'cpu.procesoActual.tiempoEjecutado antes ejecutar():{cpu.procesoActual.tiempoEjecutado}')
                proceso.ejecutar()
                #x = input(f'cpu.procesoActual.tiempoEjecutado post ejecutar():{cpu.procesoActual.tiempoEjecutado}')
                #cpu.setProcesoActual(proceso) ver si funciona lo de la referencia automatica
                self.cont += 1
                #x = input(f'simu.tiempo antes avz {simu.tiempo}')
                simu.avanzarUnTiempo()
                #x = input(f'simu.tiempo antes avz {simu.tiempo}')
        else:
            #x = input(f'simu.hayProcesos() {simu.hayProcesos()}')
            if simu.hayProcesos():
                #x = input(f'simu.listos[0] = \n{simu.listos[0]}')
                #x = input(f'simu.listos antes de simu.primeroEnLista() \n{simu.listos}')
                proceso = simu.primeroEnLista()
                #x = input(f'simu.listos post simu.primeroEnLista() \n{simu.listos}')
                #x = input(f'proceso asignado = \n{proceso}')
                #x = input(f'cpu.procesoActual antes {cpu.procesoActual}')
                cpu.setProcesoActual(proceso)
                #x = input(f'cpu.procesoActual post {cpu.procesoActual}')
                self.cont = 0 #Esto se inicializa con el constructor, capaz no sea necesario o si?
                if consola != None:
                    consola.proceso_ingresa_cpu(proceso)
                    sleep(1)
                    consola.show_status(cpu.getProcesoActual(), self.getQuantum_rest(), simu.getTiempo(), mp.particiones, simu.listos)
                    pausar()

            else:
                #x = input(f'simu.tiempo antes avz {simu.tiempo}')
                simu.avanzarUnTiempo()
                #x = input(f'simu.tiempo antes avz {simu.tiempo}')
    def getQuantum_rest(self):
        return self.quantum - self.cont