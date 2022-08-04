<?php 

$REDIS_HOST = 'localhost';
$REDIS_PORT = 6379;

ini_set('session.save_handler', 'redis');
ini_set('session.save_path', "tcp://$REDIS_HOST:$REDIS_PORT");
session_start();