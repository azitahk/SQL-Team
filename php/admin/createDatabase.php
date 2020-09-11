<?php
// Author : Steve Gale 27/03/19
// Modified : SG - 29/03/19 -
// Copyright 2019 Steve Gale - seek permission and terms of use before you copy or modify this code
$servername = "localhost";
$username = "I40";
$password = "Password1";

// Create connection
$conn = mysqli_connect($servername, $username, $password);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Create MySQL database 
$sql = "CREATE DATABASE Industry40db";
if (mysqli_query($conn, $sql)) {
    echo "Industry 4.0 Database created successfully ###";
} else {
    echo "Error creating Industry 4.0 database: " . mysqli_error($conn);
}

mysqli_close($conn);
?>