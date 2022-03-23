Base de datos

Relation Base Date (RBD)
No Onlyl Relation Base Date (NORBD)

Entidades = objetos: Fuertes | debíles | artificiales
atributos = llave primaria | compuestos | multi-valuados | 

Normalización (los 12 mandamientos de Job)
1. forma normal: atributos no repetidos
2. segunda forma: cada campo dependera de una clave única
3. tersera forma: los campos no clave deben de tener dependencias
4. los campos multi-valuados, se identifican con clave única

cadena | núm | fecha/hora | lógicos
char(#)-memoría estatica | int - integer | date | boolean
varchar(#)-memoría dinámica | bigint - muy grande | time
text - cadena inmensa | smallint -corto < 90 | datatime
  | decimal (n,s)n-num, s-num de decimales |  | timestamp
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

Cómo hacer preguntas
Conjunto A left join conjunto B
Conjunto A right join conjunto B
Conjunto A inner join conjunto B
Conjunto A union conjunto B
Conjunto A outer join conjunto B