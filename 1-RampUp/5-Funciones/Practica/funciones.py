import math


# Faltan comentarios, no me ha dado tiempo a ponerlos
def dia_semana(ndia:int)->str:
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
    for inicio in range(n, 0, -1):
        print(*range(inicio, 0, -1))  


def comparar(a, b):
    if a < b:
        return f'{a} es menor que {b}'
    if a > b:
        return f'{a} es mayor que {b}'
    return 'Son iguales'
    

def contador_letras(texto, letra):
        return texto.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').count(letra.lower())


def cont_dic(texto:str)->dict:
    dic_letras = {}
    for elem in texto:
        dic_letras[elem] = texto.count(elem)
    return dic_letras


def add_rmv_list(lista, operacion, item = None):
    if item == None:
        print('No sé qué elemento debo añadir o eliminar')
        return
    else:
        if operacion.lower() == 'add':
            lista.append(item)
            return lista
        elif operacion.lower() == 'remove':
            lista.remove(item)
            return lista
        else:
            print('No reconozco el comando')
            return
        

def frase(*args):
    for elem in args:
        frase = ' '.join(elem)
    return frase


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def a_cuad(lado):
    return 4 * lado

def a_tri(base, altura):
    return base * altura / 2

def a_circ(radio):
    return math.pi * radio**2
