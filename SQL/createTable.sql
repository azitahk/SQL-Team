CREATE TABLE roomData (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
        roomName VARCHAR(20) NOT NULL,
        humidity VARCHAR(8),
        temperature VARCHAR(8),
        outsideTemp VARCHAR(4),
        CO2 VARCHAR(8),
        readDate TIMESTAMP
    );