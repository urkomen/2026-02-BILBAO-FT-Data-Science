import Tablero
import Barcos
import Fases_del_juego as fdj
# Tablero.path.append("./Proyecto")

def main():
    tablero = fdj.inicio_hundir()
    
    fdj.configuracion_hundir(tablero)
    
    fdj.disparos_hundir(tablero)
    
    
    
    



if __name__ == "__main__":
    main()





    