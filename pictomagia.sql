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
    tipo_usuario_id INT NOT NULL DEFAULT 1,
    birthdate VARCHAR(255) NOT NULL,
    img VARCHAR(255) NOT NULL default "default-photo.png",
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
    ruta_imagen_carpeta VARCHAR(255) DEFAULT 'folder_image.png',
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);



INSERT INTO usuarios (email, contrasena, tipo_usuario_id, birthdate) 
VALUES ('admin@example.com', 'admin', 1, '1990-01-01');
INSERT INTO usuarios (email, contrasena, tipo_usuario_id, birthdate) 
VALUES ('gonsi', 'gonsi', 1, '1990-01-01');

INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) VALUES ('/pictogramas/1', '¡A cepillarse los dientes!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) VALUES ('/pictogramas/2', '¡A despertarse!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) VALUES ('/pictogramas/3', '¡Hora de merendar!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) VALUES ('/pictogramas/4', '¡Hora de cenar!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) VALUES ('/pictogramas/5', '¡Hora de vestirse!', 'folder_image.png');
INSERT INTO carpeta_general (ruta_pictograma, nombre_carpeta, ruta_imagen_carpeta) VALUES ('/pictogramas/6', '¡Hora de bañarse!', 'folder_image.png');

insert into carpeta_personal(ruta_pictograma, nombre_carpeta, usuario_id) values ('/pictogramas/p-1', '¡Al Colegio!', 1);
insert into carpeta_personal(ruta_pictograma, nombre_carpeta, usuario_id) values ('/pictogramas/p-2', '¡Mascotas!', 2);
SELECT * FROM usuarios;
select * from tipo_usuario;
select * from carpeta_general;

