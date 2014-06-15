#!/usr/bin/python3


import unittest
from unittest.mock import patch, MagicMock

from select_movie import *


class test_select_movie(unittest.TestCase):


    def test_get_random_item(self):
        sample_list = ['bb', 'aa', 'cc']
        item = get_random_item(sample_list)
        self.assertIn(item, sample_list, "Chosen film don't exist in a list")

    @patch('os.listdir', MagicMock(return_value=['/home/maciej/Video/file1.txt',
                                          '/home/maciej/Video/file2.avi',
                                          '/home/maciej/Video/file3.mkv',
                                          '/home/maciej/Video/file4.txt']))
    def test_get_fileslist_from_dirs(self):
        simulate = get_fileslist_from_dirs(os.listdir('./test1/'))
        result = ['/home/maciej/Video/file2.avi', '/home/maciej/Video/file3.mkv']
        self.assertListEqual(simulate, result, "Return values from function are not equal with the result")


    # def test_get_random_movie(self):
    #     sample_list = ['/home/maciej/Video/mama_mia.srtTS.mkv',
    #                    '/home/maciej/Video/hercules_legendary.mp4',
    #                    '/home/maciej/Video/blade-runner.blueray.avi']
    #     movie = get_random_movie(sample_list)
    #     self.assertIn(movie, sample_list, "Chosen film don't exist in a list")


    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
