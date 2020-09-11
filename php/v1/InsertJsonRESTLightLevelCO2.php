<?php
// Author : Steve Gale 20/08/20
// Modified : SG - 20/08/20 -
// Copyright 2019 Steve Gale - seek permission and terms of use before you copy or modify this code
// USage POST: { "RoomName" : "E223", "LightLevel" : "550", "CO2": "400.6" }'
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
// POST data 
$response = array();
$res=array();

//$json = json_decode($_POST[]);
$json = _json_decode(file_get_contents('php://input'));

if($json!=null){
   
    $RoomName=$json["RoomName"];
    $LightLevel=$json["LightLevel"];
    $C02=$json["CO2"];
 //   $SampleDate=$json["date"];
    
$sql = "INSERT INTO roomData (roomName, LightLevel, CO2, readDate)
VALUES ('$RoomName', '$LightLevel', '$C02', NOW())";

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

