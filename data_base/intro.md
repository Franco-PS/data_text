Base de datos

Base de datos: es el almacenamiento de datos puntuales, que se ocupa para convertir la información

Relation Base Date (RBD)
No Onlyl Relation Base Date (NORBD)

Tipos de tablas
MyISAM: es rápida (transacciones uno a uno)
InnoDB: es más lenta.
<!-- las tablas se ocupan con dos propósitos -->
- catalogo: la tabla crecere en un orden lento
- operación: se enfoca en la lectura (accede más veces al disco duro)

<!-- --------------------------------------------- -->

Entidades = objetos: Fuertes | debíles | artificiales
tip: 
  plural-ingles
  Lo que necesita una tabla (id)
atributos = llave primaria | compuestos | multi-valuados | 

Normalización (los 12 mandamientos de Job)
1. forma normal: atributos no repetidos
2. segunda forma: cada campo dependera de una clave única
3. tersera forma: los campos no clave deben de tener dependencias
4. los campos multi-valuados, se identifican con clave única

cadena | núm | fecha/hora | lógicos
char(#)-memoría estatica | int - integer           | date | boolean
varchar(#)-memoría dinámica | bigint - muy grande  | time
text - cadena inmensa       | smallint -corto < 90 | datatime
                            | decimal (n,s)n-num, s-num de decimales | timestamp |
                            | numeric (n,s)| |

constraint
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

SQL
- DDL Data Definition Language: estructura inicial; create | alter | drop
- DML Data Manupulation Language: manipula contenido; insert | update | delete | select


Teoria de conjuntos