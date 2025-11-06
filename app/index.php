<?php
echo json_encode([
    "message" => "Hello from PHP App by Adil 🚀",
    "version" => getenv('APP_VERSION'),
    "environment" => getenv('NODE_ENV')
]);
?>
