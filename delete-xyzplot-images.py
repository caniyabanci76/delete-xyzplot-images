#!/usr/bin/env python3

import os
import sys
from glob import glob
from natsort import os_sorted  # for natural sort of files list..
from pathlib import Path
import argparse

# =======================================
# for coloring text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# =======================================
base_dir = ""

# =======================================
# Initialize args parser
msg = "deletes all xyz plot images "
# Initialize parser
parser = argparse.ArgumentParser(description=msg)

# Adding optional argument
parser.add_argument("-p", "--path", help="Path to files.  Default is current directory.")
parser.add_argument("-r", "--recursive", action="store_true", help="Search all sub-directories.  Default is off.")
# Read arguments from command line
args = parser.parse_args()


# =======================================
# default to current working dir
# if path passed in as args, use that instead
base_dir = os.getcwd()
if args.path:
    base_dir = args.path
print(f"images path = {base_dir}")
# =======================================
recursive_on = False
if args.recursive:
    recursive_on = True
print(f"recursive : {recursive_on}")
# =======================================
# =======================================


def delete_xyz_images(dir_path):
    # get list of png/jpg files
    search_pattern1 = dir_path + '/*'
    image_list = os_sorted(glob(f'{search_pattern1}', recursive=False))

    # loop through all image files
    for img_path in image_list:
        if "xyz" in img_path:
            print("xyz image found - deleting")
            os.remove(img_path)


# =======================================
# =======================================
def main():

    if os.path.exists(base_dir) == False:
        print(bcolors.FAIL + "directory does not exist.  Exiting program." + bcolors.ENDC)
        sys.exit()
    else:


        # if recursive is off then just process current dir
        if not recursive_on:
            delete_xyz_images(base_dir)

        elif recursive_on:
            # if recursive is on then get list of all sub dirs

            list = glob(base_dir + '/*', recursive=True)
            dirlist = []
            for l in list:
                if os.path.isdir(l):
                    dirlist.append(l)

        # now we have our list of sub dirs
        # use each as base folder when calling the rename function
        for d in dirlist:
            delete_xyz_images(d)

main()