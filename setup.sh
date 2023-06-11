#!/bin/bash

# Check if Python is installed
python3 --version > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Python not found. Please install Python3 and add it to your PATH."
    exit 0
fi

echo $(python3 --version)

python3 -m pip install --upgrade pip
  
python3 -m pip install virtualenv
  
# Create a virtual environment
python3 -m virtualenv myenv

# Activate the virtual environment
source myenv/bin/activate

python -m pip install --upgrade pip

# Install pytest and pytest-bdd
python -m pip install pytest pytest-html pytest-bdd selenium requests webdriver-manager

python -m pip freeze > requirements.txt

# python ./runner.py --browser=firefox

# Deactivate the virtual environment
deactivate

echo "Setup complete."
