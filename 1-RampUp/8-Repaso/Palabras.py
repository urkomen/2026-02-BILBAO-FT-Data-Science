import random
import Diccionario
import time
import Presentacion

def palabra_random():
    return random.choice(Diccionario.PALABRAS_2000)


def word_oculta(word:str):
    '''
    Crea palabra oculta
    donde se representan las 
    letras ocultas con '_'
    '''
    return ['_' for _ in range(len(word))]


def word_mostrar(word:list[str]):
    '''
    Muestra la palabra en pantalla
    '''
    print(' '.join(word))


def letter_comprobar(letra:str, word:str, word_result:str, lista_letras:list, vidas:int):
    '''
    Se busca la letra en la palabra oculta.
        - Si existe la muestra.
        - Si no existe, se pierde una vida y
        se muestra
    '''
    
    letra = letra.upper()
    # Guardamos letra en la lista de letras usadas
    lista_letras, vidas, letra_repetida = letras_usadas(letra, lista_letras, vidas)
    
    # Si es letra repetida, salimos
    if letra_repetida:
        print('Letras usadas: ', lista_letras)
        return word_result, lista_letras, vidas
        
    # Si usamos 6 vidas perdemos y salimos
    if vidas == 6:
        return word_result, lista_letras, vidas

    
    list_word = list(word)
    list_wordRes = list(word_result)
    
    if letra not in list_word:
                
        Presentacion.limpiar()
        print('Esa letra no está....')
        time.sleep(2) # Pausa dramática
        
        print(Diccionario.AHORCADO[vidas])
        time.sleep(0.6)
        print('Inténtalo de nuevo')
        
        vidas += 1
        time.sleep(0.6)        
        # Si usamos 7 vidas, perdemos y salimos
        if vidas ==7:
            return word_result, lista_letras, vidas
        
    else:    
        for i, let in enumerate(list_word):
            if let == letra:
                list_wordRes[i] = letra
        word_result = ''.join(list_wordRes)
        word_mostrar(word_result)
        
    print('Letras usadas: ', lista_letras)
    # Palabra oculta con las letras descubiertas, lista de letras usadas, vidas del usuario
    return word_result, lista_letras, vidas


def letras_usadas(letra:str, lista_letras:list, vidas:int):
    '''
    Lista de las letras usadas durante la partida
    Si repetimos letra, nos resta una vida
    '''
    letra_repetida = False
    if letra in lista_letras:
        Presentacion.limpiar()
        print('Esa letra ya me la has dicho...')
        time.sleep(1.5) # Pausa dramática
        print(Diccionario.AHORCADO[vidas])
        time.sleep(0.6)
        
        vidas += 1
        letra_repetida = True
        if vidas == 7: # Fin partida, salimos
            return lista_letras, vidas, letra_repetida
    else:
        lista_letras.append(letra.upper())
        lista_letras.sort()
        
    return lista_letras, vidas, letra_repetida