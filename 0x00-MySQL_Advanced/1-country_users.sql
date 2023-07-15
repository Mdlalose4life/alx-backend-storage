-- An SQL script that creates a table users that has:
-- id, email, name, country
CREATE TABLE IF NOT EXISTS users(
    id int NOT NULL PRIMARY_KEY AUTO_INCREMENT ,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
)