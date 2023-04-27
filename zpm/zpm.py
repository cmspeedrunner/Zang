import sys
import os
import http.client as http
import json
import argparse
import models

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("-p", "--path", type=models.PathType(type="dir", dash_ok=False), default=None, help="Directory where libraries will be saved")

arg_parser.add_argument("action", default="install", choices=["install", "everything"], help="Do this action")
arg_parser.add_argument("args", nargs="*", default=None, help="Libraries to install (ignored if action is 'everything')")

arguments = arg_parser.parse_args()

os.system("")

library = sys.argv[1]
current_dir = os.getcwd()

if arguments.action == "install":
    if arguments.args == []:
        print("\u001b[31mZPMER02: WRITE THE LIBRARY NAME\u001b[0m")
        exit(1)

installer = models.Installer(arguments)
installer.handle_args()