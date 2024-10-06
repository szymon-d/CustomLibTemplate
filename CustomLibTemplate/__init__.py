from . import sub_module
from .function import *


# #Dynamic import
# import os
# import importlib
# import pkgutil
# PACKAGE_DIR = os.path.dirname(__file__)
# for module_info in pkgutil.iter_modules([PACKAGE_DIR]):
#     module_name = module_info.name
#
#     setattr(__import__(__name__), module_name, importlib.import_module(f'.{module_name}', package=__name__))

