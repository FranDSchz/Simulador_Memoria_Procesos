class CTRLMemoria:
    def __init__(self):
        pass
    
    def gestionarMemoria(self, simu, mp):
        if simu.getMultiPro() < 5:
            if simu.hayNuevosProcesos():
                simu.actualizarListas()
            if mp.obtenerParticiones('disponibles') != []:
                if simu.hayProcesos(True): #falta implementar
                    for proceso in simu.getProcesos():
                        partDisp = mp.obtenerParticiones('disponibles')
                        partDisp.sort(key=lambda particion: particion.tam, reverse=True)
                        if not partDisp or simu.getMultiP() == 5:
                            break
                        for part in partDisp:
                            if proceso.getTam() <= part.getTam():
                                proceso.setTaListos(simu.getTiempo())
                                proceso.asignar(part)
                                part.asignar(proceso)
                                simu.quitarDeLista(proceso)
                                simu.contarMultiPro() 
                                break