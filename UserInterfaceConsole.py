
import os
from subprocess import call


def Installrequirements():
    print("Necesita Otorgar Permisos de Administrador")
    print("=============================================================")
    print("Iniciando instalacion de Requerimientos")
    #Dependencia de Redis
    os.system("sudo apt install redis-server")
    #Dependencia de python py
    os.system("sudo apt install python-pip")
    #Dependencia de virtualenv
    os.system("sudo apt install virtualenv")
    #Dependencia de Create environment virtualenv
    os.system("virtualenv environment")
    #Active environment virtual
    os.system("source environment/bin/activate")
    #Install requirements in virtualenv
    os.system("pip install -r EngineSimilarityCosine/requirements.txt")
    print("=============================================================")
    print("-+-+-+-+-+ instalacion completada:")
    RunProjectWeb()

def RunProjectWeb():
    call(["ls", "-l"])
    os.system("source environment/bin/activate")
    os.system("python EngineSimilarityCosine/web.py")

def WellcomeMessage():
    print("Bienvenido al sistema  de recomendaciones basado en contenido.")
    print("=============================================================")
    print("Antes de iniciar recuerde tener instalado python-pip")
    print("El instalador automatico solo funciona en distribuciones basadas en Ubuntu 16.2 o debian")
    print("Ustede desea instalar los requerimientos necesarios para le ejecucion de la aplicaion")
    installBoolean = raw_input(" [si or no]: ")
    installBoolean = installBoolean.lower()
    if (installBoolean is "si") or "yes" or "y" or "s":
        Installrequirements()
    else:
        print(" +-+-+- Lanzar App +-+-+-")

WellcomeMessage()
