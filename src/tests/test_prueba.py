class Prueba:
    def __init__(self,id):
        self.id = id
    def __str__(self):
        return f'T{self.id}'

def probando(a):
    a = 69
nuevos = []
nuevos.append(Prueba(1))
nuevos.append(Prueba(2))
nuevos.append(Prueba(3))
nuevos.append(Prueba(4))
espera = [pru for pru in nuevos if pru.id == 1]

#espera.append(nuevos[0])
espera[0].id = 27
print(espera[0])
print(nuevos[0])
print(espera[0]==nuevos[0])
for i in nuevos:
    print(i)
nuevos.remove(espera[0])
for i in nuevos:
    print(i)

pruebita = [1]
print(not pruebita)