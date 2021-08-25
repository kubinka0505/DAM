__name__ = "Discord Art Maker"
__doc__ = """Convert image to two colors, replace one of them
to given color (with optional color inversion)
and save it on the user's device."""

#-----#

from os import *
from time import time
from pathlib import Path
from requests import get
sys = __import__("os").sys
from random import randint
from datetime import timedelta
try: from tkinter import Tk, filedialog as fd
except: pass
from argparse import ArgumentParser as ap
SUPPRESS = __import__("argparse").SUPPRESS
from PIL import Image, ImageColor, ImageOps
chdir(path.abspath(path.dirname(__file__)))
del open

#-----#

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__
__version__		= "1.0"
__date__		= "25.08.2021"
__status__		= "Mature"
__license__		= "GPL V3"

#-----#

root = Tk()
root.withdraw()

#-----#

Files = ["Utils", "ArgParse", "Path", "Processing"]

for File in Files:
	__STA_TIME = __import__("time").time()
	exec(open("./Scripts/{0}.pyw".format(File), encoding = "utf-8").read())

#-----#

print('Processing took {2}{0}{5} seconds\nOutput folder: "{3}{4}{1}{5}"{6}'.format(
	str(timedelta(seconds = time() - __STA_TIME))[2:-3], Name.replace(sep, "/"),
	Styles.LightBlue, Styles.Green, Styles.Underscore, Styles.Reset,
	__BEL
	)
)