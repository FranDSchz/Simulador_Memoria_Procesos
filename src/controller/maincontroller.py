from src.controller.simulador import Simulador
from src.controller.memoria import CTRLMemoria
from src.controller.procesador import CTRLProcesador
from src.controller.processloader import ConsoleLoader
from src.models.proceso import Proceso
class MainController:
    def __init__(self):
        self.simulador = Simulador()
        self.ctrlMem = CTRLMemoria()
        self.crtlProc = CTRLProcesador(3)
        self.loader = ConsoleLoader('Console')
    
    def cargarProcesos(self):
        self.loader.cargarProcesos(self.simulador)
    
    def ejecutar(self, cpu, mp, consola):
        while len(cpu.terminados) < Proceso.nroInstancias:
            #print('terminados',len(cpu.terminados))
            #print('procesos',Proceso.nroInstancias)
            #print()
            #x = input()
            self.ctrlMem.gestionarMemoria(self.simulador, mp)
            self.crtlProc.roundRobin(cpu, self.simulador, consola)