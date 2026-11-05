// Proceso aislado para diagramar. Perfil Flexible, indices base cero.


Proceso Proceso_historial_movimientos
    Definir fechas,codigos,tipos,descripciones Como Caracter
    Definir cantidades Como Real
    Definir nm,i Como Entero
    Dimension fechas[1],codigos[1],tipos[1],descripciones[1],cantidades[1]
    // Un movimiento de ejemplo como dato de entrada del proceso de consulta.
    nm <- 1
    fechas[0] <- "2026-11-01 09:00:00"
    codigos[0] <- "P01"
    tipos[0] <- "Entrada inicial"
    cantidades[0] <- 3
    descripciones[0] <- "Registro del producto"
    Si nm = 0 Entonces
        Escribir "No hay movimientos registrados."
    SiNo
        Para i <- 0 Hasta nm-1 Hacer
            Escribir fechas[i]," | ",codigos[i]," | ",tipos[i]," | Cantidad: ",cantidades[i]," | ",descripciones[i]
        FinPara
    FinSi
FinProceso
