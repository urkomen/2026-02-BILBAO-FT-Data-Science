import Tablero




def colocar_barcos(tipo:int, coords:list[list]):
    # Convertir coordenadas en índices de la matriz tablero
    indice = [Tablero.coords2index(coord) for coord in coords]
    
    match tipo:
        case 1:
            #pintar barco en la coordenada (coords[0][0],coords[0][1])
            pass
        case 2:
            #pintar barco desde (coords[0][0],coords[0][1]) a (coords[1][0],coords[1][1])
            # Verificar que son adyacentes y distancia de 2 posiciones
            pass
        case 3:
            #pintar barco (coords[0][0],coords[0][1]) a (coords[1][0],coords[1][1])
            # Verificar que son adyacentes, en línea y distancia de 3 posiciones
            pass
        case 4:
            #pintar barco (coords[0][0],coords[0][1]) a (coords[1][0],coords[1][1])
            # Verificar que son adyacentes, en línea y distancia de 4 posiciones
            pass


def comp_coord_barco(tipo: int, coords: list[str]):
    '''
    Comprueba si las coordenadas de entrada forman un barco 
    válido del tamaño 'tipo' (1, 2, 3, 4).
    coords es una lista de strings tipo ['A5', 'A6', 'A7']
    '''

    # Convertir a índices
    indices = [Tablero.coords2index(c) for c in coords]

    # Ordenar para evitar problemas (A3, A1, A2 → A1, A2, A3)
    indices.sort()

    # Extraer filas y columnas
    filas = [i[0] for i in indices]
    cols  = [i[1] for i in indices]
    
    # Comprobar número de casillas con el tipo de barco
    if len(indices) != tipo:
        return False

    # Caso barco simple (1 casilla)
    if tipo == 1:
        return True

    # En caso de no ser un barco simple
    # Comprobar alineación. Debe estar en línea, no doblarse (por ejemplo forma 'L')
    alineado_horizontal = len(set(filas)) == 1
    alineado_vertical   = len(set(cols)) == 1

    if not (alineado_horizontal or alineado_vertical):
        return False

    # Comprobar contigüidad
    if alineado_horizontal:
        # columnas consecutivas
        return cols == list(range(cols[0], cols[0] + tipo))

    if alineado_vertical:
        # filas consecutivas
        return filas == list(range(filas[0], filas[0] + tipo))

    return False