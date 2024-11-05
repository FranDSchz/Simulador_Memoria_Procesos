from src.controller.simulador import Simulador
from src.controller.memoria import CTRLMemoria
from src.controller.procesador import CTRLProcesador
from src.controller.processloader import ConsoleLoader
from src.models.proceso import Proceso
from os import system
from time import sleep
class MainController:
    def __init__(self):
        self.simulador = Simulador()
        self.ctrlMem = CTRLMemoria()
        self.crtlProc = CTRLProcesador(3)
        self.loader = ConsoleLoader('Console')
    
    def cargarProcesos(self):
        self.loader.cargarProcesos(self.simulador)
    
    def ejecutar(self, cpu, mp, consola):
        resg = -1
        while len(cpu.terminados) < (Proceso.nroInstancias-1):
            if self.simulador.getTiempo() != resg:
                sleep(1)
                system("cls")

                consola.mostrar_tiempo_actual(self.simulador.getTiempo())
                consola.mostrar_estado_procesador(cpu.getProcesoActual(),self.crtlProc.getQuantum_rest())
                resg = self.simulador.getTiempo()
            #print('procesos',Proceso.nroInstancias)
            #print()
            #x = input()
            self.ctrlMem.gestionarMemoria(self.simulador, mp, consola, self.crtlProc.getQuantum_rest(),cpu.getProcesoActual())
            self.crtlProc.roundRobin(cpu, self.simulador, consola,mp,Proceso.nroInstancias-1)
            print("ESTADISTICAS")
            
            