## Capa de transporte
Transmisión de segmentos de datos confiables ingluye la [segmentación](https://es.wikipedia.org/wiki/Segmentaci%C3%B3n_de_paquetes)
La capa de red y la de transporte trabajan en conjunto, 
- la capa de red se ocupa de direccionar los datos, 
- la capa de transporte actúa como oficina local (ordenando/ agrupando)

Protocolos de transmisión
- TCP (Transmission Control Protocol)
    Prioriza confiabilidad sobre rapidez, verifica del mensaje.
- UDP (User Datagram Protocol)
    Prioriza rapidez sobre confiabilidad, solo envía el mensaje.
- SCTP (Stream Control Transmission Protocol - Protocolo de Transmisión de Control de Flujo): Es un protocolo de comunicación
- SSL (Secure Socket Layer - Capa de Puertos Seguros) preceden de los TLS
  conexión segura: confidencialidad
- TLS (Transport Layer Security - Seguridad de la Capa de Transporte)        
  protocolos criptográficos que proporcionan privacidad e integridad en la comunicación entre dos puntos en una red