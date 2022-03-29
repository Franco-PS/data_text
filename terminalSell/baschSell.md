Que es un comando
- programa ejecutable (cualquier lenguaje)
- programa de la shell (la shell = programa y tienen funciones comando utilidad de la shell)
- programa externa a la shell ([como programar en shell](https://platzi.com/clases/bash-shell/))
- un alias

Manipulación de archivos y directorios

type-> naturaleza del comando | man-> manual| info->similar a manual| whatis ->descripción corta(no sirve en todos) | --help | file->da información  | tree -L #

<!-- -------------------------------------- -->
comandos de lectura archivo
cat 
head -> muestra inicio muestra las primeras 15 lineas|head -n #
tail ->muestra final 
lets

less -> puedes navegar de forma completa
/buscarPalabra
/u -> salir
<!-- --------------------------------------- -->

busqueda
locate -i -> busqueda la i no distiguira de mayusculas/minusculas
find      -> busca archivos/directorios 
find /home -name nombreArchivoCarpeta
find /home -type -df nombreArchivoCarpeta -> d= carpeta f= archivo



Permisos de usuarios

- archivo normal - |    
- directorio d     |
- link simbolico l | ln -s Documento/dato1/dato2 documentos (atajo)
- archivo de bloque especial b
<!-- guarda información de dispositivos externos usb/discos duros -->
Tipos de modos
| u= usuario | g= grup | o= otros   | a= para todos | -> Modo símbolico
| rwx        | rwx     | rwx        |
| rwx        | rwx     | rwx        |


                 |modo octal|Archivo|Directorio|
r= read     -> 1    -> 4    | lee   |lista contenido solo si también esta (x)
w= write    -> 1    -> 2    |permite escribir en un archivocrea pero solo los
                             dirctorios pueden crear|eliminar|cambiar los 
                             archivos.
x= executor!-> 1    -> 1    |archivo tratado como programa| permite entrada al directorio
rwx= 7

chmod -> permisos/          |   chmod u+w, r nombArchivo

chown -> cambiar al usuario |   chown root:root nombArcivo
                                chown root  nombArcivo


su root -> cambiar a usuario root
whoami = saber que usuario soy
<!-- ---------------------------- -->
Variables de entorno 

variables de entorno determinadas = printenv
alias l="ls -lh": estas son momentaneas 
----
alias
imprimir variables: 
echo $HOME -> 
echo $PATH -> tiene toda la ruta de binarios que ejecuta el sistema

