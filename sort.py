import glob
import shutil
import os
import sys
from config import Config

sparselist = []
mediumlist = []
denselist = []

def classify(jpgfile, the_input):
    if the_input == "s":
        sparselist.append(jpgfile)
        print(sparselist)
    if the_input == "m":
        mediumlist.append(jpgfile)
        print(mediumlist)
    if the_input == "d":
        denselist.append(jpgfile)
        print(denselist)

def load():
    count = 1
    # print(count)
    for jpgfile in glob.iglob(os.path.join(Config.src_dir, "*.jpg")):
        print(count)
        if count <= 10:
            print(jpgfile)
            os.startfile(jpgfile)
            the_input = str(input())
            classify(jpgfile,the_input)
            count += 1
        else:
            break
    print("Images in sparse list: ")
    print(sparselist)
    print("Images in medium list: ")
    print(mediumlist)
    print("Images in dense list: ")
    print(denselist)
    print("moving previous 10 images to respective directories...")
    move()

def move():
    for index, file in enumerate(sparselist):
        shutil.move(file, Config.dst_dir1)
    for index, file in enumerate(mediumlist):
        shutil.move(file, Config.dst_dir2)
    for index, file in enumerate(denselist):
        shutil.move(file, Config.dst_dir3)

for jpgfile in glob.iglob(os.path.join(Config.src_dir, "*.jpg")):
    while True:
        load()

