import os
import shutil
import variables as var


def move_files(ruta_origen, ruta_destino):
    for i in os.listdir(ruta_origen):
        if i.endswith(var.img_types): # Quedarnos los que terminan en '.jpg', '.jpeg', '.png', '.svg', '.gif'
            shutil.copy(ruta_origen + i, ruta_destino + var.img)
            os.remove(ruta_origen + i)
            
        elif i.endswith(var.software_types): # Quedarnos los que terminan en '.exe', '.py','.ipynb'
            shutil.copy(ruta_origen + i, ruta_destino + var.soft)
            os.remove(ruta_origen + i)
            
        elif i.endswith(var.doc_types): # Quedarnos los que terminan en '.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx'
            shutil.copy(ruta_origen + i, ruta_destino + var.doc)
            os.remove(ruta_origen + i)
            
        else: # Quedarnos el resto de archivos
            shutil.copy(ruta_origen + i, ruta_destino + var.otros)
            os.remove(ruta_origen + i)