tablero = [
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
]

def crear_tablero(tamaño=10): 
    '''
    Crea tablero de juego
    '~' representa agua
    Tamaño por defecto 10
    '''
    return [['~' for _ in range(tamaño)] for _ in range(tamaño)]


def pintar_tablero(tablero:list[list[str]]):
    '''
    Muestra el tablero en pantalla
    '''
    for fila in tablero:
        print(' '.join(fila))



    
    
    



def pintar_disparos():
    pass



def coords2index(coord: str):
    coord = coord.strip().lower()
    fila = coord[0]
    col = coord[1:]

    fila_idx = ord(fila) - ord('a')
    col_idx = int(col) - 1
    
    # Tablero de 10x10. Si una casilla cae fuera devuelve error
    if not (0 <= fila_idx < 10 and 0 <= col_idx < 10):
        raise ValueError(f"Coordenada fuera del tablero: {coord}")


    return [fila_idx, col_idx]

# coords = (('A',1))
# indice = [coords2index(coord) for coord in coords]
# print(indice)










AGUA = '🟦'
BARCO = '⬜'
IMPACTO = '🟥'

def pintar_tab_Emojis(tablero):
    for fila in tablero:
        print(' '.join(fila))