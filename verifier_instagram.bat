@echo off
:: Vérification de Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installé ou n'est pas trouvé dans le PATH.
    pause
    exit /b
)

:: Vérification des modules nécessaires
python -c "import instaloader" >nul 2>&1
if %errorlevel% neq 0 (
    echo Le module 'instaloader' n'est pas installé. Installation en cours...
    pip install instaloader
)

:: Lancer le script Python
python verifier_instagram.py
pause
