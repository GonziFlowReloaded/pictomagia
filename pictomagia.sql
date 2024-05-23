DROP DATABASE IF EXISTS pictomagia;

CREATE DATABASE pictomagia;

USE pictomagia;

CREATE TABLE tipo_usuario (
    id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL
);

INSERT INTO tipo_usuario (tipo) VALUES ('admin'), ('user_normal');

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    tipo_usuario_id INT NOT NULL DEFAULT 2,
    birthdate VARCHAR(255) NOT NULL,
    img VARCHAR(255) NOT NULL DEFAULT 'default-photo.png',
    FOREIGN KEY (tipo_usuario_id) REFERENCES tipo_usuario(id_tipo_usuario)
);

CREATE TABLE carpeta_general (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ruta_pictograma VARCHAR(255) NOT NULL,
    nombre_carpeta VARCHAR(100) NOT NULL,
    ruta_imagen_carpeta VARCHAR(255) DEFAULT 'folder_image.png'
);

CREATE TABLE carpeta_personal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ruta_pictograma VARCHAR(255) NOT NULL,
    nombre_carpeta VARCHAR(100) NOT NULL,
    ruta_imagen_carpeta VARCHAR(255) DEFAULT 'folder_image.png'
);

CREATE TABLE usuarios_carpetas_personales (
    usuario_id INT NOT NULL,
    carpeta_personal_id INT NOT NULL,
    PRIMARY KEY (usuario_id, carpeta_personal_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (carpeta_personal_id) REFERENCES carpeta_personal(id)
);

INSERT INTO usuarios (email, contrasena, tipo_usuario_id, birthdate) 
VALUES ('admin@example.com', 'admin', 1, '1990-01-01');
INSERT INTO usuarios (email, contrasena, tipo_usuario_id, birthdate) 
VALUES ('gonsi', 'gonsi', 2, '1990-01-01');

INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) 
VALUES ('/pictogramas/1', '¡A cepillarse los dientes!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) 
VALUES ('/pictogramas/2', '¡A despertarse!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) 
VALUES ('/pictogramas/3', '¡Hora de merendar!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) 
VALUES ('/pictogramas/4', '¡Hora de cenar!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) 
VALUES ('/pictogramas/5', '¡Hora de vestirse!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) 
VALUES ('/pictogramas/6', '¡Hora de bañarse!', 'folder_image.png');

INSERT INTO carpeta_personal (ruta_pictograma, nombre_carpeta) 
VALUES ('/pictogramas/p-1', '¡Al Colegio!');
INSERT INTO carpeta_personal (ruta_pictograma, nombre_carpeta) 
VALUES ('/pictogramas/p-2', '¡Mascotas!');

INSERT INTO usuarios_carpetas_personales (usuario_id, carpeta_personal_id) 
VALUES (1, 1), (2, 1), (2, 2);

SELECT * FROM usuarios;
SELECT * FROM tipo_usuario;
SELECT * FROM carpeta_general;
SELECT * FROM carpeta_personal;
SELECT * FROM usuarios_carpetas_personales;
