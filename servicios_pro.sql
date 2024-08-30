USE mascotas_db;


# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------- SERVICIOS ---------------------------------------

# --------------------------------------- Insertar Servicio

DELIMITER //

CREATE PROCEDURE InsertarServicio(
    IN p_nombre VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_precio DECIMAL(20,2)
)
BEGIN

    INSERT INTO servicios (nombre, descripcion, precio)
    VALUES (p_nombre, p_descripcion, p_precio);
END //

DELIMITER ;


# --------------------------------------- Buscar Servicio Por Código


DELIMITER //

CREATE PROCEDURE BuscarServicioPorCodigo(
    IN p_codigo INT
)
BEGIN

    SELECT codigo, nombre, descripcion, precio
    FROM servicios
    WHERE codigo = p_codigo;
END //

DELIMITER ;


# --------------------------------------- Buscar Servicio Por nombre


DELIMITER //

CREATE PROCEDURE BuscarServicioPorNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN

    SELECT codigo, nombre, descripcion, precio
    FROM servicios
    WHERE nombre = p_nombre;
END //

DELIMITER ;


# --------------------------------------- Buscar Servicios

DELIMITER //

CREATE PROCEDURE buscarservicios(
	IN p_nombre varchar(100)
    
)
BEGIN

	SELECT codigo, nombre, descripcion, precio
    FROM servicios;
END//

DELIMITER ;

# --------------------------------------- Eliminar Servicio


DELIMITER //

CREATE PROCEDURE EliminarServicio(
    IN p_codigo INT
)
BEGIN

    DELETE FROM servicios
    WHERE codigo = p_codigo;
END //

DELIMITER ;

