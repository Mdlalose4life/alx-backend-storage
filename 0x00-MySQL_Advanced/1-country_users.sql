-- An SQL script that creates a table users that has:
-- id, email, name, country
CREATE TABLE if NOT EXISTS users(
    id int NOT NULL AUTO_INCREMENT PRIMARY_KEY,
    email varchar(255) NOT NULL,
    name varchar(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
)