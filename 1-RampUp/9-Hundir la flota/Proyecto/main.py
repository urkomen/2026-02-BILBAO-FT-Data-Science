import Tablero
import Barcos
import Fases_del_juego as fdj
# Tablero.path.append("./Proyecto")

def main():
    # Crear 3 tableros:
        # tablero_usu: Tablero con los barcos del usuario (se muestran los disparos del PC)
        # tablero_PC: Tablero con los barcos del PC (no se muestra al usuario)
        # tablero_PCoculto: Tablero con los disparos del usuario
    tablero_usu, tablero_PC, tablero_PCoculto = fdj.inicio_hundir()
    
    # Tablero usuario
    # fdj.configuracion_hundir(tablero_usu)
    # Tablero del PC
    fdj.configuracion_hundir(tablero_usu, tablero_PC, tablero_PCoculto)
    
    # Se escoge turno de inicio
    turno = fdj.quien_empieza()
    
    fdj.disparos_hundir(tablero_usu, tablero_PC, tablero_PCoculto, turno)
    
    
    
    



if __name__ == "__main__":
    main()





    