import sys
import os
import shutil

lib = sys.argv[1]
current_dir = os.getcwd()

# Specify the directory name to check
dir_name = "libsrc"

# Create the path to the directory by joining the current directory and the directory name
dir_path = os.path.join(current_dir, dir_name)
if os.path.exists(dir_path) and os.path.isdir(dir_path):
  try:
    shutil.copy("libsrc/examples/using/libraries/"+str(lib), str(os.getcwd()))
    print("\u001b[32mINSTALLED \u001b[35m"+str(lib).upper()+"\u001b[32m SUCESSFULLY\u001b[0m")
  except FileNotFoundError as e:
    print("\u001b[31mZPMER01: COULD NOT FIND \u001b[35m"+str(lib).upper()+"\u001b[0m")
else:
  os.system("git clone https://github.com/cmspeedrunner/Zang")
  os.rename("Zang", "libsrc")
  try:
    shutil.copy("libsrc/examples/using/libraries/"+str(lib), str(os.getcwd()))
    print("\u001b[32mINSTALLED \u001b[35m"+str(lib).upper()+"\u001b[32m SUCESSFULLY\u001b[0m")
  except FileNotFoundError as e:
    print("\u001b[31mZPMER01: COULD NOT FIND \u001b[35m"+str(lib).upper()+"\u001b[0m")
