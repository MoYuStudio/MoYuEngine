
import os

project_path = os.getcwd()
print(project_path)
os.chdir(project_path)

import moyu_engine.config.setup

moyu_engine.config.setup.run()