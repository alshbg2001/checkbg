<?php

#error_reporting(E_ALL);
#ini_set('display_errors', 1);

$TOKEN = "1128799285:AAH634XjJOUgU1CfeMYK35uU0GJOkAypiL4"; # YOUR BOT TOKEN .

if (!file_exists('Telegram.php')) {
    copy('https://mohammed-api.com/Telegram/library.php', 'Telegram.php');
}
require_once "Telegram.php"; // get telegram library

if ($text == "/start") {
    SendMessage($chat_id, 'Welcome to the php code test bot.');
}

if (strpos($text, 'update')) {
    bot('sendmessage', [
        'chat_id' => $chat_id, 'text' => json_encode($update, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES)
    ]);
}

if ($text == "/del") {
    SendMessage($chat_id, 'Done Del Code.');
    unlink('php.php');
    unlink($chat_id . '.txt');
}

$str = str_replace('/run ', null, $text);

if ($text == "/run $str") {
    SendMessage($chat_id, 'Done Up Code.');
    file_put_contents('php.php', "<?php \n\n" . $str . "\n?>");
    file_put_contents($chat_id . '.txt', "run");
}

$Get = file_get_contents("php.php");

if ($text == "/stop") {
    SendMessage($chat_id, 'Done stop Code.');
    file_put_contents($chat_id . '.txt', "stop");
} elseif ($text == "/run") {
    SendMessage($chat_id, 'Done run Code.');
    file_put_contents($chat_id . '.txt', "run");
}

$code = file_get_contents($chat_id . ".txt");

if ($code == "run" && file_exists('php.php')) {
    #require_once 'php.php';

    if ($Get != null) {
        SendMessage($chat_id, $Get);
    }
}

// python

if ($text == "/py") {
    SendMessage($chat_id, 'Done Del Code.');
    unlink('main.py');
    unlink($chat_id . '.txt');
}

$str_py = str_replace('/py ', null, $text);

if ($text == "/py $str_py") {
    SendMessage($chat_id, 'Done Up Code.');
    file_put_contents('main.py', $str_py);
    file_put_contents($chat_id . '.txt', "run");
}

if ($code == "run" && file_exists('main.py')) {
   $result = shell_exec("python3 main.py");
    SendMessage($chat_id, $result);
}



if ($text) {
    $tmp = exec("python3 main.py $text");
    SendMessage($chat_id, "is : ".$tmp, null);
}
