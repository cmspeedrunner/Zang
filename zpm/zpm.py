import sys
import os
lib = sys.argv[1]
os.system("git clone https://github.com/cmspeedrunner/Zang")
import shutil
shutil.copy("zang/examples/using/libraries/"+str(lib), str(os.getcwd()))
