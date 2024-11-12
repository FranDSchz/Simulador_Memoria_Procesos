from src.models.proceso import Proceso
from abc import ABC, abstractmethod
from src.utils.constantes import TAM_MAX
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import json
import os

console = Console()

class Loader(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def cargarProcesos(self, simu):
        pass

    def validarEntero(self, mensaje, min_val, max_val):
        while True:
            try:
                valor = int(input(mensaje))
                if min_val <= valor <= max_val:
                    return valor
                console.print(f"[red]Valor inválido. Debe estar entre {min_val} y {max_val}[/red]")
            except ValueError:
                console.print("[red]El valor ingresado no es un número válido. Intente de nuevo.[/red]")

class ConsoleLoader(Loader):
    # Carga manual de procesos (ya existente)
    def cargarProcesos(self, simu):
        n = self.validarEntero("Ingrese la cantidad de procesos que desea cargar (máx 10)\n>> ", 1, 10)
        for i in range(1, n + 1):
            print(f"Proceso N°: {i}")
            ti = self.validarEntero('Ingrese el tiempo de irrupción válido (> 0): ', 1, float('inf'))
            taMemoria = self.validarEntero('Ingrese el tiempo de arribo a memoria válido (>= 0): ', 0, float('inf'))
            tam = self.validarEntero(f"Ingrese el tamaño entre > 0 y <= {TAM_MAX} sin la unidad (KB): ", 1, TAM_MAX)
            simu.nuevos.append(Proceso(i, ti, taMemoria, tam))

        print("Procesos ")
        print(f"[1] MENU | [2] INICIAR SIMULACION")
        opcion = self.validarEntero("Seleccione una opcion\n>> ", 1, 2)
        return opcion

class FileLoader(Loader):
    # Carga de procesos desde archivo
    def cargarProcesos(self, simu):
        while True:
            path = os.path.join("C:\\Users\\frank\\Desktop\\WORKSPACES\\Simulador_Memoria_procesos", "procesos")
            archivos = [f for f in os.listdir(path) if f.endswith('.json')]
            
            if not archivos:
                opcion = self.mostrar_menu_archivos_vacios()
                if opcion in ("1","3","S"):
                    return opcion
                else:
                    continue  # Regresa al menú vacío hasta que haya archivos o seleccione otra opción

            # Mostrar los archivos disponibles
            table = Table(title="Archivos Disponibles para Cargar Procesos")
            table.add_column("N°", justify="center", style="cyan")
            table.add_column("Archivo", justify="center", style="magenta")

            for idx, archivo in enumerate(archivos, 1):
                table.add_row(str(idx), archivo)

            console.print(table)

            # Seleccionar el archivo
            archivo_idx = self.validarEntero("Seleccione el número del archivo a cargar: ", 1, len(archivos))
            archivo_seleccionado = archivos[archivo_idx - 1]

            # Intentar cargar el archivo
            try:
                with open(os.path.join(path, archivo_seleccionado), "r") as file:
                    data = json.load(file)

                    # Validar y cargar hasta 10 procesos
                    procesos_cargados = []
                    for i, proc_data in enumerate(data[:10]):  # Tomar solo los primeros 10 procesos
                        if self.es_proceso_valido(proc_data):
                            proceso = Proceso(
                                proc_data["id"],
                                proc_data["ti"],
                                proc_data["taMemoria"],
                                abs(proc_data["tam"])  # Convertir tam a valor absoluto si es negativo
                            )
                            procesos_cargados.append(proceso)
                        else:
                            raise ValueError(f"Estructura inválida en proceso: {proc_data}")

                    # Agregar los procesos cargados al simulador
                    simu.nuevos.extend(procesos_cargados)
                    console.print(f"[green]Procesos cargados exitosamente desde {archivo_seleccionado}.[/green]")
                    
                    # Notificar si el archivo contenía más de 10 procesos
                    if len(data) > 10:
                        console.print("[yellow]Nota: El archivo contenía más de 10 procesos. Solo se cargaron los primeros 10.[/yellow]")
                    console.print("[blue] [1] Menú | [2] Iniciar simulacion | [S] Salir ")
                    opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "S","s"])
                    return opcion
                
            except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
                console.print(f"[bold red]Error al leer el archivo {archivo_seleccionado}: {e}[/bold red]")
                self.mostrar_menu_archivos_vacios()  # Si falla, regresa al menú vacío

    def es_proceso_valido(self, proc_data):
        required_keys = {"id", "ti", "taMemoria", "tam"}
        return all(key in proc_data for key in required_keys)
    
    #def mostrar_menu(self):

    def mostrar_menu_archivos_vacios(self):
        console.print("[bold red]La carpeta 'procesos' está vacía.[/bold red]")
        while True:
            console.print("[blue] [1] Menú | [2] Refrescar | [3] Carga manual | [S] Salir[/blue]")
            opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "S", "s"])
            if opcion == "1":
                console.print("[yellow]Regresando al menu principal...[/yellow]")
                return opcion
            elif opcion == "2":
                console.print("[yellow]Buscando nuevos archivos...[/yellow]")
                return opcion
            elif opcion == "3":
                console.print("[yellow]Cambiando a carga manual...[/yellow]")
                return opcion
            elif opcion == "S":
                console.print("[red]Saliendo del simulador...[/red]")
                return opcion
            else:
                console.print("[red]La opcion ingresada no es valida.[/red]")
        
class InterfazLoader(Loader):
    def cargarProcesos(self, simu):
        console.print("[bold blue]Métodos de carga de procesos:[/bold blue]")
        console.print("[1] Carga manual")
        console.print("[2] Carga desde archivo")

        metodo = self.validarEntero("Seleccione el método de carga: ", 1, 2)

        if metodo == 1:
            loader = ConsoleLoader("Manual")
            opcion = loader.cargarProcesos(simu)
        elif metodo == 2:
            loader = FileLoader("Archivo")
            opcion = loader.cargarProcesos(simu)
        return opcion