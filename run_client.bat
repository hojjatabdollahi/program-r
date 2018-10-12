PowerShell ^
    $pwd = (pwd).path; ^
    $src = \"$pwd\src\"; ^
    $env:PYTHONPATH = "$src"; ^
    .\dist\client\client.exe --config .\bots\ryan\config.yaml --cformat yaml --logging .\bots\ryan\logging.yaml;
