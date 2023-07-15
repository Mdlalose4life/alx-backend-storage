-- SQL Script to create table (users) with
-- id, email. name
CRATE IF NOT EXISTE users (
    id INT PRIMIRY KEY AUTO_INCREMENT,
    email varchar(255) NOT NULL UQUIE,
    name varchar(255)
)