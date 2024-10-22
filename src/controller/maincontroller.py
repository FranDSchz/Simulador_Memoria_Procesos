from src.controller.simulador import Simulador
from src.controller.memoria import CTRLMemoria
from src.controller.procesador import CTRLProcesador
from src.controller.processloader import ConsoleLoader
class MainController:
    def __init__(self):
        self.simulador = Simulador()
        self.ctrlMem = CTRLMemoria()
        self.crtlProc = CTRLProcesador(3)
        self.loader = ConsoleLoader('Console')
    
    def cargarProcesos(self):
        self.loader.cargarProcesos(self.simulador)
