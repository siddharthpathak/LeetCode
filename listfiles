#Lists all the files and folders in the given folder in tree structure

import os
import shutil


def listFiles(input):
    flag = 1
    for folder, subfolders, files in os.walk(input):
        if(flag):
            x = len(folder.split("\\"))
            flag=0
        path = folder.split("\\")
        print (len(path)-(x))*"-", os.path.basename(folder)
        for file in files:
            print (len(path)-(x-1))*"-",file



print "----------List Files----------"

input = raw_input("Enter the path ")

listFiles(input)

