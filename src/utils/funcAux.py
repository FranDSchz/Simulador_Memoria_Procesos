from rich.console import Console
from rich.prompt import Prompt

console = Console()

def pausar():
    console.print("\n[bold cyan]Presione cualquier tecla para continuar...[/bold cyan]", style="bold yellow")
    Prompt.ask("")

