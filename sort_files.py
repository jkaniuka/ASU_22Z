#***************************************
# Author: Jan Kaniuka
# Subject: Unix System and TCP/IP Network Administration
# Project: File sorting program
# Winter semester 2022
# Warsaw University of Technology  
#***************************************

import os
import sys
import shutil
import filecmp
import configparser
import subprocess
from pathlib import Path


print("The program has been launched ...")

print("Loading parameters from config file")
config = configparser.ConfigParser()		
config.read("clean_files.ini")
params = config['parameters']
troublesome_characters = params["troublesome_characters"]
substitute_char = params["substitute_char"]

arg_dirs = []
temp_file_path = str(Path.home()) + "/asu_new_x_dir"

n = len(sys.argv)
if n < 3:
    print("Shutting down. Not enough input arguments :(")
    sys.exit(0)
for i in range(1, n):
    arg_dirs.append(str(sys.argv[i]))

print("Creating temp dir in /home")
try:
    os.mkdir(temp_file_path)
    print("Temp dir created")
except OSError as error:
    print("Error while creating temp file")
    sys.exit(0)

print("Adding all files to one dir")
print("If two files have the same name, the older file is deleted")

added_files = []
added_files_mod_dates = {}

for dir in arg_dirs:
    for path, subdirs, files in os.walk(dir):
        for name in files:
            if name not in added_files:
                try:
                    print("COPY", os.path.join(path, name)," TO: ", temp_file_path)
                    shutil.copy(os.path.join(path, name), temp_file_path)
                    added_files.append(name)
                    added_files_mod_dates[name] = os.path.getmtime(os.path.join(path, name))
                except:
                    print("Error occurred while copying file.")
            elif name in added_files:
                to_be_coppied = os.path.getmtime(os.path.join(path, name))
                already_in_temp = os.path.getmtime(os.path.join(temp_file_path, name))
                if (to_be_coppied > already_in_temp):
                    try:
                        print("COPY", os.path.join(path, name)," TO: ", temp_file_path)
                        shutil.copy(os.path.join(path, name), temp_file_path)
                    except:
                        print("Error occurred while copying file.")
                else:

                    print("!!! NO COPY", os.path.join(path, name), temp_file_path)


temp_files_list = []

for filename in os.listdir(temp_file_path):
    temp_files_list.append(os.path.join(temp_file_path, filename))

pairs = [(a, b) for idx, a in enumerate(temp_files_list) for b in temp_files_list[idx + 1:]]

print("Deleting identical files: ")
for pair in pairs:
    try:
        are_identical = filecmp.cmp(*pair)
        if are_identical:
            print(pair, " Are identical? ", are_identical)
            first = added_files_mod_dates[os.path.split(pair[0])[1]]
            second = added_files_mod_dates[os.path.split(pair[1])[1]]
            if (first > second):
                print("Removing: ", pair[0])
                os.remove(pair[0])
            elif (first < second):
                print("Removing: ", pair[1])
                os.remove(pair[1])
    except FileNotFoundError:
        pass


print("Deleting empty and temporary files: ")
for filename in os.listdir(temp_file_path):
    path_to_unwanted_file = os.path.join(temp_file_path, filename)
    if os.stat(path_to_unwanted_file).st_size == 0:
        print("Removing empty file: ", path_to_unwanted_file)
        os.remove(path_to_unwanted_file)
    elif os.path.splitext(path_to_unwanted_file)[1] in params["temp_files_extensions"]:
        print("Removing temp file: ", path_to_unwanted_file)
        os.remove(path_to_unwanted_file)

print("Changing permisions")
for filename in os.listdir(temp_file_path):
    subprocess.call(["chmod", "644", os.path.join(temp_file_path, filename)])
subprocess.call(["ls", "-l", "/home/jan/asu_new_x_dir"])


print("Changing filenames")
for filename in os.listdir(temp_file_path):
    head, tail = os.path.os.path.splitext(filename)
    string_as_list = list(head)
    for idx, char in enumerate(string_as_list):
        if char in troublesome_characters:
            string_as_list[idx] = substitute_char
    
    result = "".join(string_as_list)
    if filename != (result + tail):
        print('Rename: ', filename, " to: ", result + tail)
        os.rename(os.path.join(temp_file_path, filename), os.path.join(temp_file_path, result + tail))