from src.utils.funcAux import pausar
from time import sleep
class CTRLMemoria:
    def __init__(self):
        pass
    
    def gestionarMemoria(self, simu, mp, consola):
        #x = input(f'simu.tiempo INICIO:{simu.getTiempo()}')
        #x = input(f'grado multip {simu.getMultiPro()}')
        if simu.getMultiPro() < 5:
            #x = input(f'simu.hayNuevosProcesos{simu.hayNuevosProcesos()}')
            #x = input(f'lista nuevos {simu.nuevos}')
            #x = input(f'lista espera {simu.espera}')
            if simu.hayNuevosProcesos():
                simu.actualizarListas()
                #x = input(f'act lista nuevos {simu.nuevos}')
                #x = input(f'act lista espera {simu.espera}')
            
            #x = input(f'mp.obtenerParticiones(disp) {mp.obtenerParticiones('disponibles')}')
            if mp.obtenerParticiones('disponibles') != []:
                #x = input(f'simu.hayProcesos(True) {simu.hayProcesos(True)}')
                if simu.hayProcesos(True):
                    #x = input(f'for simu.getProcesos() {simu.getProcesos()}')
                    for proceso in simu.getProcesos():
                        partDisp = mp.obtenerParticiones('disponibles')
                        #x = input(f'partDisp = mp.ob.. {partDisp}')
                        partDisp.sort(key=lambda particion: particion.tam, reverse=True)
                        #x = input(f'partDisp ordenada {partDisp}')
                        #x = input(f'not partDisp or simu.getMultiPro() == 5 {(not partDisp) or (simu.getMultiPro() == 5)}')
                        if (not partDisp) or (simu.getMultiPro() == 5):
                            break
                        for part in partDisp:
                            #x = input(f'proceso.getTam() <= part.getTam() {proceso.getTam() <= part.getTam()}')
                            if proceso.getTam() <= part.getTam():
                                #x = input(f'simu.listos {simu.listos}')
                                simu.agregarAListos(proceso)
                                #x = input(f'simu.listos post add {simu.listos}')
                                proceso.setTaListos(simu.getTiempo())
                                proceso.asignar(part)
                                part.asignar(proceso)
                                #x = input(f'susp antes de simu.quitarDeList {simu.suspendidos}')
                                #x = input(f'espera antes de simu.quitarDeList {simu.espera}')
                                simu.quitarDeLista(proceso)
                                #x = input(f'susp post de simu.quitarDeList {simu.suspendidos}')
                                #x = input(f'espera post de simu.quitarDeLis {simu.espera}')
                                #x = input(f'multipro antes cont {simu.multiPro}')
                                simu.contarMultiPro()
                                #x = input(f'multipro post cont {simu.multiPro}') 
                                consola.proceso_ingresa_cola_listos(proceso)
                                sleep(0.3)
                                consola.mostrar_tabla_particiones(mp.particiones)
                                sleep(0.3)
                                consola.mostrar_cola_procesos('Cola de listos',simu.listos,'Listos')
                                pausar()
                                break
                            else:
                                consola.proceso_ingresa_cola_suspendidos(proceso)
                                sleep(0.3)
                                simu.suspendidos.append(proceso)
                                simu.quitarDeLista(proceso)
                                simu.contarMultiPro()