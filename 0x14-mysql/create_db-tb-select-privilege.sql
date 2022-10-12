-- Create a database named tyrell_corp and table nexus6 and give SELECT privilege

CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);
INSERT INTO tyrell_corp.nexus6(name)
VALUES('Leon')
