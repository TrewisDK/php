<?php
$output = shell_exec('ls');
echo base64_encode($output);
?>