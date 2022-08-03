import sys
import os

if 'unittest' in sys.modules.keys(): # check if running under unittest
    os.environ["DB_NAME"] = "TestDB"
