import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.controller.maincontroller import MainController

def main():
    ctrl = MainController()
    ctrl.cargarProcesos()
    for i in ctrl.simulador.nuevos:
        print(i)
if __name__ == "__main__":
    main()