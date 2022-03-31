JavaScript es un lenguaje asincrono y no bloqueante
Asincronismo: acción que no ocurre en el mismo tiempo que otro suceso

Concurrencia: existe varias tareas a procesar (conjuntos muchos)
las peticiones se trabajan una a la vez. es como la fila del supermercado
los clientes(funciones) tienen productos (tareas) pero la fila solo puede
atender un cliente a la vez
Paralelismo:
cuando se ejecutan dos o más tareas al mismo tiempo

Cuando el lenguaje proesa muchas tareas debe de hacerlo en el menor tiempo
para ello tenemos dos alternativas:
- Bloqueante: mientras se haga una tarea el programa no devolverá el control 
  hasta que sea completada
- No bloqueante: no importa si la tarea es respondida (corecta o erronea) el programa seguira

Componentes del [navegador](https://miro.medium.com/max/1400/1*7GXoHZiIUhlKuKGT22gHmA.png)

Heap (memoria): lugar donde se guardan las funciones y variables
Stack (Pila de ejecución): donde se guardan los registros (frames) que se ejecutan (funciones)
Browser (web APIs): no forma parte de javaScript

CallBack