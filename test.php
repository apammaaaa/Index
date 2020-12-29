<?php
  $myfile = fopen('test.txt', 'w');
  fwrite($myfile, $_GET['draft_content'] . " ");
  fclose($myfile);
  $url = "https://apammaaaa.github.io/sprite/";
  header("Localtion:$url");
?>
