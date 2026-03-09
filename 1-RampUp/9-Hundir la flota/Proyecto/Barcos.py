import Metodos_varios as mv
import Tablero as tb
import random
import time

# Lista general de barcos con sus posiciones y si están hundidos
barcos = [
    {'tipo': 1, 'coords': [], 'hundido': False},
    {'tipo': 1, 'coords': [], 'hundido': False},
    {'tipo': 1, 'coords': [], 'hundido': False},
    {'tipo': 1, 'coords': [], 'hundido': False},
    {'tipo': 2, 'coords': [], 'hundido': False},
    {'tipo': 2, 'coords': [], 'hundido': False},
    {'tipo': 2, 'coords': [], 'hundido': False},
    {'tipo': 3, 'coords': [], 'hundido': False},
    {'tipo': 3, 'coords': [], 'hundido': False},
    {'tipo': 4, 'coords': [], 'hundido': False}
]


def guardar_barco(tipo: int, coords: list[tuple[int, int]], ind:int):
    '''
    Añadir barco a la lista general de barcos
    '''
    
    barcos[ind]["coords"] = coords



def colocar_barcos(tablero:tuple[int, int], pos_aleatorio = False):
    '''
    Coloca los barcos de inicio en el tablero
    
    pos_aleatorio: 
        False --> los barcos se colocan de forma manual
        True --> los barcos se colocan de forma aleatoria
    '''
    
    tipos_barcos = [(1, 4)]#, (2, 3), (3, 2), (4, 1)]
    ind = 0
    
    for tipo, cantidad in tipos_barcos:
        if not pos_aleatorio:
            print(f"\nColoca {cantidad} barco(s) de tamaño {tipo}:")

            for _ in range(cantidad):
                while True:
                    entrada = input(f"Introduce {tipo} coordenadas separadas por espacio (ej: A1 A2 A3): ")
                    coords = entrada.split()
                    casillas = [mv.coords2index(coord) for coord in coords]
                    
                    if barco_valido(tablero, tipo, casillas):
                        pintar_barco(tipo, casillas, tablero)
                        guardar_barco(tipo, casillas, ind)
                        ind += 1 # Incrementamos índice para el próximo barco
                        print('Aquí')
                        tb.mostrar_tablero(tablero)
                        print("Barco colocado.\n")
                        
                        break
                    else:
                        print("Coordenadas inválidas. Inténtalo de nuevo.\n")
        else:
            for _ in range(cantidad):
                generar_barco_aleatorio(tipo, tablero)
    time.sleep(1)
                        


def pintar_barco(tipo:int, casillas:list[tuple[int, int]], tablero:tuple[int, int]):
    '''
    Cambia el estado de las casillas del tablero para convertirlas en barco
    '''
    
    for tile in casillas:
    
        match tipo:
            case 1:
                tb.pintar_casilla(tablero, tile, 'BARCO1')
                
            case 2:
                    tb.pintar_casilla(tablero, tile, 'BARCO2')
                
            case 3:
                    tb.pintar_casilla(tablero, tile, 'BARCO3')
                
            case 4:
                    tb.pintar_casilla(tablero, tile, 'BARCO4')



def barco_valido(tablero:tuple[int, int], tipo: int, casillas:list[tuple[int, int]]):
    '''
    Comprueba si las coordenadas de entrada forman un barco 
    válido del tamaño 'tipo' (1, 2, 3, 4).
    casillas es una lista de strings tipo ['A5', 'A6', 'A7']
    '''

    # Ordenar coordenadas para evitar problemas ((1,3), (1,1), (1,2) → (1,1), (1,2), (1,3))
    casillas.sort()
    
    # Índices fuera de rango (tablero 10x10)
    for casilla in casillas:
        for ind in casilla:
            if ind < 0 or ind > 9:
                print('Coordenadas fuera del tablero.')
                return False
    
    # Casilla está libre
    for casilla in casillas:
        print(tablero)
        print(casilla[0], casilla[1])
        if not tb.es_agua(tablero, casilla[0], casilla[1]):
            print('La casilla está ocupada.')
            return False
        
    # Tipo de barco = número de casillas
    if len(casillas) != tipo:
        print('Cantidad de coordenadas no corresponde al tipo de barco.')
        return False

    # Caso barco simple (1 casilla)
    if tipo == 1:
        return True
    
    
    # En caso de no ser un barco simple
    # Extraemos filas y columnas
    filas = [i[0] for i in casillas]
    cols  = [i[1] for i in casillas]
    
    # Debe estar en línea, no doblarse (por ejemplo forma 'L')
    hbarco = len(set(filas)) == 1 #alineado horizontal
    vbarco   = len(set(cols)) == 1 # alineado vertical
    if not (hbarco or vbarco):
        print('Coordenadas no alineadas')
        return False

    # Casillas consecutivas horizontalmente y verticalmente
    if hbarco:
        return cols == list(range(cols[0], cols[0] + tipo))

    if vbarco:
        return filas == list(range(filas[0], filas[0] + tipo))

    print('Coordenadas no consecutivas.')
    return False



def barco_hundido(tablero:tuple[int, int], barco):
    '''
    barco = {"tipo": n, "coords": ["A1","A2",...]}
    Devuelve True si se ha impactado en todas las casillas del barco
    '''
    
    for coord in barco["coords"]:
        fil, col = mv.coords2index(coord)
        if tablero[fil][col] != mv.IMPACTO:
            return False
    return True


# EXTRA
def generar_barco_aleatorio(tipo:int, tablero:tuple[int, int]):
    '''
    Genera aleatoriamente coordenadas de 
    un barco del tipo indicado
    '''
    
    while True:
        fila = random.randint(0, 9)
        col = random.randint(0, 9)
        orientacion = random.choice(["H", "V"])

        coords = []

        if orientacion == "H":
            if col + tipo > 10:
                continue
            for c in range(col, col + tipo):
                coords.append(f"{chr(fila + ord('A'))}{c+1}")

        else:  # Vertical
            if fila + tipo > 10:
                continue
            for f in range(fila, fila + tipo):
                coords.append(f"{chr(f + ord('A'))}{col+1}")

        # Validar que no se solapa con otros barcos
        if not tb.es_agua(tablero, coords[0], coords[1]):
            continue

        return coords
