USE mascotas_db;


# ---------------------------------------------------------------------------------------------------------------------
# --------------------------------------- CITAS ---------------------------------------

# --------------------------------------- Insertar Cita

DELIMITER //

CREATE PROCEDURE insertarCita(
	IN p_fecha DATE,
    IN p_hora TIME,
    IN p_id_servicio INT,
    IN p_id_veterinario INT,
    IN p_codigo_mascota INT,
    IN p_estado ENUM('PENDIENTE', 'CANCELADA', 'VERIFICADA', 'REALIZADO')
)
BEGIN

	INSERT INTO citas(fecha, hora, id_servicio, id_veterinario, codigo_mascota, estado)
    VALUES (p_fecha, p_hora, p_id_servicio, p_id_veterinario, p_codigo_mascota, p_estado);
END//

DELIMITER ;


# --------------------------------------- Buscar Cita Por fecha

DELIMITER //

CREATE PROCEDURE BuscarCitaPorFecha(
	IN p_fecha DATE

)
BEGIN

	SELECT codigo, fecha, hora, estado
    FROM citas
    WHERE fecha = p_fecha;

END;

DELIMITER ;

# --------------------------------------- Buscar Cita Por Mascota

DELIMITER //

CREATE PROCEDURE BuscarCitaPorMascota(
	IN p_codigo_mascota int 

)

BEGIN

	SELECT codigo, fecha, hora, id_servicio, id_veterinario, estado
    FROM citas
    WHERE codigo_mascota = p_codigo_mascota;

END;

DELIMITER ;

# --------------------------------------- Elminar historial de citas Por Codigo 

DELIMITER //

CREATE PROCEDURE EliminarHistorialDeCitasPorCodigo(
	IN p_codigo INT 

)
BEGIN

	DELETE FROM citas
    WHERE codigo = p_codigo;
    
END;

DELIMITER ;