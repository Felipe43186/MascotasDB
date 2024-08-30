USE mascotas_db;

# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------- Veterinarios ---------------------------------------


# --------------------------------------- Insertar Veterinario
DELIMITER //

CREATE PROCEDURE InsertarVeterinario(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_ciudad VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(100),
    IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(255),
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
   
    INSERT INTO veterinarios (
id_usuario,
        especialidad,
        horario)
    VALUES (
p_id_usuario,
        p_especialidad,
        p_horario);

    COMMIT;
    SET autocommit = 1;
END //
DELIMITER ;

# --------------------------------------- Consultar Veterinario Por Nombre

DELIMITER //

CREATE PROCEDURE ConsultarVeterinarioPorNombre (
    IN p_nombre VARCHAR(255)
)
BEGIN
    SELECT
        u.id_usuario,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
        u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        u.contraseña,
        v.especialidad,
        v.horario
    FROM
        veterinarios v
    JOIN
        usuarios u ON v.id_usuario = u.id_usuario
    WHERE
        u.nombre = p_nombre;
END //

DELIMITER ;

# --------------------------------------- Consultar veterinario Por ID

DELIMITER //

CREATE PROCEDURE ConsultarVeterinarioPorId(
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
    v.especialidad,
    v.horario
    FROM usuarios u
    JOIN veterinarios v ON u.id_usuario = v.id_usuario
    WHERE u.id_usuario = p_id_usuario;
END //

DELIMITER ;

# --------------------------------------- Consultar Veterinarios

DELIMITER //

CREATE PROCEDURE ConsultarVeterinarios()
BEGIN
    SELECT
        u.id_usuario,
        u.nombre,
        u.apellido,
        u.ciudad,
        u.direccion,
        u.telefono,
u.es_propietario,
        u.es_veterinario,
        u.es_administrador,
        u.email,
        u.contraseña,
        v.especialidad,
        v.horario
    FROM
      veterinarios v
    JOIN
        usuarios u ON v.id_usuario = u.id_usuario;
END //

DELIMITER ;

# --------------------------------------- Actualizar Veterinarios

DELIMITER //

CREATE PROCEDURE ActualizarVeterinario(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(30),
    IN p_ciudad VARCHAR(50),
    IN p_direccion VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_email VARCHAR(100),
    IN p_contraseña VARCHAR(255),
    IN p_especialidad VARCHAR(100),
    IN p_horario VARCHAR(255)
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
    UPDATE veterinarios
    SET especialidad = p_especialidad,
        horario = p_horario
    WHERE id_usuario = p_id_usuario;
END //

DELIMITER ;

# --------------------------------------- Eliminar Veterinario

DELIMITER //

CREATE PROCEDURE EliminarVeterinario(
    IN p_id_usuario INT
)
BEGIN
    DELETE FROM veterinarios
    WHERE id_usuario = p_id_usuario;
   
    DELETE FROM usuarios
    WHERE id_usuario = p_id_usuario;
END //

DELIMITER ;
