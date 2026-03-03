tablero = [
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
]

def crear_tablero(tamaño=10): 
    '''
    Crea tablero de juego
    '~' representa agua
    Tamaño por defecto 10
    '''
    return [['~' for _ in range(tamaño)] for _ in range(tamaño)]


def pintar_tablero(tablero):
    '''
    Muestra el tablero en pantalla
    '''
    for fila in tablero:
        print(' '.join(fila))


















AGUA = '🟦'
BARCO = '⬜'
IMPACTO = '🟥'

def pintar_tab_Emojis(tablero):
    for fila in tablero:
        print(' '.join(fila))