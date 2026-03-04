import Tablero
# Tablero.path.append("./Proyecto")


''' 
INICIO DE JUEGO
    - Crear tablero inicial
    - Imprimir tablero
'''
# tablero = [
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
#     ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
# ]
tablero = Tablero.crear_tablero()

Tablero.pintar_tablero(tablero)




'''
CONFIGURACIÓN
    - Se colocan los barcos del usuario (modo manual)
      4 barcos de 1 casilla
      3 barcos de 2 casillas
      2 barcos de 3 casillas
      1 barco de 4 casillas
'''

coords = (('A','1'))
indice = [Tablero.coords2index(coord) for coord in coords]
print(indice)


'''
DISPAROS
    - Recibir coordenadas
    - Comprobación de objetivo
    - Marcar casilla (tocado/agua)
'''




'''
HUNDIR BARCOS + FIN PARTIDA
    - Partes restantes del barco sin hundir
    - Marcar casillas de barco hundido
    - No barcos --> FIN PARTIDA
'''