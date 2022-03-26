npm : es un gestor de paquetes para JavaScript. Gestiona versiones (paquetes/librerias)
1. Realizar inicio del proyecto con git
2. npm
   1. npm init / npm init -y / npm set init.author.name "PanchitoF" -> npm init -y
   2. Como instalar paquetes
      1. mkdir src | cd src/ | touch index.js -> raíz del proyecto
      2. instalar dependencias (son utiles en los proyectos)
         1. manejador de fechas JS: npm install moment --save-dev
         2. install = i | --save-dev = -D | -S
   <!-- moment apartir de npm5 es requerida en los proyectos -->
   <!-- --save (paques necesarios para estar en producción) -dev (este documento solo es necesario en el entorno de desarrollo)-->
         1. la carpeta mement/ -> es donde se guardara los modulos que agregas al proyecto (no se manda al repositorio)
         2. paquete requierido de forma global
            1. -g nodemon | npm list -g --depth 0 -> busqueda profunda
