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

SubProceso MostrarProducto(codigos,nombres,categorias,precios,stock,minimos,activos,i)
    Escribir "Codigo: ",codigos[i]," Nombre: ",nombres[i]," Categoria: ",categorias[i]
    Escribir "Precio: ",precios[i]," Cantidad: ",stock[i]," Minimo: ",minimos[i]
    Si activos[i] Entonces
        Escribir "Estado: Activo"
    SiNo
        Escribir "Estado: Inactivo"
    FinSi
FinSubProceso

Proceso Proceso_consultas_inventario
    // Datos de ejemplo para ejecutar un proceso aislado; no son datos del programa Python.
    Definir codigos,nombres,categorias Como Caracter
    Definir precios,stock,minimos Como Real
    Definir activos Como Logico
    Definir n,i,j,pos Como Entero
    Dimension codigos[3],nombres[3],categorias[3],precios[3],stock[3],minimos[3],activos[3]
    n <- 2
    codigos[0] <- "P01"
    nombres[0] <- "Cuaderno"
    categorias[0] <- "Utiles"
    precios[0] <- 12.50
    stock[0] <- 3
    minimos[0] <- 1
    activos[0] <- Verdadero
    codigos[1] <- "P02"
    nombres[1] <- "Lapiz"
    categorias[1] <- "Utiles"
    precios[1] <- 2
    stock[1] <- 0
    minimos[1] <- 2
    activos[1] <- Falso
    Definir eleccion Como Caracter
    Definir encontrados Como Entero
    Repetir
        Escribir "1. Existencias  2. Stock minimo  3. Volver"
        Leer eleccion
        eleccion <- QuitarEspacios(eleccion)
        Si eleccion = "1" O eleccion = "2" Entonces
            Si n = 0 Entonces
                Escribir "No hay productos registrados."
            SiNo
                encontrados <- 0
                Para i <- 0 Hasta n-1 Hacer
                    Si eleccion = "1" O stock[i] <= minimos[i] Entonces
                        MostrarProducto(codigos,nombres,categorias,precios,stock,minimos,activos,i)
                        encontrados <- encontrados+1
                    FinSi
                FinPara
                Si eleccion = "2" Y encontrados = 0 Entonces
                    Escribir "No hay productos en stock minimo o por debajo."
                FinSi
            FinSi
        SiNo
            Si eleccion <> "3" Entonces
                Escribir "Opcion incorrecta."
            FinSi
        FinSi
    Hasta Que eleccion = "3"
FinProceso
