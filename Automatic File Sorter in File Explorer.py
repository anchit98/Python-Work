#!/usr/bin/env python
# coding: utf-8

#Automatic File Sorter in File Explorer

import os, shutil

path = r"C:FilePath/"

file_name = os.listdir(path)

folder_names = ['Photos', 'Videos', 'Music']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print((path + folder_names[loop]))
        os.makedirs((path + folder_names[loop]))
        
for file in file_name:
    if ".mp4" in file and not os.path.exists(path + "Videos/" + file):
        shutil.move(path + file, path + "Videos/" + file)
    elif ".jpg" in file and not os.path.exists(path + "Photos/" + file):
        shutil.move(path + file, path + "Photos/" + file)
    elif ".mp3" in file and not os.path.exists(path + "Music/" + file):
        shutil.move(path + file, path + "Music/" + file)
