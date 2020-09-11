<?php
// Author : Steve Gale 27/03/19
// Modified : SG - 20/05/19 -
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

$sql = "SELECT id, roomName, humidity, temperature, outsideTemp, readDate FROM roomData ";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo "id: " . $row["id"]. " - DeviceName: " . $row["roomName"]. " - Temperature " . $row["temperature"]. " - Humidity " . $row["humidity"]."<br>";
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?>
