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

SubProceso valido <- EsNumero(texto, decimal)
    Definir valido Como Logico
    Definir i, puntos, digitos Como Entero
    Definir letra Como Caracter
    puntos <- 0
    digitos <- 0
    valido <- Verdadero
    i <- 0
    Mientras i < Longitud(texto) Hacer
        letra <- Subcadena(texto,i,i)
        Si letra >= "0" Y letra <= "9" Entonces
            digitos <- digitos+1
        SiNo
            Si letra = "." Y decimal Entonces
                puntos <- puntos+1
            SiNo
                valido <- Falso
            FinSi
        FinSi
        i <- i+1
    FinMientras
    valido <- valido Y digitos > 0 Y puntos <= 1
FinSubProceso

SubProceso valido <- FechaValida(texto)
    Definir valido,bisiesto Como Logico
    Definir anio,mes,dia,maximo Como Entero
    valido <- Falso
    Si Longitud(texto) = 10 Entonces
        Si Subcadena(texto,4,4) = "-" Y Subcadena(texto,7,7) = "-" Entonces
            Si EsNumero(Subcadena(texto,0,3),Falso) Y EsNumero(Subcadena(texto,5,6),Falso) Y EsNumero(Subcadena(texto,8,9),Falso) Entonces
                anio <- ConvertirANumero(Subcadena(texto,0,3))
                mes <- ConvertirANumero(Subcadena(texto,5,6))
                dia <- ConvertirANumero(Subcadena(texto,8,9))
                Si anio >= 1 Y anio <= 9999 Y mes >= 1 Y mes <= 12 Entonces
                    maximo <- 31
                    Si mes = 4 O mes = 6 O mes = 9 O mes = 11 Entonces
                        maximo <- 30
                    FinSi
                    Si mes = 2 Entonces
                        bisiesto <- (anio MOD 400 = 0) O (anio MOD 4 = 0 Y anio MOD 100 <> 0)
                        maximo <- 28
                        Si bisiesto Entonces
                            maximo <- 29
                        FinSi
                    FinSi
                    valido <- dia >= 1 Y dia <= maximo
                FinSi
            FinSi
        FinSi
    FinSi
FinSubProceso

SubProceso texto <- PedirFecha(campo)
    Definir texto Como Caracter
    Definir listo Como Logico
    Repetir
        Escribir campo," (YYYY-MM-DD, Enter cancela)"
        Leer texto
        texto <- QuitarEspacios(texto)
        listo <- texto = "" O FechaValida(texto)
        Si No listo Entonces
            Escribir "Fecha invalida."
        FinSi
    Hasta Que listo
FinSubProceso

SubProceso ordinal <- NumeroDia(texto)
    Definir ordinal,anio,mes,dia,anterior,m,maximo Como Entero
    Definir bisiesto Como Logico
    anio <- ConvertirANumero(Subcadena(texto,0,3))
    mes <- ConvertirANumero(Subcadena(texto,5,6))
    dia <- ConvertirANumero(Subcadena(texto,8,9))
    anterior <- anio-1
    ordinal <- anterior*365+Trunc(anterior/4)-Trunc(anterior/100)+Trunc(anterior/400)+dia
    bisiesto <- (anio MOD 400 = 0) O (anio MOD 4 = 0 Y anio MOD 100 <> 0)
    m <- 1
    Mientras m < mes Hacer
        maximo <- 31
        Si m = 4 O m = 6 O m = 9 O m = 11 Entonces
            maximo <- 30
        FinSi
        Si m = 2 Entonces
            maximo <- 28
            Si bisiesto Entonces
                maximo <- 29
            FinSi
        FinSi
        ordinal <- ordinal+maximo
        m <- m+1
    FinMientras
FinSubProceso

SubProceso PromedioPeriodo(fechas,totales,nv)
    Definir inicio,fechaFinal Como Caracter
    Definir ingresos,promedioIngresos,promedioVentas Como Real
    Definir cantidad,dias,i Como Entero
    inicio <- PedirFecha("Fecha inicial")
    Si inicio = "" Entonces
        Escribir "Reporte cancelado."
    SiNo
        Repetir
            fechaFinal <- PedirFecha("Fecha final")
            Si fechaFinal <> "" Entonces
                Si NumeroDia(fechaFinal) < NumeroDia(inicio) Entonces
                    Escribir "La fecha final no puede ser anterior a la inicial."
                FinSi
            FinSi
        Hasta Que fechaFinal = "" O fechaFinal >= inicio
        Si fechaFinal = "" Entonces
            Escribir "Reporte cancelado."
        SiNo
            cantidad <- 0
            ingresos <- 0
            Para i <- 0 Hasta nv-1 Hacer
                Si fechas[i] >= inicio Y fechas[i] <= fechaFinal Entonces
                    cantidad <- cantidad+1
                    ingresos <- ingresos+totales[i]
                FinSi
            FinPara
            dias <- NumeroDia(fechaFinal)-NumeroDia(inicio)+1
            ingresos <- Redon(ingresos*100)/100
            promedioVentas <- cantidad/dias
            promedioIngresos <- Redon((ingresos/dias)*100)/100
            Escribir "Ventas del periodo: ",cantidad
            Escribir "Dias del periodo: ",dias
            Escribir "Ingresos del periodo: ",ingresos
            Escribir "Promedio de ventas por dia: ",promedioVentas
            Escribir "Promedio de ingresos por dia: ",promedioIngresos
        FinSi
    FinSi
FinSubProceso

Proceso Proceso_promedio_periodo
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
    // Dos ventas de ejemplo para comprobar los reportes; todos los resultados se calculan.
    Definir fechas,detalleCodigos,detalleNombres Como Caracter
    Definir totales,subtotalesVenta,ivas,detalleCantidades,detallePrecios,detalleSubtotales Como Real
    Definir detalleVenta Como Entero
    Definir nv,nd Como Entero
    Dimension fechas[2],totales[2],subtotalesVenta[2],ivas[2]
    Dimension detalleCodigos[3],detalleNombres[3],detalleCantidades[3],detalleVenta[3],detallePrecios[3],detalleSubtotales[3]
    nv <- 2
    nd <- 3
    fechas[0] <- "2026-11-01"
    fechas[1] <- "2026-11-03"
    detalleCodigos[0] <- "P01"
    detalleCodigos[1] <- "P02"
    detalleCodigos[2] <- "P01"
    detalleNombres[0] <- "Cuaderno"
    detalleNombres[1] <- "Lapiz"
    detalleNombres[2] <- "Cuaderno"
    detalleCantidades[0] <- 1
    detalleCantidades[1] <- 2
    detalleCantidades[2] <- 1
    detallePrecios[0] <- 12.5
    detallePrecios[1] <- 2
    detallePrecios[2] <- 12.5
    detalleVenta[0] <- 0
    detalleVenta[1] <- 0
    detalleVenta[2] <- 1
    Para i <- 0 Hasta nv-1 Hacer
        subtotalesVenta[i] <- 0
    FinPara
    Para i <- 0 Hasta nd-1 Hacer
        detalleSubtotales[i] <- Redon(detallePrecios[i]*detalleCantidades[i]*100)/100
        j <- detalleVenta[i]
        subtotalesVenta[j] <- subtotalesVenta[j]+detalleSubtotales[i]
    FinPara
    Para i <- 0 Hasta nv-1 Hacer
        ivas[i] <- Redon(subtotalesVenta[i]*0.12*100)/100
        totales[i] <- Redon((subtotalesVenta[i]+ivas[i])*100)/100
    FinPara
    PromedioPeriodo(fechas,totales,nv)
FinProceso
