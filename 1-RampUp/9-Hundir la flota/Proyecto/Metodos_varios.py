import Tablero as tb

def coords2index(coord: str):
    """
    Convierte una coordenada tipo 'A5' en índices [fila, columna].
    A -> 0, B -> 1, ..., J -> 9
    1 -> 0, 2 -> 1, ..., 10 -> 9
    """
    coord = coord.strip().upper()
    fila = coord[0] # 'A'
    col = coord[1] # '5' o '10'
    
    for ind, valor in enumerate(tb.coordenadas):
        if valor == fila:
            fila_idx = ind
    col_idx = int(col) - 1

    return (fila_idx, col_idx)