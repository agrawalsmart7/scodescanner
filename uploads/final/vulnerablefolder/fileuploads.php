<?php

$var1 = $_POST[' Upload2 '] 
$var2 = $_POST['Upload'] 
if( isset( $_POST['Upload'] ) ) {
	// Where are we going to be writing to?
	echo $var1;
	echo $var2;

	// Can we move the file to the upload folder?
	if( !move_uploaded_file( $_FILES[ 'uploaded' ][ 'tmp_name' ], $target_path ) ) {
		// No
		$html .= '<pre>Your image was not uploaded.</pre>';
	}
	else {
		// Yes!
		$html .= "<pre>{$target_path} succesfully uploaded!</pre>";
	}
}

?>
