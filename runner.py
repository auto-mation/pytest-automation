import pytest
import sys 
import os

_version = sys.version_info 

if __name__ == "__main__":
    
    if _version < (3, 10):
        raise Exception("Python version is {}. Please upgrade to Python 3.10 or higher.".format(_version))
    args = sys.argv[1:] 
    args.extend(["--log-file=logs", "--html=Report.html"])
    print ("Execution Started....")
    pytest.main(args)
    print ("Execution is Done....")
    print (f"Execution Logs file path : {os.getcwd()}/logs")
    print (f"Execution Report file path : {os.getcwd()}/Report.html")


