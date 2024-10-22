# Estructura propuesta del proyecto simulador_memoria_procesos

/simulador_memoria_procesos/
│
├── /src/
│   ├── /controllers/        # Controladores que manejan la lógica del simulador
│   │   ├── procesador.py     # Clase y lógica del procesador
│   │   ├── memoria.py        # Clase y lógica de la memoria principal
│   │   ├── planificador.py   # Algoritmos de planificación de procesos (Round Robin, FIFO, etc.)
│   │   └── gestor.py         # Clase principal que controla el flujo general del simulador
│   │
│   ├── /models/              # Modelos que representan las entidades principales
│   │   ├── proceso.py        # Clase que modela los procesos
│   │   ├── particion.py      # Clase que modela las particiones de memoria
│   │   └── sistema.py        # Modela el sistema operativo y otras entidades globales
│   │
│   ├── /views/               # Vistas para la interfaz de usuario (si decides implementarla)
│   │   ├── consola.py        # Vista basada en consola (para la versión CLI)
│   │   └── interfaz.py       # Vista gráfica (si decides implementarla con PyQt5, Tkinter, etc.)
│   │
│   ├── /utils/               # Funciones auxiliares y de soporte
│   │   ├── logs.py           # Registro de eventos o logs del sistema
│   │   ├── validaciones.py   # Validaciones de entrada del usuario
│   │   └── constantes.py     # Constantes globales (tamaños de memoria, configuración inicial, etc.)
│   │
│   └── main.py               # Punto de entrada del programa
│
├── /tests/                   # Tests unitarios para las diferentes partes del código
│   ├── test_memoria.py        # Pruebas para la gestión de memoria
│   ├── test_procesador.py     # Pruebas para el procesador y algoritmos de planificación
│   ├── test_proceso.py        # Pruebas para la clase de procesos
│   └── test_particion.py      # Pruebas para las particiones
│
├── /docs/                    # Documentación del proyecto
│   └── diseño.md             # Explicación de la arquitectura, decisiones de diseño, etc.
│
├── requirements.txt          # Dependencias del proyecto (librerías como PyQt5, Tkinter, etc.)
└── README.md                 # Descripción general del proyecto, instrucciones de uso

## Descripción de los módulos

### Controllers
- **procesador.py**: Aquí irá toda la lógica relacionada con la ejecución y planificación de los procesos (e.g., Round Robin, First Come First Serve).
- **memoria.py**: Se encargará de la gestión de las particiones de memoria, asignación, y liberación de espacio.
- **planificador.py**: Implementará los algoritmos de planificación y controlará la ejecución de los procesos.
- **simulador.py**: Será el "cerebro" que controle el flujo de todo el sistema. Coordinará el funcionamiento entre la memoria y el procesador.

### Models
- **proceso.py**: Modela la entidad proceso (ID, tiempo de irrupción, tiempo de arribo, tamaño, etc.).
- **particion.py**: Modela las particiones de memoria con su tamaño y asignación.

### Views
- **consola.py**: Vista basada en consola (CLI) para que el usuario interactúe sin interfaz gráfica.
- **interfaz.py**: Aquí podrías implementar una interfaz gráfica si lo decides más adelante (con PyQt5, Tkinter o alguna otra librería).

### Utils
- **logs.py**: Funcionalidad para registrar eventos o errores que sucedan durante la ejecución.
- **validaciones.py**: Aquí se agrupan todas las funciones que validan entradas del usuario, tamaños de procesos, etc.
- **constantes.py**: Variables globales del sistema, como el tamaño de las particiones, parámetros del procesador, etc.

### Tests
- Todos los archivos en esta carpeta estarán dedicados a realizar pruebas unitarias para asegurarte de que los módulos se comporten correctamente.
