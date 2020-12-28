<?php
  header('content-type:text/html;charset=utf-8');
  echo '欢迎' . $_POST['draft_content'];
  $myfile = fopen('testfile.txt', 'w');
  fwrite($myfile, 'hello world');
  fclose($myfile);
?>
