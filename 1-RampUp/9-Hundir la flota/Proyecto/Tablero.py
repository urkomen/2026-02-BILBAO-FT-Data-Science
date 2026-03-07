import numpy as np
tablero_ejemplo = [['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
           ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]

def crear_tablero(n=10): 
    '''
    Crea tablero de juego '~' representa agua
    Tamaño por defecto matriz cuadrada de dimensión 10
    '''
    # return np.full((n,n),'~')
    return np.full((n,n),'🟦')


def mostrar_tablero(tablero:tuple[int, int]):
    '''
    Muestra el tablero en pantalla
    '''
    for fila in tablero:
        print(" ".join(str(elem) for elem in fila))


def pintar_casilla(tablero:tuple[int, int], casilla:tuple, state:str):
    '''
    Cambiamos el estado de la casilla del tablero: 
    BARCO(1) --> '⬜'
    BARCO(2) --> '🟩'
    BARCO(3) --> '🟫'
    BARCO(4) --> '🟪'
    AGUA     --> '⬛'
    TOCADO   --> '🟨'
    HUNDIDO  --> '🟥'
    '''
    
    n = casilla[0]
    m = casilla[1]
    
    match state:
        case 'BARCO1':
            tablero[n,m] = '⬜'
        case 'BARCO2':
            tablero[n,m] = '🟩'
        case 'BARCO3':
            tablero[n,m] = '🟫'
        case 'BARCO4':
            tablero[n,m] = '🟪'
        case 'AGUA':
            tablero[n,m] = '⬛'
        case 'TOCADO':
            tablero[n,m] = '🟨'
        case 'HUNDIDO':
            tablero[n,m] = '🟥'
    
    return tablero
    



def pintar_disparos():
    pass













AGUA = '🟦'
BARCO = '⬜'
IMPACTO = '🟥'

def pintar_tab_Emojis(tablero):
    for fila in tablero:
        print(' '.join(fila))