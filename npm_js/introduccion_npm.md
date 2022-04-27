# NPM
npm : es un gestor de paquetes para JavaScript. Gestiona versiones (paquetes/librerias)

## Pasos de instalación
1. Realizar inicio del proyecto con git
2. npm
   1. npm init / npm init -y / npm set init.author.name "PanchitoF" -> npm init -y
   2. Como instalar paquetes
      1. mkdir src | cd src/ | touch index.js -> raíz del proyecto
      2. instalar dependencias:son paquetes/variables que necesita un proyecto (globales: proyecto en producción= publicas/ locales: de desarrollo= solo el desarrollador puede acceder a ellas)
         1. npm install moment --save-dev -> dependencias requeridas para el proyecto a partir de npm5
         2. --save -> necesario para vivir en producción
         3. --save-dev = -D -> solo local o de desarrollo
         4. install = i | -S
   <!-- moment apartir de npm5 es requerida en los proyectos -->
   <!-- --save (paques necesarios para estar en producción) -dev (este documento solo es necesario en el entorno de desarrollo)-->
         1. la carpeta mement/ -> es donde se guardara los modulos que agregas al proyecto (no se manda al repositorio)
         2. paquete requerido de forma global
            1.npm -g nodemon | npm list -g --depth 0 -> busqueda profunda
            1. npm install react --dry-run -> mostrara como y que instalara (pero no se instalara)
            2. npm install webpack -f -> --force fuerza la instalación de la ultima versión del repositorio npm
         3. Actualizar paquetes
            1. npm outdate -> conocer que paquete esta desactualizado
            2. npm outdate --dd (dd = output detailed)
            3. npm update ->actualiza paquetes
            4. npm install -> se instalan los paquetes que se encuentren en packege.json
            5. npm install nomPaquete@latest -> latest = paquete más actual
            6. npm uninstall json-server -> desintalar paquete
            7. npm uninstall webpack --no-save -> desintalar solo en node_modules
         4. ejecutar en "scripts":
            1. el nombre debe de ser descriptivo
            2. "nombre": "un valor/comandos",
            3. npm test | npm start -> inicia los proyectos

## Ejecutar tareas
documento packege.json
"scripts" 
   "nombre_descriptivo": _ _ _

## Solución de errores
         - npm run name-job --dd -> permite conocer los detalles que se ejecutan

code //escribe ruta

npm cache clear --force ->eliminar cache del sistema

## Tipos de documentos
### Versionado
   Es la forma en la que los programas se versionan
   [https://static.platzi.com/media/user_upload/wheelbarrel-no-tilde-caret-white-bg-w1000-72ca1a72-4c7f-4abe-8482-425c01a72f89.jpg]
   mayor | menor | parches
   3     |  9    |   2
   cambios grandes| ^ caret 9-2: añade funcionalidades | ~ tide : añade parches

typescript "7.7.1"   -> garantiza que se queda en una sola versión 
typescript "^7.7.1"  -> va a estar actualizando solo en las versiones pequeñas

A partir de npm5 se crea el archivo package-lock.json: que nos ayuda a comprender 
lo que esta sucediendo a lo largo del proyecto

## Creación de scripts
