<?php
  $myfile = fopen('test.txt', 'w');
  fwrite($myfile, $_GET['draft_content'] . " ");
  fclose($myfile);
?>
