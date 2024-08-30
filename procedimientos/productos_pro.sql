USE mascotas_db;


#---------------------------------------------------------------------------------------------------------------------
# --------------------------------------- PRODUCTOS ---------------------------------------

# --------------------------------------- Insertar Productos

DELIMITER //

CREATE PROCEDURE InsertarProducto(
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2),
    IN p_stock SMALLINT
)
BEGIN
    INSERT INTO productos (nombre, descripcion, precio, stock)
    VALUES (p_nombre, p_descripcion, p_precio, p_stock);
END //

DELIMITER ;


# --------------------------------------- Buscar Producto Por Codigo 

DELIMITER //

CREATE PROCEDURE BuscarProductoPorCodigo(
    IN p_codigo INT
)
BEGIN
    SELECT codigo, nombre, descripcion, precio, stock
    FROM productos
    WHERE codigo = p_codigo;
END //

DELIMITER ;


# --------------------------------------- Buscar Producto Por Nombre

DELIMITER //

CREATE PROCEDURE BuscarProductoPorNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN

    SELECT codigo, nombre, descripcion, precio, stock
    FROM productos
    WHERE nombre = p_nombre;
END //

DELIMITER ;

# --------------------------------------- Buscar Productos


DELIMITER //

CREATE PROCEDURE BuscarProductos()
BEGIN

    SELECT codigo, nombre, descripcion, precio, stock
    FROM productos;
END //

DELIMITER ;


# --------------------------------------- Eliminar Productos


DELIMITER //

CREATE PROCEDURE EliminarProducto(
    IN p_codigo INT
)
BEGIN

    DELETE FROM productos
    WHERE codigo = p_codigo;
END //

DELIMITER ;

