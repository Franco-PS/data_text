Pila de ejecución (Call Stack)/ Pila de contexto/ Pila de registro 
Sirve para conocer en donde nos encontramos por donde paso y hacia 
donde va la siguiente ejecución ocupando una pila(apilación)=LIFO


LIFO (Last In First Out)
En cada llamada de una función se almacena en un registro (frame) y estos contiene:
    • Contexto de ejecución (scope)
    • Contexto (window | this)
    • Argumentos de funciones/ variables(var)
    • Nombre de la función
    • Linea Próxima a ejecutar

El alcance que tiene una variable/expresión dentro del entorno que se ejecuta se le conoce como contexto actual de ejecución
Scope global    |   Scope local
                |   scope función
                |   -limita la función aún si se trata de var
                |   scope bloque
                |   -solo se accede desde el bloque

Ambito lexico: Determina como y en donde está nuestro código

El contexto de ejecución
 >--tokenización|parsing | Generación de código-→ ejecución

tokenización: separa var coco= 7;→ var|coco| =| 7 | ; |

ejecución global 1ra fase de creación/ 2da fase de ejecución,
1ra fase: se crean objetos window, this  y si existen funciones o variables (var) se les reserva un espació en memoria (hoisting) , y se les asigna un valor especial [undefined]( se declara la variables pero sin su asignación)
2da fase: se asigna el valor a las variables globales y se invocan las funcioness
<!-- ------------------------------ -->
Primitivos
let suma= 5+5; //10
let suma2 = suma // se copia sin ninguna relación entre ambas

Objetos
todos los objetos guardan sus valor asignado en un espacio: (HEAP- memoria dinámica) se le Referencia un valor dfs458
let Dato= { ----: ….; ----:….;}
sj se modifica algún valor se modifica en el HEAP