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
![Tabla ICANN](https://static.platzi.com/media/user_upload/Screen%20Shot%202021-02-18%20at%206.31.55%20PM-d14b33e1-2cf5-4fa2-af06-44f19234986e.jpg)


Arquitectura en capas:  Es una forma sencilla de resolver problemas, 
  - la primera capa facilita la creación de la siguiente capa.
  - los problemas son específicos de cada capa
  - TCP/IP | OSI

### Modelos de Redes

### Modelo TCP/IP :(Protocolo de control de transmisión)
- creada 70's ARPANET

1. Acceso a la red
2. Internet:
    Permite la comunicación de paquetes en la red
3. Transporte:
    transmite datos de forma óptima y libre de errores
4. Aplicación:
    Da servicios específicos a los usuarios (correo, mensajes, ...)

- IP: la manera en que las pc se identifican en Internet
  <!-- Es un protocolo se encarga del ruteo (caminos que va a tomar)
  Rangos de la IP
  127.0.0.1 -> localhost (IPV4 - IPV6)
  clases de redes : ICANN IANA -->



- Modelo OSI : Open System Interconection 
- (creada por la ISO)  explica la comunicación den un host a la red, y categoriza los protocolos.
  

  1. Capa física: 
    Se encarga de los medios de comunicación, señal y transmisión (electricidad, cables, hardware ).
  
  2. Capa enlace de datos:
    Direccionamiento físico, detectar errores, distribución ordenada de tramas y control de flujo.
    subcapa de control de acceso al medio: ayuda a la seguridad
    * tramas
  Protocolo
  - MAC - identifica dispositivos en la red

  3. Capa de red: 
    Identifican enrutamiento entre una o más redes, la unidad de datos (paquetes) y se pueden clasificar en protocolos:
    - enrutables: viaja con los paquetes (IP).
    - enrutamiento: permite seleccionar rutas
    * datos
  
  4. Capa de transporte: 
    Encargada de transportar los datos libres de errores 
    - protocolos TCP - UDP
    - control de flujo
    - segmentación y re-ensamblado de paquetes
    - detección y recuperación de errores
    LA PDU (unidad de información) de está capa = segmento/datagrama
      - TCP: no pierde datos
      - UDP: puede que pierda datos

  5. Capa de sesión : 
    Encargada de mantener y controlar el enlace establecido
    - control de diálogo
    - permite indicar puntos en la comunicación para recuperar o continuar en alguno de esos puntos

  6. Capa de presentación: 
    Encarga de como presentar la información (ejem: no es lo mismo presentar la info a un cel, tablat, pc)
    -encriptación de datos
  
  7. Capa de aplicación: 
    posibilita que las aplicaciones accedan a los servicios de las demás capas y define protocolos para intercambiar datos.
    - Dar servicios específicos a los usuarios (correo, mensajes, ...)

* Diferencias TCP/IP OSI: 
  * TCP/IP: se implementan los protocolos
      - Uso solo se aplica a internet
      - es implementado
  * OSI: _modelo de referencia_
      - Conceptualiza como software/hatware se comunican en una red ( ayuda a diseñar la arquitectura de red)
      - Clara diferencia (servicios, interfaces y protocolos)
      - Prototipos generales


![modelo OSI](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/OSI_Model_v1.svg/langes-800px-OSI_Model_v1.svg.png)

## Protocolo de red
Son reglas que permiten la comunicación y transmisión de información.
La red utiliza pilas (capas una sobre otra), cada capa proporciona servicios (ocultar detalles de implementación,reglas etc), ayuda a reducir la complejidad de una red y la correcta transmisión de datos.

### jerarquias de protocolos 
Son reglas
  ![esquema modelo TCP y protocolos](https://static.platzi.com/media/user_upload/capas-tcp-53ea30d0-90e4-4abf-88e5-3f86b7b7b934.jpg)


  ## Topologías física y lógica

  Nos sirve para conocer cono se van a transmitir los datos