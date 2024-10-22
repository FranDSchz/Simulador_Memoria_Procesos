from particion import Particion
class MemoriaPrincipal:
    def __init__(self):
        self.particiones = []
        self.partDisp = []
        self.partOcup = []

    def obtenerParticiones(self, filtro):
        """
        Filtra las particiones de la memoria principal según el estado (disponibles u ocupadas).
        :param filtro: 'disponibles' para obtener particiones sin procesos asignados,
                       'ocupadas' para obtener particiones con procesos asignados.
        :return: Lista de particiones según el filtro aplicado.
        """
        if filtro == 'disponibles':
            return [p for p in self.particiones if p.proAsig is None]
        elif filtro == 'ocupadas': 
            return [p for p in self.particiones if p.proAsig is not None]
        else:
            raise ValueError('ERROR: parámetro INVALIDO')

    def agregarParticion(self, particion):
        """
        Agrega una partición a la memoria principal si no existe ya y tiene un tamaño válido.

        :param particion: Objeto de la clase Particion a agregar.
        """
        if not isinstance(particion, Particion):
            raise TypeError('ERROR: El parámetro debe ser un objeto de la clase Particion')
        
        if particion.tam <= 0:
            raise ValueError('ERROR: particion.tam INVALIDO')

        if particion.id in [p.id for p in self.particiones]:
            raise ValueError('ERROR: particion.id DUPLICADO')

        self.particiones.append(particion)
