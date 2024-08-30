
USE mascotas_db;
# --------------------------------------- MASCOTAS ---------------------------------------
 
 # --------------------------------------- insertar mascota 
 
 -- Función para insertar una mascota
DELIMITER //

CREATE PROCEDURE InsertarMascota(
    IN p_nombre VARCHAR(100),
    IN p_especie VARCHAR(100),
    IN p_raza VARCHAR(100),
    IN p_edad DECIMAL(10,2),
    IN p_peso DECIMAL(10,2),
    IN p_id_usuario INT
)
BEGIN
    DECLARE prop_id INT;

    -- Verificar si el usuario es un propietario registrado
    SELECT id_usuario INTO prop_id 
    FROM propietarios 
    WHERE id_usuario = p_id_usuario;

    IF prop_id IS NOT NULL THEN
        -- Insertar la mascota
        INSERT INTO mascotas (nombre, especie, raza, edad, peso, id_usuario) 
        VALUES (p_nombre, p_especie, p_raza, p_edad, p_peso, p_id_usuario);
    ELSE
        -- Manejo de error si el usuario no es un propietario registrado
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El usuario especificado no es un propietario registrado.';
    END IF;
END //

DELIMITER ;

 # --------------------------------------- consultar una mascota

DELIMITER //

CREATE PROCEDURE ConsultarMascota(
    IN p_codigo INT
)
BEGIN
    -- Selecciona la información de la mascota basada en su código
    SELECT 
        m.codigo,
        m.nombre,
        m.especie,
        m.raza,
        m.edad,
        m.peso,
        u.nombre AS nombre_propietario,
        u.apellido AS apellido_propietario,
        u.telefono AS telefono_propietario,
        u.email AS email_propietario
    FROM 
        mascotas m
    JOIN 
        propietarios p ON m.id_usuario = p.id_usuario
    JOIN 
        usuarios u ON p.id_usuario = u.id_usuario
    WHERE 
        m.codigo = p_codigo;
END //

DELIMITER ;

 # --------------------------------------- Consultar mascota por nombre

DELIMITER //

CREATE PROCEDURE ConsultarMascotaPorNombre(
    IN p_nombre VARCHAR(100)
)
BEGIN
    -- Selecciona la información de la mascota basada en su nombre
    SELECT 
        m.codigo,
        m.nombre,
        m.especie,
        m.raza,
        m.edad,
        m.peso,
        u.nombre AS nombre_propietario,
        u.apellido AS apellido_propietario,
        u.telefono AS telefono_propietario,
        u.email AS email_propietario
    FROM 
        mascotas m
    JOIN 
        propietarios p ON m.id_usuario = p.id_usuario
    JOIN 
        usuarios u ON p.id_usuario = u.id_usuario
    WHERE 
        m.nombre = p_nombre;
END //

DELIMITER ;

 # --------------------------------------- Consultar todas las mascotas

DELIMITER //

CREATE PROCEDURE ConsultarTodasLasMascotas()
BEGIN
    -- Selecciona toda la información de todas las mascotas y sus propietarios
    SELECT 
        m.codigo,
        m.nombre,
        m.especie,
        m.raza,
        m.edad,
        m.peso,
        u.nombre AS nombre_propietario,
        u.apellido AS apellido_propietario,
        u.telefono AS telefono_propietario,
        u.email AS email_propietario
    FROM 
        mascotas m
    JOIN 
        propietarios p ON m.id_usuario = p.id_usuario
    JOIN 
        usuarios u ON p.id_usuario = u.id_usuario;
END //

DELIMITER ;

 # --------------------------------------- Actualizar Mascota


DELIMITER //

CREATE PROCEDURE ActualizarMascota(
    IN p_codigo INT,
    IN p_nombre VARCHAR(100),
    IN p_especie VARCHAR(100),
    IN p_raza VARCHAR(100),
    IN p_edad DECIMAL(10,2),
    IN p_peso DECIMAL(10,2),
    IN p_id_usuario INT
)
BEGIN
    -- Verificar si la mascota existe
    IF EXISTS (SELECT 1 FROM mascotas WHERE codigo = p_codigo) THEN
        -- Actualizar la información de la mascota
        UPDATE mascotas
        SET 
            nombre = p_nombre,
            especie = p_especie,
            raza = p_raza,
            edad = p_edad,
            peso = p_peso,
            id_usuario = p_id_usuario
        WHERE 
            codigo = p_codigo;
    ELSE
        -- Manejo de error si la mascota no existe
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'La mascota con el código especificado no existe.';
    END IF;
END //

DELIMITER ;

 # --------------------------------------- Eliminar Mascota

DELIMITER //

CREATE PROCEDURE EliminarMascota(
    IN p_codigo INT
)
BEGIN
    -- Verificar si la mascota existe
    IF EXISTS (SELECT 1 FROM mascotas WHERE codigo = p_codigo) THEN
        -- Eliminar la mascota
        DELETE FROM mascotas WHERE codigo = p_codigo; ##########
    ELSE
        -- Manejo de error si la mascota no existe
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'La mascota con el código especificado no existe.';
    END IF;
END //

DELIMITER ;
