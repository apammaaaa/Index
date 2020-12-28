<?php
  $myfile = fopen('test.txt', 'w');
  fwrite($myfile, $_POST['draft_content']);
  fclose($myfile);
?>
