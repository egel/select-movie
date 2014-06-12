#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import random


# Global variables
__version__ = "1.0.0"
__programName__ = os.path.basename(__file__)
__author__ = "Maciej Sypień"


def main():
    if len(sys.argv) > 1:
        try:
            process_questions()

            for filename in sys.argv[1:]:
                print("Movie for tonight is: " +
                      get_random_item(get_filelist_from_dirs(filename)))
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
             "$ {2} directory1 [directory2 [ ... directoryN ]]\n"
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
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        # print path to all subdirectories first.
        #for subdirname in dirnames:
        #    list_of_files.append(os.path.join(dirname, subdirname))

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


# Run the program
main()
