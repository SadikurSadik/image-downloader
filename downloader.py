import sys 


if (sys.version_info > (3, 0)):
     from lib.downloader_py3 import *
else:
    from lib.downloader_py2 import *


