

def coords2index(coord: str):
    """
    Convierte una coordenada tipo 'A5' en índices [fila, columna].
    A -> 0, B -> 1, ..., J -> 9
    1 -> 0, 2 -> 1, ..., 10 -> 9
    """
    coord = coord.strip().lower()

    fila = coord[0]          # 'a'
    col = coord[1:]          # '5' o '10'

    fila_idx = ord(fila) - ord('a') # Convertimos a unicode y restamos con nuestro valor '0'
    col_idx = int(col) - 1

    return (fila_idx, col_idx)