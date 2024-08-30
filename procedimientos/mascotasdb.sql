CREATE DATABASE IF NOT EXISTS mascotas_db;
USE mascotas_db;

# Tabla usuarios

CREATE TABLE usuarios (
id_usuario INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(30) NOT NULL,
ciudad VARCHAR(50) NOT NULL,
direccion VARCHAR(100) NOT NULL,
telefono VARCHAR(20) NOT NULL,
es_propietario BOOLEAN DEFAULT TRUE,
es_veterinario BOOLEAN DEFAULT FALSE,
es_administrador BOOLEAN DEFAULT FALSE,
email VARCHAR(100) NOT NULL ,
contraseña VARCHAR(255) NOT NULL
);

# Tbala administradores

CREATE TABLE administradores (
id_usuario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
cargo VARCHAR(100) NOT NULL,
fecha_ingreso DATE NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

# Tabla propietarios

CREATE TABLE propietarios (
id_usuario INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

# Tabla veterinarios

CREATE TABLE veterinarios (
id_usuario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
especialidad VARCHAR(100)NOT NULL,
horario VARCHAR(255)NOT NULL,
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

# Tabla mascotas

CREATE TABLE mascotas (
codigo INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombre VARCHAR (100) NOT NULL,
especie VARCHAR(100) NOT NULL,
raza VARCHAR (100) NOT NULL,
edad DECIMAL (10,2) NOT NULL,
peso DECIMAL (10,2) NOT NULL,
id_usuario int,
FOREIGN KEY (id_usuario) REFERENCES propietarios(id_usuario)
);

# Tabla productos

CREATE TABLE productos(
codigo INT NOT NULL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
descripcion TEXT NOT NULL,
precio DECIMAL(20,2) NOT NULL,
stock SMALLINT NOT NULL
);

# Tabla servicios

CREATE TABLE servicios(
codigo INT NOT NULL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
descripcion TEXT NOT NULL,
precio DECIMAL(20,2) NOT NULL
);

#  Tabla citas

CREATE TABLE citas(
codigo INT NOT NULL PRIMARY KEY,
fecha DATE NOT NULL,
hora TIME NOT NULL,
id_servicio INT NOT NULL,
id_veterinario INT NOT NULL,
codigo_mascota INT NOT NULL,
FOREIGN KEY (id_servicio) REFERENCES servicios(codigo),
FOREIGN KEY (id_veterinario) REFERENCES veterinarios(id_usuario),
FOREIGN KEY (codigo_mascota) REFERENCES mascotas(codigo),
estado ENUM('PENDIENTE', 'CANCELADA', 'VERIFICADA', 'REALIZADA')
);

# Tabla historiales medicos

CREATE TABLE historiales_medicos(
codigo INT NOT NULL PRIMARY KEY,
fecha DATE NOT NULL,
descripcion TEXT NOT NULL,
tratamiento TEXT NOT NULL,
FOREIGN KEY (codigo) REFERENCES mascotas(codigo)
);



# Insertar datos a la tabla Usuarios

INSERT INTO usuarios(id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña)
VALUES
(1, 'Juan', 'Pérez', 'Madrid', 'Calle Falsa 123', '123456789', 1, 0, 0, 'juan.perez@email.com', 'password123'),
(2, 'Ana', 'López', 'Barcelona', 'Av. Siempre Viva 742', '987654321', 1, 1, 0, 'ana.lopez@email.com', 'password456'),
(3, 'Carlos', 'Gómez', 'Valencia', 'Plaza Mayor 5', '456123789', 0, 0, 1, 'carlos.gomez@email.com', 'password789'),
(4, 'Marta', 'Ruiz', 'Sevilla', 'C/ de la Esperanza 9', '654321987', 0, 0, 1, 'marta.ruiz@email.com', 'password321'),
(5, 'Luis', 'Martínez', 'Bilbao', 'C/ Libertad 15', '321654987', 1, 0, 0, 'luis.martinez@email.com', 'password654'),
(6, 'Fernando', 'García', 'Madrid', 'Calle del Sol 45', '612345678', 0, 0, 1, 'fernando.garcia@email.com', 'password135'),
(7, 'Sofía', 'Hernández', 'Valencia', 'Plaza del Ayuntamiento 3', '698765432', 1, 0, 0, 'sofia.hernandez@email.com', 'password246'),
(8, 'Javier', 'Martínez', 'Sevilla', 'Calle de la Paz 27', '634567890', 1, 0, 0, 'javier.martinez@email.com', 'password357'),
(9, 'Lucía', 'González', 'Bilbao', 'Av. de la Libertad 12', '612987654', 0, 1, 0, 'lucia.gonzalez@email.com', 'password468'),
(10, 'Pedro', 'Sánchez', 'Granada', 'Calle Nueva 8', '678123456', 0, 0, 1, 'pedro.sanchez@email.com', 'password579');

SELECT * FROM usuarios;


# Insertar datos a la tabla propietarios

INSERT INTO propietarios (id_usuario)
VALUES
('1'),
('2'),
('3'),
('4'),
('5');                

SELECT * FROM propietarios;

# Insertar datos a la tabla mascotas

insert into mascotas(codigo, nombre, especie, raza, edad, peso)
values
('11', 'MELOSO', 'PERRO', 'BULL DOG', '1', '22.00'),
('12', 'PULGAS', 'PERRO', 'FRENCH POODLE', '3', '12.01'),
('13', 'PELIROJO', 'PERRO', 'CRIOLLO COLOMBIANO', '2', '26.00'),
('14', 'MICHIFUS', 'GATO', 'ABISINO', '4', '5.00'),
('15', 'FIRULAIS', 'PERRO', 'XOLITZCUINTLE', '10', '16.00'),
('16', 'THOR', 'PERRO', 'PASTOR ALEMAN', '1', '32.00'),
('17', 'ESTRELLA', 'CABALLO', 'FRISON', '5', '236.00'),
('18', 'ALMA', 'PERRO', 'BEAGLE', '4', '22.00'),
('19', 'MIMI', 'GATO', 'GATO ESFINGE', '2', '7.00'),
('20', 'OREO', 'GATO', 'RAGDOLL', '6', '5.00'),
('21', 'LUNA', 'PERRO', 'HUSKI SIBERIANO', '8', '22.00');


# ------------------------------------- RELACIONAR DOS TABLAS--------------------------------------------------------- #

SELECT p.*, m.*, u.*
FROM propietarios p
INNER JOIN mascotas m ON p.id_usuario = m.id_usuario
INNER JOIN usuarios u ON p.id_usuario = u.id_usuario;

SELECT p.*, u.*
FROM propietarios p
INNER JOIN usuarios u ON p.id_usuario = u.id_usuario;

SELECT a.*, u.*
FROM administradores a
INNER JOIN usuarios u ON a.id_usuario = u.id_usuario;

SELECT v.*, u.*
FROM veterinarios v
INNER JOIN usuarios u ON v.id_usuario = u.id_usuario;

SELECT LOWER(email) AS email, UPPER(nombre) AS nombre, UPPER(apellido) AS apellido
FROM usuarios;

