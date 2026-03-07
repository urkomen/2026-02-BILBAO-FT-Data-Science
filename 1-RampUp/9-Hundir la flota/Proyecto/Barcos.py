import Metodos_varios
import Tablero

def colocar_barcos(tablero, pos_aleatorio = False):
    '''
    Se colocan los barcos de inicio
    
    pos_aleatorio: 
        False --> los barcos se colocan de forma manual
        True --> los barcos se colocan de forma aleatoria
    '''
    lista_barcos = [(1, 4), (2, 3), (3, 2), (4, 1)]
    
    if not pos_aleatorio:
        for tipo, cantidad in lista_barcos:
            print(f"\nColoca {cantidad} barco(s) de tamaño {tipo}:")

            for _ in range(cantidad):
                while True:
                    entrada = input(f"Introduce {tipo} coordenadas separadas por espacio (ej: A1 A2 A3): ")
                    coords = entrada.split()
                    # coords = ['A1','B1']
                    casillas = [Metodos_varios.coords2index(coord) for coord in coords]
                    

                    if barco_valido(tipo, casillas):
                        pintar_barco(tipo, casillas, tablero)
                        print("Barco colocado.\n")
                        Tablero.mostrar_tablero(tablero)
                        break
                    else:
                        print("Coordenadas inválidas. Inténtalo de nuevo.\n")


def pintar_barco(tipo:int, casillas:list[tuple[int, int]], tablero:tuple[int, int]):
    # Convertir coordenadas en índices de la matriz tablero
    
    for tile in casillas:
    
        match tipo:
            case 1:
                Tablero.pintar_casilla(tablero, tile, 'BARCO1')
                
            case 2:
                    Tablero.pintar_casilla(tablero, tile, 'BARCO2')
                
            case 3:
                    Tablero.pintar_casilla(tablero, tile, 'BARCO3')
                
            case 4:
                    Tablero.pintar_casilla(tablero, tile, 'BARCO4')


def barco_valido(tipo: int, casillas:list[tuple[int, int]]):
    '''
    Comprueba si las coordenadas de entrada forman un barco 
    válido del tamaño 'tipo' (1, 2, 3, 4).
    casillas es una lista de strings tipo ['A5', 'A6', 'A7']
    '''

    # Ordenar coordenadas para evitar problemas ((1,3), (1,1), (1,2) → (1,1), (1,2), (1,3))
    casillas.sort()
    
    # Comprobar que no hay índices fuera de rango (tablero 10x10)
    for casilla in casillas:
        for ind in casilla:
            if ind > 9:
                return False
    
    # Comprobar que esa casilla está libre
    
    
    # Comprobar número de casillas con el tipo de barco
    if len(casillas) != tipo:
        return False

    # Caso barco simple (1 casilla)
    if tipo == 1:
        return True
    
    
    # En caso de no ser un barco simple
    # Extraemos filas y columnas
    filas = [i[0] for i in casillas]
    cols  = [i[1] for i in casillas]
    
    # Comprobar alineación. Debe estar en línea, no doblarse (por ejemplo forma 'L')
    hbarco = len(set(filas)) == 1 #alineado horizontal
    vbarco   = len(set(cols)) == 1# alineado vertical

    if not (hbarco or vbarco):
        return False

    # Casillas consecutivas horizontalmente/verticalmente
    if hbarco:
        return cols == list(range(cols[0], cols[0] + tipo))

    if vbarco:
        return filas == list(range(filas[0], filas[0] + tipo))

    return False


