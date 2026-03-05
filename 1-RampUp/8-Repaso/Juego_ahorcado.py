import Presentacion
import Palabras

def juego_ahorcado(word:str, word_oculta:str, vidas:int, lista_letras:list):
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