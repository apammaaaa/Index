<?php
  echo "<h1>感谢下载</h1>";
  $myfile = fopen('test.txt', 'w');
  fwrite($myfile, $_GET['draft_content'] . " ");
  fclose($myfile);
?>
