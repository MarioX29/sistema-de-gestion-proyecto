// Proceso aislado para diagramar. Perfil Flexible, indices base cero.
SubProceso MostrarProducto(codigos,nombres,categorias,precios,stock,minimos,activos,i)
    Escribir "Codigo: ",codigos[i]," Nombre: ",nombres[i]," Categoria: ",categorias[i]
    Escribir "Precio: ",precios[i]," Cantidad: ",stock[i]," Minimo: ",minimos[i]
    Si activos[i] Entonces
        Escribir "Estado: Activo"
    SiNo
        Escribir "Estado: Inactivo"
    FinSi
FinSubProceso

Proceso Proceso_listar_productos
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
    Si n = 0 Entonces
        Escribir "No hay productos registrados."
    SiNo
        Para i <- 0 Hasta n-1 Hacer
            MostrarProducto(codigos,nombres,categorias,precios,stock,minimos,activos,i)
        FinPara
    FinSi
FinProceso
