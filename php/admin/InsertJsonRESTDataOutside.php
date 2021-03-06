<?php
// Author : Steve Gale 29/03/19
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
// get outside temp from weatherdata table

$sql = "SELECT ID, OUTSIDE_TEMP FROM weatherData ORDER BY ID DESC LIMIT 1";
$result = mysqli_query($conn, $sql);

    // only one row of data
if (mysqli_num_rows($result) > 0) {
    if($row = mysqli_fetch_assoc($result)) {
        $outsideTemp = $row["OUTSIDE_TEMP"];
    }
else {
        $outsideTemp = "0";
        $response["code"] = "3";
        $response["message"] = mysqli_error($conn);
        // echoing JSON response
        echo json_encode($response);
    } 
}   



// POST Data
$response = array();
$res=array();

//$json = json_decode($_POST[]);
$json = _json_decode(file_get_contents('php://input'));

if($json!=null){
   
    $RoomName=$json["RoomName"];
    $Humidity=$json["Humidity"];
    $Temperature=$json["Temperature"];
 //   $SampleDate=$json["date"];
 
// added outside temp to the room data insert query 
$sql = "INSERT INTO roomData (roomName, humidity, temperature, outsideTemp)
VALUES ('$RoomName', '$Humidity', '$Temperature', '$outsideTemp')";

    if (mysqli_query($conn, $sql)) {
        // successfully inserted into database
        $response["code"] = "1";
        $response["message"] = "successfully stored";
        // echoing JSON response
        echo json_encode($response);
    } else {
            // failed to insert row
        $response["code"] = "2";
        $response["message"] = mysqli_error($conn);
        // echoing JSON response
        echo json_encode($response);
    }
} else {
   echo "json data error";
}
mysqli_close($conn);


// fixes magic quotes issue in json post data
function _json_decode($string) {
    if (get_magic_quotes_gpc()) {
        $string = stripslashes($string);
    }
    return json_decode($string,true);
    }
?>

