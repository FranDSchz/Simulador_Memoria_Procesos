from src.utils.funcAux import pausar
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.markdown import Markdown
from time import sleep

class UIConsola:
    def __init__(self):
        self.console = Console()

    def mostrar_tiempo_actual(self, tiempo_actual):
        """Muestra el instante de tiempo actual"""
        self.console.print(Panel(f"[bold yellow]Tiempo actual: [cyan]{tiempo_actual}[/cyan] segundos[/bold yellow]", style="bold green"))

    def mostrar_estado_procesador(self, proceso, quantum_restante):
        """Muestra el estado del procesador"""
        if proceso:
            tiempo_ejecucion_restante = proceso.ti - proceso.tiempoEjecutado
            self.console.print(Panel(f"[bold cyan]Estado del Procesador[/bold cyan]", style="blue"))
            self.console.print(f"[bold]Proceso en Ejecución:[/bold] [green]T{proceso.id}[/green]")
            self.console.print(f"[bold]Quantum restante:[/bold] [yellow]{quantum_restante}[/yellow]")
            self.console.print(f"[bold]Tiempo de ejecución restante:[/bold] [magenta]{tiempo_ejecucion_restante}[/magenta]")
        else:
            self.console.print(Panel("[bold red]El procesador está inactivo[/bold red]", style="red"))


    def mostrar_tabla_particiones(self, particiones):
        """Muestra el estado de la memoria con colores para particiones ocupadas y libres"""
        table = Table(title="Estado de la Memoria")

        table.add_column("ID de Partición", justify="center", style="cyan", no_wrap=True)
        table.add_column("Tamaño", justify="center", style="green")
        table.add_column("ID Proceso", justify="center", style="yellow")
        table.add_column("Fragmentación Interna", justify="center", style="red")
        table.add_column("Dirección Comienzo", justify="center", style="magenta")
        table.add_column("Dirección Fin", justify="center", style="magenta")

        for part in particiones:
            id_proceso = str(part.proAsig.id) if part.proAsig else "Libre"
            frag_interna = f"{part.tam - part.proAsig.tam}" if part.proAsig else "N/A"
            dir_fin = part.dir_inicio + part.tam
            color = "blue" if part.proAsig else "green"

            table.add_row(
                f"[{color}]{part.id}[/{color}]",
                f"{part.tam}KB",
                f"[{color}]{id_proceso}[/{color}]",
                f"{frag_interna}KB" if frag_interna != "N/A" else "N/A",
                str(part.dir_inicio),
                str(dir_fin),
            )

        self.console.print(table)
        

    def mostrar_cola_procesos(self, titulo, procesos, tiempo_key):
        """Muestra el estado de una cola de procesos (listos, suspendidos, etc.)"""
        table = Table(title=titulo)

        table.add_column("ID de Proceso", justify="center", style="cyan")
        table.add_column("Tamaño", justify="center", style="green")
        table.add_column("Tiempo de Ejecución Restante", justify="center", style="magenta")
        table.add_column(f"Tiempo de arribo a {tiempo_key}", justify="center", style="yellow")

        for proceso in procesos:
            tiempo_ejecucion_restante = proceso.ti - proceso.tiempoEjecutado
            tiempo_llegada = getattr(proceso, f"ta{tiempo_key}", "N/A")
            table.add_row(
                f"T{proceso.id}",
                f"{proceso.tam}KB",
                f"{tiempo_ejecucion_restante} segundos",
                str(tiempo_llegada)
            )

        self.console.print(table)
        

    def mostrar_cola_terminados(self, procesos_terminados):
        """Muestra los procesos terminados y su tiempo de retorno"""
        table = Table(title="Procesos Terminados")

        table.add_column("ID de Proceso", justify="center", style="cyan")
        table.add_column("Tamaño", justify="center", style="green")
        table.add_column("Tiempo de Retorno", justify="center", style="magenta")

        for proceso in procesos_terminados:
            table.add_row(
                f"T{proceso.id}",
                f"{proceso.tam}KB",
                f"{proceso.tr} segundos"
            )

        self.console.print(table)
        

    def progreso(self, cantidad):
        """Muestra una barra de progreso cuando un proceso ingresa a CPU"""
        with Progress(BarColumn(), transient=True) as progress:
            task = progress.add_task("[cyan]Ejecutando proceso...", total=cantidad)
            while not progress.finished:
                progress.advance(task, 1)
                

    def mensaje_inicial(self):
        """Muestra un mensaje inicial con Markdown y emojis"""
        md = """
        # Bienvenido al Simulador de Procesos 🚀

        Este simulador te permitirá ver:

        - [cyan]El estado del procesador[/cyan] 💻
        - [green]La memoria principal con particiones[/green] 🧠
        - [yellow]Las colas de procesos[/yellow] 🔄
        - [red]Los procesos terminados[/red] ✅

        ¡Prepárate para administrar tus recursos!
        """
        self.console.print(Markdown(md))
        pausar()
    
    def proceso_ingresa_sistema(self, proceso):
        """Muestra un mensaje cuando un proceso ingresa al sistema operativo (taMemoria)"""
        self.console.print(f"[bold green]El proceso T{proceso.id} ingresó al sistema operativo[/bold green]")
        self.console.print(f"Tiempo de arribo a memoria: [cyan]{proceso.taMemoria}[/cyan] segundos")
        

    def proceso_ingresa_cola_listos(self, proceso):
        """Muestra un mensaje cuando un proceso ingresa a la cola de listos"""
        self.console.print(f"[bold cyan]El proceso T{proceso.id} ingresó a la cola de listos[/bold cyan]")
        self.console.print(f"Tiempo de arribo a la cola de listos: [magenta]{proceso.taListos}[/magenta] segundos")
        
    def proceso_ingresa_cola_suspendidos(self, proceso):
        """Muestra un mensaje cuando un proceso ingresa a la cola de suspendidos"""
        self.console.print(f"[bold yellow]El proceso T{proceso.id} ingresó a la cola de suspendidos[/bold yellow]")
        self.console.print(f"Tiempo de arribo a la cola de suspendidos: [magenta]{proceso.taMemoria}[/magenta] segundos")
        sleep(2)
    
    def proceso_ingresa_cpu(self, proceso):
        """Muestra un mensaje cuando un proceso ingresa al CPU"""
        self.console.print(f"[bold blue]El proceso T{proceso.id} ingresó al CPU[/bold blue]")
        self.console.print(f"Tiempo de ejecución restante: [magenta]{proceso.ti - proceso.tiempoEjecutado}[/magenta] segundos")
        
    
    def proceso_abandona_cpu(self, proceso):
        """Muestra un mensaje cuando un proceso abandona el CPU"""
        self.console.print(f"[bold red]El proceso T{proceso.id} abandonó el CPU[/bold red]")
        
    
    def procesoFinalizado(self, proceso):
        self.console.print(Panel(f"[bold red]El proceso T{proceso.id} ha finalizado[/bold red]", style="green"))
        