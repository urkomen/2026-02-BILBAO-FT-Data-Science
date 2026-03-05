import Presentacion
import Palabras
import Diccionario as dic
import Juego_ahorcado as jarc

def main():
    # PRESENTACION JUEGO
    Presentacion.intro_ahorcado()   
    
    # Generar palabra oculta
    # word = input('¿Cuál es la palabra oculta?').upper()
    word = Palabras.palabra_random().upper()
    # word = 'VELOCIDAD'
    # word = 'V'
    
    # print(word) # Mostrar solución para las pruebas
    word_oculta = Palabras.word_oculta(word)

    jarc.juego_ahorcado(word, word_oculta, dic.vidas, dic.lista_letras)
    



if __name__ == "__main__":
    main()
