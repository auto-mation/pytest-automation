# pytest-automation
GUI &amp; API test automation scripts using based on pytest framework


STEPS: 

    PYTHON 3.10 or newer version are installed

    Python3 PATH exist and configured in os

    clone reposiotry to a local directory 

    from reposiotry directory run .\setup.bat for win or .setup.sh for linux

    installation should start and all scripts will be triggered

    for re-execution run : 
                    source "~/pytest-automation/myenv/bin/activate"
                    python ./runner.py --browser=firefox

    GUI execution support firefox, chrome and edge browsers, default is edge, make sure installed browser are selected

    available tags for executions are @api @api_list_users @api_login @gui 
    
    Excution can be done on windows or linux  


    for linux :
    git clone https://github.com/auto-mation/pytest-automation.git
    cd pytest-automation
    chmod +x ./setup.sh
    ./setup.sh
    source myenv/bin/activate
    python ./runner.py --browser=firefox


    for windows using CMD :
    git clone https://github.com/auto-mation/pytest-automation.git
    cd pytest-automation 
    .\setup.bat
    myenv\Scripts\activate.bat
    python ./runner.py --browser=firefox