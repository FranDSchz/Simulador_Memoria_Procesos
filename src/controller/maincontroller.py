from src.controller.simulador import Simulador
from src.controller.memoria import CTRLMemoria
from src.controller.procesador import CTRLProcesador
from src.controller.processloader import InterfazLoader
from src.models.proceso import Proceso
from os import system
from time import sleep
from rich.prompt import Prompt

class MainController:
    def __init__(self):
        self.simulador = Simulador()
        self.ctrlMem = CTRLMemoria()
        self.crtlProc = CTRLProcesador(3)
        self.loader = InterfazLoader('UI')
    
    def cargarProcesos(self):
        opcion = self.loader.cargarProcesos(self.simulador)
        return opcion
    def ejecutarSimulador(self, cpu, mp, consola = None):
        resg = -1
        self.simulador.resetearDatos()
        cpu.resetearDatos()
        while (len(cpu.terminados) + len(self.simulador.noEjecutados)) < (Proceso.nroInstancias-1):
            if self.simulador.getTiempo() != resg and consola != None:
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
    
    def obtenerStats(self):
        print("en construccion")

    def abandonarSimulador(self, consola):
        consola.mensajeDespedida()
        sleep(2)

    def iniciar(self, cpu,mp,consola):
        opcion = ""
        mostrarMenu = True
        flag =  False
        while opcion.upper() != "S":
            if mostrarMenu:
                consola.menuPrincipal()
                opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4", "5","S", "s"])
                mostrarMenu = False

            if str(opcion) == "1":
                system("cls")
                flag =  True #Ver si esta bien en esta posicion por que puede ser que no se cargan los arhivos por mas que se llame a cargarProcesos()
                opcion = self.cargarProcesos()
                if opcion == "1":
                    mostrarMenu = True
            elif str(opcion) == "2":
                system("cls")
                #print(self.simulador.nuevos)
                if self.simulador.nuevos != []:
                    flag =  False
                    self.ejecutarSimulador(cpu, mp, consola)
                    print("Simulacion finalizada")
                    print("[1] MENU| [2] VER ESTADISTICAS | [S] SALIR ")
                    opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "S", "s"])
                    if opcion == "1":
                        mostrarMenu = True
                    elif opcion == "2":
                        opcion = "4"
                else:
                    print("No se cargaron procesos para iniciar la simulacion o ya fueron ejecutados")
                    mostrarMenu = True
            elif str(opcion) == "3":
                pass
            elif str(opcion) == "4":
                system("cls")
                #tengo que ver como ejecutar el algoritmo sin impresiones
                if flag:
                    self.ejecutarSimulador(cpu, mp)
                    flag =  False
                if cpu.terminados != []:
                    acu_retorno = 0
                    acu_espera = 0
                    cant_ejecutados = len(cpu.terminados)
                    print("------- ESTADISTICAS --------")
                    for proceso in cpu.terminados:
                        tiempo_retorno = proceso.tr - proceso.taMemoria
                        tiempo_espera = tiempo_retorno - proceso.ti
                        acu_retorno += tiempo_retorno
                        acu_espera += tiempo_espera
                        print(f'Proceso ID: {proceso.id}')
                        print(f'Tiempo de Retorno: {tiempo_retorno}')
                        print(f'Tiempo de Espera: {tiempo_espera}')
                        print("_"*50)
                    print(f"Tiempo de retorno promedio: {acu_retorno/cant_ejecutados}")
                    print(f"Tiempo de espera promedio: {acu_espera/cant_ejecutados}")
                    print("_"*50)
                    print(f"Rendimiento del sistema: {cant_ejecutados/self.simulador.getTiempo()}")
                    print("_"*50)
                    print("[1] MENU | [S] SALIR ")
                    opcion = Prompt.ask("Seleccione una opción", choices=["1","S", "s"])
                else:
                    print("Aun no se han ejecutado procesos")
                mostrarMenu = True
            elif str(opcion) == "5":
                pass
            elif str(opcion).upper() != "S":
                system("cls")
                print("Opcion no valida")
                mostrarMenu = True

        self.abandonarSimulador(consola)
