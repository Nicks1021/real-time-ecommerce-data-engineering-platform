@echo off
title Real-Time Data Engineering Platform

set "PROJECT=C:\Users\NIKHIL\OneDrive\Desktop\RealTime-Data-Engineering-Platform 2"

echo ==========================================
echo   REAL-TIME DATA ENGINEERING PLATFORM
echo ==========================================
echo.

echo [1/4] Starting Kafka...
start "Kafka Server" cmd /k "cd /d C:\kafka\kafka_2.13-4.3.1 && bin\windows\kafka-server-start.bat config\server.properties"

echo.
echo Waiting for Kafka to become READY...
echo.

:WAIT_KAFKA
powershell -NoProfile -Command "$x=Test-NetConnection localhost -Port 9092 -WarningAction SilentlyContinue; if($x.TcpTestSucceeded){exit 0}else{exit 1}"

if errorlevel 1 (
    timeout /t 2 /nobreak >nul
    goto WAIT_KAFKA
)

echo Kafka is READY!
echo.

echo [2/4] Starting Consumer...
start "Kafka Consumer" cmd /k "cd /d %PROJECT% && venv\Scripts\python.exe kafka\consumer.py"

timeout /t 3 /nobreak >nul

echo [3/4] Starting Producer...
start "Data Producer" cmd /k "cd /d %PROJECT% && venv\Scripts\python.exe producer\producer.py"

timeout /t 3 /nobreak >nul

echo [4/4] Starting Flask API...
start "Flask API" cmd /k "cd /d %PROJECT%\api && ..\venv\Scripts\python.exe app.py"

timeout /t 5 /nobreak >nul

echo.
echo Opening Live Dashboard...
start "" "http://127.0.0.1:5000/dashboard"

echo.
echo ==========================================
echo   LIVE DASHBOARD STARTED
echo ==========================================
echo.

pause