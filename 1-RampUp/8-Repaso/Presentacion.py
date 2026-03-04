import time
import os
import Diccionario

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro_ahorcado():
    limpiar()
    for linea in Diccionario.titulo:
        print(linea)
        time.sleep(0.05)

    time.sleep(0.5)
    print('\nBienvenido al legendario juego del Ahorcado...\n')
    time.sleep(1)

    print('Preparando la horca...\n')
    time.sleep(1)
    
    limpiar()
    print(Diccionario.AHORCADO_0)
    
    for escena in Diccionario.AHORCADO:
        limpiar()
        print(escena)
        time.sleep(0.4)

    limpiar()
    print(Diccionario.AHORCADO_0)
    print('''
    ¡La horca está lista!
    ''')

    time.sleep(1)
    print('\nTu misión es simple: ADIVINAR la palabra antes de que sea demasiado tarde.')
    time.sleep(1.2)
    print('\n¿Listo para jugar?\n')
    time.sleep(0.8)

def outro_victoria():
    import time
    import os

    os.system("cls" if os.name == "nt" else "clear")
    
    for linea in Diccionario.victoria:
        print(linea)
        time.sleep(0.05)

    print("\n¡HAS GANADO LA PARTIDA!\n")
    time.sleep(0.8)

    mensaje = "El ahorcado ha sido salvado... ¡por ahora!"
    for c in mensaje:
        print(c, end="", flush=True)
        time.sleep(0.03)

    time.sleep(1)
    print("\n\nCelebrando tu victoria...\n")
    time.sleep(0.5)

    efectos = ["✨", "🎉", "🔥", "💥", "⭐", "🏆"]
    for _ in range(20):
        print(" " * 10 + efectos[_ % len(efectos)])
        time.sleep(0.05)

    print("\n¡Eres un auténtico maestro del ahorcado!\n")


def outro_derrota():
    import time
    import os

    os.system("cls" if os.name == "nt" else "clear")

    for linea in Diccionario.derrota:
        print(linea)
        time.sleep(0.05)

    print("\nHas perdido la partida...\n")
    time.sleep(0.8)

    mensaje = "La horca ha reclamado su víctima."
    for c in mensaje:
        print(c, end="", flush=True)
        time.sleep(0.03)

    time.sleep(1.2)
    print("\n\nMostrando el destino final...\n")
    time.sleep(0.6)

    # for linea in Diccionario.AHORCADO[-1]:
    #     print(linea)
    #     time.sleep(0.2)
    limpiar()
    print(Diccionario.AHORCADO_0)
    
    for escena in Diccionario.AHORCADO:
        limpiar()
        print(escena)
        time.sleep(0.2)

    time.sleep(1)
    print("\nLa próxima vez quizá tengas más suerte...\n")