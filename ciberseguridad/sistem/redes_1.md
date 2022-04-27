# Redes computacionales

## Tecnologías de transmisión
- BROADCAST: enlaces de uno a todos
- MULTICAST: enlaces uno a varios
- UNICAST : enlaces de punto a punto

## Clasificación por escala
- PAN (Personal Area Network) blooto-infrarrojo (1m[2])
- LAN (Local area Network): áreas de casas - departamentos (10 m - 1km)
- MAN (Metropolitan area Network): extensiones de ciudad - ciudades (10km)
- WAN (Wide area Network): extensión de un país o varios continentes (100km - )
- existen las versiones inhalámbricas, a las anteriores e les pone el sufijo W - Wireless

* Internet (International Network | área global): internet (redes de una área)

## Protocolo de red
Son reglas que permiten la comunicación y transmisión de información.
La red utiliza pilas (capas una sobre otra), cada capa proporciona servicios (ocultar detalles de implementación,reglas etc), ayuda a reducir la complejidad de una red y la correcta transmisión de datos.

### jerarquias de protocolos 
Son reglas
  ![esquema modelo TCP](https://static.platzi.com/media/user_upload/capas-tcp-53ea30d0-90e4-4abf-88e5-3f86b7b7b934.jpg)

#### Modelos de Redes
- Modelo TCP/IP : evita perdida de información

- IP: la manera en que las compus se identifican en Internet
  protocolo IP se encarga del ruteo (caminos que va a tomar)
  Rangos de la IP
  127.0.0.1 -> localhost (IPV4 - IPV6)
  clases de redes : ICANN IANA

![Tabla ICANN](https://static.platzi.com/media/user_upload/Screen%20Shot%202021-02-18%20at%206.31.55%20PM-d14b33e1-2cf5-4fa2-af06-44f19234986e.jpg)

- Modelo OSI : Open System Interconection (creada por la ISO)
  explica la comunicación den un host a la red, y categoriza los protocolos.

  - 1ra Capa: física: Se encarga de los medios de comunicación, señal y transmisión (electricidad, cables, hardware ).
  - 2da capa: enlace de datos: Se le añade un nivel lógico. La capa que convierte la información a bits le pasa la información a la capa 2 del enlace de datos En esta capa:

    - Se envían los datos que se convirtieron a bits
    - Se le añade información sobre el direccionamiento físico
    - Llega a la capa de red

  - 3ra capa: red: Se hace la definición de ruta y el direccionamiento de información. (Ruta: Camino que va a tomar la información a través de la red).
  
  - 4ta capa: transporte: se añade la información de la conexión punto a punto y la confiabilidad (se encuentran protocolos como TCP).

  - 5ta capa: sesión : Se establece la comunicación entre dos host.

  - 6ta capa: presentación: Formatea los datos (para transferirlos a la capa 7).
  
  - 7ma capa: aplicación: Con la que tiene contacto directo el usuario. Procesamiento de red a aplicación.

* Diferencias TCP/IP OSI: 
  * OSI es un modelo de referencia; interpreta que debe tener un modelo para la comunicación efectiva.
  * TCP/IP: se implementa detalladamente (modulos, protocolos, cables, etc.) para las conexiones de red.