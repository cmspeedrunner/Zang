import sys
import os
import shutil

lib = sys.argv[1]
current_dir = os.getcwd()

# Specify the directory name to check
dir_name = "Zang"

# Create the path to the directory by joining the current directory and the directory name
dir_path = os.path.join(current_dir, dir_name)
if os.path.exists(dir_path) and os.path.isdir(dir_path):
  shutil.copy("zang/examples/using/libraries/"+str(lib), str(os.getcwd()))
  print("INSTALLED "+str(lib).upper()+" SUCESSFULLY")
else:
  os.system("git clone https://github.com/cmspeedrunner/Zang")
  shutil.copy("zang/examples/using/libraries/"+str(lib), str(os.getcwd()))
