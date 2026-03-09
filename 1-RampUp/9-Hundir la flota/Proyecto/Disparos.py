import Metodos_varios as mv
import Tablero as tb
import Barcos as bar
import Disparos as disp
import random
import time


def disparos_usu(tablero1, tablero2):
    while True:
        coord_disp = disp.recibir_disparos(tablero1)
        
        # Si las coordenadas no son válidas, las volvemos a pedir
        if not disp.comprobar_coords(tablero1, coord_disp):
            print("Coordenadas inválidas. Inténtalo de nuevo.\n")
            continue
            
        print("Disparo realizado.\n")
        time.sleep(1)        
        
        # Si el objetivo no es un barco, cambio de turno
        if not disp.comprobar_objetivo(coord_disp,tablero1):
            print('Cambio turno')
            break



def disparos_PC(tablero):
    while True:
        coord_disp = disp.recibir_disparos(tablero, maquina = True)
        
        # Si las coordenadas no son válidas, las volvemos a pedir
        if not disp.comprobar_coords(tablero, coord_disp):
            print("Coordenadas inválidas. Inténtalo de nuevo.\n")
            continue
            
        print("Disparo realizado.\n")
        time.sleep(1)        
        
        # Si el objetivo no es un barco, cambio de turno
        if not disp.comprobar_objetivo(coord_disp,tablero):
            print('Cambio turno')
            break






def recibir_disparos(tablero:tuple[int, int], maquina = False):
    '''
    Recibir coordenadas del disparo del usuario
    '''
    
    if not maquina:
        coords = input(f"Introduce coordenadas del objetico que quieres disparar (ej: A1, C2, G9): ")
        casilla = mv.coords2index(coords)
    else:
        casilla = disparo_aleatorio()
    
    return casilla
    
    

def comprobar_objetivo(tablero:tuple[int, int],coords:tuple[int, int]):
    '''
    Comprobar si el disparo impacta en un barco o cae al agua
    '''
    
    if tb.es_agua(tablero, coords[0], coords[1]):
        tb.pintar_casilla(tablero, coords, 'DISP_AGUA')
        tb.mostrar_tablero(tablero)
        print("Agua!")
        time.sleep(1)
        
        return False # Disparo al agua
    else:
        
        tb.pintar_casilla(tablero, coords, 'TOCADO')
        tb.mostrar_tablero(tablero)
        print("Tocado!")
        # Comprobar si el barco se ha hundido
        # if bar.barco_hundido(tablero, coords):
        #     print("Barco hundido!")
        #     tb.pintar_casilla(tablero, coords, 'HUNDIDO')
        
        return True # Impacto en un barco



def comprobar_coords(tablero:tuple[int, int], casilla:tuple[int, int]):
    '''
    Comprobar si las coordenadas introducidas están dentro del tablero
    '''
    
    # Índice fuera de rango (tablero 10x10)
    for ind in casilla:
        if ind < 0 or ind > 9:
            print('Coordenadas fuera del tablero. Int')
            return False
    
    # Casilla previamente disparada
    if tb.ya_disparado(tablero, casilla[0], casilla[1]):
        tb.mostrar_tablero(tablero)
        print('Ya has disparado en esa casilla')
        return False
    
    return True



def disparo_aleatorio():
    fil = random.randint(0,9)
    col = random.randint(0,9)
    
    return (fil, col)