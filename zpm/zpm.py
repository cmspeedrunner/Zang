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

HTTP_URL = "api.github.com"
HTTP_DOWNLOAD_URL = "raw.githubusercontent.com"
HTTP_HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "zpm-app"
}
HTTP_DOWNLOAD_HEADERS = {
    "User-Agent": "zpm-app"
}
LIBRARIES_PATH = "/repos/cmspeedrunner/Zang/contents/examples/using/libraries"

connection = http.HTTPSConnection(HTTP_URL)
connection.request("GET", LIBRARIES_PATH, headers=HTTP_HEADERS)
try:
    response = json.loads(connection.getresponse().read())
except json.JSONDecodeError:
    print("\u001b[31mZPMER01: JSON DECODE ERROR WHILE TRYING TO GET LIBRARIES LIKE \u001b[35m"+str(library).upper()+"\u001b[0m")
    exit(1)

zang_libraries = {library["name"]: library for library in response}
connection = http.HTTPSConnection(HTTP_DOWNLOAD_URL)

if arguments.action == "everything":
    path = arguments.path

    if not arguments.path:
        path = os.path.join(current_dir, "using")+"/"
        if not os.path.exists(path):
            os.mkdir(path)
  
    for library in response:
        connection.request("GET", library["download_url"].replace("https://"+HTTP_DOWNLOAD_URL, ""), headers=HTTP_DOWNLOAD_HEADERS)

        with open(path+library['name'], "w") as file:
            file.write(connection.getresponse().read().decode("utf-8"))
    
        print("\u001b[32mINSTALLED \u001b[35m"+str(library["name"]).upper()+"\u001b[32m SUCESSFULLY\u001b[0m")
  
    print("\u001b[32mEVERYTHING INSTALLED SUCESSFULLY\u001b[0m")
    exit(0)

for library in arguments.args:
    if library+".zang" not in zang_libraries.keys():
        print("\u001b[31mZPMER02: COULD NOT FIND \u001b[35m"+str(library).upper()+"\u001b[0m")
        continue

    connection.request("GET", zang_libraries[library+".zang"]["download_url"].replace("https://"+HTTP_DOWNLOAD_URL, ""), headers=HTTP_DOWNLOAD_HEADERS)

    path = arguments.path

    if not arguments.path:
        path = current_dir

    with open(path+library+".zang", "w") as file:
        file.write(connection.getresponse().read().decode("utf-8"))
  
    print("\u001b[32mINSTALLED \u001b[35m"+str(library).upper()+"\u001b[32m SUCESSFULLY\u001b[0m")