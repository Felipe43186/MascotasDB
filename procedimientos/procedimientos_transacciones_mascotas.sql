
use mascotas_db;

-- Preparar tablas para que usen el motor INNO y acepten transacciones
-- ------------------------------------------------------------
-- Verificar el motor de almacenamiento
SHOW TABLE STATUS WHERE Name = 'usuarios';
SHOW TABLE STATUS WHERE Name = 'propietarios';

-- Cambiar el motor de almacenamiento a InnoDB si no es ya InnoDB
ALTER TABLE usuarios ENGINE = InnoDB;
ALTER TABLE propietarios ENGINE = InnoDB;
-- ------------------------------------------------------------


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


-- Con TRANSACCIONES

-- Procedimiento para insertar en tablas propietarios y usuarios usando una TRANSACCION SQL
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

