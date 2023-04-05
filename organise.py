import os
import shutil
fromdir="C:/Users/Cliente Especial/Downloads/PRO_1-1_C102_AtividadeDoAluno1-main/PRO_1-1_C102_AtividadeDoAluno1-main/"
todir="C:/Users/Cliente Especial/Downloads/PRO_1-1_C102_AtividadeDoAluno1-main/PRO_1-1_C102_AtividadeDoAluno1-main/guardaImagens/"
listadearquivos=os.listdir(fromdir)
print(listadearquivos)
for i in listadearquivos:
    name,extension=os.path.splitext(i)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in [".gif",".png",".jpg"]:
        path1=fromdir+i
        path2=todir
        path3=todir+i
        if os.path.exists(path2):
            print("movendo "+i+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("movendo "+i+"...")
            shutil.move(path1,path3)