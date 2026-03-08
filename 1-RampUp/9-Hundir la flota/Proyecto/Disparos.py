import Metodos_varios as mv
import Tablero as tb
import Barcos as bar
import time

def recibir_disparos(tablero:tuple[int, int]):
    '''
    Recibir coordenadas del disparo del usuario
    '''
    
    while True:
        coords = input(f"Introduce coordenadas del objetico que quieres disparar (ej: A1, C2, G9): ")
        casilla = mv.coords2index(coords)
        
        if comprobar_coords(casilla):
            tb.limpiar()
            print("Disparo realizado.\n")
            break
        else:
            print("Coordenadas inválidas. Inténtalo de nuevo.\n")
    
    return casilla
    
    

def comprobar_objetivo(tablero:tuple[int, int],coords:tuple[int, int]):
    '''
    Comprobar si el disparo impacta en un barco o cae al agua
    '''
    
    if not tb.es_agua(tablero, coords[0], coords[1]):
        print("Tocado!")
        tb.pintar_casilla(tablero, coords, 'TOCADO')
        time.sleep(1)
        # Comprobar si el barco se ha hundido
        if bar.barco_hundido(tablero, coords):
            print("Barco hundido!")
            tb.pintar_casilla(tablero, coords, 'HUNDIDO')
        
        return True # Impacto en un barco
    else:
        print("Agua!")
        tb.pintar_casilla(tablero, coords, 'AGUA')
        return False # Disparo al agua



def comprobar_coords(casilla:tuple[int, int]):
    '''
    Comprobar si las coordenadas introducidas están dentro del tablero
    '''
    
    # Índice fuera de rango (tablero 10x10)
    for ind in casilla:
        if ind < 0 or ind > 9:
            return False
    return True