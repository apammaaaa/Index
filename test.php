<?php
  $myfile = fopen('test.txt', 'w');
  fwrite($myfile, $_POST['v'] . "");
  fclose($myfile);
  $url = "https://apammaaaa.github.io/sprite/";
  header("Location:$url");
?>
