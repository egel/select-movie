#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import random


# Global variables
__version__ = "1.0.0"
__programName__ = os.path.basename(__file__)
__author__ = "Maciej Sypień"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def main():
    if len(sys.argv) > 1:
        try:
            # Basic-info questions
            process_questions()

            directories = []
            for path in sys.argv[1:]:
                directories.append(path)
                #print_all_files(get_filelist_from_dirs(filename))

            print(directories)

            s = (
                "Known video extensions: " +
                bcolors.HEADER + "{0}" + bcolors.ENDC + "\n"
                "Searching file into: " +
                bcolors.OKBLUE + "{1}" + bcolors.ENDC + "\n"
                "Found video files: " +
                bcolors.OKGREEN + "{2}" + bcolors.ENDC + "\n"
                "Movie for tonight is: " +
                bcolors.WARNING + "{3}" + bcolors.ENDC
                ).format(len(get_list_of_video_extensions()),
                         directories[0],
                         len(get_filelist_from_dirs(directories[0])),
                         get_random_movie(directories[0]))
            print(s)
        except ValueError as err:
            print(err)
    else:
        s = ("Nothing happen.\n"
             "Use '{0} --help' for help.").format(__programName__)
        print(s)
        sys.exit()


def process_questions():
    if sys.argv[1] in ("-h", "--help"):
        s = ("{0:-^89}\n"
             "Example usage:\n"
             "\t$ {2} /my/example/directory\n\n"
             "Practical examples:\n"
             "\t$ {2} ~/Video\n"
             "{1:-<89}".format(" Help ", "", __programName__))
        print(s)
        sys.exit()
    elif sys.argv[1] in ("-V", "--version"):
        s = ("{0}  v{1}\n"
             "License GPLv3+: GNU GPL version 3 or later "
             "http://gnu.org/licenses/gpl.html\n"
             "\n"
             "Author: {2}").format(__programName__, __version__, __author__)
        print(s)
        sys.exit()


def get_filelist_from_dirs(directory):
    """Get a list of all files in directory.

    Arguments:
    directories -- is a array of paths of searching directories
    """
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        # print path to all filenames.
        for file in files:
            list_of_files.append(os.path.join(root, file))

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from
        # recursing into there.
        if '.git' in root:
            # don't go into any .git directories.
            dirs.remove('.git')
    return list_of_files


def get_random_item(my_list):
    return random.choice(my_list)


def print_all_files(my_list):
    for index, file in enumerate(my_list):
        print(index, ") ", file, sep='')


def get_random_movie(list_of_dirs):
    list_of_files = get_filelist_from_dirs(list_of_dirs)
    movie = get_random_item(list_of_files).split('/')
    return movie[-1]


def get_list_of_video_extensions():
    ins = open("video_extensions.txt", "r")
    ext_list = []
    for line in ins:
        ext = line.split(" ")
        ext_list.append(ext[0])
    ins.close()
    return ext_list


# Run the program
main()
