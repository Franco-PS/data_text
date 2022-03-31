JavaScript
Lenguaje devilmente tipado
*sintaxis: Son reglas que definen la estructura

declaración | asignación
var/let/const nameVariable = data asignation
palablas clave

- Operadores: expresiones que por si mismos producen nuevos valores (5+5->10)
- Sentencias: marcan el final de una instrucción (;) 
  - sentencias de expresión
    - let dato= funtion(){}; | let dato= 4*5;
  - sentencias vacias
  - sentencias de bloque 
  <!-- - dichas no tienen ";" -->
  - {} agrupan
  - if(){}
  - funtion(){}

<!-- ---------------------------------------- -->
Tipos de datos
Datos primitivos
- string|number|boolean
- Null:valor vació/nulo
- Underfined: valor no asignado/desconocido
  *symbol(EMACS15)
Datos de objetos
- Objetos   |   fechas
- funciones |   expresiones regulares
- array     |   
<!-- --------------------------------------- -->
Operadores 

``->backticks (comillas invertidas)pueden ejecutar variables = ${}
Oparadores matemáticos
+ - x / %-resto **-exponente
Operadores 
< > = == != ===-> tipo
Operadores lógicos
or  ||  -> encuentra el primer valor verdadero se detiene y retorna dicho valor
and &&  -> si encuentra falso se detiene y retorna valor TODO: completar
!not-> valor contrario al que tiene

Coerción de tipos:
Se trata de como el motor del navegador forza los valores para completar las operaciones
to string   |   to number   |   boleano a number
value= string(2) -> //"2"   |   "6"/"3"->3  |   0/"  ", null, undefined y NAM -> false
concadenación
let data= "my"+"string"     |   let data= Number("123")->123      |   1/"0"/"--"-> true
"1"+1 -> 11                 |   let data= Number("hola")->nan     |   
2+2+"1" -> 41               |   let data= Number(true/false)->1/0 |   
"2"+2+1 -> 221              |   

incremento ++| decremento --
solo a variables y es de uno en uno: 
let data= 1         |let data= 1         |
let a= ++data -> 2  |let a= data++ -> 1  | primero imprime y despues suma

<!-- ----------------------------------- -->

condicionales
if(true){
    //body
    else/ else if{}
}

operador ternario 
let data= condition ? value1 : value2 ;

switch
switch(x){
    case 'value1':-.> if(x === 'value1')
    //body
    [breack]-> sino existe se seguira ejecutando
    <!-- agrupación de clases -->
    case 'value2':
    case 'value3':
    alert('incorrecto');
    alert('toma');
}

let data= (value1 > 'value')? 'value2':
    (value1 > 'value')? 'value2':
    (value1 > 'value')? 'value2':
    (value1 > 'value')? 'value2':
    'valueN';

<!-- --------------------------------------- -->

while
Mientras que sea verdadero se seguirá ejecutando
while(condition){
    //body
}

for(begin ; condition ; step){
    //body
}

<!-- ----------------------------------------- -->
funtion
funtion name_funtion(parameter1, parameterN....){
    //body
    //return    -> indispensable para que la función devuelva
}

llama a la function
name_funtion(arguments)
<!-- tanto los parametros/argumentos debén de ordenarse con sus pares parmetro1-argumento1 .. -->