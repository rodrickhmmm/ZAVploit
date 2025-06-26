@echo off
echo Instaluji python...
winget install Python.Python.3.12 --accept-package-agreements --accept-source-agreements

call refreshenv.cmd 2>nul || echo Warning: refreshenv not found, you may need to restart your terminal

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing required packages...
python -m pip install -r requirements.txt

echo Installing Playwright browsers...
python -m playwright install

echo Hotovo! Spouštím ZAVploit...
pause
ZAVploit.bat