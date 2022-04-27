## Entrar a MySQL
mysql -u root -h localhost -p
sudo mysql

show databases; -> muestra la base de datos de mysql

user nombre_tabla; -> selecciona base de datos

show tables;   -> tablas que se tienen

select database();  -> saber en que tabla me encuentro
describe name_table; | desc name_table; | show full columns from name_table;

CREATE DATABASES nombre_nueva_baseDatos;
CREATE DATABASES IF NOT EXISTS nombre_nueva_baseDatos;

## Creación de librería
CREATE TABLE IF NOT EXISTS books(
  book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  author_id INTEGER UNSIGNED,
  title VARCHAR(100) NOT NULL,
  year INTEGER UNSIGNED NOT NULL DEFAULT 1900,
  language VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'ISO 658-458',
  cover_url VARCHAR(500),
  price DOUBLE(6,2) NOT NULL DEFAULT 10.0 , 
  sellable TINYINT(1) DEFAULT 1,
  copies INTEGER NOT NULL DEFAULT 1,
  description TEXT
);
CREATE TABLE IF NOT EXISTS authors(
  author_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  nationality VARCHAR(3)
);

CREATE TABLE IF NOT EXISTS clients(
  client_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  birthdate DATETIME,
  gender ENUM ('M', 'F', 'ND') NOT NULL,
  active TINYINT (1) NOT NULL DEFAULT 1,
  create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

SELECT column,column, col...(se encarga de presentar datos)
FROM table_name (conocer de donde se obtendran los datos)
WHERE condition; (filtra)
GROUP BY
ORDER BY
HAVING

WHERE condition = condition
= != 
NOT AND OR

Cómo hacer preguntas
Conjunto A left join conjunto B
- dame todos los datos
- de la tabla A
  - quiero todos los datos A junto con los datos B
  - une con las llaves

