import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="C:/Users/Cliente Especial/Downloads/"
to_dir = "C:/Users/preet/Desktop/Arquivos_Documentos" 
# Crie a pasta "Arquivos_Documentos" em sua área de trabalho e atualize o caminho de acordo. 
dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }
class FileMovementHandler(FileSystemEventHandler):
    def oncreated(self,event):
        print(event)
        name,extension=os.path.splitext(event.src_path)
        print(name)
        print(extension)
        time.sleep(1)
        for key,value in dir_tree.items():

            if extension=="":
                continue
            if extension in [".gif",".png",".jpg"]:
                path1=from_dir+key
                path2=to_dir
                path3=to_dir+key
                if os.path.exists(path2):
                    print("movendo "+key+"...")
                    shutil.move(path1,path3)
                else:
                    os.makedirs(path2)
                    print("movendo "+key+"...")
                    shutil.move(path1,path3)
event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("executando")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()