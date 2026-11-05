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

SubProceso numero <- LeerNumero(campo, decimal, anterior, conservar)
    Definir numero Como Real
    Definir texto Como Caracter
    Definir listo Como Logico
    listo <- Falso
    Repetir
        Escribir campo
        Leer texto
        texto <- QuitarEspacios(texto)
        Si texto = "" Y conservar Entonces
            numero <- anterior
            listo <- Verdadero
        SiNo
            Si EsNumero(texto,decimal) Entonces
                numero <- ConvertirANumero(texto)
                listo <- numero >= 0
            FinSi
            Si No listo Entonces
                Escribir "Numero invalido. Usar digitos, y punto solo para precio."
            FinSi
        FinSi
    Hasta Que listo
FinSubProceso

SubProceso posicion <- Buscar(codigos, n, codigo)
    Definir posicion, i Como Entero
    posicion <- -1
    i <- 0
    Mientras i < n Hacer
        Si codigos[i] = Mayusculas(QuitarEspacios(codigo)) Entonces
            posicion <- i
        FinSi
        i <- i+1
    FinMientras
FinSubProceso

SubProceso respuesta <- Confirmar(pregunta)
    Definir respuesta Como Caracter
    Repetir
        Escribir pregunta, " (S/N)"
        Leer respuesta
        respuesta <- Mayusculas(QuitarEspacios(respuesta))
        Si respuesta <> "S" Y respuesta <> "N" Entonces
            Escribir "Respuesta invalida."
        FinSi
    Hasta Que respuesta = "S" O respuesta = "N"
FinSubProceso

Proceso Proceso_registrar_venta
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
    Definir codigo,respuesta Como Caracter
    Definir cantidades,subtotales Como Real
    Definir cantidad,restante,precio,nuevaLinea,nuevoSubtotal,nuevoIva,nuevoTotal,subtotal,iva,total Como Real
    Definir disponible,terminar,importeValido Como Logico
    Definir lineas,numeroVentas Como Entero
    Dimension cantidades[n],subtotales[n]
    disponible <- Falso
    Para i <- 0 Hasta n-1 Hacer
        cantidades[i] <- 0
        subtotales[i] <- 0
        Si activos[i] Y stock[i] > 0 Entonces
            disponible <- Verdadero
        FinSi
    FinPara
    lineas <- 0
    numeroVentas <- 0
    Si No disponible Entonces
        Escribir "No hay productos activos con existencias para vender."
    SiNo
        terminar <- Falso
        Repetir
            Escribir "Codigo del producto: Enter para finalizar"
            Leer codigo
            codigo <- Mayusculas(QuitarEspacios(codigo))
            Si codigo = "" Entonces
                terminar <- Verdadero
            SiNo
                pos <- Buscar(codigos,n,codigo)
                Si pos = -1 Entonces
                    Escribir "No existe un producto con ese codigo."
                SiNo
                    Si No activos[pos] Entonces
                        Escribir "El producto esta inactivo."
                    SiNo
                        restante <- stock[pos]-cantidades[pos]
                        Si restante = 0 Entonces
                            Escribir "No hay mas existencias disponibles."
                        SiNo
                            Escribir "Producto: ",nombres[pos]
                            Escribir "Precio unitario: ",Redon(precios[pos]*100)/100
                            Escribir "Disponible para agregar: ",restante
                            Repetir
                                cantidad <- LeerNumero("Cantidad a vender",Falso,0,Falso)
                                Si cantidad = 0 Entonces
                                    Escribir "La cantidad debe ser mayor que cero."
                                SiNo
                                    Si cantidad > restante Entonces
                                        Escribir "Inventario insuficiente."
                                    FinSi
                                FinSi
                            Hasta Que cantidad > 0 Y cantidad <= restante
                            precio <- Redon(precios[pos]*100)/100
                            nuevaLinea <- Redon(precio*(cantidades[pos]+cantidad)*100)/100
                            nuevoSubtotal <- nuevaLinea
                            Para i <- 0 Hasta n-1 Hacer
                                Si i <> pos Entonces
                                    nuevoSubtotal <- nuevoSubtotal+subtotales[i]
                                FinSi
                            FinPara
                            nuevoSubtotal <- Redon(nuevoSubtotal*100)/100
                            nuevoIva <- Redon(nuevoSubtotal*0.12*100)/100
                            nuevoTotal <- Redon((nuevoSubtotal+nuevoIva)*100)/100
                            // PSeInt no captura OverflowError; usar valores representables.
                            importeValido <- nuevoTotal >= 0
                            Si importeValido Entonces
                                Si cantidades[pos] = 0 Entonces
                                    lineas <- lineas+1
                                FinSi
                                cantidades[pos] <- cantidades[pos]+cantidad
                                subtotales[pos] <- nuevaLinea
                                subtotal <- nuevoSubtotal
                                iva <- nuevoIva
                                total <- nuevoTotal
                            SiNo
                                Escribir "Importe fuera de rango. No se agrego."
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        Hasta Que terminar
        Si lineas = 0 Entonces
            Escribir "Venta cancelada. No se agregaron productos."
        SiNo
            Para i <- 0 Hasta n-1 Hacer
                Si cantidades[i] > 0 Entonces
                    Escribir codigos[i]," Cantidad: ",cantidades[i]," Subtotal: ",subtotales[i]
                FinSi
            FinPara
            Escribir "Subtotal: ",subtotal," IVA: ",iva," Total: ",total
            respuesta <- Confirmar("Confirmar venta")
            Si respuesta = "N" Entonces
                Escribir "Venta cancelada."
            SiNo
                numeroVentas <- numeroVentas+1
                Escribir "Venta numero: ",numeroVentas," Fecha: ",FechaActual()," Hora: ",HoraActual()
                Para i <- 0 Hasta n-1 Hacer
                    Si cantidades[i] > 0 Entonces
                        stock[i] <- stock[i]-cantidades[i]
                        // En Python se agregan la venta, su detalle y estos movimientos a sus listas.
                        Escribir "Salida por venta: ",codigos[i]," Cantidad: ",cantidades[i]
                    FinSi
                FinPara
                Escribir "Venta registrada correctamente."
            FinSi
        FinSi
    FinSi
FinProceso
