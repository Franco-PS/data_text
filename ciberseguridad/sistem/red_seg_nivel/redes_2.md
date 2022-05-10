# Subnetear
VLSM Máscara de red de Longitud Variable 
  se divide la red en subredes

## Máscaras
Definen cuantas maquinas puede tener la red

existen dos mascaras que no podemos utilizar
- Usada para identificar la red
- Usada como Broadcast (puede mandar señal a todas las maquinas)

Cuantas maquinas puede tener la red

n -> 0 -> cantidad de ceros

host_posibles = 2^n -2

Direcciones IP, sirve para conocer la dirección de la maquina dentro de un grupo de red

### Clases de direcciones
A partir de IPV4 se crean las clases

- A : del 0 al 127 (0 no se ocupa | 127 local host personal) queda del 1 al 126
  - Máscara por defecto: 255.0.0.0
  - Rango: 1.0.0.0 - 126.0.0.0

- B : 
  - Máscara por defecto: 255.255.0.0
  - Rango: 128.0.0.0 - 191.255.0.0

- C :
  - Máscara por defecto: 255.255.255.0
  - Rango: 192.0.0.0 - 223.255.255.0 

- D : Se ocupa para el multicast(comunicaciones entre maquinas- grupo común) por lo cual no tiene máscara, 
  - enrutadores  
  * No tienen aplicación directa en el direccionamiento
    - Rango clase: D 224.0.0.0 - 239.0.0.0

-E