USE mascotas_db;

# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------- HISTORIALES MÉDICOS ---------------------------------------

# --------------------------------------- Insertar Historial Medico


DELIMITER //

CREATE PROCEDURE InsertarHistorialMedico(
    IN p_codigo_mascota INT,
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT
)
BEGIN
    INSERT INTO historiales_medicos (codigo, fecha, descripcion, tratamiento)
    VALUES (p_codigo_mascota, p_fecha, p_descripcion, p_tratamiento);
END //

DELIMITER ;


# --------------------------------------- Buscar Historial Por Mascota


DELIMITER //

CREATE PROCEDURE BuscarHistorialPorMascota(
    IN p_codigo_mascota INT
)
BEGIN
 
	SELECT codigo, fecha, descripcion, tratamiento
    FROM historiales_medicos
    WHERE codigo = p_codigo_mascota;
END //

DELIMITER ;


# --------------------------------------- Actualizar Historia Por Mascota


DELIMITER //

CREATE PROCEDURE ActualizarHistorialPorMascota(
    IN p_codigo_mascota INT,
    IN p_fecha DATE,
    IN p_descripcion TEXT,
    IN p_tratamiento TEXT
)
BEGIN

    UPDATE historiales_medicos
    SET fecha = p_fecha,
        descripcion = p_descripcion,
        tratamiento = p_tratamiento
    WHERE codigo = p_codigo_mascota;
END //

DELIMITER ;

# --------------------------------------- Consultar Todos los Historiales Medicos

DELIMITER //

CREATE PROCEDURE ConsultarTodosLosHistorialesMedicos()
BEGIN
    SELECT 
        h.id_historial, 
        h.fecha, 
        h.diagnostico, 
        h.tratamiento, 
        m.nombre AS nombre_mascota, 
        v.nombre AS nombre_veterinario
    FROM 
        historiales_medicos h
    JOIN 
        mascotas m ON h.id_mascota = m.id_mascota
    JOIN 
        veterinarios v ON h.id_veterinario = v.id_veterinario;
END;

DELIMITER ;

# --------------------------------------- Eliminar Historial
 

DELIMITER //

CREATE PROCEDURE EliminarHistorial(
    IN p_codigo_mascota INT
)
BEGIN

    DELETE FROM historiales_medicos
    WHERE codigo = p_codigo_mascota;
END //

DELIMITER ;

