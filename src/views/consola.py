from src.utils.funcAux import pausar
class UIConsola:
    def __init__(self):
        pass
    def procesoFinalizado(self,proceso):
        print(f'El proceso T{proceso.id} finalizo')
        pausar()

    def abandonoCPU(self,proceso):
        print(f'El proceso T{proceso.id} abandono el CPU')
        pausar()

    def ingresaCPU(self,proceso):
        print(f'El proceso T{proceso.id} ingreso a la CPU')
        pausar()
    
        