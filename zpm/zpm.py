import sys
import os
import http.client as http
import json

os.system("")

library = sys.argv[1]
current_dir = os.getcwd()

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
  print("\u001b[31mZPMER01: JSON DECODE ERROR WHILE TRYING TO INSTALL \u001b[35m"+str(library).upper()+"\u001b[0m")
  exit(1)

zang_libraries = {library["name"]: library for library in response}
if library+".zang" not in zang_libraries.keys():
  print("\u001b[31mZPMER02: COULD NOT FIND \u001b[35m"+str(library).upper()+"\u001b[0m")
  exit(1)

print(zang_libraries[library+".zang"]["download_url"])

connection = http.HTTPSConnection(HTTP_DOWNLOAD_URL)
connection.request("GET", zang_libraries[library+".zang"]["download_url"].replace("https://"+HTTP_DOWNLOAD_URL, ""), headers=HTTP_DOWNLOAD_HEADERS)

with open(current_dir+"/"+library+".zang", "w") as file:
  file.write(connection.getresponse().read().decode("utf-8"))

print("\u001b[32mINSTALLED \u001b[35m"+str(library).upper()+"\u001b[32m SUCESSFULLY\u001b[0m")