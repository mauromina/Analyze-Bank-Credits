
import os
from subprocess import call


def Installrequirements():
    print("Necesita Otorgar Permisos de Administrador")
    print("=============================================================")
    print("Iniciando instalacion de Requerimientos")
    #Dependencia de Redis
    os.system("sudo apt install redis-server")
    #Dependence curl
    os.system("sudo apt install curl")
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
    print("Carga servicio Web")
    call(["source environment/bin/activate"])


def LoadindDate():
    print("Carga Datos de Entranamiento")
    call(["curl", "-X GET -H ","X-API-TOKEN: FOOBAR1", "-H ", "Content-Type: application/json; charset=utf-8", "http://127.0.0.1:5000/train", "-d", " '{","data-url": "sample-data.csv"}'"])

def SearchRelation():
    idItem = raw_input("Ingrese un Id de articulo para encontrar similitudes: ")


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
        RunProjectWeb() # Lanza el servicio web en la direccion 127.0.0.1:5000
        LoadindDate() # Carga el archivo CVS para la creacion de las matrices

WellcomeMessage()
