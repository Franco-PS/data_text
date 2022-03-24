left join

SELECT * 
FROM table_A
LEFT JOIN table_B ON table_A.clave-primaria = table_B.clave-primaria
<!-- Pero no quiero ningun dato que sea de la table_B -->
WHERE table_B.clave-primaria IS NULL;

right join

SELECT * 
FROM table_A
RIGHT JOIN table_B ON table_A.clave-primaria = table_B.clave-primaria
<!-- Pero no quiero ningun dato que sea de la table_B -->
WHERE table_B.clave-primaria IS NULL;

Join

SELECT * 
FROM table_A
INNER JOIN table_B ON table_A.clave-primaria = table_B.clave-primaria;

Une todos los conjuntos

SELECT * 
FROM table_A
LEFT JOIN table_B ON table_A.clave-primaria = table_B.clave-primaria
<!-- Se puede ocupar CROSS JOIN | FULL OUTER JOIN | 
pero no se recomiendo ya que no en todos los sistemas son compatibles -->
SELECT * 
FROM table_A
RIGHT JOIN table_B ON table_A.clave-primaria = table_B.clave-primaria;