# Simulador de Planificación de CPU y Gestión de Memoria 🖥️

Este proyecto es un simulador desarrollado en Python que modela dos conceptos fundamentales de los Sistemas Operativos: la **planificación de procesos de corto plazo** y la **gestión de memoria principal con particiones fijas**.

Fue creado como trabajo práctico para la materia de Sistemas Operativos, con el objetivo de implementar y visualizar el ciclo de vida de los procesos en un sistema mono-procesador.

### Demo Visual

Pendiente
---

## 🎯 Conceptos Clave Implementados

Este simulador pone en práctica los siguientes algoritmos y políticas de gestión de un Sistema Operativo:

### 1. **Planificación de CPU: Round-Robin**
* Los procesos en la cola de listos son asignados a la CPU en un esquema de turnos rotatorios.
* **Quantum (`q`):** Se ha implementado un quantum de **3 unidades de tiempo**. Si un proceso no finaliza en este lapso, es desalojado de la CPU y puesto al final de la cola de listos, permitiendo que otro proceso tome su lugar.

### 2. **Gestión de Memoria: Particiones Fijas**
* La memoria principal está dividida en particiones de tamaño predefinido, incluyendo un espacio reservado para el Sistema Operativo.
* **Esquema de Particiones:**
    * `100 KB`: Sistema Operativo
    * `250 KB`: Partición para procesos grandes
    * `150 KB`: Partición para procesos medianos
    * `50 KB`: Partición para procesos pequeños

### 3. **Política de Asignación de Memoria: Worst-Fit (El Peor Ajuste)**
* Cuando un proceso nuevo debe ser cargado en memoria, el sistema busca la partición libre más grande disponible.
* **Fragmentación Interna:** Esta política puede generar una fragmentación interna significativa, la cual es calculada y mostrada por el simulador para cada partición ocupada.

---

## 🛠️ Stack Tecnológico

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

El proyecto fue desarrollado utilizando únicamente las librerías estándar de Python, sin dependencias externas.

---

## ⚙️ Cómo Ejecutar el Simulador

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/FranDSchz/Simulador_Memoria_Procesos.git
    cd Simulador_Memoria_Procesos
    ```

2.  **Crea y activa un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate    # Windows
    ```

3.  **Configura los procesos de entrada:**
    El simulador lee los procesos a simular desde un archivo JSON. Puedes modificar el archivo `procesos/prueba1.json` para definir tus propios procesos. La estructura es la siguiente:

    ```json
    [
      {
        "id": 1,
        "tamano": 80,
        "arribo": 0,
        "irrupcion": 8
      },
      {
        "id": 2,
        "tamano": 140,
        "arribo": 2,
        "irrupcion": 5
      }
    ]
    ```

4.  **Ejecuta el simulador:**
    ```bash
    python src/main.py
    ```
    El programa te pedirá que ingreses el nombre del archivo de procesos (ej: `prueba1`). La simulación comenzará y mostrará el estado del sistema en cada evento clave (llegada o fin de un proceso).

---

## 📊 Métricas de Rendimiento

Al finalizar la simulación, el programa genera un informe con las siguientes métricas para evaluar el rendimiento del sistema:

* **Tiempo de Retorno:** Tiempo total que cada proceso pasó en el sistema (desde su llegada hasta su finalización).
* **Tiempo de Espera:** Tiempo total que cada proceso pasó en la cola de listos.
* **Rendimiento del Sistema (Throughput):** Cantidad de procesos completados por unidad de tiempo.