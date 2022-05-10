# Base de datos

Base de datos: es el almacenamiento de datos puntuales, que se ocupa para convertir la información
SQL (Structured Query Language)

Relation Base Date (RBD)
No Onlyl Relation Base Date (NORBD)

### RDBMS (Relational Database Management System)
- MySQL
- Posgress
- Oracle
### Cliente gráfico
- mySQL -> Workbench

## Diseño de Base de datos
Existen dos potentes motores que ofrece MySQL, que se clasifican según su velocidad y escritura.
Es muy importante encontrar el funcionamiento predominante de nuestro sistema.
- ¿la escritura de datos sera seguida?
- ¿Necesitamos hacer consultas constantemente?
- Es importante cumplir con ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad)?


InnoDB: escritura/lectura es más lenta.
MyISAM: escritura/lectura es rápida.
<!-- las tablas se ocupan con dos propósitos -->
- catalogo: la tabla crecerá en un orden lento (InnoDB)
- operación: se enfoca en la lectura accede más veces al disco duro (MyISAM)

<!-- --------------------------------------------- -->

Entidades = objetos: Fuertes | debíles | artificiales
tip: 
  plural-ingles
  Lo que necesita una tabla (id)
atributos = llave primaria | compuestos | multi-valuados | 

Normalización (los 12 mandamientos de Job)
1. primera forma: atributos no repetidos
2. segunda forma: cada campo dependera de una clave única
3. tersera forma: los campos no clave deben de tener dependencias
4. los campos multi-valuados, se identifican con clave única

## Tipo de datos

cadena                      | núm                  | fecha/hora     | lógicos
char(#)-memoría estatica    | int - integer        | date           | boolean
varchar(#)-memoría dinámica | bigint - muy grande  | time
text - cadena inmensa       | smallint -corto < 90 | datatime
                            | decimal (n,s)n-num, 
                            |  s-num de decimales   | timestamp |
                            | numeric (n,s)| |

## Constraint
Son restricciones que nos ayuda a asegurar la integridad de datos almacenados 
not null (nn)
unique (uq)
primary key (pk)
foreign key (fk)
check
default
index

Diagramas
entidad relación
cardinalidad: 

## Comandos SQL
- DDL Data Definition Language: _estructura inicial_; create | alter | drop
- DML Data Manupulation Language: manipula contenido; insert | update | delete | select


Teoria de conjuntos