#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import random
import time


# Global variables
__version__ = "1.0.0"
__programName__ = os.path.basename(__file__)
__author__ = "Maciej Sypień"

video_extensions = [
    '.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2',
    '.3mm', '.3p2', '.60d', '.787', '.890', '.aaf', '.aec', '.aep',
    '.aepx', '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv',
    '.amx', '.anim', '.aqt', '.arcut', '.arf', '.asf', '.asx', '.avb',
    '.avc', '.avchd', '.avd', '.avi', '.avp', '.avs', '.avs', '.avv',
    '.awlive', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik',
    '.bin', '.bix', '.bmc', '.bmk', '.bnp', '.box', '.bs4', '.bsf',
    '.bu', '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced',
    '.cel', '.cine', '.cip', '.clk', '.clpi', '.cmmp', '.cmmtpl',
    '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v',
    '.d3v', '.dash', '.dat', '.dav', '.db2', '.dce', '.dck', '.dcr',
    '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb',
    '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss', '.dmx', '.dnc',
    '.dpa', '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4',
    '.dvdmedia', '.dvr', '.dvr-ms', '.dvx', '.dxr', '.dzm', '.dzp',
    '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4f', '.f4p', '.f4v',
    '.fbr', '.fbr', '.fbz', '.fcp', '.fcproject', '.ffd', '.flc',
    '.flh', '.fli', '.flv', '.flx', '.fpdx', '.ftc', '.gcs', '.gfp',
    '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp', '.h264',
    '.hdmov', '.hdv', '.hkm', '.ifo', '.imovieproj',
    '.imovieproject', '.inp', '.int', '.ircp', '.irf', '.ism',
    '.ismc', '.ismclip', '.ismv', '.iva', '.ivf', '.ivr', '.ivs',
    '.izz', '.izzy', '.jmv', '.jss', '.jts', '.jtv', '.k3g',
    '.kdenlive', '.kmv', '.ktn', '.lrec', '.lrv', '.lsf', '.lsx',
    '.lvix', '.m15', '.m1pg', '.m1v', '.m21', '.m21', '.m2a', '.m2p',
    '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani',
    '.meta', '.mgv', '.mj2', '.mjp', '.mjpg', '.mk3d', '.mkv',
    '.mmv', '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi',
    '.moov', '.mov', '.movie', '.mp21', '.mp21', '.mp2v', '.mp4',
    '.mp4.infovid', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4',
    '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl', '.mpl', '.mpls',
    '.mproj', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse',
    '.msh', '.mswmm', '.mts', '.mtv', '.mvb', '.mvc', '.mvd', '.mve',
    '.mvex', '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor',
    '.nsv', '.nut', '.nuv', '.nvc', '.ogm', '.ogv', '.ogx', '.orv',
    '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow',
    '.piv', '.pjs', '.playlist', '.plproj', '.pmf', '.pmv', '.pns',
    '.ppj', '.prel', '.pro', '.pro4dvd', '.pro5dvd', '.proqc',
    '.prproj', '.prtl', '.psb', '.psh', '.pssd', '.pva', '.pvr',
    '.pxv', '.qt', '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz',
    '.r3d', '.rcd', '.rcproject', '.rdb', '.rec', '.rm', '.rmd',
    '.rmd', '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp', '.rsx',
    '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt',
    '.scc', '.scm', '.scm', '.scn', '.screenflow', '.sdv', '.sec',
    '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv', '.smi', '.smi',
    '.smil', '.smk', '.sml', '.smv', '.snagproj', '.spl', '.sqz',
    '.srt', '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi', '.swf',
    '.swi', '.swt', '.tda3mt', '.tdt', '.tdx', '.thp', '.tid',
    '.tivo', '.tix', '.tod', '.tp', '.tp0', '.tpd', '.tpr', '.trec',
    '.trp', '.ts', '.tsp', '.ttxt', '.tvlayer', '.tvrecording',
    '.tvs', '.tvshow', '.usf', '.usm', '.vbc', '.vc1', '.vcpf',
    '.vcr', '.vcv', '.vdo', '.vdr', '.vdx', '.veg', '.vem', '.vep',
    '.vf', '.vft', '.vfw', '.vfz', '.vgz', '.vid', '.video',
    '.viewlet', '.viv', '.vivo', '.vix', '.vlab', '.vob', '.vp3',
    '.vp6', '.vp7', '.vpj', '.vro', '.vs4', '.vse', '.vsp', '.w32',
    '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx',
    '.wot', '.wp3', '.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel',
    '.xesc', '.xfl', '.xlmv', '.xmv', '.xvid', '.y4m', '.yog',
    '.yuv', '.zeg', '.zm1', '.zm2', '.zm3', '.zmv']


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
                #print_all_files(get_fileslist_from_dirs(filename))

            s = (
                "Known video extensions: " +
                bcolors.HEADER + "{0}" + bcolors.ENDC + "\n"
                "Searching file into: " +
                bcolors.OKBLUE + "{1}" + bcolors.ENDC + "\n"
                "Found video files: " +
                bcolors.OKGREEN + "{2}" + bcolors.ENDC + "\n"
                "Movie for today is: " +
                bcolors.WARNING + "{3}" + bcolors.ENDC
                ).format(len(video_extensions),
                         directories[0],
                         len(get_fileslist_from_dirs(directories[0])),
                         get_random_movie(directories[0]))
            print(s)
        except ValueError as err:
            print(err)
    else:
        s = ("Nothing happen.\n"
             "Use '{0} --help' for help.").format(__programName__)
        print(s)


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


def get_fileslist_from_dirs(directory):
    """Get a list of all files in directory.

    Arguments:
    directories -- is a array of paths of searching directories
    """
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        # print path to all files names.
        for file in files:
            fileName, fileExtension = os.path.splitext(file)
            if fileExtension in video_extensions:
                list_of_files.append(os.path.join(root, file))
    return list_of_files


def get_random_item(my_list):
    return random.choice(my_list)


def print_all_files(my_list, show_line_numbers=True):
    """Printing all elements in my_list.

    Keywords:
    my_list -- List of items
    show_line_numbers -- (Defaul1t: True) adding at the start of line
                         a current index number.
    """
    for index, file in enumerate(my_list):
        if(show_line_numbers):
            print(index, ") ", file, sep='')
        else:
            print(file)


def get_random_movie(my_list):
    """Return single random element from a list (of directories).

    Keywords:
    my_list -- List of items
    """
    try:
        if not my_list:
            raise Exception("List is empty")
        list_of_files = get_fileslist_from_dirs(my_list)
        movie = get_random_item(list_of_files)
        return movie
    except Exception as err:
        print(err)


def get_list_of_video_extensions():
    ins = open("../select-movie/video_extensions.txt", "r")
    ext_list = []
    for line in ins:
        ext = line.split(" ")
        ext_list.append(ext[0])
    ins.close()
    return ext_list


# Run the program
start_time = time.time()
main()
print("Total time exec:", time.time() - start_time, "seconds")
