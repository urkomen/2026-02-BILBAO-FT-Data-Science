import Tablero as tb
import Barcos as bar
import Disparos as disp
import time

def inicio_hundir(n = 10):
    ''' 
    INICIO DE JUEGO
        - Crear tablero inicial
        - Imprimir tablero
    '''
    # tablero:
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    #    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    tb.limpiar()
    tablero_usu = tb.crear_tablero(n)
    tablero_PC = tb.crear_tablero(n)
    tablero_PCoculto = tb.crear_tablero(n)

    print('TABLERO DE LA MÁQUINA')
    print('-'*30)
    tb.mostrar_tablero(tablero_usu)
    print('-'*30)
    print('TABLERO DEL USUARIO')
    tb.mostrar_tablero(tablero_PC)
    
    return tablero_usu, tablero_PC, tablero_PCoculto



def configuracion_hundir(tablero_usu:tuple[int, int], tablero_PC:tuple[int, int], tablero_PCoculto:tuple[int, int]):
    '''
    CONFIGURACIÓN
        - Se colocan los barcos del usuario (modo manual/aleatorio)
          4 barcos de 1 casilla
          3 barcos de 2 casillas
          2 barcos de 3 casillas
          1 barco de 4 casillas
    '''
    
    # Usuario coloca sus barcos
    manual_aleatorio = input('Colocar barcos de manera (1 - manual o 2 - aleatoria): ')
    barcos_usu = bar.lista_barcos
    if manual_aleatorio == '1':
        barcos = bar.colocar_barcos(tablero_usu, barcos_usu,True)
    else:
        barcos = bar.colocar_barcos(tablero_usu, barcos_usu, False)
    
    
    
    
    print(barcos)
    tb.mostrar_tablero(tablero_usu)
    input()



def quien_empieza():
    empieza = input('Quién comienza el primer turno? (Yo/PC)').upper()
    
    if empieza == 'YO':
        return 0
    else:
        return 1
    
    

def disparos_hundir(tablero_usu:tuple[int, int], tablero_PC:tuple[int, int], tablero_PCoculto:tuple[int, int], turno:int):
    '''
    DISPAROS
        - Recibir coordenadas
        - Comprobación de objetivo
        - Marcar casilla (tocado/agua)
    '''
    
    turno = 1
    if turno%2 == 0: # Turno usuario
        disp.disparos_usu(tablero_PC, tablero_PCoculto)
    else: # Turno PC
        print('Turno PC')
        disp.disparos_PC(tablero_usu)
    
    turno += 1 # Siguiente turno
    return turno
    
    
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