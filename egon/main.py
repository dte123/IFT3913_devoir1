import math
import os
from jls.main import jls
from lcsec.main import lcsec
from nvloc.main import nvloc


def egon(folder_name: str, threshold: float):
    folder_name = os.path.abspath(folder_name)
    
