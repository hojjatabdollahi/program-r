PowerShell ^
    $pwd = (pwd).path; ^
    $src = \"$pwd\src\"; ^
    $env:PYTHONPATH = "$src"; ^
    python.exe .\src\programr\clients\events\majordomo\client.py --config .\bots\ryan\config.yaml --cformat yaml --logging .\bots\ryan\logging.yaml;
