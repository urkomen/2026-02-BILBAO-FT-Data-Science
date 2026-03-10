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

    tb.mostrar_tableros2(tablero_usu, tablero_PC)
    
    return tablero_usu, tablero_PC, tablero_PCoculto



def configuracion_hundir(tablero_usu:tuple[int, int], tablero_PC:tuple[int, int]):
    '''
    CONFIGURACIÓN
        - Se colocan los barcos del usuario (modo manual/aleatorio)
          4 barcos de 1 casilla
          3 barcos de 2 casillas
          2 barcos de 3 casillas
          1 barco de 4 casillas
    '''
    
    tb.limpiar()
    print('Comienza la partida')
    time.sleep(1)
    tb.limpiar()
    print('Preparando tableros...')
    time.sleep(1)
    
    # Usuario coloca sus barcos
    manual_aleatorio = input('Colocar barcos de manera (1 - manual o 2 - aleatoria): ')
    barcos = bar.lista_barcos
    if manual_aleatorio == '1':
        barcos_usu = bar.colocar_barcos(tablero_usu, barcos,True)
    else:
        barcos_usu = bar.colocar_barcos(tablero_usu, barcos, False)
    
    # Se colocan barcos de la máquina
    barcos_PC = bar.colocar_barcos(tablero_PC, barcos_usu, False)
    
    time.sleep(1.5)
    
    
    # tb.mostrar_tableros2(tablero_usu, tablero_PC)
    return barcos_usu, barcos_PC


def quien_empieza():
    empieza = input('Quién comienza el primer turno? (YO/PC)').upper()
    
    if empieza == 'YO':
        return 0
    else:
        return 1
    
    

def turnos_hundir(tablero_usu:tuple[int, int], tablero_PC:tuple[int, int], tablero_PCoculto:tuple[int, int], barcos_usu:list, barcos_PC:list, turno:int):
    '''
    DISPAROS
        - Recibir coordenadas
        - Comprobación de objetivo
        - Marcar casilla (tocado/agua)
    '''
    
    tb.mostrar_tableros2(tablero_PCoculto, tablero_usu)
    print('Todo listo. Que comience la batalla!')
    time.sleep(0.7)
    
    fin = False
    # turno = 1
    
    while turno < 20:
        if turno%2 == 0: # Turno usuario
            tb.mostrar_tableros2(tablero_PCoculto, tablero_usu)
            fin = disp.disparos_usu(tablero_PC, tablero_PCoculto, tablero_usu, barcos_PC)
        else: # Turno PC
            print('Turno PC')
            fin = disp.disparos_PC(tablero_PCoculto, tablero_usu, barcos_usu)

        tb.mostrar_tableros2(tablero_PCoculto, tablero_usu)
        print('Turno finalizado.')
        
        turno += 1 # Siguiente turno
        
    
    
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