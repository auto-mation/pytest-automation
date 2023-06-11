@echo off
REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install Python3 and add it to your PATH.
    exit /b 0
)

python -m pip install --upgrade pip

REM Install virtualenv if not installed
python -m pip install virtualenv

REM Create a virtual environment
python -m virtualenv myenv

REM Activate the virtual environment
call myenv\Scripts\activate.bat

REM Install pytest and pytest-bdd
python -m pip install pytest pytest-html pytest-bdd selenium requests webdriver-manager

python -m pip freeze > requirements.txt

@REM python ./runner.py --browser=firefox

REM Deactivate the virtual environment
call deactivate.bat

echo Setup complete.
