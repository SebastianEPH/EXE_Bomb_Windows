````
██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██████╗░░█████╗░███╗░░░███╗██████╗░
██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ██╔══██╗██╔══██╗████╗░████║██╔══██╗
╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ██████╦╝██║░░██║██╔████╔██║██████╦╝
░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░

░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░
````

# Advertencia
Ésta herramienta sumamente destructiva, usarlo bajo sus propio criterio, una vez la pc está infectada, la unica solución es reinstalar windows. 

__[Solo fines educativos, Todo el código está completamente comentado]__


# Información
* __Documentación:__ `10/05/20`
* __Versión actual:__ `1.0`
* __Estado:__ `Terminado y estable`
* __Plataforma:__ `Windows all`
* __Lenguaje:__ `Python 3.7` <== _NOTA:_ Solo funciona en esa versión

# Contenido de Repositorio
![Contenido del repositorio](https://i.imgur.com/1bBiYVg.png)

* __Folder CompiladoEXE :__ Contiene `EXE_Bomb_Windows.exe`  <== EXE Destructivo [Cuidado con ejecutarlo]
* __Compile.bat :__ Convierte `EXE_Bomb_Windows.py` a `EXE_Bomb_Windows.exe`
* __EXE_Bomb_Windows.py :__ Codigo del repositorio
* __information.txt :__ Propiedades del programa. `Se puede modificar a su gusto`
* __README .md :__ `Documentación`
* __SEPH.ico :__ `Icono del dueño del repositorio`


# Caracteristicas
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
* __Ejecución en segundo plano:__ Todo el proceso se realiza en segundo plano `[cuando está compilado]`
* __StartUp:__ Sobrescribe el registro, causando que se autoinicie en todos los `usuarios` existentes o solo en la actual.
* __Sistema inteligente de BoOm:__ Al ejecutarlo por primera vez, el virus solo se ocultará en el sistema y modificará el registro para que se autoinicie, luego de este proceso el virus se cerrará dejando la computadora intacta. La explosión del virus comienza en la siguiente vez que la PC infectada inicie sesión, el virus recien hará boOm.
* __CPU 100%:__ El virus ejecutará en simultaneo muchos procesos exponencial independientes de calculos mátematicos, lo cual en segundos saturará tu procesador.  `Probado en un Ryzen 52400g`
* __RAM 100%:__ Por los distintos procesos que se realizarán tambien la RAM terminará usandose
* __Ejecuta programas:__ Abrirá una cantidad de programas predeterminados como paneles de control, word, block de notas, etc. `En desarrollo...`


# Compilación
* Solo hay que ejecutar el archivo `Compile.bat` y empesará el proceso de compilación, se recomienda no cambiar de nombre del archivo.

    ![](https://i.imgur.com/7hMN0aW.png)
* Y al finalizar tendrá el archivo.

    ![](https://i.imgur.com/SHKHeKl.png)

__Recursos utilizados:__
* __Función:__  [KeyAndMouse_Block](https://github.com/SebastianEPH/KeyAndMouse_Block) <== Bloquea los eventos del teclado y el mouse
* __Función:__ [100 %CPU](https://github.com/SebastianEPH/CPU_Stress) <= un conjunto de calculos básicos matemáticos y bucles exponenciales.

<!-- Creador  -->
---
## By SebastianEPH
- [Github](https://github.com/SebastianEPH)
- [Facebook](https://www.facebook.com/SebastianEPH)
- [Linkedin](https://www.linkedin.com/in/sebastianeph/)
- [Telegram](https://t.me/sebastianeph)
