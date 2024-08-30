USE mascotas_db;

# --------------------------------------- PROPIETARIOS DE MASCOTAS ---------------------------------------

# --------------------------------------- Insertar Propietarios (Usando transaccion para insertar usuario y propietario)


DELIMITER //

CREATE PROCEDURE InsertarPropietario(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_barrio VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_es_propietario BOOLEAN,
    IN p_es_veterinario BOOLEAN,
    IN p_es_administrador BOOLEAN,
    IN p_email VARCHAR(100),
    IN p_contraseña VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		-- Deshacer los cambios en la BD si algo falla
		ROLLBACK;
        RESIGNAL;
	END;
    
    SET autocommit = 0;
    
    -- Arrancar la transacción:
    START TRANSACTION;
    -- Insertar en la tabla 'usuarios'
    INSERT INTO usuarios (
		id_usuario,
        nombre, 
        apellido,
        ciudad,
        direccion,
        telefono,
        es_propietario,
        es_veterinario,
        es_administrador,
        email,
        contraseña)
    VALUES (
		p_id_usuario,
        p_nombre,
        p_apellido,
        p_ciudad,
        p_direccion,
        p_telefono,
        p_es_propietario,
        p_es_veterinario,
        p_es_administrador,
        p_email, 
        p_contraseña);
    
    -- Insertar en la tabla 'propietarios'
    INSERT INTO propietarios (
		id_usuario,
        barrio)
    VALUES (
		p_id_usuario,
        p_barrio);
    
    -- Confirmar la transacción si ambas operaciones son exitosas
    COMMIT;
    SET autocommit = 1;
END //
DELIMITER ;

-- Procedimiento CrearPropietario() sin usar una TRANSACCION SQL
DELIMITER //
CREATE PROCEDURE CrearPropietario(
IN p_id_usuario INT,
IN p_nombre VARCHAR(100),
IN p_apellido VARCHAR(100),
IN p_ciudad VARCHAR(100),
IN p_direccion VARCHAR(100),
IN p_barrio VARCHAR(100), 
IN p_telefono VARCHAR(100),
IN p_es_propietario BOOLEAN,
IN p_es_veterinario BOOLEAN,
IN p_es_administrador BOOLEAN,
IN p_email VARCHAR(100),
IN p_contraseña VARCHAR(255)
)
BEGIN
	INSERT INTO usuarios(
		id_usuario, 
        nombre, 
        apellido, 
        ciudad, 
        direccion, 
        telefono, 
        es_propietario, 
        es_veterinario, 
        es_administrador, 
        email, 
        contraseña)
    VALUES(
		p_id_usuario, 
        p_nombre, 
        p_apellido,
        p_ciudad, 
        p_direccion, 
        p_telefono, 
        p_es_propietario, 
        p_es_veterinario, 
        p_es_administrador, 
        p_email, 
        p_contraseña);
	INSERT INTO propietarios(
		id_usuario,
        barrio)
    VALUES(
		p_id_usuario,
        p_barrio);
    
END //
DELIMITER ;
-- Fin del procedimiento



 # --------------------------------------- Consultar Propietarios por id
 

DELIMITER //

CREATE PROCEDURE ConsultarPropietarioPorID(
    IN p_id_usuario INT
)
BEGIN
    -- Selecciona la información del propietario y el usuario asociado
    SELECT 
        u.id_usuario,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email
    FROM 
        usuarios u
    JOIN 
        propietarios p ON u.id_usuario = p.id_usuario
    WHERE 
        u.id_usuario = p_id_usuario;
END //

DELIMITER ;

# --------------------------------------- Consultar Propietario por nombre 


DELIMITER //

CREATE PROCEDURE ConsultarPropietarioPorNombre(
    IN p_nombre VARCHAR(50)
)
BEGIN
    -- Selecciona la información del propietario y el usuario asociado por nombre
    SELECT 
        u.id_usuario,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email
    FROM 
        usuarios u
    JOIN 
        propietarios p ON u.id_usuario = p.id_usuario
    WHERE 
        u.nombre = p_nombre;
END //

DELIMITER ;

# --------------------------------------- Consultar todos los Propietarios


DELIMITER //

CREATE PROCEDURE ConsultarTodosLosPropietarios()
BEGIN
    -- Selecciona toda la información de todos los propietarios y sus datos de usuario
    SELECT 
        u.id_usuario,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.email
    FROM 
        usuarios u
    JOIN 
        propietarios p ON u.id_usuario = p.id_usuario;
END //

DELIMITER ;

# --------------------------------------- Actualizar Propietario


DELIMITER //

CREATE PROCEDURE ActualizarPropietario(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(30),
    IN p_ciudad VARCHAR(50),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_email VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Manejo de errores: en caso de error, realiza un ROLLBACK
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar propietario.';
    END;

    -- Inicia la transacción
    START TRANSACTION;

    -- Verificar si el usuario existe
    IF EXISTS (SELECT 1 FROM usuarios WHERE id_usuario = p_id_usuario) THEN
        -- Actualizar la información del usuario
        UPDATE usuarios
        SET 
            nombre = p_nombre,
            apellido = p_apellido,
            ciudad = p_ciudad,
            direccion = p_direccion,
            telefono = p_telefono,
            email = p_email
        WHERE 
            id_usuario = p_id_usuario;
        
        -- Confirmar la transacción
        COMMIT;
    ELSE
        -- Manejo de error si el usuario no existe
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El usuario con el ID especificado no existe.';
    END IF;
END //

DELIMITER ;

# --------------------------------------- Eliminar Propietario


DELIMITER //

CREATE PROCEDURE EliminarPropietario(
    IN p_id_usuario INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Manejo de errores: en caso de error, realiza un ROLLBACK
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar propietario.';
    END;

    -- Inicia la transacción
    START TRANSACTION;

    -- Verificar si el propietario existe
    IF EXISTS (SELECT 1 FROM propietarios WHERE id_usuario = p_id_usuario) THEN
        -- Eliminar el propietario
        DELETE FROM propietarios WHERE id_usuario = p_id_usuario;

        -- Eliminar el usuario asociado
        DELETE FROM usuarios WHERE id_usuario = p_id_usuario;

        -- Confirmar la transacción
        COMMIT;
    ELSE
        -- Manejo de error si el propietario no existe
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El propietario con el ID especificado no existe.';
    END IF;
END //

DELIMITER ;

# No se xd

-- Preparar tablas para que usen el motor INNO y acepten transacciones
-- ------------------------------------------------------------
-- Verificar el motor de almacenamiento
SHOW TABLE STATUS WHERE Name = 'usuarios';
SHOW TABLE STATUS WHERE Name = 'propietarios';

-- Cambiar el motor de almacenamiento a InnoDB si no es ya InnoDB
ALTER TABLE usuarios ENGINE = InnoDB;
ALTER TABLE propietarios ENGINE = InnoDB;
-- ------------------------------------------------------------


