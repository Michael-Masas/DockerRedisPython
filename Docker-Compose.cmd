PowerShell.exe -Command Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
cd C:\DockerRedisPython
powershell.exe -command "docker-compose up -d"