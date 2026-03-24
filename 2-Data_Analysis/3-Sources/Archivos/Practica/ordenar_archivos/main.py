import funciones as fun
import variables as var


def main():
    ruta_origen = var.ruta_descarga
    ruta_destino = var.ruta_ordenados
    
    fun.move_files(ruta_origen, ruta_destino)




if __name__ == "__main__":
    main()

