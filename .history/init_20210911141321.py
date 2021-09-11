
import os
import sys

def __init__():
    project_path = os.getcwd()
    print(project_path)
    os.chdir(project_path)

    os.path.join(os.path.dirname(sys.argv[0]))

project_path = os.getcwd()
print(project_path)
os.chdir(project_path)
    
os.path.join(os.path.dirname(sys.argv[0]))

import moyu_engine.config.setup

moyu_engine.config.setup.run() 