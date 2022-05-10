## Capa de enlace de datos

Es la capa encargada de recibir datos, 
_tramas_: Unidad de envío de datos: verifica que los datos no sean demaciado ni muy chicos [runts] ni muy grandes [giants] (ayuda a que los datos no se atoren/inunde en cuellos de botella)

### Protocolos 
- Ethernet: estándar de redes de área local 
- LLC MAC: 
  - LLC (Logical Link Control)
    - transporta protocolos de red, ayudando a que se entregue el paquete
    - Proporciona independencia de la (capa red - independiente de la tecnología a ocupar)
    - LLC subcapa encapsula 
    - Componentes de direccionamiento:
      - DSAP (Punto de acceso al servicio destino)
      - SSAP (Punto de acceso al servicio fuente)
  - MAC (Media Access Control): 
    El direccionamiento MAC es un identificador único de los dispositivos dentro de la red
    - protocolo que sigue el host para acceder a los medios físicos.
    - topología de la red, cada tecnología de red tiene su sub-MAC diferente
  
1. VLAN (Virtual Local Area Network): métodos para crear redes lógicas
2. ATM (Asyncronous Transfer Mode): 
3. HDP (Heterogeneous Data Protocol): 
4. Frame Relay
5. HDLC (High-Level Data Link Control)
6. PPP (Point-to-Point Protocol)
7. Q.921
8. Token Ring