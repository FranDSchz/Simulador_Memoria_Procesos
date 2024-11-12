import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.models.memoria_principal import MemoriaPrincipal
from src.models.particion import Particion
from src.models.proceso import Proceso
from src.models.procesador import Procesador
from src.views.consola import UIConsola
from src.controller.maincontroller import MainController

def main():
    ctrl = MainController()
    mp = MemoriaPrincipal()
    # ver si no hay drama con cargar SO en mp
    so = Proceso('SO',0,0,100)
    mp.particiones = [Particion(0,100,so),Particion(1,250),Particion(2,150),Particion(3,50)]
    cpu = Procesador()
    consola = UIConsola()
    consola.mensaje_inicial()
    ctrl.iniciar(cpu,mp,consola)
        
if __name__ == "__main__":
    main()