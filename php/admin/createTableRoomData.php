<?php
// Author : Steve Gale 27/03/19
// Modified : SG - 29/03/19 -
// Copyright 2019 Steve Gale - seek permission and terms of use before you copy or modify this code
$servername = "localhost";
$username = "I40";
$password = "Password1";
$dbname = "Industry40db";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// sql to create table
$sql = "CREATE TABLE roomData (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
        roomName VARCHAR(20) NOT NULL,
        humidity VARCHAR(8),
        temperature VARCHAR(8),
        outsideTemp VARCHAR(4),
        CO2 VARCHAR(8),
        readDate TIMESTAMP
    )";


if (mysqli_query($conn, $sql)) {
    echo "Table TestData created successfully";
} else {
    echo "Error creating table: " . mysqli_error($conn);
}

mysqli_close($conn);
?>
