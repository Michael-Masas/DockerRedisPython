PowerShell.exe -Command Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
cd C:\DockerRedisPython
docker-compose -f docker-compose.yml up -d