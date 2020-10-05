#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 00:09:48 2020

@author: nutchapoldendumrongsup
"""

import unittest
import shutil


class TestSum(unittest.TestCase):
    
    

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")
        
    def manage_folder():
        folder_name='test_arXiv_downloader'
        if not os.path.isdir(path)
            # Create target Directory
            os.mkdir(folder_name)
        else:
            shutil.rmtree(folder_name)
            
    # test with normal query 
    def test_pdf_normal_1(self):
        manage_folder()
        search_query='cnn'
        search_by='all'
        sort_by='relevance'
        max_results='1'
        folder_name='test_arXiv_downloader'
        download_arXiv_pdf(search_query, search_by, sort_by, max_results, folder_name)
        downloaded_files=os.listdir(folder_name)
        num_files=len(downloaded_files)
        self.assertEqual(num_files, 1, "Should be 1")
        
    # test with normal query 
    def test_pdf_normal_2(self):
        manage_folder()
        search_query='nlp'
        search_by='abs'
        sort_by='lastUpdatedDate'
        max_results='5'
        folder_name='test_arXiv_downloader'
        download_arXiv_pdf(search_query, search_by, sort_by, max_results, folder_name)
        downloaded_files=os.listdir(folder_name)
        num_files=len(downloaded_files)
        self.assertEqual(num_files, 5, "Should be 5")
        
    # test with query that should not return any matching 
    def test_pdf_no_result(self):
        manage_folder()
        search_query='fueirbfejbiuhekjfbehirgfwalfhnksjefeirlba'
        search_by='jr'
        sort_by='submittedDate'
        max_results='5'
        folder_name='test_arXiv_downloader'
        download_arXiv_pdf(search_query, search_by, sort_by, max_results, folder_name)
        downloaded_files=os.listdir(folder_name)
        num_files=len(downloaded_files)
        self.assertEqual(num_files, 0, "Should be 0")
        

if __name__ == '__main__':
    unittest.main()