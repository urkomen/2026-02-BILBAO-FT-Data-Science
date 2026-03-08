import numpy as np
import os

# Constantes
AGUA = '🟦'
BARCO1 = '⬜'
BARCO2 = '🟩'
BARCO3 = '🟫'
BARCO4 = '🟪'
DISP_AGUA = '⬛'
TOCADO   = '💥'
HUNDIDO  = '☠️'

def crear_tablero(n=10): 
    '''
    Crea tablero de juego '~' representa agua
    Tamaño por defecto matriz cuadrada de dimensión 10
    '''
    # return np.full((n,n),'~')
    return np.full((n,n), AGUA)


def mostrar_tablero(tablero:tuple[int, int]):
    '''
    Muestra el tablero en pantalla
    '''
    for fila in tablero:
        print(' '.join(str(elem) for elem in fila))


def es_agua(tablero, fil, col):
    return tablero[fil][col] == AGUA


def pintar_casilla(tablero:tuple[int, int], casilla:tuple, state:str):
    '''
    Cambiamos el estado de la casilla del tablero: 
    BARCO(1) --> '⬜'
    BARCO(2) --> '🟩'
    BARCO(3) --> '🟫'
    BARCO(4) --> '🟪'
    AGUA     --> '⬛'
    TOCADO   --> '💥'
    HUNDIDO  --> '☠️'
    '''
    
    n = casilla[0]
    m = casilla[1]
    
    match state:
        case 'BARCO1':
            tablero[n,m] = BARCO1
        case 'BARCO2':
            tablero[n,m] = BARCO2
        case 'BARCO3':
            tablero[n,m] = BARCO3
        case 'BARCO4':
            tablero[n,m] = BARCO4
        case 'AGUA':
            tablero[n,m] = DISP_AGUA
        case 'TOCADO':
            tablero[n,m] = TOCADO
        case 'HUNDIDO':
            tablero[n,m] = HUNDIDO
    
    return tablero
    



def pintar_disparos():
    pass



def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


