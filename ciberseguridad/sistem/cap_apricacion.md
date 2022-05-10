## Capa de aplicación

tenemos contacto directo con los usuarios finales
Compuesta por:
- aplicaciones: programas de usuario que se comunican en la red
- Servicios: programa que el usuario no ve
- Protocolos: establecen reglas para el intercambio de datos
  - Telnet (Teletype Network - Red de teletipo)
    Nos permite acceder a otra máquina para manejarla remotamente como si estuviéramos sentados delante de ella.
   - POP (Post Office Protocol - Protocolo de oficina de correo)
    Es usado para recuperar mensajes de correo electrónico de un mail server a un cliente de correo, la versión más reciente es POP3.


### Banderas

    URG. La etiqueta “Urgent” (en español, “urgente”) señaliza a la aplicación TCP que los datos de uso hasta el Urgent-Pointer (véase más abajo) fijado se deben procesar inmediatamente.
    ACK. Junto con el número de confirmación, ACK sirve para confirmar la recepción de paquetes TCP. Si no se ha ajustado la etiqueta, el número de confirmación se convierte en inválido de forma automática.
    PSH. “Push” sirve para facilitar un segmento TCP inmediatamente sin tener que pasar por el buffer de datos del emisor y el receptor.
    RST. Si ha surgido un error durante la transmisión, la aplicación se puede restablecer mediante un paquete TCP con flag RST (“Reset”) ajustado.
    SYN. Los mensajes con una etiqueta SYN representan el primer paso del triple apretón de manos, es decir, inician el establecimiento de conexión.
    FIN. “Finish” señaliza a la contraparte que uno de los interlocutores de la comunicación ha finalizado la transmisión.