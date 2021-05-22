class ViewFile { public $filename = ''; 


public function __toString()


 { include $this->filename; return ""; } }



 if (isset($_GET['page']))
 
 
 { $pdfobject = unserialize($_GET['page']); } 
 
 else { $pdfobject = new File(); } ?> 
