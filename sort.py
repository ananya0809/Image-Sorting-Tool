import glob
import shutil
import os
import sys
from config import Config

for jpgfile in glob.iglob(os.path.join(Config.src_dir, "*.jpg")):
    print(jpgfile)
    os.startfile(jpgfile)
    the_input = str(input())

    if the_input == "s":
        shutil.move(jpgfile, Config.dst_dir1)
    if the_input == "m":
        shutil.move(jpgfile, Config.dst_dir2)
    if the_input == "d":
        shutil.move(jpgfile, Config.dst_dir3)
