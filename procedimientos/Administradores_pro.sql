USE mascotas_db;


# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------- Administradores ---------------------------------------


#        Cree una transacción con SQL Workbench que inserte un usuario y un administrador
DELIMITER //

CREATE PROCEDURE insertar_usuario_administrador (
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(30),
    IN p_ciudad VARCHAR(50),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_email VARCHAR(100),
    IN p_contraseña VARCHAR(255),
    IN p_cargo VARCHAR(100),
    IN p_fecha_ingreso DATE
)
BEGIN
    DECLARE last_inserted_id INT;
    
    -- Iniciar la transacción
    START TRANSACTION;
    
    -- Insertar el nuevo usuario
    INSERT INTO usuarios (nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña)
    VALUES (p_nombre, p_apellido, p_ciudad, p_direccion, p_telefono, FALSE, FALSE, TRUE, p_email, p_contraseña);
    
    -- Obtener el ID del usuario recién insertado
    SET last_inserted_id = LAST_INSERT_ID();
    
    -- Insertar el administrador usando el ID del usuario
    INSERT INTO administradores (id_usuario, cargo, fecha_ingreso)
    VALUES (last_inserted_id, p_cargo, p_fecha_ingreso);
    
    -- Confirmar la transacción
    COMMIT;
    
END //

DELIMITER ;
 # Iniciar una transacción
START TRANSACTION;

# Insertar un nuevo usuario
INSERT INTO usuarios (nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña)
VALUES ('Javier', 'García', 'Madrid', 'Calle de la Luna 35', '987654321', 0, 0, 1, 'javier.garcia@email.com', 'newpassword123');

# Obtener el id del nuevo usuario insertado
SET @new_user_id = LAST_INSERT_ID();

# Insertar un nuevo administrador utilizando el id del nuevo usuario
INSERT INTO administradores (id_usuario, cargo, fecha_ingreso)
VALUES (@new_user_id, 'Coordinador de Recursos Humanos', CURDATE());

# Finaliza la transacción
COMMIT;

# --------------------------------------- Insertar Administrador
DELIMITER //

CREATE PROCEDURE InsertarAdministrador(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_cargo VARCHAR(100),
    IN p_fecha_ingreso DATE,
    IN p_es_propietario BOOLEAN,
    IN p_es_veterinario BOOLEAN,
    IN p_es_administrador BOOLEAN,
    IN p_email VARCHAR(100),
    IN p_contraseña VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
ROLLBACK;
        RESIGNAL;
END;
   
    SET autocommit = 0;
   
    START TRANSACTION;
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
   
    INSERT INTO administradores (
id_usuario,
        cargo,
        fecha_ingreso)
    VALUES (
p_id_usuario,
        p_cargo,
        p_fecha_ingreso);

    COMMIT;
    SET autocommit = 1;
END //
DELIMITER ;

# --------------------------------------- Actualizar Administrador

DELIMITER //

CREATE PROCEDURE ActualizarAdministrador(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(30),
    IN p_ciudad VARCHAR(50),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_email VARCHAR(100),
    IN p_contraseña VARCHAR(255),
    IN p_cargo VARCHAR(100),
    IN p_fecha_ingreso DATE
)
BEGIN
    UPDATE usuarios
    SET nombre = p_nombre,
        apellido = p_apellido,
        ciudad = p_ciudad,
        direccion = p_direccion,
        telefono = p_telefono,
        email = p_email,
        contraseña = p_contraseña
    WHERE id_usuario = p_id_usuario;
    UPDATE administradores
    SET cargo = p_cargo,
        fecha_ingreso = p_fecha_ingreso
    WHERE id_usuario = p_id_usuario;
END //

DELIMITER ;

# --------------------------------------- Consultar Administrador Por Nombre

DELIMITER //

CREATE PROCEDURE ConsultarAdministradorPorNombre(
    IN p_nombre VARCHAR(50)
)
BEGIN
    SELECT
    u.id_usuario,
    u.nombre,
    u.apellido,
    u.ciudad,
    u.direccion,
    u.telefono,
    u.email,
    a.cargo,
    a.fecha_ingreso
    FROM usuarios u
    JOIN administradores a ON u.id_usuario = a.id_usuario
    WHERE u.nombre = p_nombre;
END //

DELIMITER ;

# --------------------------------------- Consultar Todos Los Admnistradores

DELIMITER //

CREATE PROCEDURE ConsultarAdministradores()
BEGIN
    SELECT
    u.id_usuario,
    u.nombre,
    u.apellido,
    u.ciudad,
    u.direccion,
    u.telefono,
    u.email,
    a.cargo,
    a.fecha_ingreso
    FROM usuarios u
    JOIN administradores a ON u.id_usuario = a.id_usuario;
END //

DELIMITER ;

# --------------------------------------- Eliminar Administrador

DELIMITER //

CREATE PROCEDURE EliminarAdministrador(
    IN p_id_usuario INT
)
BEGIN
    DELETE FROM administradores
    WHERE id_usuario = p_id_usuario;
   
    DELETE FROM usuarios
    WHERE id_usuario = p_id_usuario;
END //

DELIMITER ;

# --------------------------------------- Consultar Administrador Por ID

DELIMITER //

CREATE PROCEDURE ConsultarAdministradorPorId(
    IN p_id_usuario INT
)
BEGIN
    SELECT
    u.id_usuario,
    u.nombre,
    u.apellido,
    u.ciudad,
    u.direccion,
    u.telefono,
    u.email,
    a.cargo,
    a.fecha_ingreso
    FROM usuarios u
    JOIN administradores a ON u.id_usuario = a.id_usuario
    WHERE u.id_usuario = p_id_usuario;
END //

DELIMITER ;

# ------------------------------- elimine un usuario y un administrador

DELIMITER //

CREATE PROCEDURE EliminarUsuarioYAdministrador(
    IN p_id_usuario INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Manejo de errores: en caso de error, realiza un ROLLBACK
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar usuario y administrador.';
    END;

    -- Inicia la transacción
    START TRANSACTION;

    -- Verificar si el administrador existe
    IF EXISTS (SELECT 1 FROM administradores WHERE id_usuario = p_id_usuario) THEN
        -- Eliminar el administrador
        DELETE FROM administradores WHERE id_usuario = p_id_usuario;

        -- Eliminar el usuario asociado
        DELETE FROM usuarios WHERE id_usuario = p_id_usuario;

        -- Confirmar la transacción
        COMMIT;
    ELSE
        -- Manejo de error si el administrador no existe
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El administrador con el ID especificado no existe.';
    END IF;
END //

DELIMITER ;

