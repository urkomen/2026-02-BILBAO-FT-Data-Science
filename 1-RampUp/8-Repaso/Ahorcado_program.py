import Presentacion
import Palabras
import time

def main():
    # PRESENTACION JUEGO
    Presentacion.intro_ahorcado()
    
    
    # Inicializamos variables
    vidas = 0 # Vidas de usuario (al llegar a 6 muere)
    lista_letras = [] # Lista de letras usadas
    
    
    # Generar palabra oculta
    # word = input('¿Cuál es la palabra oculta?').upper()
    word = Palabras.palabra_random().upper()
    # word = 'VELOCIDAD'
    # word = 'V'
    
    # print(word) # Mostrar solución para las pruebas
    word_oculta = Palabras.word_oculta(word)

    
    while vidas < 6:
        # Mostramos palabra oculta
        Palabras.word_mostrar(word_oculta)
        
        # Recoger letra del usuario, en mayúsculas y sin tildes
        let = input('¿Qué letra escoges?').upper().replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U')
        
        # Comprobar si la letra está en la palabra
        word_oculta, lista_letras, vidas = Palabras.letter_comprobar(let, word, word_oculta, lista_letras, vidas)
        
        if '_' not in word_oculta:
            Presentacion.outro_victoria()
            break


    if vidas == 6:
        Presentacion.outro_derrota()



if __name__ == "__main__":
    main()
