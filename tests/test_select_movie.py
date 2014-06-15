#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
from select_movie import *


class test_select_movie(unittest.TestCase):

    def test_dummy(self):
        self.assertTrue(True)

    def test_get_random_item(self):
        sample_list = ['bb', 'aa', 'cc']
        item = get_random_item(sample_list)
        self.assertIn(item, sample_list, "Chosen film don't exist in a list")

    @patch('os.listdir',
           MagicMock(return_value=['/home/maciej/Video/file1.txt',
                                   '/home/maciej/Video/file2.avi',
                                   '/home/maciej/Video/file3.mkv',
                                   '/home/maciej/Video/file4.txt']))
    def test_get_fileslist_from_dirs(self):
        simulate = get_fileslist_from_dirs(os.listdir('./test1/'))
        result = ['/home/maciej/Video/file2.avi',
                  '/home/maciej/Video/file3.mkv']
        self.assertListEqual(simulate,
                             result,
                             "Return values from function are " +
                             "not equal with the result")

    @patch('os.listdir',
           MagicMock(return_value=['/home/maciej/mama_mia.srtTS.mkv',
                                   '/home/maciej/hercules_legendary.mp4',
                                   '/home/maciej/blade-runner.blueray.avi']))
    def test_get_random_movie(self):
        sample_list = os.listdir('./test2/')
        movie = get_random_movie(sample_list)
        self.assertIn(movie, sample_list, "Chosen film don't exist in a list")


if __name__ == '__main__':
    unittest.main()
