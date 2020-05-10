````
██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗
██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║
╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ██████╦╝██║░░██║██║░░██║██╔████╔██║
░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║
░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝

░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░
````

# Advertencia
Ésta herramienta sumamente destructiva, usarlo bajo sus propio criterio, una vez la pc está infectada, la unica solución es reinstalar windows,


# Información
* __Documentación:__ `10/05/20`
* __Versión actual:__ `0.4.0`
* __Lenguaje:__ `Python 3.7` <== _NOTA:_ Solo funciona en esa versión

# Caracteristicas BoOm
* El virus se replica en las siguientes directorios:
    * `'C:\Users\' + UserName +'\Documents'`
    * `'C:\Users\' + UserName +'\Music'`
    * `'C:\Users\' + UserName +'\Videos'`
    * `'C:\Users\' + UserName +'\Pictures'`
    * `'C:\Users\' + UserName +'\Downloads'`
    * `'C:\Users\' + UserName +'\AppData\Roaming\VirusBomb'`
    * `'C:\Users\' + UserName +'\AppData\LocalLow\VirusBomb'`
    * `'C:\Users\' + UserName +'\AppData\Local\VirusBomb'`
* __Oculto:__ El virus se oculta en la siguiente dirección
    * `C:\Users\Public\EXEBombWindows\Virus\NoMeBorres`
* __Infección:__ El virus se replicará en las carpetas mencionadas en un bucle infinito, podría llegar a saturar el disco duro a un 100% y llenar el disco duro por completo `No borrará datos, solo llenará el espacio libre disponible`
* __Bloqueo de Perifericos:__ Se deshabilitará los eventos del Mouse y Teclado 
* __StartUp:__ Sobrescribe el registro, causando que se autoinicie en todos los `usuarios` existentes o solo en la actual.
* __Sistema inteligente de BoOm:__ Al ejecutarlo por primera vez, el virus solo se ocultará en el sistema y modificará el registro para que se autoinicie, luego de este proceso el virus se cerrará dejando la computadora intacta. La explosión del virus comienza en la siguiente vez que la PC infectada inicie sesión, el virus recien hará boOm.
* __CPU 100%:__ El virus ejecutará muchos procesos independientes que lograrán saturár el procesador.
* __RAM 100%:__ Por los distintos procesos que se realizarán tambien la RAM terminará usandose

__Librerías utilizada:__
__Lib:__  [KeyAndMouse_Block](https://github.com/SebastianEPH/KeyAndMouse_Block) <== Bloquea los eventos del teclado y el mouse