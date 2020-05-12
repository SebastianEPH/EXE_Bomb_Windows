echo off
pyinstaller --clean --distpath "CompiladoEXE"  --upx-dir upx-* --windowed   -F --onefile --icon SEPH.ico --version-file information.txt EXE_Bomb_Windows.py

:cmd
pause null 
