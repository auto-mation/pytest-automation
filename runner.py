import pytest
import sys
if __name__ == "__main__":
    args = sys.argv[1:] 
    args.extend(["--log-file=logs", "--html=report.html"])
    print ("Execution Started....")
    pytest.main(args)
    print ("Execution is Done....")


