

<?php
// $foldername =  $_GET["foldername"];

echo "Folder that needs to scan - " .$_GET["foldername"];



echo system("python scscanner.py " . $_GET["foldername"] );


?>