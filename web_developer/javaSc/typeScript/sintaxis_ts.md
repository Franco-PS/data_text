# TypeScript
es un super-conjunto que compila a javaScript 
con typescript muestra los errores al compilar
## Análisis de código estático 
  - Static analysis runs: análisis de código automáticamente
  - Unit tests: se realizan pruebas
  - Integration tests:  tests que comprueba todo
  - Code review: el código se pasa a verificar por otro equipo el cual verifica (si se sigue las normas/buenas practicas)
  

Tipado
- alto nivel: legible para humanos
- puedes prevenir bugs de forma más sencilla

## Instalación local:
- crea .editoconfig | .gitignore | src
- .gitignore -> colocar código (ignorar)[https://www.toptal.com/developers/gitignore] (Windows/linux/mac node)
- .editorconfig -> ayuda a tener una configuración estandar entre todo el equipo (plugin: EditorConfig for VS Code)
- carpeta src -> source la fuente del código
    npm init
    npm install typescript --save-dev
    npx tsc --version       -> conocer si se instalo bien
    tsc -> typescript system compiler
    crea index.js/ts
        para activar el analizador de código .js escribe en la primera linea: //@ts-check (en los archivos .ts corren automáticamente)

<!-- análisis del código -->

Compilador/transpiling 
en la web solo ejecuta javaScript, 
- de .ts -> .js   npx tsc src/archivo.ts
- de .js -> .ts   npx tsc src/archivo.js
  Tener cuidado al compilar a que version de js/ts --target es6
  pero todos los .js se colocan en otra carpeta diferente a src -> dist (distribution)
    npx tsc src/*.ts --target es6 --outDir dist

### TSConfig.json
Es un archivo que nos permite configurar la compilación (automática)
  npx tsc --init
    - se deseleccionara y colocara las carpetas que queremos que lea: 
    "outDir": "./dist", | "rootDir": "./src",
    - para que corra el archivo: npx tsc
    - compilador automáticamente: npx tsc --watch
    para parar ejecución "Ctrl + c"


## tipado TypeScript
  javaScript             |        TypeScript
const productPrice = 12; | const productPrice: number = 12; -> se define variable : number 

inferir datos, en ts al asignar valor a las variables el motor de ts infiere el tipo 
de datos, (se recomienda, solo en casos específicos se asignara de forma especifica el tipo de dato)
1. Nos ayuda a conocer los métodos que ocupa cada tipo de dato.

### number


