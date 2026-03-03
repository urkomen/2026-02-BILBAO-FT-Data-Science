import math # Funciones matemáticas

def dia_semana(ndia:int)->str:
    '''
    Convierte números del 1 al 7 en nombres de los dias de la semana
    '''
    
    match ndia:
        case 1:
            return 'Lunes'
        case 2:
            return 'Martes'
        case 3:
            return 'Miércoles'
        case 4:
            return 'Jueves'
        case 5:
            return 'Viernes'
        case 6:
            return 'Sábado'
        case 7:
            return 'Domingo'
        case _:
            return 'Nono, solo tenemos 7 días de la semana (numérico del 1 al 7)'



def piramide(n):
    '''
    Crea una pirámide invertida de números desde el número de entrada
    '''
    
    for inicio in range(n, 0, -1):
        print(*range(inicio, 0, -1))  



def comparar(a, b):
    '''
    Se comparan los números de entrada.
    Posibles salidas:
        --> a es mayor que b
        --> a es menor que b
        --> a y b son iguales
    '''
    
    
    if a < b:
        return f'{a} es menor que {b}'
    if a > b:
        return f'{a} es mayor que {b}'
    return 'Son iguales'
    



def contador_letras(texto, letra)->int:
    '''
    Se cuentan las veces que aparece la letra en el texto
    '''
    
    return texto.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').count(letra.lower())



def contador_texto(texto:str)->dict:
    '''
    Se crea un diccionario con el conteo de todas las letras del texto de entrada
    '''
    
    texto2 = texto.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    dic_letras = {}
    for elem in texto2:
        dic_letras[elem] = texto2.count(elem)
    return dic_letras



def add_rmv_list(lista, operacion, item = None):
    '''
    Se añaden o eliminan elementos en una lista
    '''
    
    if item == None:
        print('No sé qué elemento debo añadir o eliminar')
        return
    else:
        if operacion.lower() == 'add':
            lista.append(item)
            return lista
        elif operacion.lower() == 'remove':
            try:
                lista.remove(item)
                return lista
            except:
                pass
        else:
            print('No reconozco el comando')
            return
        


def frase(*args):
    '''
    Recibe un número arbitrario de palabras, 
    y devuelve una frase completa, separando 
    las palabras con espacios
    '''
    
    # for elem in args:
    #     frase = ' '.join(elem)
    # return frase
    return ' '.join(args) # join por dentro ya itera sobre el iterable de entrada



def fibonacci(n):
    '''
    Se obtiene el número en la posición n de la serie de Fibonacci
    '''
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def a_cuad(lado:float)->float:
    '''
    Se calcula el área de un cuadrado
    '''
    
    return lado**2



def a_tri(base:float, altura:float)->float:
    '''
    Se calcula el área de un triángulo
    '''
    
    return base * altura / 2



def a_circ(radio:float)->float:
    '''
    Se calcula el área de un círculo
    '''

    return math.pi * radio**2
