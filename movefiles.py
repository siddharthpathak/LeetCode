# Program to remove irrelevant files(.nfo,.txt etc) from a folder, and keep the video files. Also, removes the video
# files from folder and moves them to the parent folder. Doesn't change the folder structure if it contains subtitles

import os
import shutil
import stat
import errno


def handleRemoveReadonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise


def movefiles(path, fileExtension):
    containssrt = False
    containsextension = False

    for folder, subfolders, files in os.walk(path):

        for file in files:
            if file.endswith(".srt"):
                containssrt = True
                break

        if containssrt == False and len(files) > 0:
            for file in files:
                if "sample" not in file and file.endswith(fileExtension) and folder != path:
                    shutil.copy(os.path.join(folder, file), path)
                    containsextension = True
            if containsextension:
                shutil.rmtree(folder, ignore_errors=False, onerror=handleRemoveReadonly)
        containssrt = False
        containsextension = False


print "Take backup before running, the program might delete wrong files if the folder structure is different."

path = raw_input("Enter path: ")
fileExtension = raw_input("Enter file extension. Extension should lead with a dot. Eg: .mp4  ")

movefiles(path, fileExtension)
