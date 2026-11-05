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

SubProceso texto <- LeerTexto(campo, anterior, conservar)
    Definir texto Como Caracter
    Definir listo Como Logico
    listo <- Falso
    Repetir
        Escribir campo
        Leer texto
        texto <- QuitarEspacios(texto)
        Si texto = "" Y conservar Entonces
            texto <- anterior
            listo <- Verdadero
        SiNo
            Si texto <> "" Entonces
                listo <- Verdadero
            SiNo
                Escribir "Campo obligatorio."
            FinSi
        FinSi
    Hasta Que listo
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

SubProceso MostrarProducto(codigos,nombres,categorias,precios,stock,minimos,activos,i)
    Escribir "Codigo: ",codigos[i]," Nombre: ",nombres[i]," Categoria: ",categorias[i]
    Escribir "Precio: ",precios[i]," Cantidad: ",stock[i]," Minimo: ",minimos[i]
    Si activos[i] Entonces
        Escribir "Estado: Activo"
    SiNo
        Escribir "Estado: Inactivo"
    FinSi
FinSubProceso

Proceso Proceso_modificar_producto
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
    Definir codigo,nombre,categoria Como Caracter
    Definir precio,existencia,minimo,diferencia Como Real
    Si n = 0 Entonces
        Escribir "No hay productos registrados."
    SiNo
        codigo <- Mayusculas(LeerTexto("Codigo","",Falso))
        pos <- Buscar(codigos,n,codigo)
        Si pos = -1 Entonces
            Escribir "No existe un producto con ese codigo."
        SiNo
            MostrarProducto(codigos,nombres,categorias,precios,stock,minimos,activos,pos)
            nombre <- LeerTexto("Nombre: Enter conserva",nombres[pos],Verdadero)
            categoria <- LeerTexto("Categoria: Enter conserva",categorias[pos],Verdadero)
            precio <- LeerNumero("Precio: Enter conserva",Verdadero,precios[pos],Verdadero)
            existencia <- LeerNumero("Cantidad: Enter conserva",Falso,stock[pos],Verdadero)
            minimo <- LeerNumero("Stock minimo: Enter conserva",Falso,minimos[pos],Verdadero)
            Si nombre = nombres[pos] Y categoria = categorias[pos] Y precio = precios[pos] Y existencia = stock[pos] Y minimo = minimos[pos] Entonces
                Escribir "No se realizaron cambios."
            SiNo
                diferencia <- existencia-stock[pos]
                nombres[pos] <- nombre
                categorias[pos] <- categoria
                precios[pos] <- precio
                stock[pos] <- existencia
                minimos[pos] <- minimo
                // El codigo y el estado no cambian.
                Si diferencia <> 0 Entonces
                    Escribir "Registrar movimiento con fecha ",FechaActual()," cantidad ",Abs(diferencia)
                    Si diferencia > 0 Entonces
                        Escribir "Tipo: Ajuste de entrada"
                    SiNo
                        Escribir "Tipo: Ajuste de salida"
                    FinSi
                FinSi
                Escribir "Producto modificado correctamente."
            FinSi
        FinSi
    FinSi
FinProceso
