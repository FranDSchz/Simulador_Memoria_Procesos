# Simulador_Memoria_Procesos
Repositorio para el desarrollo del simulador de gestión de memoria y planificación de procesos

## Pasos para configurar el entorno virtual:

### 1. Navega al directorio del proyecto

```sh
cd Simulador_Memoria_Procesos
```

### 2. Crea un entorno virtual

Crea un entorno virtual en tu máquina local. El entorno virtual se llamará env-simulador.

```sh
python -m venv env-simulador
```

### 3. Activa el entorno virtual

```sh
env-simulador\Scripts\activate
```

for linux:

````sh
source env-simulador/bin/activate```

> Nota: Si obtienes un error sobre la ejecución de scripts, ejecuta lo siguiente en PowerShell:

```sh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

> Luego, intenta activar el entorno de nuevo.

### 4. Instala las dependencias

Una vez que el entorno virtual esté activado, instala todas las dependencias necesarias utilizando el archivo requirements.txt.

```sh
pip install -r requirements.txt
```

### 3. Desactivar el entorno virtual

Cuando termines de trabajar, puedes desactivar el entorno virtual usando el comando:

```sh
deactivate
```

### 4. Agregar o eliminar dependencias

Si deseas añadir una dependencia debes ejecutar el comando:

```sh
pip install nombre_dependencia
```

Si deseas eliminar una dependencia debes ejecutar el comando:

```sh
pip uninstall nombre_dependencia
```

### 5. Actualizar dependencias

Si añades o cambias dependencias, asegúrate de actualizar el archivo requirements.txt con:

```sh
pip freeze > requirements.txt
```

> Nota: Esto lo debes hacer antes de desactivar el entorno virtual.