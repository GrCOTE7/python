@echo off
chcp 65001
echo 🚀 Lancement de FastAPI dans une nouvelle fenêtre...
start "FastAPI Server" cmd /k "uvicorn main:app --reload"

timeout /t 2 >nul

echo 🎨 Lancement de Flet dans une autre fenêtre...
start "Flet UI" cmd /k "flet run main.py"

echo ✅ Les deux serveurs sont lancés !
pause
