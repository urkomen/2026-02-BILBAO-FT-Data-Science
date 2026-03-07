import Tablero
import Barcos

def inicio_hundir(n = 10):
    ''' 
    INICIO DE JUEGO
        - Crear tablero inicial
        - Imprimir tablero
    '''
    # tablero:
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    #     ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
    tablero = Tablero.crear_tablero(n)

    Tablero.mostrar_tablero(tablero)
    return tablero


def configuracion_hundir(tablero):
    '''
    CONFIGURACIÓN
        - Se colocan los barcos del usuario (modo manual)
          4 barcos de 1 casilla
          3 barcos de 2 casillas
          2 barcos de 3 casillas
          1 barco de 4 casillas
    '''
    
    
    Barcos.colocar_barcos(tablero)
    Tablero.mostrar_tablero(tablero)

def disparos_hundir():
    '''
    DISPAROS
        - Recibir coordenadas
        - Comprobación de objetivo
        - Marcar casilla (tocado/agua)
    '''
    
    pass
    
    
    
def barcos_hundidos():
    '''
    HUNDIR BARCOS + FIN PARTIDA
        - Partes restantes del barco sin hundir
        - Marcar casillas de barco hundido
        - No barcos --> FIN PARTIDA
    '''
    
    pass

def fin_hundir():
    pass