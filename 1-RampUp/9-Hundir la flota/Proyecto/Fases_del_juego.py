import Tablero as tb
import Barcos as bar
import Disparos as disp

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
    tb.limpiar()
    tablero = tb.crear_tablero(n)

    tb.mostrar_tablero(tablero)
    return tablero


def configuracion_hundir(tablero:tuple[int, int]):
    '''
    CONFIGURACIÓN
        - Se colocan los barcos del usuario (modo manual)
          4 barcos de 1 casilla
          3 barcos de 2 casillas
          2 barcos de 3 casillas
          1 barco de 4 casillas
    '''
    bar.colocar_barcos(tablero)
    # tablero = bar.colocar_barcos(tablero)


def disparos_hundir(tablero:tuple[int, int]):
    '''
    DISPAROS
        - Recibir coordenadas
        - Comprobación de objetivo
        - Marcar casilla (tocado/agua)
    '''
    coord_disp = disp.recibir_disparos()
    disp.comprobar_objetivo(coord_disp,tablero)
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