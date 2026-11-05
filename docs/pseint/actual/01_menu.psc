// Proceso aislado para diagramar. Perfil Flexible, indices base cero.
SubProceso limpio <- QuitarEspacios(texto)
    Definir limpio Como Caracter
    Definir inicio, ultimo Como Entero
    Definir seguir Como Logico
    inicio <- 0
    ultimo <- Longitud(texto)-1
    seguir <- Verdadero
    Mientras inicio <= ultimo Y seguir Hacer
        Si Subcadena(texto,inicio,inicio) = " " Entonces
            inicio <- inicio+1
        SiNo
            seguir <- Falso
        FinSi
    FinMientras
    seguir <- Verdadero
    Mientras ultimo >= inicio Y seguir Hacer
        Si Subcadena(texto,ultimo,ultimo) = " " Entonces
            ultimo <- ultimo-1
        SiNo
            seguir <- Falso
        FinSi
    FinMientras
    limpio <- ""
    Si inicio <= ultimo Entonces
        limpio <- Subcadena(texto,inicio,ultimo)
    FinSi
FinSubProceso

Proceso Proceso_menu
    Definir eleccion Como Caracter
    // Cada rama representa la llamada al modulo correspondiente de Python.
    Repetir
        Escribir "1. Productos  2. Ventas  3. Inventario  4. Reportes  5. Salir"
        Leer eleccion
        eleccion <- QuitarEspacios(eleccion)
        Segun eleccion Hacer
            "1": Escribir "Llamar menu_productos(productos,movimientos)"
            "2": Escribir "Llamar registrar_venta(productos,ventas,movimientos)"
            "3": Escribir "Llamar menu_inventario(productos,movimientos)"
            "4": Escribir "Llamar menu_reportes(productos,ventas)"
            "5": Escribir "Hasta luego."
            De Otro Modo: Escribir "Opcion incorrecta."
        FinSegun
    Hasta Que eleccion = "5"
FinProceso
