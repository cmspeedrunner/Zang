import http.client as http
import os
import json
from argparse import Namespace
import traceback

class Library:

    def __init__(self, data: dict, connection: http.HTTPSConnection):
        self.connection = connection

        self.HTTP_DOWNLOAD_HEADERS = {
            "User-Agent": "zpm-app"
        }
        self.HTTP_DOWNLOAD_URL = "raw.githubusercontent.com"

        self.name: str = data["name"]
        self.html: str = data["html_url"]
        self.sha: str = data["sha"]
        self.git_url: str = data["git_url"]
        self.download_url: str = data["download_url"]

    def download(self, path: str = os.getcwd()+"/"):
        connection = http.HTTPSConnection(self.HTTP_DOWNLOAD_URL)
        connection.request("GET", self.download_url.replace("https://"+self.HTTP_DOWNLOAD_URL, ""), headers=self.HTTP_DOWNLOAD_HEADERS)

        with open(path+self.name, "w") as file:
            file.write(connection.getresponse().read().decode("utf-8"))
        
            print("\u001b[32mINSTALLED \u001b[35m"+str(self.name).upper()+"\u001b[32m SUCESSFULLY\u001b[0m")

class Libraries:

    def __init__(self, data: list, connection: http.HTTPSConnection):
        self.connection = connection

        self.libraries: list[Library] = []
        for library in data:
            self.libraries.append(Library(library, self.connection))
        
        self.libs_dict = {lib.name: lib for lib in self.libraries}
        self.names = map(lambda lib: lib.name, self.libraries)
        self.html_urls = map(lambda lib: lib.html, self.libraries)
        self.hashes = map(lambda lib: lib.sha, self.libraries)
        self.git_urls = map(lambda lib: lib.git_url, self.libraries)
        self.download_urls = map(lambda lib: lib.download_url, self.libraries)

    def download(self, library: str, path: str = os.getcwd()):
        if library+".zang" not in self.libs_dict.keys():
            raise LibraryNotFound(library)
        
        self.libs_dict[library+".zang"].download(path)

    def download_all(self, path: str = os.getcwd()+"/using/"):
        for library in self.libraries:
            try:
                self.download(library.name.replace(".zang", ""), path)
            except LibraryNotFound as error:
                traceback.print_exception(error)

class Installer:

    def __init__(self, args: Namespace) -> None:
        self._libraries: None | Libraries = None
        
        self.HTTP_URL = "api.github.com"
        self.HTTP_HEADERS = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "zpm-app"
        }
        self.LIBRARIES_PATH = "/repos/cmspeedrunner/Zang/contents/examples/using/libraries"
        self.connection = http.HTTPSConnection(self.HTTP_URL)

        self.arguments = args

    def handle_args(self):
        current_dir = os.getcwd()

        if self.arguments.action == "everything":
            path = self.arguments.path
            if not self.arguments.path:
                path = os.path.join(current_dir, "using")+"/"
                if not os.path.exists(path):
                    os.mkdir(path)
        
            self.libraries.download_all(path)
            print("\u001b[32mEVERYTHING INSTALLED SUCESSFULLY\u001b[0m")
        
        elif self.arguments.action == "install":
            path = self.arguments.path
            if self.arguments.path is None:
                path = current_dir+"/"
            
            for library in self.arguments.args:
                self.libraries.download(library, path)
            
            #map(lambda lib: self.libraries.download(lib, path), self.arguments.args)

    @property
    def libraries(self):
        if self._libraries:
            return self._libraries

        self.connection.request("GET", self.LIBRARIES_PATH, headers=self.HTTP_HEADERS)

        try:
            response = json.loads(self.connection.getresponse().read())
        except json.JSONDecodeError:
            print("\u001b[31mZPMER01: JSON DECODE ERROR WHILE TRYING TO GET LIBRARIES \u001b[0m")
            exit(1)
        
        self._libraries = Libraries(response, self.connection)
        return self._libraries

class LibraryNotFound(Exception):
    """Exception raised if library not finded.

    Attributes:
        library -- library name
        message -- explanation of the error
    """

    def __init__(self, library: str, message: str = None):
        self.library = library
        self.message = message
        if message is None:
            self.message = "\u001b[31mZPMER02: COULD NOT FIND \u001b[35m"+str(library).upper()+"\u001b[0m"
        super().__init__(self.message)

# Thanks Dan Lenski
class PathType(object):
    def __init__(self, exists=True, type='file', dash_ok=True):
        '''exists:
                True: a path that does exist
                False: a path that does not exist, in a valid parent directory
                None: don't care
           type: file, dir, symlink, None, or a function returning True for valid paths
                None: don't care
           dash_ok: whether to allow "-" as stdin/stdout'''

        assert exists in (True, False, None)
        assert type in ('file','dir','symlink',None) or hasattr(type,'__call__')

        self._exists = exists
        self._type = type
        self._dash_ok = dash_ok

    def __call__(self, string):
        if string=='-':
            # the special argument "-" means sys.std{in,out}
            if self._type == 'dir':
                raise '\u001b[31mstandard input/output (-) not allowed as directory path\u001b[0m'
            elif self._type == 'symlink':
                raise '\u001b[31mstandard input/output (-) not allowed as symlink path\u001b[0m'
            elif not self._dash_ok:
                raise '\u001b[31mstandard input/output (-) not allowed\u001b[0m'
        else:
            e = os.path.exists(string)
            if self._exists==True:
                if not e:
                    raise f"\u001b[31mpath does not exist: '{string}'\u001b[0m"

                if self._type is None:
                    pass
                elif self._type=='file':
                    if not os.path.isfile(string):
                        raise f"\u001b[31mpath is not a file: '{string}'\u001b[0m"
                elif self._type=='symlink':
                    if not os.path.symlink(string):
                        raise f"\u001b[31mpath is not a symlink: '{string}'\u001b[0m"
                elif self._type=='dir':
                    if not string.endswith("/"):
                        raise f"\u001b[31mpath is not a directory: '{string}'\u001b[0m"
                    elif not os.path.exists(os.path.join(os.getcwd(), string)):
                        raise f"\u001b[31mpath is not a directory: '{string}'\u001b[0m"
                elif not self._type(string):
                    raise f"\u001b[31mpath not valid: '{string}'\u001b[0m"
            else:
                if self._exists==False and e:
                    raise f"\u001b[31mpath exists: '{string}'"

                p = os.path.dirname(os.path.normpath(string)) or '.'
                if not os.path.isdir(p):
                    raise f"\u001b[31mparent path is not a directory: '{p}'\u001b[0m"
                elif not os.path.exists(p):
                    raise f"\u001b[31mparent directory does not exist: '{p}'\u001b[0m"

        return string