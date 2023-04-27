import os

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